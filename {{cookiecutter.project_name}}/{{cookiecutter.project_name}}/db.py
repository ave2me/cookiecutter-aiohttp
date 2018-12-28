from motor.motor_asyncio import AsyncIOMotorClient
from umongo import MotorAsyncIOInstance

from {{cookiecutter.project_name}}.config

instance = MotorAsyncIOInstance()


@instance.register
class {{cookiecutter.mongo_model_name}}(Document):
    """
    Document model for a {{cookiecutter.project_name}} collection.
    """
    class Meta:  # noqa: Z306
        collection_name = "{{cookiecutter.project_name}}"


async def mongo_client(app):
    """
    Handle mongo set up and tear down.

    :param app: application instance
    """
    conf = app["config"]["mongo"]
    client = AsyncIOMotorClient(host=conf["host"], port=conf["port"])
    db = client[conf["db"]]
    instance.init(db)
    await {{cookiecutter.mongo_model_name}}.ensure_indexes()
    app["db_client"]: AsyncIOMotorClient = client
    app["db"] = db
    yield
    await app["db_client"].close()
