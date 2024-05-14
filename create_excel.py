# Import the necessary libraries
import openpyxl
from openpyxl.styles import Alignment
import pandas as pd

# Create a new Excel workbook
workbook = openpyxl.Workbook()
# Select the default sheet (usually named 'Sheet')
sheet = workbook.active
# Add data to the Excel sheet
data = [
    ["Name", "Age", "City"],
    ["John", 28, "New York"],
    ["Alice", 24, "San Francisco"],
    ["Bob", 32, "Los Angeles"]
]
for row in data:
    sheet.append(row)
# Save the workbook to a file
workbook.save(f"C:/Users/pierry.benoit/Documents/my_excel_file.xlsx")
# Print a success message
print("Excel file created successfully!")


