from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Video, Profile, FriendRequest, Message, User
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username', 'id')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):  # hash化したuserデータをデータベースに入れる(・create_userテーブル)
        user = get_user_model().objects.create_user(**validated_data)

        return user


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video', 'thum', 'like', 'dislike']


class ProfileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'userPro', 'created_on', 'img')
        extra_kwargs = {'userPro': {'read_only': True}}


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'askFrom', 'askTo', 'approved')
        extra_kwargs = {'askFrom': {'read_only': True}}


class FriendsFilter(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        request = self.context['request']
        friends = FriendRequest.objects.filter(Q(askTo=request.user) & Q(approved=True))

        list_friend = []
        for friend in friends:
            list_friend.append(friend.askFrom.id)
        queryset = User.objects.filter(id__in=list_friend)
        return queryset


class MessageSerializer(serializers.ModelSerializer):

    receiver = FriendsFilter()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'message')
        extra_kwargs = {'sender': {'read_only': True}}
