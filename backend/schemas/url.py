from typing import Optional, Any

from pydantic import BaseModel


class URLSchema(BaseModel):
    long: Optional[str]

    class Collection:
        name = "url"

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk/",
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
