from django.db import models
from django.contrib.auth.hashers import Argon2PasswordHasher

# Create your models here.
class User(models.Model):
    email = models.CharField(name='email' , unique=True , max_length=50 , null=False)
    password = models.CharField(name='password' , max_length=10 , null=False)
    
    def save(self):
        passwordHasher = Argon2PasswordHasher()
        self.password = passwordHasher.encode(self.password , passwordHasher.salt())
        super().save()

    def verify_email(self , p):
        try:
            if isinstance(p.objects.get(email = self.email) , p):
                return True
        except p.DoesNotExist:
            return False
    
    def verify_password(self , p):
        passwordHasher = Argon2PasswordHasher()
        try:
            if passwordHasher.verify(self.password , p.objects.get(email = self.email).password):
                return True
        except p.DoesNotExist:
            return False
    