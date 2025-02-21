import os
import torch
from matplotlib.pyplot import imread
import core
from utils import *
from cv2 import cvtColor, COLOR_RGBA2RGB

class Dataset(torch.utils.data.Dataset):

    def __init__(self, lr_path, hr_path, scale_factor, crop = True, start_num = 0):
        self.hr_path = hr_path
        self.lr_path = lr_path
        self.start_num = start_num
        self.sf = scale_factor
        self.crop = crop
        self.file = ".png"
    def __len__(self):
        return len(os.listdir(self.hr_path))
    
    def __getitem__(self, idx):
        # idx = idx+self.start_num
        name = str(idx)
        # if idx < 100:
        #     name = '0'+name
        #     if idx < 10:
        #         name = '0'+name
        hr = imread(os.path.join(self.hr_path, name + self.file))
        hr = cvtColor(hr, COLOR_RGBA2RGB)
        hr = torch.tensor(hr).permute(2,0,1)

        lr = imread(os.path.join(self.lr_path, name + self.file))
        lr= cvtColor(lr, COLOR_RGBA2RGB)
        lr = torch.tensor(lr).permute(2,0,1)
        if self.crop:
            lr, hr = random_crop_image_pair(high_res_tensor=hr,low_res_tensor=lr,crop_size=64,scale_factor=self.sf)
        lr = core.imresize(lr, scale=self.sf).clamp(0,255)
        return lr, hr
