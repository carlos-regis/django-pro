import os

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
env.prefix = "DJANGO_"

site_root = environ.Path(__file__) - 3  # Root of the project

env_file = site_root(".env")
if os.path.exists(env_file):  # pragma: no cover
    environ.Env.read_env(env_file=env_file)
