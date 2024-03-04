from torch.utils.data import Dataset
from PIL import Image
import os
import random
import json

class ImageDataset(Dataset):
    
    def __init__(self, data_dir, transform=None, reshape = False):
        self.data_dir = data_dir
        self.label_name = {}
        self.data_info = self.get_img_info()
        random.seed(0)
        random.shuffle(self.data_info)
        self.transform = transform
        self.reshape = reshape

        
    def __getitem__(self, index):
        path_img, label = self.data_info[index]
        img = Image.open(path_img).convert('RGB')     
 
        if self.reshape:
            x = 15
            y = 0 
            width = 64
            height = 64
            (l,h) = img.size
            rate = min(l,h) / width
            img = img.resize((int(l // rate),int(h // rate)),Image.BILINEAR) 
            img = img.crop((x,y,width+x,height+y))

        if self.transform is not None:
            img = self.transform(img)
 
        return img, label

    
    def __len__(self):
        return len(self.data_info)
    
    
    # 获取图片信息
    def get_img_info(self):
        data_info = list()
        for root, dirs, _ in os.walk(self.data_dir):
            # 遍历类别
            for idx in range(len(dirs)):
                sub_dir = dirs[idx]
                img_names = os.listdir(os.path.join(root, sub_dir))
                img_names = list(filter(lambda x: x.endswith('.jpg'), img_names))
                self.label_name[idx] = sub_dir
                
                # 遍历图片
                for i in range(len(img_names)):
                    img_name = img_names[i]
                    path_img = os.path.join(root, sub_dir, img_name)
                    label = idx
                    data_info.append((path_img, label))
        return data_info
    
    
    def save_label(self):
        with open('./model/label_map.json', 'w') as f:
            # 将字典保存为JSON格式的文件
            json.dump(self.label_name, f)
    
    
if __name__ == '__main__':
    from torchvision import transforms
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    dataset = ImageDataset('C:/Custom/DataSet/WildLife', transform=transform)
    # dataset = ImageDataset('C:/Custom/DataSet/AnimalOrNot', transform=transform)
    print(len(dataset))
    print(dataset.label_name)
    dataset.save_label()