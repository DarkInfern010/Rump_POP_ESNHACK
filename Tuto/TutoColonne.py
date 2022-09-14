import time

data = ["pets"+str(i) for i in range(1,52)]
print(data)

time.sleep(2)

NumberCol = int(len(data)/3)
arrayShow = [""] * NumberCol
compt = 0
for i in data:
    if compt < 10:
        arrayShow[compt % NumberCol] += "[0" + str(compt) + "] - " + i + "//"
    else:
        arrayShow[compt % NumberCol] += "[" + str(compt) + "] - " + i + "//"
    compt += 1
for j in arrayShow:
    test = j.split("//")
    print(test[0] + " " * (30 - len(test[0])) +
          test[1] + " " * (30 - len(test[1])) +
          test[2] + " " * (30 - len(test[2])))