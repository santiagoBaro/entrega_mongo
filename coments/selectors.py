from collections import Iterable

from coments.models import Message, User


def get_users() -> Iterable[User]:
    return User.objects.all()


def get_messages() -> Iterable[Message]:
    return Message.objects.all()


def get_message(id) -> Message:
    return Message.objects.get(id=id)


def get_messages_by_user(user_mail) -> Iterable[Message]:
    return Message.objects.filter(mail=user_mail)