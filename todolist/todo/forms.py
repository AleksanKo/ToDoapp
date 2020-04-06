from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ToDoNode

class ToDoFormCreate(forms.ModelForm):
    todo = forms.CharField(label='',)
    class Meta:
        model = ToDoNode
        fields = ['todo',]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='')

    class Meta:
        model = User
        fields = ["username", "email", "password1", ]

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", ]

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', ]:
            self.fields[fieldname].help_text = None