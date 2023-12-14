from django.contrib.auth.models import(AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
import uuid

class userManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('User must have a username')
        
        if email is None:
            raise TypeError('User must have a email')
        
        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password)
        user.save
        return user
    
    def create_institution_user(self, username, email, password=None):
        if username is None:
            raise TypeError('User must have a username')
        
        if email is None:
            raise TypeError('User must have a email')
        
        user = self.create_user(username, email, password)
        user.is_institution_user = True
        user.save
        return user

        
    
    def createsuperuser(self, username, email, password=None):
        if password is None:
            raise TypeError('password should not be none')
        
        user = self.createsuperuser(username, email, password)
        user.is_superuser = True
        user.is_staff =True
        user.save
        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    class UserType(models.TextChoices):
        CANDIDATE='candidate'
        INSTITUTION = 'institution'

    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    name = models.CharField(max_length=20, null=True)
    middle_name=models.CharField(max_length=20, blank=True)
    surname= models.CharField(max_length=20, unique=False, null=True)
    Username = models.CharField(max_length=256, unique=True, )
    date_of_birth=models.DateField(null=True)
    degree =models.CharField(max_length=200, null=True)
    country_of_birth=models.TextField(max_length=200, null=True)
    native_language=models.TextField(max_length=200, null = True)
    country_of_citizenship=models.TextField(max_length=200, null=True)
    email = models.EmailField(max_length=256, unique=True)
    institution_name =models.CharField(max_length=250, null=True)
    Acronym=models.CharField(max_length=50, blank=True)
    biography= models.TextField(max_length=500, blank=True)
    type_of_unversity=models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    linkedin= models.URLField(blank=True, null=True)
    twitter= models.URLField(blank=True)
    facebook= models.URLField(blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    usertype= models.CharField(max_length= 20, null=True, choices = UserType.choices, default=UserType.CANDIDATE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = userManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        return ''  