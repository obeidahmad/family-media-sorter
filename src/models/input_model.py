from enum import Enum

from pydantic import BaseModel, model_validator
from typing_extensions import Self


class ManagingMode(str, Enum):
    EXECUTE = "execute"
    CREATE = "create"


class InputModel(BaseModel):
    input_path: str | None = None
    output_path: str | None = None
    exiftool_path: str | None = None
    exec_file_path: str = "./exec_file.json"
    mode: ManagingMode

    @model_validator(mode='after')
    def validate(self) -> Self:
        if self.mode == ManagingMode.CREATE:
            if not [x for x in (self.input_path, self.output_path, self.exiftool_path) if x is None]:
                # Todo: Make sure paths are correct
                pass
            else:
                print("input, output and exiftool paths cannot be null when in create mode!")
        else:
            if self.exec_file_path is not None:
                # Todo: Make sure path is correct
                pass
            else:
                print("exec file path cannot be null when in create mode!")
        return self
