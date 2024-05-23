from enum import Enum

from flatten_dict import unflatten

from models.info_model import InfoModel
from models.input_model import ManagingMode


class MediaManagingMode(str, Enum):
    COPY = "copy"
    MOVE = "move"


class MediaManager:
    def __init__(self, info_list: list[InfoModel], output_dir: str, mode: str):
        self.info_list: list[InfoModel] = info_list
        self.output_dir: str = output_dir
        self.mode: ManagingMode = ManagingMode(mode)

    def create_new_path(self, info: InfoModel) -> str:
        year = info.og_date.year
        month = info.og_date.month
        file_name = info.og_date.strftime('%Y.%m.%d_%H-%M-%S.%f')

        return f"{self.output_dir}/{year}.{str(month).zfill(2)}/{info.camera_model_name}/{file_name}.{info.file_extension}"

    # def manage_file(self, info: InfoModel) -> str:
    #     new_path: str = self.create_new_path(info)
    #
    #     if self.mode in [MediaManagingMode.MOVE, MediaManagingMode.COPY]:
    #         dir_name: str = os.path.dirname(new_path)
    #         os.makedirs(dir_name, exist_ok=True)
    #
    #         if self.mode == MediaManagingMode.MOVE:
    #             shutil.move(info.abs_path, new_path)
    #             if len(os.listdir(dir_name)) == 0:
    #                 os.rmdir(dir_name)
    #         else:
    #             shutil.copy(info.abs_path, new_path)
    #
    #     return new_path
    #
    # def manage_files(self) -> dict:
    #     pass

    def generate_management_dict(self) -> dict:
        paths: dict = {}
        for new_path, old_path in [(self.create_new_path(metadata), metadata.abs_path) for metadata in self.info_list]:
            if new_path not in paths:
                paths[new_path] = old_path
            else:
                counter = 0
                while True:
                    other_path = f"{new_path}_{counter}"
                    if other_path in paths:
                        counter += 1
                    else:
                        paths[other_path] = old_path
                        break

        return unflatten(paths, splitter='path')
