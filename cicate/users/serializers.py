
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True, style={'input_type': 'password', 'placeholder': 'password'})
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True, 
                                            style={'input_type': 'password', 'placeholder': 'Confirm password'})

    class Meta:
        model = User
        fields = [ 'id','name', 'middle_name', 'surname','Username', 'email', 'date_of_birth', 
                  'degree', 'country_of_birth', 'native_language', 'country_of_citizenship',
                 'usertype', 'password', 'password2']
       
        
    #def validate(self, value):
        #email = value.get ('email', '')
        #Username= value.get ('Username', ' ')

    def validate(self, value):
        if value.get('password') != value.get('password2'):
            raise serializers.ValidationError("password don't match") 

        elif value.get('password') == value.get('password2'):
                value['password'] = make_password(
                value.get('password')
            )

        value.pop('password2') # add this
        return value
        
        

    
       

        #if not username.isalnum():
            #raise serializers.ValidationError(
                #'The username should  only contain alphanumeric characters '
            #)
        #return  value
    #def create(self, validated_data):
        #return User.objects.create(**validated_data)
    
    
    
    #def create(self, Validated_data):
        #return User.objects.create_user(**Validated_data)
    



class InstitutionRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True, style={'input_type': 'password', 'placeholder': 'password'})
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True, 
                                            style={'input_type': 'password', 'placeholder': 'Confirm password'})

    class Meta:
        model = User
        fields = [ 'id','name', 'middle_name', 'Username','surname', 'email', 'institution_name', 
                  'Acronym', 'biography', 'type_of_unversity', 'location', 'linkedin', 
                  'twitter', 'facebook','usertype', 'password', 'password2']

    #def validate(self, value):
        #email = value.get ('email', '')
        #username= value.get ('username', ' ')

        #if not username.isalnum():
            #raise serializers.ValidationError(
                #'The username should  only contain alphanumeric characters '
            #)
        #return  value
    
    #def validate(self, value):
        #email = value.get ('email', '')
        #username= value.get ('username', ' ')
    def validate(self, value):
        if value.get('password') != value.get('password2'):
            raise serializers.ValidationError("Those password don't match") 

        elif value.get('password') == value.get('password2'):
                value['password'] = make_password(
                value.get('password')
            )

        value.pop('password2') # add this
        return value
    
    
    
    #def create(self, Validated_data):
        #return User.objects.create_user(**Validated_data)



