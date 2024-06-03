"""
Authors: Owen Saxton

Credit to: Aayesha Mohammed, Mariyam Mohammed, Rogue Lyons for Text, Indentation & Footer limits/ranges

pdfplumber can be installed via commandline using "pip install pdfplumber"
"""

import pdfplumber

# Configuration for processing each identified section of the RVP PDF
sections = [
    {"start": 55, "end": 82, "output_file": "Section 1.txt"},
    {"start": 88, "end": 293, "output_file": "Section 2.txt"},
    {"start": 301, "end": 394, "output_file": "Section 3.txt"}
]

# Constants for filtering conditions
text_size_limit = 9.01  # Maximum font size to include
indentation_limit = 61       # Horizontal indentation threshold for new records
footer_font_range = (5.0, 6.0)  # Font size range for footers

def extract_text_by_font_size(file_name, sections):
    """Extracts text from specified sections of a PDF based on font size criteria."""
    with pdfplumber.open(file_name) as pdf:
        for section in sections:
            with open(section["output_file"], "a") as output_file:
                for page_number in range(section["start"], section["end"]):
                    page = pdf.pages[page_number]
                    previous_height = 0
                    write = True

                    for char in page.chars:
                        if not write:
                            break

                        current_height = char.get("top")
                        if char.get("size") < text_size_limit:
                            text = char.get("text")
                            if current_height > previous_height:  # New line
                                text = '\n' + text
                                previous_height = current_height
                                if footer_font_range[0] < char.get("size") < footer_font_range[1]:
                                    write = False  # Exclude footer
                            if write:
                                if char.get("x0") < indentation_limit:  # New record
                                    output_file.write('\n' + text)
                                else:
                                    output_file.write(text)

# Process the PDF sections as specified
extract_text_by_font_size("RVP.pdf", sections)