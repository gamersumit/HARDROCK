
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CustomUserSerializer, LoginSerializer
from .models import CustomUser
from .utils import Utils
import json


# Create your views here.

class RegisterView(generics.GenericAPIView) :
    serializer_class = CustomUserSerializer

    def post(self, request):
        # create a user
        try :
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({'status': True, 'message' : 'Registration Successful'}, status =200)
        
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status = 400)
        
        # sending email verification link ---- >

        # relative_link = reverse('email_verify')
        # subject = "Verification Mail  for Django testing app"
        # message = "This email is sent to verify if it\'s you who registered on our djangowebsite.\nTo verify please click on the link below."
       
        # send mail
        # status = Utils.sendLink(serializer.data['email'], request, relative_link, subject, message)
        
        # if status[0] :
        #     return Response({'status': True, 'data': serializer.data,'message' : 'User Registered Successfully'}, status =200)
        
        # if status[1] == 'email not found':
        #     return Response({'status': False, 'data': "",'message' : 'Email Not Found'}, status = 400)

class LoginView(generics.GenericAPIView) :
    serializer_class = LoginSerializer

    def post(self, request):
        # get login data from request
        request_body_str = request.body.decode('utf-8')

        # Parse the JSON data
        data = json.loads(request_body_str)

        # Extract the values
        email = data.get('email', None)
        password = data.get('password', None)
        is_admin = data.get('is_admin', None)    

        if (email is None) or (password is None) or (is_admin is None) :
             return Response({'status': False, 'user': None,'message' : 'provided crdentials are not in proper format'}, status = 400)
        
        if CustomUser.objects.filter(email = email).exists():
            user = CustomUser.objects.get(email=email)
            print(user.is_admin)
            print(is_admin)
            if user.is_admin == is_admin:

                if user.check_password(password):
                
                    token = Utils.generate_token(user)
                    return Response({'status': True, 'token' : token, 'message' : 'Logged in Successfully'}, status =200)
       
                else :
                    return Response({'status': False, 'message' : 'Invalid Password'}, status = 400)
                
            else :
                return Response({'status': False, 'message' : 'User is trying to login with different status'}, status = 400)

        else :
            return Response({'status': False, 'message' : 'Email Not Found'}, status = 400)
        


# class EmailVerifyView(generics.GenericAPIView):

#     def get(self, request):
#         # fetch token from url
#         token = request.GET.get('token')

#         try:
#             # try to decode token and then get payload attached to the token
#             payload = AccessToken(token).payload
#             # get usrd id from payload and get user associated with that id
#             user = CustomUser.objects.get(id=payload['user_id'])
            
#             # check if user is already verified or not
#             if not user.is_verified :
#                 # if not than verify user and return succesful response
#                 user.is_verified = True
#                 user.save()
#                 return Response({"status" : True, "message" : "user verified successfully"}, status = 200)
           
#             # if user is already verfied than send response accordingly
#             return Response({"status" : False, "message" : "user already verified"}, status = 400)
        
#         # if decoding token fails than handle the response accordingly
#         except :
#             return Response({"status": False, "message": 'Invalid link or Link Expired'}, status=400)

# class SendVerificationLinkView(generics.GenericAPIView):
    
#     def get(self, request):
#         relative_link = reverse('email_verify')
#         subject = "Verification Mail  for Django testing app"
#         message = "This email is sent to verify if it\'s you who registered on our djangowebsite.\nTo verify please click on the link below."
#         # send mail
#         status = Utils.sendLink(request.GET.get('email'), request, relative_link, subject, message)

#         if status :
#             return Response({'status': True, 'message' : 'Link Sent Successfully'}, status =200)
        
#         return Response({'status': False,'message' : 'Email Not Found'}, status = 400)

# class ForgotPasswordView(generics.GenericAPIView):
#     serializer_class = PasswordSerializer

#     def put(self, request):
#         token = request.GET.get('token')

#         try:
#             # Try to decode the token and get the payload attached to it
#             payload = AccessToken(token).payload
#             user_id = payload.get('user_id')

#             if not user_id:
#                 raise ValueError("User ID not found in token payload")

#             # Get the user associated with the user ID
#             user = CustomUser.objects.get(id=user_id)
            

#             # Handle resetting the user's password here
        
#             serializer = self.serializer_class(user, data = {'password' : request.data.get('password')}, partial=True)
            
#             serializer.is_valid(raise_exception = True)
#             serializer.save()
            
#             return Response({"status": True, "message": "Password reset successfully"}, status=200)
        
#         except Exception as e:
#             return Response({"status": False, "message": str(e)}, status=400)
        
# class SendForgotPasswordLinkView(generics.GenericAPIView):
#      def get(self, request):
#         print("********************************")

#         relative_link = reverse('forgot_password')
#         subject = "Password Reset Mail for Django test app"
#         message = "To Reset your password please click on the link below."

#         try :
#             body = json.loads(request.body.decode('utf-8'))
#             email = body['email']
#         except Exception as e :
#              return Response({'status': False, 'user': None,'message' : 'Something is Wrong With Request Body'}, status = 400)
        
        
#         # send mail
#         status = Utils.sendLink(email, request, relative_link, subject, message)
        
#         if status :
#             return Response({'status': True, 'message' : 'Link Sent Successfully'}, status =200)
        
        
#         return Response({'status': False,'message' : 'Email Not Found'}, status = 400)


        
            
      

# SHORT NAMING :
user_register_view = RegisterView.as_view()
signin_view = LoginView.as_view()

# email_verify_view = EmailVerifyView.as_view()
# send_verification_link_view = SendVerificationLinkView.as_view()
# forgot_password_view = ForgotPasswordView.as_view()
# send_forgot_password_link_view = SendForgotPasswordLinkView.as_view()