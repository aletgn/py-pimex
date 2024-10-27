import os
from math import log10

import argparse
import yaml

import logging
_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_filename(path):
    return path.split("/")[-1]

def trail(num, max_value):
    return str(num).zfill(int(log10(max_value)) + 1)

def mkdir(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        _log.warning(f"Created folder: {output_folder}")
    else:
        _log.info(f"Folder already exists: {output_folder}")

def check_filename(filename):
    if filename.lower().endswith('.pdf'):
        _log.debug("The document ends with .pdf")
        return filename[0:-4]
    else:
        _log.warning("The document does not end with .pdf")
        return filename
    
def get_config_file(path):
    with open(path, "r") as config_file:
        return yaml.safe_load(config_file)

def parse_args():
    parser = argparse.ArgumentParser(description='Convert PDF files to images.')
    
    parser.add_argument('--config', type=str,
                        help='Path to the configuration file (YAML format).')
    
    parser.add_argument('--input_path', type=str, default='../../test.pdf',
                        help='Path to the input PDF file.')
    
    parser.add_argument('--dpi', type=int, default=72,
                        help='DPI for the converted images (default: 72).')
    
    parser.add_argument('--format', type=str, choices=['png', 'jpeg'], default='png',
                        help='Output image format (default: png).')
    
    parser.add_argument('--output_folder', type=str, default='./converted_',
                        help='Folder to save converted images (default: ./converted_).')
    
    parser.add_argument('--start_page', type=int, default=1,
                        help='Starting page number for conversion (default: 1).')
    
    parser.add_argument('--end_page', type=int, default=None,
                        help='Ending page number for conversion (default: None, converts to the last page).')
    
    parser.add_argument('--dry_run', action='store_false',
                        help='Perform a dry run without actual conversion.')
    
    return parser.parse_args()