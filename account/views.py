from django.shortcuts import render
from account.models import User
from django.views import View
from django.urls import reverse_lazy
from account.forms import CustomLoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

class RegisterView(View):
    '''
    User registration view class
    '''
    template_name = 'auth/register.html'

    def get(self, request):
        form = RegisterForm()  # Create an instance of the form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)  # Bind POST data to the form instance
        if form.is_valid():  # Check if form data is valid
            # Retrieve cleaned data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Create the user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            return redirect('/account/login/')
        else:
            # If form is not valid, render the form with errors
            return render(request, self.template_name, {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            # eger form valid ise
            # kullanıcıyı kontrol et
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Eğer kullanıcı varsa anasayfaya yönlendir
            form.add_error(None, 'Hatalı Kullanıcı Bilgileri!') # Eğer hata varsa hatayı forma ekle
            return render(request, 'auth/login.html', context={'form': form})  # Eğer hata varsa hatayı goster
        return render(request, 'auth/login.html', context={'form': form})
    else:
        form = CustomLoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('account:login')