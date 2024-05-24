import glob
import os

from exiftool import ExifToolHelper
from tqdm import tqdm

from models.info_model import InfoModel


class MetadataReader:
    def __init__(self, exiftool_path: str | None):
        self.exiftool_path = exiftool_path

    def read_metadata(self, images_path: list[str]) -> list[dict]:
        with ExifToolHelper(executable=self.exiftool_path, common_args=None, check_execute=False) as et:
            return et.get_metadata(images_path)

    def read_metadata_directory(self, images_dir_path: str) -> tuple[list[InfoModel], dict]:
        print("Extracting Media ...")
        images_path = [x for x in glob.glob(f"{images_dir_path}/**/*", recursive=True) if os.path.isfile(x)]
        print("Media Extracted.")

        raw_metadata: list[dict] = self.read_metadata(images_path)

        metadata_list: list[InfoModel] = []
        corrupt_list: dict = {}
        print("Reading Metadata ...")
        for metadata in tqdm(raw_metadata):
            if "Error" in metadata:
                corrupt_list[os.path.join(metadata["Directory"], metadata["FileName"])] = {"message": metadata["Error"], "data": metadata}
            else:
                try:
                    metadata_list.append(InfoModel.from_exiftool_dict(metadata))
                except Exception as e:
                    corrupt_list[os.path.join(metadata["Directory"], metadata["FileName"])] = {"message": f"{type(e).__name__}: {e}", "data": metadata}
        print("Metadata Read.")

        print(f"{len(corrupt_list)} corrupted file(s) found.")

        return metadata_list, corrupt_list
