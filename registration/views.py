from django import forms
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    
    def get_form(self, *args):
        formData = super(SignUpView, self).get_form(*args)
        formData.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'}
        )
        formData.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2','placeholder':'Contraseña'}
        )
        formData.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2','placeholder':'Repetir Contraseña'}
        )
        return formData