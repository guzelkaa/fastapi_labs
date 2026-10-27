from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Задача Кумушбаевой: сдать лабораторную №4"
            }
        }

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Задача Кумушбаевой: обновить отчёт по практике"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Задача Кумушбаевой: прочитать главу 1"},
                    {"item": "Задача Кумушбаевой: написать отчёт"}
                ]
            }
        }