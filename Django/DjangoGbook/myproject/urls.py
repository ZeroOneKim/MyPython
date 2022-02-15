from django.contrib import admin
from django.urls import path, include
from myproject import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('member/', include('member.urls')),
    path('guestbook/', include('guestbook.urls')),
]
