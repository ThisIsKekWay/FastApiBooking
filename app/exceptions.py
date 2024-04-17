from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UserDataIsWrongException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен просрочен"


class TokenIsMissingException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class TokenFormatIsWrongException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class UserIsMissingException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не осталось свободных номеров"


class DateConflictException(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Дата въезда не может быть больше даты выезда"


class DateTooLongBookingPeriodException(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Слишком большой срок аренды"


class DateBlastFromThePastException(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Нельзя забронировать номер с датой заезда раньше текущей даты"


class DateTooFarPlanningException(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Нельзя планировать дальше чем на год"
