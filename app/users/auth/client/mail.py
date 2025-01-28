import json
import uuid
from dataclasses import dataclass

import aio_pika

from app.settings import Settings


@dataclass
class MailClient:
    settings: Settings

    async def send_welcome_email(self, to: str) -> None:
        connection = await aio_pika.connect_robust(self.settings.CELERY_BROKER_URL)
        email_body = {
            "message":"Welcome to taskmanager",
            "user_email": to,
            "subject": "Welcome message",
        }

        async with connection:
            channel = await connection.channel()
            message = aio_pika.Message(
                body = json.dumps(email_body).encode("utf-8"),
                correlation_id=str(uuid.uuid4())
            )
            await channel.default_exchange.publish(
                message=message,
                routing_key="email_queue"
            )

