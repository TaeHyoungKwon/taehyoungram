from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer

class ListAllImages(APIView):
    
    def get(self, request, format=None):
        
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return Response(data=serializer.data)
