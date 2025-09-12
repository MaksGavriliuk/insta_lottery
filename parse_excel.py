from openpyxl import load_workbook
import json

# Путь к вашему Excel файлу
file_path = "rpk.comments.xlsx"

# Загружаем книгу и выбираем первый лист
wb = load_workbook(file_path)
sheet = wb.active

# Читаем все значения из столбца A
column_a_values = [cell.value for cell in sheet['A'] if cell.value is not None]

# Сохраняем в JSON файл
with open("participants.json", "w", encoding="utf-8") as f:
    json.dump({"participants": column_a_values}, f, ensure_ascii=False, indent=4)

print("Список участников сохранён в participants.json")
