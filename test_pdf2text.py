import cv2
print(cv2.__version__)

from pdf2text.pdf2text import extract_pdf_file_to_text

from typing import BinaryIO

file_path = "/Users/user/Downloads/AUDIT_MATERIALS/budget_materials/personal/2021/2021 03 remarks 2.pdf"
  
with open(file_path, "rb") as file:
  text_data, text = extract_pdf_file_to_text(
    filename="abc.pdf",
    file=file,
    meta_data_mapping = {
        "document_category": "DEF",
    }
  )
  
  print(text_data, text)
