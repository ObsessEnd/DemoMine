import os
import re
import json

summary_dir = r"C:\Users\THAI ANH\.gemini\antigravity\scratch\modpack-analyzer\extracted_data\summary"

def parse_quests_from_markdown(file_path, default_chapter_name, chapter_id):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    
    # 1. First, try parsing Markdown Tables (like in 03_magic.md)
    lines = content.split("\n")
    current_section = default_chapter_name
    for line in lines:
        if line.startswith("# ") or line.startswith("## ") or line.startswith("### "):
            current_section = line.strip("# ").strip()
            continue

        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 6:
                stt = parts[1]
                title = parts[2]
                quest_id = parts[3]
                tasks = parts[4]
                deps = parts[5] if len(parts) > 5 else ""
                rewards = parts[6] if len(parts) > 6 else ""

                if stt.isdigit() or (len(stt) == 2 and stt.isdigit()):
                    clean_title = re.sub(r"\*\*|&[0-9a-fk-or]", "", title).strip()
                    clean_tasks = tasks.replace("<br>", " • ").replace("`", "").strip()
                    clean_deps = deps.replace("<br>", " • ").replace("`", "").strip()
                    clean_rewards = rewards.replace("<br>", " • ").replace("`", "").strip()

                    quests.append({
                        "id": quest_id.replace("`", "").strip(),
                        "stt": int(stt),
                        "title": clean_title,
                        "chapter": default_chapter_name,
                        "chapter_id": chapter_id,
                        "section": current_section,
                        "tasks": clean_tasks,
                        "dependencies": clean_deps if clean_deps else "Khởi đầu (None)",
                        "rewards": clean_rewards if clean_rewards else "XP & KubeJS Coin"
                    })

    # 2. If table didn't yield all quests, split by headers (####, #####, etc.)
    if len(quests) < 10:
        quests = []
        blocks = re.split(r'\n(?=#{2,6}\s+)', content)
        stt_counter = 1

        for block in blocks:
            # Look for ID pattern: ID: or Quest ID:
            id_match = re.search(r'-\s*\*\*(?:Quest\s+)?ID[\*:]*\s*[`]?([A-Fa-f0-9]{16})[`]?', block)
            if not id_match:
                id_match = re.search(r'ID[\*:]*\s*[`]?([A-Fa-f0-9]{16})[`]?', block)

            if id_match:
                qid = id_match.group(1).strip()

                # Extract Title
                title_match = re.search(r'#{2,6}\s*(?:\[.*?\]\s*|\d+\.\s*)?([^\n]+)', block)
                if not title_match:
                    title_match = re.search(r'Tiêu đề[\*:]*\s*([^\n]+)', block)
                title = title_match.group(1).strip() if title_match else "Nhiệm vụ"
                title = re.sub(r'&[0-9a-fk-or]', '', title) # Remove MC color codes
                title = re.sub(r'[\*`#]', '', title).strip()

                # Extract Subtitle
                sub_match = re.search(r'Subtitle[\*:]*\s*([^\n]+)', block)
                subtitle = sub_match.group(1).strip().strip('*') if sub_match else ""
                subtitle = re.sub(r'&[0-9a-fk-or]', '', subtitle)

                # Extract Tasks / Yêu Cầu
                tasks = "Hoàn thành mục tiêu nhiệm vụ"
                tasks_match = re.search(r'(?:Yêu cầu|Tasks)[\s\(\)a-zA-Z]*[\*:]*\s*\n(.*?)(?=\n- \*\*|\n#{2,6}|\Z)', block, re.DOTALL)
                if tasks_match:
                    t_lines = [re.sub(r'&[0-9a-fk-or]', '', l.strip("- * `1234567890.")) for l in tasks_match.group(1).split("\n") if l.strip()]
                    tasks = " • ".join(t_lines[:4])
                else:
                    req_single = re.search(r'-\s*\*\*(?:Yêu cầu|Tasks)[\*:]*\s*([^\n]+)', block)
                    if req_single:
                        tasks = re.sub(r'&[0-9a-fk-or]|[\*`]', '', req_single.group(1)).strip()

                # Extract Rewards / Phần Thưởng
                rewards = "XP & KubeJS Coin"
                rew_match = re.search(r'(?:Phần thưởng|Rewards)[\*:]*\s*([^\n]+)', block)
                if rew_match:
                    rewards = re.sub(r'&[0-9a-fk-or]|[\*`]', '', rew_match.group(1)).strip()

                # Extract Dependencies
                deps = "Khởi đầu (None)"
                deps_match = re.search(r'Dependencies[\*:]*\s*([^\n]+)', block)
                if deps_match:
                    deps = re.sub(r'&[0-9a-fk-or]|[\*`]', '', deps_match.group(1)).strip()

                quests.append({
                    "id": qid,
                    "stt": stt_counter,
                    "title": title,
                    "subtitle": subtitle,
                    "chapter": default_chapter_name,
                    "chapter_id": chapter_id,
                    "section": default_chapter_name,
                    "tasks": tasks,
                    "dependencies": deps,
                    "rewards": rewards
                })
                stt_counter += 1

    return quests

files = [
    ("01_adventure_core.md", "Chương 1: Thám Hiểm Cốt Lõi & Terramity (Adventure Core)", "adventure"),
    ("02_creatures.md", "Chương 2: Sinh Vật, Hang Động & Rồng Ice & Fire (Creatures)", "creatures"),
    ("03_magic.md", "Chương 3: Đại Ma Thuật & Pháp Điển (Magic & Spells)", "magic"),
    ("04_dimensions.md", "Chương 4: Chiều Không Gian & 12 Mắt Thần (Dimensions)", "dimensions"),
    ("05_utilities_others.md", "Chương 5: Tiện Ích, Cổ Vật & Bách Khoa Câu Cá (Utilities)", "utilities")
]

master_quests = []
for fname, ch_name, ch_id in files:
    fpath = os.path.join(summary_dir, fname)
    qs = parse_quests_from_markdown(fpath, ch_name, ch_id)
    print(f"File {fname:<25}: Parsed {len(qs):>3} Quests")
    master_quests.extend(qs)

print(f"\n==========================================")
print(f"TOTAL MASTER QUESTS EXTRACTED: {len(master_quests)}")
print(f"==========================================")

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_quests.js", "w", encoding="utf-8") as f:
    f.write(f"/**\n * Terramity Awakened Wiki - Complete 430+ FTB Quests Database\n */\nconst QUESTS_DATABASE = {json.dumps(master_quests, ensure_ascii=False, indent=2)};\n")

print("Saved data_quests.js successfully!")
