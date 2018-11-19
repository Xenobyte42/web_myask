from django import forms

from quesions.models import Question

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharFiled(widget=forms.PasswordInput)


    # clean _ <field name>
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if "!" in username:
            raise forms.ValidationError('username')
        return username

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'long'})

    class Meta:
        model = Question
        exclude = 'author'
