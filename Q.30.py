#index와 find의 차이점.
data = input('문장 입력하세요 : ')
word = input('단어 입력하세요 : ')

print(data.index(word))

#find와 index는 문자열에서 원하는 문자나 문자열이 어디있는지 알려준다.
#없는 문자를 찾을 때에 find는 -1값을 리턴하지만 index의 경우 오류, 즉 에러창을 띄운다