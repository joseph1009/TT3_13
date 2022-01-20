import collections
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_extensions.serializers import PartialUpdateSerializerMixin

from .models import *



class PostingSerializer(PartialUpdateSerializerMixin, ModelSerializer):
    # posting_num = serializers.SerializerMethodField(label='posting_number')
    # relative_posting_time = serializers.SerializerMethodField(label='relative_posting_time')
    # relative_reply_time = serializers.SerializerMethodField(label='relative_reply_time')
    formated_posting_time = serializers.SerializerMethodField(label='formated_posting_time')
    formated_reply_time = serializers.SerializerMethodField(label='formated_reply_time')
    user_nickname = serializers.SerializerMethodField(label='user_nickname')
    user_head = serializers.SerializerMethodField(label='user_head')


    class Meta:
        model = Posting
        fields = ['posting_id', 'user_head', 'posting_user', 'user_nickname',
                  'reply_num','theme', 'posting_content', 'category_id',
                  'posting_thumb_num', 'formated_posting_time', 'formated_reply_time']

    def get_formated_posting_time(self, obj):
        return obj.posting_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_formated_reply_time(self, obj):
        return obj.reply_time.strftime("%Y-%m-%d %H:%M:%S")

    # def get_posting_num(self, obj):
    #     return Posting.objects.filter(category_id=obj.category_id).count()

    # def get_relative_posting_time(self, obj):
    #     return calculate_relative_time(obj.posting_time)
    #
    # def get_relative_reply_time(self, obj):
    #     return calculate_relative_time(obj.reply_time)

    def get_user_nickname(self, obj):
        return obj.posting_user.nickname

    def get_user_head(self, obj):
        return obj.posting_user.head