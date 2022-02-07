'''주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.'''
inp = []
count = 0
requireN = int(input())
if requireN<=100:
    for i in range(0, requireN):
        a = int(input())
        if a <= 1000:
            inp.append(a) #리스트에 추가
        elif a > 1000:
            print("1000 이하만 받음")
            inp = ["ERROR"]
            break
elif requireN>100:
    pass

for i in range(0, len(inp)):
    for j in range(2, inp[i]):
        if inp[i]%j ==0:
            zero = 1
        else:
            zero = 0
    if zero == 0:
        count += 1
    else:
        pass
print(count)