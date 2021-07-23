# Q. 2-gram
data = input('입력 : ')

for i in range(len(data)-1) :
    print(data[i], data[i+1], sep='')