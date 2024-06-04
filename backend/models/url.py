from beanie import Document


class URLModel(Document):
    short: str
    long: str

    class Config:
        json_schema_extra = {
            "example": {
                "short": "ABC1234",
                "long": "https://llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk/",
            }
        }

    class Settings:
        name = "url"
