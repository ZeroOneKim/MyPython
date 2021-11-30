#별 찍기로 트리만들기.
num = int(input("숫자를 입력하세요: "))

for i in range (1, num+1):
    print(' '*(num - i)+'*' * (2 * i - 1))

print(' '*(num-2),'I')
