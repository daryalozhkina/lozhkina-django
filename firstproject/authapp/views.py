from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render

from authapp.forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            pass

    form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)

