from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Kullanıcı Adı', widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adı'}))
    password = forms.CharField(max_length=128, label='Şifre', widget=forms.PasswordInput(attrs={'placeholder': 'Şifre'}))
    
    class Meta:
        model = AuthenticationForm
        fields = ('username', 'password')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label='Kullanıcı Adı', widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adı'}))
    password = forms.CharField(max_length=128, label='Şifre', widget=forms.PasswordInput(attrs={'placeholder': 'Şifre'}))
    password2 = forms.CharField(max_length=128, label='Şifre Doğrula', widget=forms.PasswordInput(attrs={'placeholder': 'Şifre Doğrula'}))
    email = forms.EmailField(max_length=254, label='E-posta', widget=forms.EmailInput(attrs={'placeholder': 'E-posta'}))
    first_name = forms.CharField(max_length=30, label='Ad', widget=forms.TextInput(attrs={'placeholder': 'Ad'}))
    last_name = forms.CharField(max_length=150, label='Soyad', widget=forms.TextInput(attrs={'placeholder': 'Soyad'}))

    class Meta:
        model = forms.ModelForm
        fields = ('username', 'password', 'password2' 'email', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        if password and password2 and password != password2:
            raise forms.ValidationError('Şifreler eşleşmiyor!')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Bu e-posta adresi kullanımda!')
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Bu kullanıcı adı kullanımda!')
        return cleaned_data