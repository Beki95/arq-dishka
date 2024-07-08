from arq import cron
from arq.connections import RedisSettings
from dishka.integrations.arq import setup_dishka
from dishka.integrations.fastapi import setup_dishka

from infra.arq_integration.settings import _WorkerSettings as WorkerSettings
from presentation.di.di_providers import get_container
from presentation.jobs import some_jobs
from presentation.tasks import some_tasks


def init_arq_worker(worker: WorkerSettings):
    REDIS_SETTINGS = RedisSettings()
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
