from aiohttp import ClientSession, web


async def fetch(url: str, client: ClientSession) -> dict:
    """
    Send get request to specified url.

    :param url: request url
    :param client: client session
    :return: deserialized response json
    """
    async with client.get(url) as response:
        return await response.json()


async def fetch_post(url: str, client: ClientSession, json_body: dict) -> dict:
    """
    Send post request to specified url with provided json.

    :param url: request url
    :param client: client session
    :param json_body: body dict that will be serialized to json
    :return: deserialized response json
    """
    async with client.post(url, json=json_body) as response:
        return await response.json()


async def api_client(app: web.Application):
    """
    Init API client.

    :param app: application instance
    """
    async with ClientSession() as client:
        app["api_client"] = client
        yield
