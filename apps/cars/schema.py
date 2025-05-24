import uuid

from ninja import Schema

from apps.users.schema import UserSchema
from utils.base_schema import BaseSchema


class CarSchema(BaseSchema):
    name: str
    year: int
    description: str
    sold: bool
    user: UserSchema


class CarCreateSchema(Schema):
    name: str
    year: int
    description: str
    sold: bool | None = False
    user: uuid.UUID


class CarUpdateSchema(Schema):
    name: str | None = None
    year: int | None = None
    description: str | None = None
    sold: bool | None = False
