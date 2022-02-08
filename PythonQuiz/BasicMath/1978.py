'''주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.'''

requireN = input()
nums = list(map(int, input().split()))
sosu = 0
if len(nums) == int(requireN):
    for i in nums:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            sosu += 1
        elif count != 2:
            pass
print(sosu)
