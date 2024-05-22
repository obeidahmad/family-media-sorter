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
        try:
            og_date = datetime.datetime.strptime(exiftool_dict["Date/Time Original"], "%Y:%m:%d %H:%M:%S.%f")
        except:
            og_date = datetime.datetime.strptime(exiftool_dict["Date/Time Original"], "%Y:%m:%d %H:%M:%S")

        return InfoModel(
            filename=exiftool_dict["File Name"],
            file_extension=exiftool_dict["File Type Extension"],
            abs_path=os.path.join(exiftool_dict["Directory"], exiftool_dict["File Name"]),
            file_type=exiftool_dict["MIME Type"].split("/")[0],
            camera_model_name=f"{exiftool_dict['Make'].replace(' ', '-')}_{exiftool_dict['Camera Model Name'].replace(' ', '-')}",
            og_date=og_date,
        )
