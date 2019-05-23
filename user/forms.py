from django import forms

class registrationForm(forms.Form):
    email = forms.EmailField(label='email' , max_length=50)
    password = forms.CharField(label='password' , max_length=10)
    
    def clean_email(self):
        data = self.cleaned_data['email'] 
        if(data.split('@')[1] != "gmail.com" ):
            raise forms.ValidationError("Invalid email address")
        return data
    def clean_password(self):
        data = self.cleaned_data['password']
        if(not data.isalnum()):
            raise forms.ValidationError('Password not alphanumeric')
        return data
class loginForm(forms.Form):
    email = forms.EmailField(label='email' , max_length=50)
    password = forms.CharField(label='password' , max_length=10)
    
    def clean_email(self):
        data = self.cleaned_data['email'] 
        if(data.split('@')[1] != "gmail.com" ):
            raise forms.ValidationError("Invalid email address")
        return data
    def clean_password(self):
        data = self.cleaned_data['password']
        if(not data.isalnum()):
            raise forms.ValidationError('Password not alphanumeric')
        return data
