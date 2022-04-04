from auto_doc_engine import AutoDoc
from import_data_to_db import ImportDataToDb
import config as cfg
import os
from main_window import MainWindow

# test doc schema function
# AutoDoc.fill_doc_test('Accept_complainant.docx')
# AutoDoc.doc_of_accept_complaint("Accept_complainant.docx", "1")
# ImportDataToDb.import_data_from_excel(cfg.excel_to_db_file_name, cfg.dB_path, cfg.dB_table_name)

# AutoDoc.doc_of_accept_complaint("Accept_complainant.docx", "2")

MainWindow(710, 480, 200, 200, 'Main Window').run()

