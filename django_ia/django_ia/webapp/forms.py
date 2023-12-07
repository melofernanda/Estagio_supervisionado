from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

USERNAME_HELP_TEXT = '''
<span class="form-text text-muted">
    <small>
        No máximo 150 caracteres. letras, números e @/./_/-/_ somente
    </small>
</span>
'''
PASSWORD1_HELP_TEXT = '''
<ul class="form-text text-muted small">
    <li>
        Sua senha não pode ser similar a outras informações pessoais.
    </li>

    <li>
        Sua senha precisa conter no mínimo 8 caracteres.
    </li>

    <li>
        Sua senha não pode ser uma senha comum.
    </li>

    <li>
        Sua senha não pode conter somente números.
    </li>
</ul>
'''
PASSWORD2_HELP_TEXT = '''
<ul class="form-text text-muted">
    <small>
        Para verificação é necessário digitar a mesma senha.
    </small>
</ul>
'''

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Endereço de email"
            }
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Primeiro Nome"
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Sobrenome"
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
            )
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Usuário"
        self.fields["username"].label = ""
        self.fields["username"].help_text = USERNAME_HELP_TEXT

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = PASSWORD1_HELP_TEXT

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirma o password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = PASSWORD2_HELP_TEXT
