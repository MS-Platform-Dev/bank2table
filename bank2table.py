#-------------------------------------------------------------------------------
# Copyright ©2024 MonaCompta
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#-------------------------------------------------------------------------------

# Module:       bank2table.py
# Description:  Convert PDF bank statements to data tables for processing
#
# Author:       Mike
# Copyright:    ©2024 MonaCompta
# Licence:      MIT

# Change Log:
# DATE          VERSION       DESCRIPTION
# 2022-01-20    0.1  alpha    Removed play code and initial commit
# 2022-01-24    0.2  alpha    Re-created for new repo. Changed license to MIT.
#                             Added skeleton functions
# 2022-04-19    0.3  alpha    Added GUI placeholder
# 2023-11-20    0.4  alpha    Version refresh
# 2024-10-17    0.5  alpha    Bumped version
# 2024-10-19    0.6  alpha    Bumped version
#-------------------------------------------------------------------------------

from datetime import datetime
import os
import pandas as pd
import pdfplumber
import pysimplegui as sg
import guiforms as gui


def ask_target_folder():
    folder = input("Type or paste path to local statement destination folder: ")
# TODO: Check folder exists (try...)
    return folder

def ask_output_format():
    format = input("Type preferred output format [EXCEL | CSV | TSV]: ")
    return format

def check_if_new_stmts(source):
    pass

def collect_new_stmts(source):
    pass

def save_new_stmt(download):
    pass

def check_cat_state():
    pass

def update_cat_state(stmt):
    pass

def extract_pdf_text(file):
    pass

def convert_text_to_data(text):
    pass

def write data_to_table(data):
    pass

def main():
    gui.gui_banner()
    os.chdir(ask_target_folder())


if __name__ == '__main__':
    main()
