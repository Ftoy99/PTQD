import torch

inputs_collected = torch.load("imagenet_input_20steps.pth")
print(inputs_collected[0][0])
print(inputs_collected[0][1])
print(inputs_collected[0][2])
print(inputs_collected[0][3])