import pandas as pd
from tkinter import Tk, filedialog
import os

def select_files():
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(title="Select Excel files to combine", filetypes=[("Excel files", "*.xlsx *.xls")])
    return list(files)

def select_save_location():
    root = Tk()
    root.withdraw()
    save_location = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Save combined file as")
    return save_location

def combine_excel_files(file_list, save_location):
    combined_df = pd.DataFrame()

    for file in file_list:
        df = pd.read_excel(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    combined_df.to_excel(save_location, index=False)
    print(f"Files combined and saved to {save_location}")

if __name__ == "__main__":
    files_to_combine = select_files()
    if files_to_combine:
        save_location = select_save_location()
        if save_location:
            combine_excel_files(files_to_combine, save_location)
        else:
            print("Save location not selected.")
    else:
        print("No files selected.")