from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import ExplorerUserSerializer

class ExploerUsers(APIView):

    def get(self, request, format=None):
        last_five = User.objects.all().order_by('-date_joined')[:5]
        serializer = ExplorerUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)