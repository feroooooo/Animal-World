from torchvision import transforms
import torchvision.models as models
import torch.nn as nn
import torch
import os
import json
from PIL import Image

class Predict():
    def __init__(self, path):
        self.path = path
        model = models.resnet50()

        # 修改最后一层以匹配六个类别
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 6)
        
        self.model = self.load_model(model)
    
    def load_model(self, model):
        # 检查点文件路径
        checkpoint_path = 'checkpoint/best_epoch30.pth'

        # 确保文件存在
        if os.path.isfile(checkpoint_path):
            # 加载保存的状态字典
            checkpoint = torch.load(checkpoint_path)
            
            # 加载模型权重
            model.load_state_dict(checkpoint['model'])
            
            # 获取保存的accuracy, loss和epoch
            accuracy = checkpoint['accuracy']
            validation_loss = checkpoint['loss']
            epoch = checkpoint['epoch']
            
            print(f"Model loaded successfully with accuracy: {100.*accuracy:.2f}%, loss: {validation_loss:.6f}, at epoch: {epoch}")
        else:
            print(f"No checkpoint found at '{checkpoint_path}'")
        return model
    
    def predict(self):
        # 图片预处理流程，这需要根据您模型训练时使用的预处理相匹配
        transform = transforms.Compose([
            transforms.Resize((224, 224)),  # 示例尺寸，根据需要调整
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # ImageNet标准化
        ])

        # 加载图片
        img_path = self.path
        image = Image.open(img_path)

        # 预处理图片
        image = transform(image)

        # 增加一个批次维度，因为PyTorch模型通常期望批次输入
        image = image.unsqueeze(0)
        # 打开之前保存的JSON格式的文件
        with open('./model/label_map.json', 'r') as f:
            # 从文件加载数据回字典
            label_map = json.load(f)

        
        self.model.eval()
        # 无需计算梯度
        with torch.no_grad():
            # 进行预测
            outputs = self.model(image)
            
            # 输出处理，获取预测结果
            _, predicted = torch.max(outputs, 1)
            # 返回Predicted class
            return label_map[str(predicted.item())]
    
    
if __name__ == '__main__':
    predictor = Predict("C:/Custom/DataSet/WildLife/cheetah/00000000_224resized.png")
    print(predictor.predict())