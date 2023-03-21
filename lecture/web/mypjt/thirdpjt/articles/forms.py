from django import forms

class ArticleForm(forms.form):
    title = forms.CharField(max_length=30)
    content = forms.CharField()