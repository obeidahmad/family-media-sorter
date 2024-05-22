import os
import shutil
from enum import Enum

from models.info_model import InfoModel
from models.input_model import InputModel

class ManagingMode(str, Enum):
    COPY = "copy"
    MOVE = "move"
    SHOW = "show"


class MediaManager:
    def __init__(self, info_list: list[InfoModel], output_dir: str, mode: str):
        self.info_list: list[InfoModel] = info_list
        self.output_dir: str = output_dir
        self.mode: ManagingMode = ManagingMode(mode)

    def create_new_path(self, info: InfoModel) -> str:
        year = info.og_date.year
        month = info.og_date.month
        file_name = info.og_date.strftime('%Y.%m.%d_%H-%M-%S')

        return f"{self.output_dir}/{year}.{str(month).zfill(2)}/{info.camera_model_name}/{file_name}.{info.file_extension}"

    def manage_file(self, info: InfoModel) -> None:
        new_path: str = self.create_new_path(info)
        dir_name: str = os.path.dirname(new_path)

        if self.mode in [ManagingMode.MOVE, ManagingMode.COPY]:
            os.makedirs(dir_name, exist_ok=True)
            if self.mode == ManagingMode.MOVE:
                shutil.move(info.abs_path, new_path)
                if len(os.listdir(dir_name)) == 0:
                    os.rmdir(dir_name)
            else:
                shutil.copy(info.abs_path, new_path)
        else:
            split_path = new_path.split("/")
            

    def move_files(self) -> None:
        for metadata in self.info_list:
            self.move_file(metadata)
