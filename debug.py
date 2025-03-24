import torch

# inputs_collected = torch.load("imagenet_input_20steps.pth")
# for x in inputs_collected:
#     print(x[0].shape)
#     print(x[1])
#     print(x[1].shape)
#     print(x[2].shape)


inputs_collected = torch.load("data_error_t_w4a8_scale3.0_eta0.0_step20.pth")
for x in inputs_collected:
    print(x[100][0])
    print(x[100][1])
    print(x[100][2])
    print(x[100][3])
    print(x[100][4])
    print(x[100][5])