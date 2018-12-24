from django import forms

from .models import Profile, Question


class SettingsForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'nickname', 'avatar_path',)


class LoginForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'password',)


class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'description', 'tag_list',)


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('username', 'email', 'nickname', 'password', 'avatar_path',)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords does not match")
