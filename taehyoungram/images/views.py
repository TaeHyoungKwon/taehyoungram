from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image, Comment, Like
from .serializers import ImageSerializer, CommentSerializer, LikeSerializer



class Feed(APIView):
    
    def get(self, request, format=None):
        user = request.user
        follwoing_users = user.following.all()

        image_list = []

        for following_user in follwoing_users:
            user_images = following_user.images.all()[:2]

            for image in user_images:
                image_list.append(image)
        
        sorted_list = sorted(image_list, key=lambda image:image.created_at, reverse=True)
        serializer = ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):
    
    def get(self, request, image_id, format=None):
        
        try:
            found_image = Image.objects.get(id=image_id)
        except Image.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            pre_exisiting_like = Like.objects.get(
            creator=request.user,
            image=found_image
            )
            pre_exisiting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Like.DoesNotExist:
            new_like = Like.objects.create(
                creator=request.user,
                image=found_image
            )
            new_like.save()

            return Response(status=status.HTTP_201_CREATED)


class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):
        
        user = request.user

        try:
            found_image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=user, image=found_image)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
