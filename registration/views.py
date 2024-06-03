from django import forms
from django.views.generic import CreateView
from .forms import UserCreationFormWithEmail
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    
    def get_form(self, *args):
        formData = super(SignUpView, self).get_form(*args)
        formData.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mt-2','placeholder':'Nombre de usuario'}
        )
        formData.fields['email'].widget = forms.TextInput(
            attrs={'class':'form-control mt-4','placeholder':'Correo electrónico'}
        )
        formData.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mt-4','placeholder':'Contraseña'}
        )
        formData.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mt-4','placeholder':'Repetir Contraseña'}
        )
        return formData