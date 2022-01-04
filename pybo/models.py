from django.db import models

# Create your models here.
# model은 데이터를 다룬다
# model의 모든 클래스는 db table의 필드 정보를 갖는다
# models에 작성한것은 선언일뿐, 실제 db 테이블을 생성하지는 않는다.
# 실제 테이블은
# 1. pybo앱을 config/settings.py의 INSTALLED_APPS 항목에 'pybo.apps.PyboConfig' 클래스(pybo/apps.py에 있음)를 추가하고
# 2. (가상환경)cmd에서 python manage.py makemigtations(pybo/migrations/0001_initial.py생성됨. 설계도임.), python manage.py migrate(실제 테이블생성)를 수행해 주어야 한다. ddl문은 python manage.py pybo 0001을 통해 확인가능

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject #Question.objects.all() 함수 호출시 <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>... 처럼 조회되니 불편하다.
                            #<QuerySet [<Question: pybo가 무엇인가요?>, <Question: 장고 모델 질문입니다.>]> 의 형태로 조회되게 하려고.

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
