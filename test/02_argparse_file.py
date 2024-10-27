from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/py-pimex/src/'))

import fitz
from pypimex.converter import PDFConverter
from pypimex.util import parse_args, get_config_file

def main():
    config = get_config_file(parse_args().config)
    p = PDFConverter(input_path=config["input_path"], reader=fitz)
    p.config(dpi=config["dpi"], format=config["format"], output_folder=config["output_folder"])
    p.set_pages(start_page=config["start_page"], end_page=config["end_page"])
    p.convert_pages(dry_run=config["dry_run"])

if __name__ == "__main__":

    main()