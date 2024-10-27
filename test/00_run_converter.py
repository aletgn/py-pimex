from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/py-pimex/src/'))

import fitz
from pypimex.converter import PDFConverter

if __name__ == "__main__":

    p = PDFConverter(input_path="/home/ale/Desktop/test.pdf", reader=fitz)
    p.config(dpi=72, format='png', output_folder="./converted_")
    p.set_pages(start_page=1, end_page=15, range_page=None)
    p.convert_pages(dry_run=True)