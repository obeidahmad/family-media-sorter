import json

from models.info_model import InfoModel
from models.input_model import InputModel
from utils.media_manager import MediaManager
from utils.metadata_reader import MetadataReader


class Starter:
    def __init__(self, **kwargs):
        self.input: InputModel = InputModel(**kwargs)

    def start(self):
        info, corrupt = self.read_metadata()
        self.manage_media(info)
        print()
        print()
        print(f"corrupt: {json.dumps(corrupt, indent=4)}")

    def read_metadata(self) -> tuple[list[InfoModel], list[dict]]:
        return MetadataReader(self.input.exiftool_path).read_metadata_directory(self.input.input_path)

    def manage_media(self, info_list: list[InfoModel]) -> None:
        manager = MediaManager(info_list, self.input.output_path, self.input.mode.value)

        print(json.dumps(manager.manage_files(), indent=4))
