##Author: @panthadeep_b
##Created on: 06.Oct.25; 20.57 IST
##Introduction to PyTorch

import torch

x = torch.tensor([1.0, 2.0, 3.0]);
print('1D Tensor: \n', x);

y = torch.zeros((3, 3));
print('2D Tensor: \n', y);

dev_info = torch.cuda.get_device_name(0);
print("The device is:", dev_info);
