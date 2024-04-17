from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_booking_confirmation_message(
        booking: dict,
        email_to: EmailStr
):
    email = EmailMessage()

    email["Subject"] = "Недавнее бронирование"
    email["From"] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>Подтвердите бронирование</h1>
            Вы забронировали с {booking["date_from"]} по {booking["date_to"]}
        """,
        subtype="html"
    )
    return email
