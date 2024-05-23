import os
import datetime

from pydantic import BaseModel, model_validator
from typing_extensions import Self


class InfoModel(BaseModel):
    filename: str
    file_extension: str
    abs_path: str
    file_type: str
    camera_model_name: str
    og_date: datetime.datetime

    @model_validator(mode='after')
    def create_new_path(self) -> Self:
        if self.abs_path.startswith("."):
            self.abs_path = os.getcwd() + self.abs_path[1:]
        return self

    @staticmethod
    def from_exiftool_dict(exiftool_dict) -> "InfoModel":
        str_date = exiftool_dict["Create Date"].split("+")[0]
        try:
            og_date = datetime.datetime.strptime(str_date, "%Y:%m:%d %H:%M:%S.%f")
        except ValueError as e:
            if "does not match format" in str(e):
                og_date = datetime.datetime.strptime(str_date, "%Y:%m:%d %H:%M:%S")
            else:
                raise e

        try:
            camera_model_name = f"{exiftool_dict['Make'].replace(' ', '-')}_{exiftool_dict['Camera Model Name'].replace(' ', '-')}"
        except KeyError:
            camera_model_name = "unknown"

        return InfoModel(
            filename=exiftool_dict["File Name"],
            file_extension=exiftool_dict["File Type Extension"],
            abs_path=os.path.join(exiftool_dict["Directory"], exiftool_dict["File Name"]),
            file_type=exiftool_dict["MIME Type"].split("/")[0],
            camera_model_name=camera_model_name,
            og_date=og_date,
        )
