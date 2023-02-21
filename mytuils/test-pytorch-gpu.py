# 测试torch-gpu是否安装成功
import torch
if __name__ == '__main__':
    print(torch.cuda.is_available())
    print(torch.backends.cudnn.is_available())
    print(torch.cuda_version)
    print(torch.backends.cudnn.version())