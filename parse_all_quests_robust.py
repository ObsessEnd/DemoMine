import os
import re
import json

summary_dir = r"C:\Users\THAI ANH\.gemini\antigravity\scratch\modpack-analyzer\extracted_data\summary"

def parse_quests_from_file(file_path, default_chapter_name, chapter_id):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    lines = content.split("\n")
    current_section = default_chapter_name

    # Check for Markdown Table format
    has_table = False
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
                    has_table = True
                    clean_title = re.sub(r"\*\*", "", title).strip()
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

    # If not a table or has few table rows, parse structured blocks (#### N. Title ...)
    if len(quests) < 5:
        quests = []
        blocks = re.split(r'\n(?=#### |\n### |\n## )', content)
        stt_counter = 1

        for block in blocks:
            if "**Quest ID**" in block or "Quest ID:" in block:
                # Extract Quest ID
                qid_match = re.search(r'Quest ID[\*:]*\s*[`]?([A-Fa-f0-9]+)[`]?', block)
                qid = qid_match.group(1) if qid_match else f"Q_{stt_counter}"

                # Extract Title
                title_match = re.search(r'####\s*[\d\.]*\s*([^\n]+)', block)
                if not title_match:
                    title_match = re.search(r'Tiêu đề[\*:]*\s*([^\n]+)', block)
                title = title_match.group(1).strip() if title_match else "Nhiệm vụ"
                title = re.sub(r'\(.*?\)', '', title).strip() if not title else title

                # Extract Subtitle
                sub_match = re.search(r'Subtitle[\*:]*\s*([^\n]+)', block)
                subtitle = sub_match.group(1).strip() if sub_match else ""

                # Extract Tasks
                tasks = []
                tasks_match = re.search(r'Tasks[\*:]*\s*\n(.*?)(?=\n- \*\*|\n##|\Z)', block, re.DOTALL)
                if tasks_match:
                    task_lines = [l.strip("- * `") for l in tasks_match.group(1).split("\n") if l.strip()]
                    tasks = " • ".join(task_lines[:4])
                else:
                    tasks = "Hoàn thành mục tiêu nhiệm vụ"

                # Extract Rewards
                rewards = []
                rewards_match = re.search(r'Rewards[\*:]*\s*\n(.*?)(?=\n- \*\*|\n##|\Z)', block, re.DOTALL)
                if rewards_match:
                    rew_lines = [l.strip("- * `") for l in rewards_match.group(1).split("\n") if l.strip()]
                    rewards = " • ".join(rew_lines[:3])
                else:
                    rewards = "XP & KubeJS Coin"

                # Extract Dependencies
                deps_match = re.search(r'Dependencies[\*:]*\s*([^\n]+)', block)
                deps = deps_match.group(1).strip() if deps_match else "Khởi đầu (None)"

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
    ("01_adventure_core.md", "Chương 1: Thám Hiểm Cốt Lõi (Adventure Core)", "adventure"),
    ("02_creatures.md", "Chương 2: Sinh Vật & Hang Động (Creatures & Dragons)", "creatures"),
    ("03_magic.md", "Chương 3: Đại Ma Thuật & Pháp Điển (Magic & Spells)", "magic"),
    ("04_dimensions.md", "Chương 4: Chiều Không Gian & 12 Mắt Thần (Dimensions)", "dimensions"),
    ("05_utilities_others.md", "Chương 5: Tiện Ích, Cổ Vật & Bách Khoa Câu Cá (Utilities)", "utilities")
]

total_all_quests = []
for fname, ch_name, ch_id in files:
    fpath = os.path.join(summary_dir, fname)
    qs = parse_quests_from_file(fpath, ch_name, ch_id)
    print(f"File {fname:<25}: Parsed {len(qs):>3} Quests")
    total_all_quests.extend(qs)

print(f"\n==========================================")
print(f"TOTAL QUESTS PARSED: {len(total_all_quests)}")
print(f"==========================================")

# Write to js/data_quests.js
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_quests.js", "w", encoding="utf-8") as f:
    f.write(f"/**\n * Terramity Awakened Wiki - 430+ FTB Quests Database (Complete)\n */\nconst QUESTS_DATABASE = {json.dumps(total_all_quests, ensure_ascii=False, indent=2)};\n")

print("Saved js/data_quests.js successfully!")
