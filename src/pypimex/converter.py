
import fitz # PyMuPDF

from pypimex.util import get_filename, trail, _log, mkdir, check_filename
class PDFConverter:
    
    def __init__(self, input_path, reader=fitz) -> None:
        self.input_path = input_path
        self.reader = reader
        self.filename = check_filename(get_filename(input_path))
        pdf = self.reader.open(self.input_path)
        self.pages = pdf.page_count
        self.metadata = pdf.metadata
        pdf.close()
        _log.debug(f"Probe document at {input_path}")
        _log.info(f"Filename {self.filename}")
        _log.info(f"Pages {self.pages}")
        _log.debug(f"Metadata\n{self.metadata}")
        self.config()
        self.set_pages()

    def config(self, dpi=72, format='png', output_folder="./converted_"):
        self.dpi = dpi
        self.format = '.' + format
        self.output_folder = output_folder + self.filename + "/"
        _log.info(f"Pages shall be saved {self.dpi} dpi")
        _log.info(f"Pages shall be saved in {self.format} format")
        _log.info(f"Pages shall be saved in {self.output_folder}")

    def set_pages(self, range_page=None, start_page=None, end_page=None):        
        if range_page:
            self.range_page = sorted(list(set(range_page)))
            _log.info(f"Pages to convert {self.range_page}")

        else:
            self.start_page = start_page if start_page is not None else 1
            self.end_page = end_page if end_page is not None else self.pages
            self.range_page = list(range(self.start_page, self.end_page+1))
            _log.info(f"Pages to convert {self.range_page}")

        if all(x > 0 for x in self.range_page):
            _log.debug("Page numbers are greater than 0")
        else:
            _log.error("Page numbers must be > 0")
            raise ValueError
        
        if all(x <= self.pages for x in self.range_page):
            _log.debug(f"Page numbers are lower or equal than {self.pages}")
        else:
            _log.error("Page numbers must be > 0")
            raise ValueError

    def convert_pages(self, dry_run=True):
        _log.warning(f"Convert pages in {self.output_folder}")
        if dry_run == False:
            mkdir(self.output_folder)
        
        pdf = self.reader.open(self.input_path)
        for p in [s - 1 for s in self.range_page]:
            
            if dry_run == True:
                _log.info(f"Skip saving page {p+1} since dry_run: {dry_run}")
            else:
                _log.info(f"Save page {p+1}")
                page = pdf.load_page(p)
                pix = page.get_pixmap(dpi=self.dpi)
                pix.save(self.output_folder + trail(p+1, self.pages) + "_" + self.filename + self.format)
        pdf.close()


