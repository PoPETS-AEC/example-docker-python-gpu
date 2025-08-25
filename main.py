# Imports
import torch


if __name__ == "__main__":

    x = torch.rand(5, 3)
    print(x)

    print("CUDA available?: {}".format(torch.cuda.is_available()))

    print("Nb CUDA device(s)?: {}".format(torch.cuda.device_count()))

    print("CUDA current device?: {}".format(torch.cuda.current_device()))
