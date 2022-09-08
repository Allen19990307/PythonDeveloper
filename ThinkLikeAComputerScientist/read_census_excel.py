#!python3
# read_census_excel.py - Tabulates population and number of census tracts for　# each county.
import openpyxl,pprint
print('opening workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
for row in range(2,sheet.get_highest_row() + 1):
    State = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
