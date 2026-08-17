import os
import re
import json

summary_dir = r"C:\Users\THAI ANH\.gemini\antigravity\scratch\modpack-analyzer\extracted_data\summary"

# 1. Extract Starcatcher Fishing Almanac from 05_utilities_others.md
with open(os.path.join(summary_dir, "05_utilities_others.md"), "r", encoding="utf-8") as f:
    u_content = f.read()

fishing_items = []
fishing_blocks = re.findall(r'\|\s*([0-9]+)\s*\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|', u_content)
for b in fishing_blocks:
    stt, name, biome, time_weather, rod, effect = [x.strip() for x in b]
    if stt.isdigit() and int(stt) <= 120 and "Tên Cá" not in name:
        fishing_items.append({
            "stt": int(stt),
            "name": re.sub(r'[\*`]', '', name).strip(),
            "biome": re.sub(r'[\*`]', '', biome).strip(),
            "condition": re.sub(r'[\*`]', '', time_weather).strip(),
            "rod": re.sub(r'[\*`]', '', rod).strip(),
            "effect": re.sub(r'[\*`]', '', effect).strip()
        })

print(f"Extracted {len(fishing_items)} Fish Species from 05_utilities_others.md!")

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_fishing.js", "w", encoding="utf-8") as f:
    f.write(f"const FISHING_DATABASE = {json.dumps(fishing_items, ensure_ascii=False, indent=2)};\n")

# 2. Extract Creatures & Monsters from 02_creatures.md
with open(os.path.join(summary_dir, "02_creatures.md"), "r", encoding="utf-8") as f:
    c_content = f.read()

creatures_items = []
c_blocks = re.findall(r'\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|', c_content)
for b in c_blocks:
    cname, ctype, cbiome, cdrops, cnotes = [x.strip() for x in b]
    if "Sinh vật" not in cname and "---" not in cname and len(cname) > 2:
        creatures_items.append({
            "name": re.sub(r'[\*`]', '', cname).strip(),
            "type": re.sub(r'[\*`]', '', ctype).strip(),
            "biome": re.sub(r'[\*`]', '', cbiome).strip(),
            "drops": re.sub(r'[\*`]', '', cdrops).strip(),
            "notes": re.sub(r'[\*`]', '', cnotes).strip()
        })

print(f"Extracted {len(creatures_items)} Creatures & Monsters from 02_creatures.md!")

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_creatures.js", "w", encoding="utf-8") as f:
    f.write(f"const CREATURES_DATABASE = {json.dumps(creatures_items, ensure_ascii=False, indent=2)};\n")

print("Generated js/data_fishing.js & js/data_creatures.js successfully!")
