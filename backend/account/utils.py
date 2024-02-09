# from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
# from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import re
class Utils :

    @staticmethod
    def generate_token(user):
        token = {'access' : str(RefreshToken.for_user(user).access_token), 'refresh' : str(RefreshToken.for_user(user))}
        return token
    
    # @staticmethod
    # def sendLink(email, request, relative_link, subject, message): 
    #     # from email fetch user
    #     print(email)
    #     try :
    #         user = CustomUser.objects.get(email = email)
        
    #     # if email not found or user is already verified
    #     except :
    #         return False
        
    #     else :        
    #         # else
    #         # generate an access token for the user
    #         token = RefreshToken.for_user(user).access_token

    #         # absolute url to verify that user
    #         current_site = str(get_current_site(request))
    #         absurl = 'http://'+ current_site + relative_link + "?token=" + str(token)

            
    #         # send email to user to verify itself    
    #         body = f'Hii {user.first_name+" "+user.last_name}\n\n{message}\n\nLINK : {absurl}\n\nThis link is valid only for 1 hour.\nTHANKYOU !!'
            
    #         send_mail(
    #             subject, 
    #             body,
    #             settings.EMAIL_HOST_USER,
    #             [email],
    #             fail_silently=False 
    #             )
            
    #         return (True, 'email sent successfully')
        
   
    @staticmethod
    def validate_password(value):
    # valid password : >= 8 char, must contains lower at least 1 char of each 
    # lower(alpha), upper(alpha), (number), (symbols)
    

        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        if  not re.search("\d", value) :
            raise serializers.ValidationError("Password must contains a number 0 to 9")
        
        if not re.search("[a-z]", value) :
            raise serializers.ValidationError("Password must contain a lowercase letter ")
        
        if not re.search("[A-Z]", value) :
            raise serializers.ValidationError("Password must contain a uppercase letter")
        
        if not re.search(r"[@#$%^&*()\-_+=.]", value):
            raise serializers.ValidationError("Password must contain a special character(@,#,$,%,^,&,*,(,),-,_,+,=,.)")

        return make_password(value)    # return hashed password