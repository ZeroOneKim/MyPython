#프레임워크에서 기본적으로 서버를 구축하고 앱을 만들 때 기본적인 틀 관리자는 편리하게 만들어졌다

-------------------------------settings.py-------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appName',    #yourapp
]
----------------------------------------------------------------------------------
--------------------------------models.py---------------------------------------
class ~~~(models.Model):
    idx = models.AutoField(primary_key=True)  #autoField 자동증가 일련번호
    name = models.CharField(max_length=50, blank=True, null=True)
-----------------------------------------------------------------------------------
--------------------------------admin.py----------------------------------------
from ~~~.models import ~~~2
#모델 등록
class ~~~3(admin.ModelAdmin):
    #관리자 화면에서 관리할 필드명
    list_display = ('like DB text')

admin.site.register(~~~2, ~~~3)
--------------------------------------------------------------------------------------
#이 작업한 모델클래스들을 DB에 반영가능
#python manage.py makemigrations/ migrate