from rest_framework import serializers
from . import models

class ExplorerUserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.User
    fields = (
      'profile_image',
      'username',
      'name',
    )