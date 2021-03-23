from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': '제목을 입력하세요',
                'maxlength': 10,
            }
        ),
        error_messages={
            'required': '데이터를 입려하세요',
        }
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': '내용을 입력하세요',
                'rows': 5,
                'cols': 30,
            }
        ),
        error_messages={
            'required': '데이터를 입력하세요',
        }
    )

    class Meta:
        model = Notice
        fields = '__all__'