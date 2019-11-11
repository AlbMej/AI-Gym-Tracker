from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='gym_app:post-detail', )
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']