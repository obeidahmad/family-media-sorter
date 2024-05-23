import argparse

from starter import Starter

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", default="show")

parser.add_argument("-d", "--detect-video", action="store_true")

parser.add_argument("-l", "--logs", action="store_true")

parser.add_argument("exiftool_path")
parser.add_argument("input_path")
parser.add_argument("output_path")

args = vars(parser.parse_args())

Starter(**args).start()
