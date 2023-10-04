# in the name of God
# SMani24
import os

imageNames = []
for fileName in os.listdir("./images"):
    # print(fileName)
    imageNames.append(fileName[:-4])

labelNames = []
for fileName in os.listdir("./labels"):
    # print(fileName)
    labelNames.append(fileName[:-4])

for name in imageNames:
    if name not in labelNames:
        print("****************************************************************")
        print(f"{name} in images but not in labels!")

for name in labelNames:
    if name not in imageNames:
        print("****************************************************************")
        print(f"{name} in labels but not in images!")
