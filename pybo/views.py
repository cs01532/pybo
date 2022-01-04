#from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question # views는 로직, 로직에서 데이터를 다루기 위해, models 모듈의 Question 클래스를 import

# views.py는 로직을 담당한다.

def index(request):
#    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')  # Question이라는 모델은 models.py에 정의되어 있다. 모든 데이터를 조회함. models.py에서 보면 모든 subject만 리턴해준다.
    context = {'question_list':question_list}                  # 템플릿에서 받아서 쓸 데이터를 딕셔너리 형태로! 조회한 모든 데이터를 딕셔너리 형태로 저장.
    return render(request, 'pybo/question_list.html', context) # 템플릿은 templates/pybo/question_list.html이다. config/settings.py에 TEMPLATES = [ ... 'DIRS': [BASE_DIR / 'templates'], ... ] 정의되어 있다.

def detail(request, question_id):
    """
    pybo 내용 출력
    """
#    question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) # Question이라는 모델은 models.py에 정의되어 있다., question_id가 없는 숫자이면, 404에러를 뱉기위해
    context = {'question':question} # 호출될 템플릿에서 받아서 사용할 data를 딕셔너리 형태로 만들어서 넘긴다!
    #print(context)
    return render(request,'pybo/question_detail.html',context) # 사용할 템플릿은 templates/pybo/question_detail.html이다

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id) # Question이라는 모델은 models.py에 정의되어 있다., question_id가 없는 숫자이면, 404에러를 뱉기위해
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id) # name='detail' 이라는 url패턴을 urls.py에서 찾아서, 해당 url주소 패턴에 해당하는 로직을 views.py에서 찾아서 동작시켜라.