import os

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from info_model import InfoModel


class MainModel(BaseModel):
    output_path: str
    info_list: list[InfoModel]

    @model_validator(mode='after')
    def create_new_path(self) -> Self:
        if self.output_path.startswith("."):
            self.output_path = os.getcwd() + self.output_path[1:]
        return Self
