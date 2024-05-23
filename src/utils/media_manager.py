import json
import os
import shutil
from enum import Enum

from flatten_dict import unflatten, flatten

from models.info_model import InfoModel


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

    def manage_file(self, info: InfoModel) -> str:
        new_path: str = self.create_new_path(info)

        if self.mode in [ManagingMode.MOVE, ManagingMode.COPY]:
            dir_name: str = os.path.dirname(new_path)
            os.makedirs(dir_name, exist_ok=True)

            if self.mode == ManagingMode.MOVE:
                shutil.move(info.abs_path, new_path)
                if len(os.listdir(dir_name)) == 0:
                    os.rmdir(dir_name)
            else:
                shutil.copy(info.abs_path, new_path)

        return new_path

    def manage_files(self) -> dict:
        paths: dict = {self.manage_file(metadata): metadata.abs_path for metadata in self.info_list}
        path_dict_tree = unflatten(paths, splitter='path')

        flat = flatten(path_dict_tree, reducer='path')

        print(json.dumps(flat, indent=4))
        print()
        print()

        return path_dict_tree
