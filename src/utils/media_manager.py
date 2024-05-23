import os
import shutil

from flatten_dict import flatten

from models.media_management_model import MediaManagementModel, MediaManagementMode


class MediaManager:
    def __init__(self, media_management_params: MediaManagementModel, path_mapping: dict, errored_files: list):
        self.media_management_params: MediaManagementModel = media_management_params
        self.path_mapping: dict = path_mapping
        self.errored_files: list = errored_files

    def manage_file(self, old_path: str, new_path: str) -> str:
        dir_name: str = os.path.dirname(new_path)
        os.makedirs(dir_name, exist_ok=True)

        if self.media_management_params.mode == MediaManagementMode.MOVE:
            shutil.move(old_path, new_path)
            if self.media_management_params.delete_empty_dir:
                dir_to_delete: str = os.path.dirname(old_path)
                while len(os.listdir(dir_to_delete)) == 0:
                    os.rmdir(dir_to_delete)
                    dir_to_delete = os.path.dirname(dir_to_delete)
        else:
            shutil.copy(old_path, new_path)

        return new_path

    def manage_files(self) -> None:
        paths: dict = flatten(self.path_mapping, reducer="path")

        for new_path, old_path in paths.items():
            self.manage_file(old_path, new_path)

        if self.media_management_params.delete_error_files:
            for error_path in self.errored_files:
                os.remove(error_path)
                if self.media_management_params.delete_empty_dir:
                    dir_to_delete: str = os.path.dirname(error_path)
                    while len(os.listdir(dir_to_delete)) == 0:
                        os.rmdir(dir_to_delete)
                        dir_to_delete = os.path.dirname(dir_to_delete)
