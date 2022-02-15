from django.contrib import admin
from guestbook.models import Guestbook #모델.py에서 만든 내용을 admin에 적용

class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'passwd', 'content')

admin.site.register(Guestbook, GuestbookAdmin)
