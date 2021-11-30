#거꾸로 출력
oppo = str(input("문장 입력 : "))
num = 0
for i in range(len(oppo)):
    if len(oppo) > 0:
        num += 1
        print(oppo[len(oppo) - num], end=(""))
    else:
        break
