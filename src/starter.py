import json
import os

from models.input_model import InputModel, ManagingMode
from models.media_management_model import MediaManagementModel
from utils.exec_file_creator import ExecFileCreator
from utils.media_manager import MediaManager
from utils.metadata_reader import MetadataReader


class Starter:
    def __init__(self, **kwargs):
        self.input: InputModel = InputModel(**kwargs)

    def start(self):
        if self.input.mode == ManagingMode.CREATE:
            success_read, error_read = MetadataReader(self.input.exiftool_path).read_metadata_directory(self.input.input_path)

            exec_dict: dict = ExecFileCreator(success_read, self.input.output_path, error_read).generate_management_dict()

            with open(self.input.exec_file_path, 'w') as fp:
                json.dump(exec_dict, fp, ensure_ascii=False, indent=4, sort_keys=True)
        else:
            with open(self.input.exec_file_path, 'r') as fp:
                exec_data = json.load(fp)

            parameters = MediaManagementModel(**exec_data["$options"])
            MediaManager(parameters, exec_data["path_mapping"], list(exec_data["errors"].keys())).manage_files()

            if parameters.delete_exec_file:
                os.remove(self.input.exec_file_path)
