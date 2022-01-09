from django import forms
from pybo.models import Question, Answer

# form 이란: url요청시, 파라미터 값 체크, HTML 자동생성, 데이터 저장(연결된 model을 이용하여) form은 일반form, 모델form으로 나뉨. 데이터저장+추후 템플릿에서 HTML생성
class QuestionForm(forms.ModelForm): #이 클래스는 모델form을 상속함(forms.ModelForm)
    class Meta: #QuestionForm은 모델폼으로, inner클래스가 필수임. 사용할 모델(Question)과 모델(Question)의 속성을 아래 처럼 적여야 함.
        model = Question # QuestionForm이라는 모델폼은 Question이라는 모델(데이터를 담당)과 연결되는 폼이다! 이 폼에서 사용할 모델:Question
        fields = ['subject','content'] # QuestionForm이라는 모델폼은 속성으로 Question모델의 subject와 content라는 속성 2개를 사용한다! 이 폼에서 사용할 속성:subject,content
        labels = {
            'subject': '제목',
            'content': '내용',
        }
"""
        widgets = {
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control','rows':10})
        }
"""

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }