#리스트형 변수의 여러 기능
tree = ['apple', 'orange', 'Fruit', 'cap']
print(tree[1:3]) #tree[1]부터 tree[2]가 출력
#print(tree[0])
#print(tree[1:])

tree2 = tree
tree2.append('over')
print(tree2) #tree와 tree2의 값이 동일하게 나타난다.
print(tree)
print(id(tree)) #그 이유는 객체 식별자(번호)가 동일하게 때문이다.
print(id(tree2)) #tree2 = tree[:] 이방식으로 복사해야 식별자가 달라진다.

tree3 = tree[:]
print(id(tree3))
