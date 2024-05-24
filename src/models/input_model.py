import os.path
import sys
from enum import Enum

from exiftool import ExifTool
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
            if not [x for x in (self.input_path, self.output_path) if x is None]:
                if not os.path.isdir(self.input_path):
                    sys.exit(f"{self.input_path} is not a valid path!")
            else:
                sys.exit("input, output paths cannot be null when in create mode!")

            try:
                ExifTool(executable=self.exiftool_path)
            except FileNotFoundError:
                sys.exit("ExifTool was not found!")

        else:
            if self.exec_file_path is not None:
                if not os.path.isfile(self.exec_file_path):
                    sys.exit(f"{self.exec_file_path} is not a valid path!")
            else:
                sys.exit("exec file path cannot be null when in create mode!")
        return self
