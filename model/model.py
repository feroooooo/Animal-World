import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
from torchvision.models.resnet import ResNet50_Weights


class MyResNet(nn.Module):
    def __init__(self, classes_num=6):
        super(MyResNet, self).__init__()
        # self.model = models.resnet50(weights=ResNet50_Weights.DEFAULT)
        # num_ftrs = self.model.fc.in_features
        # self.model.fc = nn.Linear(num_ftrs, 6)

    def forward(self, x):
        # Define the forward pass
        return x