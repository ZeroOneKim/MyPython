'''세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.'''

x = []
y = []
for _ in range(3):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)

for i in range(3):
    if x.count(x[i]) == 1:
        xxx = x[i]
    if y.count(y[i]) == 1:
        yyy = y[i]
print(xxx, yyy)