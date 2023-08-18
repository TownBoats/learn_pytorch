import os
for root, dirs, file in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(file)