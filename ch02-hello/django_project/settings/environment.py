from pathlib import Path  # noqa: D100

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)  # noqa: COM812
)
env.prefix = "DJANGO_"

site_root = environ.Path(__file__) - 3  # Root of the project

env_file = site_root(".env")
if Path.exists(env_file):  # pragma: no cover
    environ.Env.read_env(env_file=env_file)
