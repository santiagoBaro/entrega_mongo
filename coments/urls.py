from django.urls import path
from .views import (
    MesageDetailApi,
    MesageListApi,
    MessageCreateApi,
    MessageReactionCreateApi, UserCreateApi,
    )

api_urlpatterns = [
    path("messages/", MesageListApi.as_view(), name="messages-user", ),
    path("message/", MesageDetailApi.as_view(), name="message", ),
    path("create_message/", MessageCreateApi.as_view(), name="create-message", ),
    path("react_message/", MessageReactionCreateApi.as_view(), name="react-message", ),
    path("create_user/", UserCreateApi.as_view(), name="create-user", ),
    ]