from django.views.generic import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from .models import Profile
from django import forms


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

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class    = ProfileForm 
    success_url   = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class    = EmailForm
    success_url   = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        formData = super().get_form(form_class)
        formData.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control','placeholder':'Email'}
        )
        return formData