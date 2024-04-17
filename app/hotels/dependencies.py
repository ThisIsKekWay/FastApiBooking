from datetime import date, datetime

from app.exceptions import (
    DateBlastFromThePastException,
    DateConflictException,
    DateTooFarPlanningException,
    DateTooLongBookingPeriodException,
)


def date_validator(date_from: date, date_to: date, location):
    print(location)
    if (date_from - datetime.utcnow().date()).days > 548:
        raise DateTooFarPlanningException
    if date_from <= datetime.utcnow().date():
        raise DateBlastFromThePastException
    if date_from > date_to:
        raise DateConflictException
    if (date_to - date_from).days > 31:
        raise DateTooLongBookingPeriodException
