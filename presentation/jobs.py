from dishka.integrations.arq import DISHKA_APP_CONTAINER_KEY

from application.interface.service import IServiceLogic


async def some_jobs(ctx):
    container = ctx[DISHKA_APP_CONTAINER_KEY]
    service = await container.get(IServiceLogic)
    print(service())
