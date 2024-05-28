import argparse
import json
import os

from models.input_model import InputModel, ManagingMode
from models.media_management_model import MediaManagementModel
from utils.exec_file_creator import ExecFileCreator
from utils.media_manager import MediaManager
from utils.metadata_reader import MetadataReader

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", default="create")

parser.add_argument("-t", "--exiftool-path", required=False)
parser.add_argument("input_path", nargs='?')
parser.add_argument("output_path", nargs='?')

parser.add_argument("exec_file_path", default="./exec_file.json")


# Todo: Transform into executable


def main():
    input_params: InputModel = InputModel(**vars(parser.parse_args()))

    if input_params.mode == ManagingMode.CREATE:
        success_read, error_read = MetadataReader(input_params.exiftool_path).read_metadata_directory(input_params.input_path)

        print("Generating Management Dict ...")
        exec_dict: dict = ExecFileCreator(success_read, input_params.output_path, error_read).generate_management_dict()
        print("Management Dict Generated.")

        print("Saving Execution File ...")
        with open(input_params.exec_file_path, 'w') as fp:
            json.dump(exec_dict, fp, ensure_ascii=False, indent=4, sort_keys=True)
        print("Execution File Saved.")
    else:
        print("Reading Execution File ...")
        with open(input_params.exec_file_path, 'r') as fp:
            exec_data = json.load(fp)

        parameters = MediaManagementModel(**exec_data["$options"])
        print("Read Successfully.")
        MediaManager(parameters, exec_data["path_mapping"], list(exec_data["errors"].keys())).manage_files()

        if parameters.delete_exec_file:
            os.remove(input_params.exec_file_path)


if __name__ == "__main__":
    main()
