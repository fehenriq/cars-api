import uuid

from ninja import Router

from apps.users.schema import UserSchema
from apps.users.service import UserService
from utils.jwt import JWTAuth, decode_jwt_token

user_router = Router(auth=JWTAuth())
service = UserService()


@user_router.get("/{user_id}", response=UserSchema)
def retrieve_user(request, user_id: uuid.UUID):
    decode_jwt_token(request.headers.get("Authorization"))
    return service.get_user(user_id)
