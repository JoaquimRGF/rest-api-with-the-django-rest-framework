from rest_framework import serializers

from status.models import Status
from accounts.api.serializers import UserPublicSerializer

from rest_framework.reverse import reverse as api_reverse





class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    # user_id = serializers.HyperlinkedRelatedField(
    #     source='user',
    #     lookup_field='username',
    #     view_name='api-user:detail',
    #     read_only=True)

    # username = serializers.SlugRelatedField(source='user', read_only=True, slug_field='email')

    class Meta:
        model = Status
        fields = [
            'uri',
            # 'user_id',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']  # GET usado em conjunção com func perform_create em views

    # def get_user(self, obj):
    #     request = self.context.get('request')  # para meter os urls a funcionar
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={"request": request}).data

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-status:detail', kwargs={'id': obj.id}, request=request)

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way to long.")
    #     return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")
        return data


class StatusInlineUserSerializer(StatusSerializer):
    #uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image'
        ]

    # def get_uri(self, obj):
    #     return "/api/status/{id}/".format(id=obj.id)


# class StatusInlineUserSerializer(serializers.ModelSerializer):
#     uri = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Status
#         fields = [
#             'uri',
#             'id',
#             'user',
#             'content',
#             'image'
#         ]
#
#     def get_uri(self, obj):
#         return "/api/status/{id}/".format(id=obj.id)