from django import forms
from .models import Article

# form은 사용자의 입력을 받기 위해 사용한다
# Django form 종류는 2가지가 있다.

# 1. Form
# - 사용자의 입력을 개발자가 직접 구성
#   -> Model의 필드와 관계없이 마음대로 구성할 수 있다
# - 장점: 내 마음대로 원하는 입력을 받을 수 있음
# - 단점: DB에 정확히 저장하기 위해서는 models를 완벽하게 파악
#       models.py 와 중복 코드가 많이 발생함

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30)
    # widget: form이 지원하는 기본 기능 외의 추가적인 동작을 원할 떄 사용
    content = forms.CharField(widget=forms.Textarea)


# 2. ModelForm
# - model에 정의된 필드만 입력받을 수 있음
# - 장점: 사용법이 쉬움
# - 단점: 내 마음대로 입력을 못 받음
class ArticleModelForm(forms.ModelForm):
    class Meta:
        # 특정 모델을 참조해야 한다
        model = Article
        # 원하는 필드만 입력을 받겠다
        # 튜플이나 리스트 형태로 작성
        # fields - ('title',)
        fields = ('title', 'content', 'author',)
        # 전체를 받으려면
        fields = '__all__'
        # 특정 필드 제외하고 입력을 받겠다
        # 마찬가지로 튜플(리스트) 형태로 작성
        exclude = ('author', )
