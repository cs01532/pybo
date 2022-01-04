from django.urls import path

from . import views #현재 패키지의 views모듈(views.py)을 import

app_name = 'pybo' # 도메인명:포트번호/앱이름(=pybo), 즉, http://localhost:8000/pybo/xxx 요청시

urlpatterns = [
    path('',views.index, name='index'), # xxx가 비었으면, views.py의 index라는 함수를 호출, http://localhost:8000/pybo/ 라는 url에 index라는 별칭을 부여. 추후, 템플릿에서 <a href="{% url 'detail' question.id %}"> 태그에서 detail 이라는 name을 사용가능하다.
    path('<int:question_id>/',views.detail, name='detail'), # xxx가 int형의 question_id라는 수자이면, views.py의 detail라는 함수를 호출, http://localhost:8000/pybo/숫자../라는 패턴의 url에 detail이라는 별칭을 부여함.
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'), # xxx가 answer/create/int형 question_id라는 숫자이면, views.py의 answer_create라는 함수를 호출, http://localhost:8000/pybo/answer/create/숫자.../ 라는 패턴의 url에는 answer_create라는 별핑을 부여함.
               ]