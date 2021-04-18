import torch
import numpy as np


print("=======")
a = torch.randint(1, 10, (3,3))
print(a)
b = torch.randint(1, 10, (3,3))
#print(b)

c = a.add_(5)
print(c)