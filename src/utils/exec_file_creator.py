from flatten_dict import unflatten
from tqdm import tqdm

from models.info_model import InfoModel
from models.media_management_model import MediaManagementModel


class ExecFileCreator:
    def __init__(self, info_list: list[InfoModel], output_dir: str, error_list: dict[str, str]):
        self.info_list: list[InfoModel] = info_list
        self.output_dir: str = output_dir
        self.error_list: dict[str, str] = error_list

    def create_new_path(self, info: InfoModel) -> str:
        year = info.og_date.year
        month = info.og_date.month
        file_name = info.og_date.strftime('%Y.%m.%d_%H-%M-%S.%f')

        return f"{self.output_dir}/{year}.{str(month).zfill(2)}/{info.camera_model_name}/{file_name}.{info.file_extension}"

    def generate_mapping_dict(self) -> dict:
        paths: dict = {}
        for new_path, old_path in tqdm([(self.create_new_path(metadata), metadata.abs_path) for metadata in self.info_list]):
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

    def generate_management_dict(self) -> dict:
        mapping_dict = self.generate_mapping_dict()
        parameters = dict(MediaManagementModel(mode="copy", delete_empty_dir=True, delete_error_files=False, delete_exec_file=False))
        return {
            "$options": parameters,
            "path_mapping": mapping_dict,
            "errors": self.error_list
        }


