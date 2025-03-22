import torch

inputs_collected = torch.load("imagenet_input_20steps.pth")
for x in inputs_collected:
    print(x[0].shape)
    print(x[1].shape)
    print(x[2].shape)