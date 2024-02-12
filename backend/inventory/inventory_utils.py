import base64
from django.core.files.base import ContentFile

class InvUtils:
    @staticmethod
    def base64_to_image(base64_image, image_name):
        try :
            format, imgstr = base64_image.split(';base64,') 
            ext = format.split('/')[-1] 
            image = ContentFile(base64.b64decode(imgstr), name=image_name+'.' + ext)
            return image
        except :
            return None 