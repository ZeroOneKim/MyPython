#딕셔너리 생성
keys = input('Key 값 입력 : ').split()
values = map(int, input('점수 : ').split())

result = dict(zip(keys, values))
print(result)
#dict >> {'key':values, .....}
#list >> [('key', values),  (....)]

# map()함수
# a = [1.2, 4.15, 6.42]
# a = list(map(int, a))  --> a>> [1, 4, 6] 