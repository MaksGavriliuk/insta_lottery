import json
import re
from bs4 import BeautifulSoup

# читаем html из файла
with open("Instagram.mhtml", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

comments = []

# вытаскиваем все блоки с юзернеймами (ссылки на профили)
for a in soup.find_all("a", href=True):
    if re.match(r"^/[^/]+/$", a["href"]):  # ссылки вида "/username/"
        username = a.get_text(strip=True)
        if username:
            # ищем текст комментария рядом
            parent = a.find_parent()
            if parent:
                text_tag = parent.find("span", attrs={"dir": "auto"})
                if text_tag:
                    text = text_tag.get_text(strip=True)
                    comments.append({"username": username, "text": text})

# сохраняем в json
with open("comments.json", "w", encoding="utf-8") as f:
    json.dump(comments, f, ensure_ascii=False, indent=2)

print(f"Извлечено {len(comments)} комментариев, записано в comments.json")
