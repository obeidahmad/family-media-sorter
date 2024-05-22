from models.info_model import InfoModel
from models.input_model import InputModel
from utils.media_manager import MediaManager
from utils.metadata_reader import MetadataReader


class Starter:
    def __init__(self, **kwargs):
        self.input: InputModel = InputModel(**kwargs)

    def start(self):
        pass

    def read_metadata(self) -> tuple[list[InfoModel], list[dict]]:
        return MetadataReader(self.input.exiftool_path).read_metadata_directory(self.input.input_path)

    def manage_media(self):
        MediaManager()
