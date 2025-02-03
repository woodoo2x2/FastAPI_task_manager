import asyncio

import httpx
from aiokafka import AIOKafkaProducer
from fastapi import Depends
from fastapi import security, Security, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.broker.producer import BrokerProducer
from app.cache.access import get_redis_connection
from app.cache.logic import CacheTask
from app.database.database import get_db_session
from app.exceptions import TokenExpiredException, TokenNotCorrectException
from app.settings import Settings
from app.tasks.logic import TaskLogic
from app.tasks.service import TaskService
from app.users.auth.client.google import GoogleClient
from app.users.auth.client.mail import MailClient
from app.users.auth.client.yandex import YandexClient
from app.users.auth.service import AuthService
from app.users.logic import UserLogic
from app.users.service import UserService

event_loop = asyncio.get_event_loop()


async def get_broker_producer() -> BrokerProducer:
    settings = Settings()
    return BrokerProducer(
        producer=AIOKafkaProducer(
            bootstrap_servers=settings.BROKER_URL,
            loop=event_loop,
        ),
        email_topic=settings.EMAIL_TOPIC,
    )


async def get_mail_client(broker_producer: BrokerProducer = Depends(get_broker_producer)) -> MailClient:
    return MailClient(settings=Settings(), broker_producer=broker_producer)


async def get_task_logic(db: AsyncSession = Depends(get_db_session)):
    return TaskLogic(db)


async def get_cache_logic(redis_conn=Depends(get_redis_connection)):
    return CacheTask(redis_conn)


async def get_task_service(cache_task: CacheTask = Depends(get_cache_logic),
                           task_logic: TaskLogic = Depends(get_task_logic)):
    return TaskService(cache_task, task_logic)


async def get_async_client():
    return httpx.AsyncClient()


async def get_yandex_client(async_client: httpx.AsyncClient = Depends(get_async_client)) -> YandexClient:
    return YandexClient(settings=Settings(), async_client=async_client)


async def get_google_client(async_client: httpx.AsyncClient = Depends(get_async_client)) -> GoogleClient:
    return GoogleClient(settings=Settings(), async_client=async_client)


async def get_user_logic(db_session: AsyncSession = Depends(get_db_session)) -> UserLogic:
    return UserLogic(db_session=db_session)


async def get_auth_service(user_logic: UserLogic = Depends(get_user_logic),
                           google_client: GoogleClient = Depends(get_google_client),
                           yandex_client: YandexClient = Depends(get_yandex_client),
                           mail_client: MailClient = Depends(get_mail_client)) -> AuthService:
    return AuthService(user_logic, google_client, yandex_client, mail_client)


async def get_user_service(user_logic: UserLogic = Depends(get_user_logic),
                           auth_service: AuthService = Depends(get_auth_service),
                           mail_client: MailClient = Depends(get_mail_client)) -> UserService:
    return UserService(user_logic=user_logic, auth_service=auth_service, mail_client=mail_client)


reusable_oauth2 = security.HTTPBearer()


async def get_request_user_id(request: Request,
                              auth_service: AuthService = Depends(get_auth_service),
                              token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
                              ) -> int:
    try:
        user_id = auth_service.get_user_id_from_token(token.credentials)
    except TokenExpiredException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    except TokenNotCorrectException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    return user_id
