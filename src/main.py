from utils.mv_to_new_dir import move_files
from models.main_model import MainModel
from utils.read_metadata import read_metadata_directory

input_ims_path = "./ims"
info_list, corrupt_list = read_metadata_directory(input_ims_path)

input_ims: MainModel = MainModel(
    output_path="./new_ims",
    info_list=info_list
)

move_files(input_ims)

print(corrupt_list)
