'''어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.'''
n = int(input())
if n == 1000:
    n = 999

def hansoo(request):
    res = 99
    if request < 100:
        print(request)
    elif request < 1000:
        for i in range(100, request+1):
            baek = int(i / 100)
            sip = int((i-baek*100) / 10)
            il = (i-(baek*100)-(sip*10))
            if (sip-baek)==(il - sip):
                res += 1
        print(res)
hansoo(n)
