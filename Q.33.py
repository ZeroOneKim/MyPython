n = input()

l = list(n.strip().split())
len1 = len(l) - 1
for i in range(len1, -1, -1):
	print(l[i], end=' ')