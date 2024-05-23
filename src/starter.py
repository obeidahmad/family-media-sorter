import json

from models.input_model import InputModel, ManagingMode
from utils.media_manager import MediaManager
from utils.metadata_reader import MetadataReader


class Starter:
    def __init__(self, **kwargs):
        self.input: InputModel = InputModel(**kwargs)

    def start(self):
        success_read, error_read = MetadataReader(self.input.exiftool_path).read_metadata_directory(self.input.input_path)

        if self.input.mode == ManagingMode.CREATE:
            path_mapping_dict: dict = MediaManager(success_read, self.input.output_path, self.input.mode.value).generate_management_dict()

            exec_dict: dict = {
                "options": {
                    "delete_empty_dir": False,
                    "delete_error_files": False,
                    "mode": "move"
                },
                "path_mapping": path_mapping_dict,
                "errors": error_read
            }

            with open(self.input.exec_file_path, 'w') as fp:
                json.dump(exec_dict, fp, ensure_ascii=False, indent=4)
        else:
            pass
