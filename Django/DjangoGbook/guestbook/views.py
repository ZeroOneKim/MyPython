from wsgiref.util import request_uri
from django.shortcuts import render, redirect
import guestbook
from guestbook.models import Guestbook
import math
import os
from django.db.models import Q
#from django.utils.http import urlquote

def list(request):
    try:
        searchkey = request.POST['searchkey']
    except:
        searchkey='name'

    try:
        search=request.POST['search']
    except:
        search=''
        
    if searchkey == 'name_content':
        gbList=Guestbook.objects.filter(Q(name__contains=search) | Q(content__contains = search)).order_by('-idx')
    elif searchkey == 'name':
        gbList = Guestbook.objects.filter(Q(name__contains=search)).order_by('-idx')
    elif searchkey == 'content':
        gbList = Guestbook.objects.filter(Q(content__contains=search)).order_by('-idx')
    
    try:
        msg=request.GET['msg']
    except:
        msg=''

    return render(request, 'guestbook/list.html', 
    {'gbList': gbList, 'gbCount':len(gbList), 'searchkey':searchkey, 'search':search, 'msg':msg})

def write(request):
    return render(request, 'guestbook/write.html')

def insert(request):
    row = Guestbook(name = request.POST['name'], email=request.POST['email'], passwd =request.POST['passwd'], 
    content = request.POST['content'])
    row.save()
    return redirect('/guestbook')

def passwd_check(request):
    id = request.POST['idx']  #쓴 글에대한 idx 번호
    pwd = request.POST['passwd'] #비밀번호
    row = Guestbook.objects.get(idx=id) 
    if row.passwd==pwd:
        return render(request, 'guestbook/edit.html', {'row': row})
    else:
        return redirect('/guestbook/?msg=error')

def update(request):
    id=request.POST['idx']
    row=Guestbook(idx= id, name= request.POST['name'], email = request.POST['email'], passwd = request.POST['passwd'], content = request.POST['content'])
    row.save()
    return redirect('/guestbook')

def delete(request):
    id = request.POST['idx']
    Guestbook.objects.get(idx=id).delete()  #삭제 코드
    return redirect('/guestbook')