import uuid
from datetime import datetime

from ninja import Schema


class BaseSchema(Schema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None


class ErrorSchema(Schema):
    detail: str
