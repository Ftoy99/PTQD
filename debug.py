import torch

inputs_collected = torch.load("imagenet_input_20steps.pth")
print(inputs_collected[0])