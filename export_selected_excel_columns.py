import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

# Function to handle file upload
def upload_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    return file_path

# Function to get user input for selected columns
def get_selected_columns():
    columns = input("Enter the desired columns to extract, separated by commas: ").split(",")
    return columns

# Function to export the selected columns to a new Excel file
def export_selected_columns(file_path, columns):
    df = pd.read_excel(file_path)
    new_df = df[columns]
    new_file_path = os.path.join(os.path.dirname(file_path), "new_file.xlsx")
    new_df.to_excel(new_file_path, index=False)
    return new_file_path

# Main function
def main():
    # Upload the Excel file
    file_path = upload_file()
    if not file_path:
        print("No file uploaded.")
        return

    # Get the selected columns from the user
    selected_columns = get_selected_columns()

    # Export the selected columns to a new Excel file
    new_file_path = export_selected_columns(file_path, selected_columns)

    # Inform the user about the new file location
    print(f"New file saved at: {new_file_path}")

# Run the main function
if __name__ == "__main__":
    main()