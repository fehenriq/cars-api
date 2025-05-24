import uuid
from http import HTTPStatus

from ninja.errors import HttpError

from apps.cars.models import Car
from apps.users.service import UserService


class CarService:
    def __init__(self):
        self.user_service = UserService()

    @staticmethod
    def get_car_by_id(car_id: uuid.UUID) -> Car:
        return Car.objects.filter(id=car_id).first()

    @staticmethod
    def get_all_cars() -> list[Car]:
        return Car.objects.all()

    def create_car(self, payload) -> Car:
        user = self.user_service.get_user_object(user_id=payload.user)
        new_car = Car.objects.create(
            name=payload.name,
            year=payload.year,
            description=payload.description,
            sold=payload.sold,
            user=user,
        )

        return new_car

    def list_cars(self) -> list[Car]:
        if not (cars := self.get_all_cars()):
            raise HttpError(HTTPStatus.NOT_FOUND, "Nenhum carro encontrado")

        return list(cars)

    def get_car(self, car_id: uuid.UUID) -> Car:
        if not (car := self.get_car_by_id(car_id=car_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Carro não encontrado")

        return car

    def update_car(self, car_id: uuid.UUID, payload) -> Car:
        if not (car := self.get_car_by_id(car_id=car_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Carro não encontrado")

        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(car, attr, value)
        car.save()

        return car

    def delete_car(self, car_id: uuid.UUID) -> None:
        if not (car := self.get_car_by_id(car_id=car_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Carro não encontrado")
        car.delete()
