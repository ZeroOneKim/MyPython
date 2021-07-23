# 대 소문자 거르기
al = input('Alphabet : ')

if al.isupper() :
    print('yes')
else :
    print('NO')

#variable.upper() -> mary >> MARY / MARY >> MARY
#variable.isupper() -> mary >> false / MARY >> true