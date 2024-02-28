import torch.optim as optim
import torch
import torchvision.models as models
import torch.nn as nn
import os
import time
from torch.utils.data import DataLoader, random_split, WeightedRandomSampler
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
from image_dataset import ImageDataset
from model import MyResNet

# TensorBoard
path = 'logs'
if os.path.exists(path):
    for file_name in os.listdir(path):
        os.remove(os.path.join(path, file_name))
writer = SummaryWriter(path)

path = 'checkpoint'
if os.path.exists(path):
    for file_name in os.listdir(path):
        os.remove(os.path.join(path, file_name))

# 训练步数
step = 0
# 训练
def train(model, device, train_loader, optimizer, criterion, epoch):
    model.train()
    global step
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f'\rEpoch: {epoch}\t{batch_idx * len(data):>4} / {len(train_loader.dataset):<4} ({100. * batch_idx / len(train_loader):.0f}%)\tLoss: {loss.item():.6f}', end='')
        if step % 100 == 0:
            writer.add_scalar("train loss", loss.item(), step)
        step += 1
    print(f'\rEpoch: {epoch}\t{len(train_loader.dataset):>4} / {len(train_loader.dataset):<4} ({100.:.0f}%)\tLatest Loss: {loss.item():.6f}')


# 最优损失函数
best_loss = float("inf")
# 最优准确率
best_accuracy = 0

# 验证
def validate(model, device, validation_loader, criterion):
    model.eval()
    validation_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in validation_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            validation_loss += criterion(output, target).item() * data.size(0)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    validation_loss /= len(validation_loader.dataset)

    accuracy = correct / len(validation_loader.dataset)
    print('Validate:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(
        validation_loss, correct, len(validation_loader.dataset), accuracy * 100.))
    writer.add_scalar("validation loss", validation_loss, epoch)
    writer.add_scalar("validation accuracy", accuracy, epoch)
    
    # 存储模型
    global best_accuracy
    global best_loss
    if best_accuracy < accuracy:
        best_accuracy = accuracy
        print('Saving model...')
        state = {
            'model': model.state_dict(),
            'accuracy': accuracy,
            'loss': validation_loss,
            'epoch': epoch,
        }
        if not os.path.isdir('checkpoint'):
            os.mkdir('checkpoint')
        torch.save(state, f'checkpoint/best_epoch{epoch}.pth')
    if best_loss > validation_loss:
        best_loss = validation_loss
        
        
# 测试
def test(model, device, test_loader, criterion):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item() * data.size(0)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)

    accuracy = correct / len(test_loader.dataset)
    print('Test:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset), accuracy * 100.))


# 向控制台打印蓝色字符串
def color_print(str):
    print(f"\033[94m{str}\033[0m")


# 超参数配置
epoch_num = 150
batch_size = 32
learning_rate = 0.005

if __name__ == "__main__":
    time_start = time.perf_counter()
    color_print("Infomations:")
    # 初始化数据集
    train_transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),  # 以0.5的概率水平翻转图片
        transforms.RandomRotation(10),  # 随机旋转图片，范围为-10到10度
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),  # 随机调整图片的亮度、对比度和饱和度
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.9, 1.1)),  # 使用随机仿射变换
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    base_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    data_dir = 'E:\Data\WildLife'
    
    dataset = ImageDataset(data_dir, transform=train_transform)

    # 数据集大小
    dataset_size = len(dataset)
    train_size = int(dataset_size * 0.7)
    validation_size = int(dataset_size * 0.15)
    test_size = dataset_size - train_size - validation_size
    print("train size:", train_size)
    print("validation size:", validation_size)
    print("test size:", test_size)

    # # 数据集切分
    train_dataset, validation_dataset, test_dataset = random_split(dataset, [train_size, validation_size, test_size])
    
    # validation_dataset.transform = test_dataset.transform =  base_transform

    
    # 类别不平衡
    # all_labels = []
    # for _, label in train_dataset:
    #     all_labels.append(label)
    # all_labels = torch.tensor(all_labels)
    # class_count = torch.tensor([(all_labels == t).sum() for t in torch.unique(all_labels, sorted=True)])

    # class_weights = 1. / class_count.float()  # 计算类权重
    # samples_weights = class_weights[all_labels.long()]  # 每个样本的权重
    # sampler = WeightedRandomSampler(weights=samples_weights, num_samples=len(samples_weights), replacement=True)

    # DataLoader
    # train_loader = DataLoader(train_dataset, batch_size=batch_size, sampler=sampler)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print('current device:', device)
    
    # 加载预训练的ResNet50模型
    model = MyResNet().to(device)
    
    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.1)
    
    color_print("\nStart Training:")
    for epoch in range(1, epoch_num + 1):
        train(model, device, train_loader, optimizer, criterion, epoch)
        validate(model, device, validation_loader, criterion)
        scheduler.step()
    
    writer.close()
    time_stop = time.perf_counter()
    color_print("Finish Training.")
    
    print(f"\ntotal time:{time_stop - time_start:.3f}s")
    print(f"best loss: {best_loss:.6f}")
    print(f"best accuracy: {best_accuracy * 100.:.1f}%\n")
    
    test(model, device, test_loader, criterion)
