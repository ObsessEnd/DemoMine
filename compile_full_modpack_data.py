import os
import re
import json

summary_dir = r"C:\Users\THAI ANH\.gemini\antigravity\scratch\modpack-analyzer\extracted_data\summary"

def parse_markdown_table_quests(file_path, chapter_name, chapter_id):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    # Match markdown tables: | STT | Tên Quest | Quest ID | Mục Tiêu (Tasks) | Yêu Cầu Trước (Dependencies) | Phần Thưởng (Rewards) |
    # or variations
    lines = content.split("\n")
    current_section = chapter_name

    for line in lines:
        if line.startswith("# ") or line.startswith("## ") or line.startswith("### "):
            current_section = line.strip("# ").strip()
            continue

        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            # Filter valid table rows (usually 6-8 parts)
            if len(parts) >= 6:
                stt = parts[1]
                title = parts[2]
                quest_id = parts[3]
                tasks = parts[4]
                deps = parts[5] if len(parts) > 5 else ""
                rewards = parts[6] if len(parts) > 6 else ""

                if stt.isdigit() or (len(stt) == 2 and stt.isdigit()):
                    # Clean markdown bolding
                    clean_title = re.sub(r"\*\*", "", title).strip()
                    clean_tasks = tasks.replace("<br>", " • ").replace("`", "").strip()
                    clean_deps = deps.replace("<br>", " • ").replace("`", "").strip()
                    clean_rewards = rewards.replace("<br>", " • ").replace("`", "").strip()

                    quests.append({
                        "id": quest_id.replace("`", "").strip(),
                        "stt": int(stt),
                        "title": clean_title,
                        "chapter": chapter_name,
                        "chapter_id": chapter_id,
                        "section": current_section,
                        "tasks": clean_tasks,
                        "dependencies": clean_deps if clean_deps else "Khởi đầu (None)",
                        "rewards": clean_rewards if clean_rewards else "XP & KubeJS Coin"
                    })

    return quests

# Process all 5 files
all_quests = []

# 1. Adventure Core
f1 = os.path.join(summary_dir, "01_adventure_core.md")
q1 = parse_markdown_table_quests(f1, "Chương 1: Thám Hiểm Cốt Lõi (Adventure Core)", "adventure")
all_quests.extend(q1)
print(f"01_adventure_core.md: parsed {len(q1)} quests.")

# 2. Creatures & Dragons
f2 = os.path.join(summary_dir, "02_creatures.md")
q2 = parse_markdown_table_quests(f2, "Chương 2: Sinh Vật & Hang Động (Creatures & Dragons)", "creatures")
all_quests.extend(q2)
print(f"02_creatures.md: parsed {len(q2)} quests.")

# 3. Magic & Spells
f3 = os.path.join(summary_dir, "03_magic.md")
q3 = parse_markdown_table_quests(f3, "Chương 3: Đại Ma Thuật & Pháp Điển (Magic & Rituals)", "magic")
all_quests.extend(q3)
print(f"03_magic.md: parsed {len(q3)} quests.")

# 4. Dimensions & Eyes
f4 = os.path.join(summary_dir, "04_dimensions.md")
q4 = parse_markdown_table_quests(f4, "Chương 4: Chiều Không Gian & 12 Mắt Thần (Dimensions)", "dimensions")
all_quests.extend(q4)
print(f"04_dimensions.md: parsed {len(q4)} quests.")

# 5. Utilities & Fishing
f5 = os.path.join(summary_dir, "05_utilities_others.md")
q5 = parse_markdown_table_quests(f5, "Chương 5: Tiện Ích, Cổ Vật & Bách Khoa Câu Cá (Utilities)", "utilities")
all_quests.extend(q5)
print(f"05_utilities_others.md: parsed {len(q5)} quests.")

print(f"Total Quests parsed: {len(all_quests)}")

# Write to js/data_quests.js
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_quests.js", "w", encoding="utf-8") as f:
    f.write(f"const QUESTS_DATABASE = {json.dumps(all_quests, ensure_ascii=False, indent=2)};\n")

print("Generated js/data_quests.js successfully!")
