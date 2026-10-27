from typing import List, Optional
from pydantic import BaseModel


class Event(BaseModel):
    id: Optional[int] = None
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Запуск проекта Кумушбаевой",
                "image": "https://linktomymage.com/image.png",
                "description": "Обсуждаем итоги разработки планировщика FastAPI.",
                "tags": ["python", "fastapi", "planner"],
                "location": "Google Meet"
            }
        }