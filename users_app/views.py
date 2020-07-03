from django.shortcuts import render
from users_app.models import User
from users_app import forms
# Create your views here.


def list_users(request):

    list_with_users = User.objects.order_by('first_name')

    users = {
        "list_with_users": list_with_users,
    }

    return render(request, template_name="users_app/users_page.html", context=users)


def home(request):
    return render(request, template_name='users_app/index.html')


def forms_view(request):
    form = forms.UserForm()

    if request.method == "POST":
        form = forms.UserForm(request.POST)

        if form.is_valid():
            new_user = User(first_name=form.cleaned_data['first_name'],
                            second_name=form.cleaned_data['second_name'],
                            email=form.cleaned_data['email'])
            new_user.save()
            return home(request)

    return render(request, 'users_app/form_page.html', {'form': form})
