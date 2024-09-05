import json

with open('comments.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

nicknames = []
for i in range(1, len(lines), 4):
    nickname = lines[i].strip()
    comment = lines[i + 1].strip() if i + 1 < len(lines) else ''

    if comment.count('@') >= 3:
        nicknames.append(nickname)

with open('participants.json', 'w', encoding='utf-8') as json_file:
    json.dump({"participants": nicknames}, json_file, ensure_ascii=False, indent=4)

print("Никнеймы успешно записаны в participants.json")
