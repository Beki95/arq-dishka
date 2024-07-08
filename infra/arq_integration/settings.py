from dishka.integrations.arq import (
    job_end,
    job_start,
)


class _WorkerSettings:
    on_job_start = job_start(None)
    on_job_end = job_end(None)
    functions = []
    cron_jobs = []
    redis_settings = ...
