from django import forms
from .models import Blog

class BlogPost(forms.ModelForm) : # 모델을 기반으로한 입력공간
    class Meta :
        model = Blog # Blog 모델을 기반으로한 공간을 만들건데
        fields = ['title', 'body'] # title과 body를 입력받을 수 있는 공간

# class BlogPost(forms.Form): # 그냥 만든 입력공간 씐기방기
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'), ('3','three')]) # one이라는 값에는 1이라고 간주하겠다.
