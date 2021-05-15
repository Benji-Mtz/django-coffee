from django import forms

from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                               min_length=4, 
                               max_length=80,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                   'class': 'form-control',
                                   'id': 'email',
                                   'placeholder': 'Ejemplo: hola@gmail.com'
                               }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'id': 'password'
                               }))
    password2 = forms.CharField(label='Confirmar password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))
    
    # Esta funcion esta conectada al atributo usernama y verifica su existencia
    # con form.is_valid() 
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username already exists')
        
        else:
            return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email already exists')
        
        else:
            return email
        
    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'The password dont match')
            
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )