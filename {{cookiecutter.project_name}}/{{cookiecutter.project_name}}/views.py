import logging

from aiohttp import web

logger = logging.getLogger(__name__)


async def dummy_handler(request: web.Request) -> web.Response:
    """
    Example request handler.

    :param request: request object
    """
    user_data: dict = request["user_data"]

    return web.json_response({"ok": True})
