import json

file_path = "comments.2025.txt"

with open(file_path, "r", encoding="utf-8") as f:
    # читаем строки и убираем пустые
    lines = [line.strip() for line in f if line.strip()]

nicknames = []

for i in range(len(lines)):
    print(lines[i])
    if "Фото профил" in lines[i]:  # проверяем по ключевому слову
        if i + 1 < len(lines):
            if lines[i + 3].startswith("@"):
                nickname = lines[i + 1].strip()
                nicknames.append(nickname)

# сохраняем в JSON
with open("participants.json", "w", encoding="utf-8") as f:
    json.dump({"participants": nicknames}, f, ensure_ascii=False, indent=4)

print(f"\nСобрано {len(nicknames)} ников, сохранено в participants.json")
