from pip._vendor.requests import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from coments.models import Message
from coments.selectors import get_message, get_messages_by_user
from coments.services import create_message, create_user, react_message


class MesageDetailApi(APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Message
            fields = ('id', 'user', 'message', 'likes', 'dislikes')

    def get(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = get_message(**serializer.validated_data)

        serializer = self.OutputSerializer(message)

        return Response(serializer.data)


class MesageListApi(APIView):
    class InputSerializer(serializers.Serializer):
        user = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Message
            fields = ('id', 'user', 'message', 'likes', 'dislikes')

    def get(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        messages = get_messages_by_user(**serializer.validated_data)

        serializer = self.OutputSerializer(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        mail = serializers.CharField()
        message = serializers.CharField()

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

        user = create_user(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class MessageReactionCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        message_id = serializers.IntegerField()
        reaction = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        react_message(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)