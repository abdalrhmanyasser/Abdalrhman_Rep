from openpyxl import load_workbook
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append([input("input i guess\n"), "Hey Mate"])
ws.append(["meow"])
wb.save("empty_book.xlsx")
