import os

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from info_model import InfoModel


class InputModel(BaseModel):
    input_path: str
    output_path: str
    exiftool_path: str
    move: bool
    copy: bool
    detect_video: bool
    logs: bool
    # info_list: list[InfoModel]

    @model_validator(mode='after')
    def create_new_path(self) -> Self:
        if self.output_path.startswith("."):
            self.output_path = os.getcwd() + self.output_path[1:]

        if self.input_path.startswith("."):
            self.input_path = os.getcwd() + self.input_path[1:]
        # Todo: handle input path does not exist
        if not os.path.isdir(self.input_path):
            pass

        if self.copy:
            self.move = False

        # Todo: handle exiftool_path is Null
        if self.exiftool_path is None:
            pass
        elif self.exiftool_path.startswith("."):
            self.exiftool_path = os.getcwd() + self.exiftool_path[1:]

        return self
