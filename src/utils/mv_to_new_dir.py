import os
import shutil

from models.info_model import InfoModel
from models.main_model import MainModel


def create_new_path(info: InfoModel, output_path: str) -> str:
    year = info.og_date.year
    month = info.og_date.month
    file_name = info.og_date.strftime('%Y.%m.%d_%H-%M-%S')

    return f"{output_path}/{year}.{str(month).zfill(2)}/{info.camera_model_name}/{file_name}.{info.file_extension}"


def move_file(info: InfoModel, output_path: str) -> None:
    new_path: str = create_new_path(info, output_path)
    dir_name: str = os.path.dirname(new_path)

    os.makedirs(dir_name, exist_ok=True)

    shutil.move(info.abs_path, new_path)

    if len(os.listdir(dir_name)) == 0:
        os.rmdir(dir_name)


def move_files(info: MainModel) -> None:
    for metadata in info.info_list:
        move_file(metadata, info.output_path)
