import os
import re
import json

summary_dir = r"C:\Users\THAI ANH\.gemini\antigravity\scratch\modpack-analyzer\extracted_data\summary"

all_master_quests = []

# ==========================================
# 1. PARSE 01_adventure_core.md
# ==========================================
def parse_adventure_core(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    # Split by #### N.
    blocks = re.split(r'\n(?=####\s+\d+\.)', content)
    for block in blocks:
        qid_m = re.search(r'Quest ID[\*:]*\s*[`]?([A-Fa-f0-9]{16})[`]?', block)
        if qid_m:
            qid = qid_m.group(1)
            title_m = re.search(r'####\s*\d+\.\s*([^\n]+)', block)
            title = title_m.group(1).strip() if title_m else "Adventure Quest"
            title = re.sub(r'\(.*?\)', '', title).strip()

            sub_m = re.search(r'Subtitle[\*:]*\s*([^\n]+)', block)
            sub = sub_m.group(1).strip().strip('*') if sub_m else ""

            tasks_m = re.search(r'Tasks[\*:]*\s*\n(.*?)(?=\n- \*\*|\n##|\Z)', block, re.DOTALL)
            tasks = " • ".join([l.strip("- * `") for l in tasks_m.group(1).split("\n") if l.strip()][:3]) if tasks_m else "Mục tiêu phiêu lưu"

            rew_m = re.search(r'Rewards[\*:]*\s*\n(.*?)(?=\n- \*\*|\n##|\Z)', block, re.DOTALL)
            rewards = " • ".join([l.strip("- * `") for l in rew_m.group(1).split("\n") if l.strip()][:2]) if rew_m else "XP & Coin"

            deps_m = re.search(r'Dependencies[\*:]*\s*([^\n]+)', block)
            deps = deps_m.group(1).strip() if deps_m else "Khởi đầu (None)"

            quests.append({
                "id": qid,
                "stt": len(quests) + 1,
                "title": title,
                "subtitle": sub,
                "chapter": "Chương 1: Thám Hiểm Cốt Lõi (Adventure Core)",
                "chapter_id": "adventure",
                "tasks": tasks,
                "dependencies": deps,
                "rewards": rewards
            })
    return quests

# ==========================================
# 2. PARSE 02_creatures.md
# ==========================================
def parse_creatures(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    blocks = re.split(r'\n(?=#{3,5}\s+)', content)
    for block in blocks:
        qid_m = re.search(r'-\s*\*\*ID[\*:]*\s*[`]?([A-Fa-f0-9]{16})[`]?', block)
        if qid_m:
            qid = qid_m.group(1)
            title_m = re.search(r'#{3,5}\s*(?:\[.*?\]\s*|\d+\.\s*)?([^\n]+)', block)
            title = title_m.group(1).strip() if title_m else "Creature Quest"
            title = re.sub(r'&[0-9a-fk-or]|[\*`#]', '', title).strip()

            sub_m = re.search(r'Subtitle[\*:]*\s*([^\n]+)', block)
            sub = sub_m.group(1).strip().strip('*') if sub_m else ""
            sub = re.sub(r'&[0-9a-fk-or]', '', sub)

            tasks_m = re.search(r'(?:Yêu cầu|Tasks)[\s\(\)a-zA-Z]*[\*:]*\s*\n(.*?)(?=\n- \*\*|\n#{2,6}|\Z)', block, re.DOTALL)
            if tasks_m:
                tasks = " • ".join([re.sub(r'&[0-9a-fk-or]', '', l.strip("- * `1234567890.")) for l in tasks_m.group(1).split("\n") if l.strip()][:3])
            else:
                req_s = re.search(r'-\s*\*\*(?:Yêu cầu|Tasks)[\*:]*\s*([^\n]+)', block)
                tasks = re.sub(r'&[0-9a-fk-or]|[\*`]', '', req_s.group(1)).strip() if req_s else "Săn bắt / thuần phục sinh vật"

            rew_m = re.search(r'(?:Phần thưởng|Rewards)[\*:]*\s*([^\n]+)', block)
            rewards = re.sub(r'&[0-9a-fk-or]|[\*`]', '', rew_m.group(1)).strip() if rew_m else "XP & Coin"

            deps_m = re.search(r'Dependencies[\*:]*\s*([^\n]+)', block)
            deps = re.sub(r'&[0-9a-fk-or]|[\*`]', '', deps_m.group(1)).strip() if deps_m else "Khởi đầu (None)"

            quests.append({
                "id": qid,
                "stt": len(quests) + 1,
                "title": title,
                "subtitle": sub,
                "chapter": "Chương 2: Sinh Vật & Hang Động (Creatures & Dragons)",
                "chapter_id": "creatures",
                "tasks": tasks,
                "dependencies": deps,
                "rewards": rewards
            })
    return quests

# ==========================================
# 3. PARSE 03_magic.md (Table)
# ==========================================
def parse_magic(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    lines = content.split("\n")
    for line in lines:
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
                        "subtitle": "Iron's Spells, Goety & Apotheosis",
                        "chapter": "Chương 3: Đại Ma Thuật & Pháp Điển (Magic & Spells)",
                        "chapter_id": "magic",
                        "tasks": clean_tasks,
                        "dependencies": clean_deps if clean_deps else "Khởi đầu (None)",
                        "rewards": clean_rewards if clean_rewards else "XP & Coin"
                    })
    return quests

# ==========================================
# 4. PARSE 04_dimensions.md (Table with Quest ID in col 1)
# ==========================================
def parse_dimensions(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    lines = content.split("\n")
    for line in lines:
        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            # Format: | Quest ID | Tên / Mục Tiêu Nhiệm Vụ | Yêu Cầu (Tasks) | Phần Thưởng (Rewards) | Phụ Thuộc (Dependencies) | Ghi Chú / Mô Tả |
            if len(parts) >= 6:
                qid = parts[1].replace("`", "").strip()
                title = parts[2]
                tasks = parts[3]
                rewards = parts[4]
                deps = parts[5] if len(parts) > 5 else "Khởi đầu (None)"

                if re.match(r'^[A-Fa-f0-9]{16}$', qid):
                    clean_title = re.sub(r"\*\*|&[0-9a-fk-or]", "", title).strip()
                    clean_tasks = tasks.replace("<br>", " • ").replace("`", "").strip()
                    clean_deps = deps.replace("<br>", " • ").replace("`", "").strip()
                    clean_rewards = rewards.replace("<br>", " • ").replace("`", "").strip()

                    quests.append({
                        "id": qid,
                        "stt": len(quests) + 1,
                        "title": clean_title,
                        "subtitle": "Aether, Otherside, Nether, End & 12 Mắt Thần",
                        "chapter": "Chương 4: Chiều Không Gian & 12 Mắt Thần (Dimensions)",
                        "chapter_id": "dimensions",
                        "tasks": clean_tasks,
                        "dependencies": clean_deps if clean_deps else "Khởi đầu (None)",
                        "rewards": clean_rewards if clean_rewards else "XP & Coin"
                    })
    return quests

# ==========================================
# 5. PARSE 05_utilities_others.md (### N.M. Title [QID])
# ==========================================
def parse_utilities(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    quests = []
    blocks = re.split(r'\n(?=###\s+\d+\.\d+\.)', content)
    for block in blocks:
        # Match [`QID`] or [QID] at end of header
        qid_m = re.search(r'\[[`]?([A-Fa-f0-9]{16})[`]?\]', block)
        if qid_m:
            qid = qid_m.group(1)
            title_m = re.search(r'###\s+\d+\.\d+\.\s*([^\[\n]+)', block)
            title = title_m.group(1).strip() if title_m else "Utility Quest"
            title = re.sub(r'[\*`#]', '', title).strip()

            sub_m = re.search(r'Phụ đề[^\:]*[\*:]*\s*([^\n]+)', block)
            sub = sub_m.group(1).strip().strip('*') if sub_m else ""

            tasks_m = re.search(r'Nhiệm vụ[^\:]*[\*:]*\s*([^\n]+)', block)
            tasks = tasks_m.group(1).replace("`", "").strip() if tasks_m else "Hoàn thành mục tiêu"

            rew_m = re.search(r'Phần thưởng[^\:]*[\*:]*\s*([^\n]+)', block)
            rewards = rew_m.group(1).replace("`", "").strip() if rew_m else "XP & Coin"

            deps_m = re.search(r'Điều kiện[^\:]*[\*:]*\s*([^\n]+)', block)
            deps = deps_m.group(1).replace("`", "").strip() if deps_m else "Khởi đầu (None)"

            quests.append({
                "id": qid,
                "stt": len(quests) + 1,
                "title": title,
                "subtitle": sub,
                "chapter": "Chương 5: Tiện Ích, Cổ Vật & Bách Khoa Câu Cá (Utilities)",
                "chapter_id": "utilities",
                "tasks": tasks,
                "dependencies": deps,
                "rewards": rewards
            })
    return quests

# Execute all parsers
q1 = parse_adventure_core(os.path.join(summary_dir, "01_adventure_core.md"))
q2 = parse_creatures(os.path.join(summary_dir, "02_creatures.md"))
q3 = parse_magic(os.path.join(summary_dir, "03_magic.md"))
q4 = parse_dimensions(os.path.join(summary_dir, "04_dimensions.md"))
q5 = parse_utilities(os.path.join(summary_dir, "05_utilities_others.md"))

print(f"01_adventure_core.md : {len(q1):>3} Quests")
print(f"02_creatures.md      : {len(q2):>3} Quests")
print(f"03_magic.md          : {len(q3):>3} Quests")
print(f"04_dimensions.md     : {len(q4):>3} Quests")
print(f"05_utilities_others  : {len(q5):>3} Quests")

total = q1 + q2 + q3 + q4 + q5
print(f"====================================")
print(f"TOTAL PARSED: {len(total)} QUESTS")
print(f"====================================")

# Write to js/data_quests.js
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_quests.js", "w", encoding="utf-8") as f:
    f.write(f"/**\n * Terramity Awakened Wiki - Complete 432 FTB Quests Database\n */\nconst QUESTS_DATABASE = {json.dumps(total, ensure_ascii=False, indent=2)};\n")

print("Generated js/data_quests.js successfully!")
