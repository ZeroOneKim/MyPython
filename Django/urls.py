from django.contrib import admin
from django.urls import path, include
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('blog/', include('blog.urls'))
]

'''View/ urls Not read
다행히 5시간 헤맸지만 결과는 참담하다. 최신 장고버전 4.0.1 공식 사이트
path('blog/', include('blog/urls')) 로 설명하나, 제대로 동작하지않았고, 슬래시를 온점으로 바꾼다.

해결 에러 : [WinError 123] 파일 이름, 디렉터리 이름 또는 볼륨 레이블 구문이 잘못되었습니다: '<frozen importlib._bootstrap>'
이는 95%이상이 Settings.py에 잘못 적용시켜논 에러지만 url path를 불러 오지 못할때도 동작한다.


'''