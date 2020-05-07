from users.forms.login_form import LoginForm


def login_form(request):
    return {
        "login_form": LoginForm(request)
    }
