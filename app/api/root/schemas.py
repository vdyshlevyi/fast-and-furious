from app.schemas import BaseSchema


class RootSchema(BaseSchema):
    message: str


class HealthCheckSchema(BaseSchema):
    result: str
