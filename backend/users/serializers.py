import collections
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_extensions.serializers import PartialUpdateSerializerMixin

from .models import *


class UserSerializer(PartialUpdateSerializerMixin, ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']