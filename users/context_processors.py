from users.forms.login_form import LoginForm
from users.forms.register_form import RegisterForm

def login_form(request):
    return {
        "login_form": LoginForm(request)
    }

def register_form(request):
    return {

        'register_form': RegisterForm(auto_id='False')
    }