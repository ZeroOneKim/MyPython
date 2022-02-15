from django.shortcuts import render

def home(request):
    #template을 해석해서 html의 코드를 생성해주는 함수
    return render(request, 'index.html')