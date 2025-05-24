import uuid
from http import HTTPStatus

from ninja.errors import HttpError

from apps.users.models import CustomUser
from apps.users.schema import UserSchema


class UserService:
    @staticmethod
    def build_user_response(user: CustomUser):
        user_data = UserSchema(id=user.id, email=user.email, name=user.name)

        return user_data

    def get_user_by_id(self, user_id: uuid.UUID) -> CustomUser:
        return CustomUser.objects.filter(id=user_id).first()

    def get_user(self, user_id: uuid.UUID) -> UserSchema:
        if not (user := self.get_user_by_id(user_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Usuário não encontrado")

        user_data = self.build_user_response(user=user)

        return user_data

    def get_user_object(self, user_id: uuid.UUID) -> CustomUser:
        if not (user := self.get_user_by_id(user_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Usuário não encontrado")

        return user
