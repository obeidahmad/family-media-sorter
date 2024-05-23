import argparse

from starter import Starter

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", default="create")

parser.add_argument("exiftool_path", nargs='?')
parser.add_argument("input_path", nargs='?')
parser.add_argument("output_path", nargs='?')

parser.add_argument("exec_file_path", default="./exec_file.json")


args = vars(parser.parse_args())

Starter(**args).start()
