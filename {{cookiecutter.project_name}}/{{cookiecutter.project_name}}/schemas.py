from marshmallow import (
    Schema,
    fields,
    validate,
)


class MongoConfigSchema(Schema):
    """
    Schema for MongoDB-related config section.
    """

    host = fields.String(required=True)
    port = fields.Integer(
        required=True, validate=validate.Range(min=1024, max=65535)  # noqa: Z432
    )
    db = fields.String(required=True)


class ConfigSchema(Schema):
    """
    Schema for config validation and deserialization.
    """

    mongo = fields.Nested(MongoConfigSchema, required=True)

    host = fields.String(required=True)
    port = fields.Integer(
        required=True, validate=validate.Range(min=1024, max=65535)  # noqa: Z432
    )
