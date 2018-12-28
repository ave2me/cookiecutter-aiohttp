from aiohttp import web

from {{cookiecutter.project_name}}.views import dummy_handler


def register_routes(app: web.Application):
    """
    Register existing routes in the app instance.

    :param app: application instance
    """
    app.router.add_post("/index", dummy_handler)
