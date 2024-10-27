from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/py-pimex/src/'))

import fitz
from pypimex.converter import PDFConverter
from pypimex.util import parse_args

def main():
    args = parse_args()
    p = PDFConverter(input_path=args.input_path, reader=fitz)
    p.config(dpi=args.dpi, format=args.format, output_folder=args.output_folder)
    p.set_pages(start_page=args.start_page, end_page=args.end_page)
    p.convert_pages(dry_run=args.dry_run)

if __name__ == "__main__":
    main()