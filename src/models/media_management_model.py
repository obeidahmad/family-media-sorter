from enum import Enum

from pydantic import BaseModel


class MediaManagementMode(str, Enum):
    COPY = "copy"
    MOVE = "move"


class MediaManagementModel(BaseModel):
    mode: MediaManagementMode
    delete_empty_dir: bool
    delete_error_files: bool
    delete_exec_file: bool
