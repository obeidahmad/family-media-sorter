import os

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from utils.media_manager import ManagingMode


class InputModel(BaseModel):
    input_path: str
    output_path: str
    exiftool_path: str
    mode: ManagingMode
    detect_video: bool
    logs: bool

    @model_validator(mode='after')
    def create_new_path(self) -> Self:
        self.output_path = os.path.abspath(self.output_path)
        self.input_path = os.path.abspath(self.input_path)
        # Todo: handle input path does not exist
        if not os.path.isdir(self.input_path):
            pass

        # Todo: handle exiftool_path is Null
        if self.exiftool_path is None:
            pass

        return self
