from adaptix import Retort
from tomli import load as tomli_load

from app.config import Config


def read_toml(path: str) -> dict:
    with open(path, "rb") as f:
        return tomli_load(f)


def config_loader(config_path) -> Config:
    retort = Retort()
    data = read_toml(config_path)

    config = retort.load(data, Config)

    return config
