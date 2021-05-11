from pathlib import Path
from pprint import pprint

from src.file_sorter import group_files_by_suffix


PATH = Path('C:/Users/patri/Desktop')
files = group_files_by_suffix(PATH)
pprint(files)
