from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        # 모델값 변경 없이 출력 명목 바꾸기
        labels = {
            'issue_a': 'RED TEAM',
            'issue_b': 'BLUE TEAM',
        }

class CommentForm(forms.ModelForm):
    # pick => RED TEAM 선택 시 0 저장, BLUE TEAM 선택 시 1 저장
    pick = forms.ChoiceField(choices=[('0', 'RED TEAM'), ('1', 'BLUE TEAM')])
    class Meta:
        model = Comment
        exclude= ('question', )