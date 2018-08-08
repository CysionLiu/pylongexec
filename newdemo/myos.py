import os
import os.path
from os.path import *

print(os.name)
# for root, dirs, files in os.walk('./'):
#     print(root)
#     if len(dirs) != 0:
#         print(dirs)
#     if len(files) != 0:
#         print(files)

li = os.listdir('./')
print(li)
p = './byte.dat'
print(getatime(p))
print(getmtime(p))
print(getctime(p))
