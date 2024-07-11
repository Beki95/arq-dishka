from typing import (
    final,
)

from arq import cron
from arq.connections import RedisSettings
from dishka.integrations.arq import setup_dishka

from app.config import Config
from infra.arq_integration.settings import _WorkerSettings as WorkerSettings
from infra.di.di_providers import get_container
from infra.loader import config_loader
from presentation.jobs import some_jobs
from presentation.tasks import some_tasks

_CONFIG_PATH: final = './config/dev.toml'


def init_arq_worker(worker: WorkerSettings):

    config: Config = config_loader(_CONFIG_PATH)
    redis_conf = config.redis
    REDIS_SETTINGS = RedisSettings(
        host=redis_conf.host,
        port=redis_conf.port,
        username=redis_conf.username,
        password=redis_conf.password,
        database=redis_conf.database,
    )
    funcs = [some_tasks]
    worker.functions.extend(funcs)
    worker.redis_settings = REDIS_SETTINGS

    jobs = [
        cron(some_jobs, second={0, 30, 59})
    ]
    worker.cron_jobs.extend(jobs)
    container = get_container()
    setup_dishka(container=container, worker_settings=worker)

    return worker


init_arq_worker(WorkerSettings)
