from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin, logout as dlogout
from member.models import UserForm, LoginForm

def home(request):
    if not request.user.is_authenticated: #로그아웃 
        data={'username': request.user, 'is_authenticated':request.user.is_authenticated}
    else: #로그인
        data={'last_login':request.user.last_login, 'username':request.user.username,
        'password': request.user.password, 'is_authenticated':request.user.is_authenticated}

    return render(request, 'member/index.html', {'data':data})

def join(request):
    if request.method=='POST':  #POST 방식일 경우 가입Form 생성
        form=UserForm(request.POST) #request.POST > POST방식으로 전달된 데이터들
        if form.is_vaild(): 
            new_user=User.objects.create_user(**form.cleaned_data) #사용자 계정 추가
            dlogin(request, new_user) #로그인
            return redirect('/member') #메인페이지를 return을 한다
        else:
            return render(request, 'member/index.html', {'msg': '회원가입에 실패했습니다.'}) #문제가 생기면 돌아가기
    else:
        form=UserForm() #전달 된 데이터가 없으면 빈폼을 만든다.
        return render(request, 'member/join.html', {'form': form})

def login_check(request):
    if request.method=='POST':
        name=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(username=name, password=pwd)
        if user is not None:
            dlogin(request,user) #정상적을 처리
            request.session['userid']=name #세션에 저장
            return redirect('/member/')
        else:  #로그인 실패시
            return render(request, 'member/index.html', {'msg':'로그인에 실패했습니다.'})
    else:
        form = LoginForm()
        return render(request, 'member/login.html', {'form':form})

def logout(request):
    dlogout(request)
    return redirect('/member')
