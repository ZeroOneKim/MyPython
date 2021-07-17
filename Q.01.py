#문제 1. 리스트의 삭제
nums = [100, 200, 300, 400, 500]

nums.pop() #nums의 배열중 가장 우측의 배열 500을 삭제함
nums.pop(1) #배열은 0에서 시작하며 1번째 배열인 200의 내용을 삭제하는 역할
print(nums)

repeat = [1, 2, 3, 4, 5]
print(repeat)
print(repeat.pop(0)) #이의 경우 0번째 배열만 살리고 모두 삭제가 됨,