from coments.models import Message, User


def create_user(
    *,
    mail: str,
    password: str
) -> User:
    user = User.objects.filter(mail=mail)
    if not user:
        user = User.objects.create(email=mail, password=password)

    return user


def create_message(
    *,
    mail: str,
    message: str
) -> User:
    user = User.objects.filter(mail=mail)
    if user:
        message = Message.objects.create(user=user, message=message)

    return message


def react_message(
    *,
    reaction: str,
    message_id: str
) -> User:
    message = Message.objects.get(message_id)
    if message:
        if reaction == "like":
            message.likes = message.likes + 1
        else:
            message.dislikes = message.dislikes + 1

    message.save()
    return message
