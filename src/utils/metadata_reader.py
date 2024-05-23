import glob
import os
import subprocess

from tqdm import tqdm

from models.info_model import InfoModel


class MetadataReader:
    def __init__(self, exiftool_path: str):
        self.exiftool_path = exiftool_path

    def read_metadata(self, image_path: str) -> dict:
        metadata: dict = {}
        process = subprocess.Popen([self.exiftool_path, image_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        for tag in process.stdout:
            line = tag.strip().split(':', 1)
            metadata[line[0].strip()] = line[-1].strip()

        return metadata

    def read_metadata_directory(self, images_dir_path: str) -> tuple[list[InfoModel], dict]:
        print("Extracting Media ...")
        images_path = [x for x in glob.glob(f"{images_dir_path}/**/*", recursive=True) if os.path.isfile(x)]
        print("Media Extracted.")

        metadata_list: list[InfoModel] = []
        corrupt_list: dict = {}
        print("Reading Metadata ...")
        for image_path in tqdm(images_path):
            metadata: dict = self.read_metadata(image_path)
            if "Error" in metadata:
                corrupt_list[os.path.join(metadata["Directory"], metadata["File Name"])] = metadata["Error"]
            else:
                try:
                    metadata_list.append(InfoModel.from_exiftool_dict(metadata))
                except Exception as e:
                    corrupt_list[os.path.join(metadata["Directory"], metadata["File Name"])] = f"{type(e).__name__}: {e}"
        print("Metadata Read.")

        print(f"{len(corrupt_list)} corrupted file(s) found.")

        return metadata_list, corrupt_list
