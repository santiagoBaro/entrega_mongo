from pip._vendor.requests import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from coments.models import Message
from coments.selectors import get_message, get_messages_by_user
from coments.services import create_message, create_user, react_message


class MesageDetailApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Message
            fields = ('id', 'user', 'message', 'likes', 'dislikes')

    def get(self, request, message_id):
        message = get_message(id=message_id)

        serializer = self.OutputSerializer(message)

        return Response(serializer.data)


class MesageListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Message
            fields = ('id', 'user', 'message', 'likes', 'dislikes')

    def get(self, request, user_mail):
        messages = get_messages_by_user(user_mail=user_mail)

        serializer = self.OutputSerializer(messages)

        return Response(serializer.data)


class MessageCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        mail = serializers.CharField()
        message = serializers.TextField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_message(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class UserCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        mail = serializers.CharField()
        password = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_user(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class MessageReactionCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        message_id = serializers.CharField()
        reaction = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        react_message(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)