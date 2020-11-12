from django.urls import path

from coments.views import (
    MesageDetailApi,
    MesageListApi,
    MessageCreateApi,
    MessageReactionCreateApi, UserCreateApi,
    )

urlpatterns = [
    path("messages/<str:user>/", MesageListApi.as_view(), name="messages-user", ),
    path("message/<int:pk>/", MesageDetailApi.as_view(), name="message", ),
    path("create_message/", MessageCreateApi.as_view(), name="create-message", ),
    path("react_message/<int:pk>/", MessageReactionCreateApi.as_view(), name="react-message", ),
    path("create_user/", UserCreateApi.as_view(), name="create-user", ),
    ]