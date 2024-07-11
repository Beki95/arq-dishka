from dishka import (
    AsyncContainer,
    Provider,
    Scope,
    provide,
)
from dishka import (
    make_async_container,
)

from application.interface.session import ISession
from application.service import (
    IServiceLogic,
    ServiceLogic,
)
from infra.db.sessions import Session


class SessionProvider(Provider):
    scope = Scope.APP

    @provide(scope=Scope.APP)
    async def get_session(self) -> ISession:
        return Session()


class ServiceProvider(Provider):

    @provide(scope=Scope.APP)
    async def get_service(self, session: ISession) -> IServiceLogic:
        return ServiceLogic(session=session)


def get_container() -> AsyncContainer:
    provider = SessionProvider()
    service_provider = ServiceProvider()
    return make_async_container(provider, service_provider)
