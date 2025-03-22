import torch

inputs_collected = torch.load("imagenet_input_20steps.pth")
print(inputs_collected[0][0].shape)
print(inputs_collected[0][1].shape)
print(inputs_collected[0][2].shape)