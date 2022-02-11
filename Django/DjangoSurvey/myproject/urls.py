from django.contrib import admin
from django.urls import path, include, re_path
from myproject import views

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('member/', include('member.urls')),
    path('survey/', include('survey.urls')),
]

if settings.DEBUG: # Mode of Debug
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] # r=정규표현식 -> __debug__의 url이 포함되어있으면 불러오기

# from django.conf.urls import url 은 Django 4.0들어서며 지원하지 않는 것으로 보인다.
# url(r'^) 형태가아닌 re_path를 임포트해주고 url대신 re_path를 사용함으로 보인다. 출처:StackOverFlow