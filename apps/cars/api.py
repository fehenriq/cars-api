import uuid

from ninja import Router
from ninja.pagination import LimitOffsetPagination, paginate

from apps.cars.schema import CarCreateSchema, CarSchema, CarUpdateSchema
from apps.cars.service import CarService
from utils.base_schema import ErrorSchema
from utils.jwt import JWTAuth, decode_jwt_token

car_router = Router(auth=JWTAuth())
car_service = CarService()


@car_router.post("", response={200: CarSchema, 201: CarSchema, 400: ErrorSchema})
def create_car(request, payload: CarCreateSchema):
    decode_jwt_token(request.headers.get("Authorization"))
    return car_service.create_car(payload)


@car_router.get("", response={200: list[CarSchema], 401: ErrorSchema, 404: ErrorSchema})
@paginate(LimitOffsetPagination)
def list_cars(request):
    decode_jwt_token(request.headers.get("Authorization"))
    return car_service.list_cars()


@car_router.get(
    "/{car_id}", response={200: CarSchema, 401: ErrorSchema, 404: ErrorSchema}
)
def get_car(request, car_id: uuid.UUID):
    decode_jwt_token(request.headers.get("Authorization"))
    return car_service.get_car(car_id)


@car_router.patch(
    "/{car_id}", response={200: CarSchema, 401: ErrorSchema, 404: ErrorSchema}
)
def update_car(request, car_id: uuid.UUID, payload: CarUpdateSchema):
    decode_jwt_token(request.headers.get("Authorization"))
    return car_service.update_car(car_id, payload)


@car_router.delete(
    "/{car_id}", response={200: None, 401: ErrorSchema, 404: ErrorSchema}
)
def delete_car(request, car_id: uuid.UUID):
    decode_jwt_token(request.headers.get("Authorization"))
    return car_service.delete_car(car_id)
