import logging
import typing
from http import HTTPStatus
from json import JSONDecodeError

from aiohttp import web
from marshmallow import Schema, UnmarshalResult, ValidationError

logger = logging.getLogger(__name__)


@web.middleware  # noqa: Z110
async def deserializer_middleware(
    request: web.Request,
    handler: typing.Callable[[web.Request], typing.Awaitable[web.Response]],
) -> web.Response:
    """
    Deserialize request's json body if it has one.

    :param request: request object
    :param handler: handler function
    :return:
    """
    if not request.can_read_body:
        return await handler(request)
    try:
        body = await request.text()
        unmarshalled_body: UnmarshalResult = get_schema(handler).loads(body)
        user_data = unmarshalled_body.data
    except JSONDecodeError:
        return web.json_response(
            {"ok": False, "errors": {"body": "Cannot deserialize JSON."}},
            status=HTTPStatus.UNPROCESSABLE_ENTITY.value,
        )
    except ValidationError as exc:
        logger.exception(exc)
        return web.json_response(
            {"ok": False, "errors": exc.messages},
            status=HTTPStatus.UNPROCESSABLE_ENTITY.value,
        )
    request["user_data"] = user_data

    return await handler(request)


_schemas = {}


def get_schema(handler: typing.Any) -> Schema:  # noqa: Z110
    """
    Get a schema for a given handler.

    :param handler: handler function
    :return: schema instance
    """
    return _schemas[handler.__name__]
