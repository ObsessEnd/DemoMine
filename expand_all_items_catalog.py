import json

# Add TravelOptics Staves, Forbidden & Arcanus Tools, and Apotheosis Relics to the database
expanded_items = [
    # -------------------------------------------------------------
    # 1. TRAVELOPTICS WEAPONS & STAVES
    # -------------------------------------------------------------
    {
        "id": "wand_of_final_light",
        "name": "Wand of Final Light",
        "name_vi": "Đũa Phép Ánh Sáng Cuối Cùng (Wand of Final Light)",
        "icon": "images/items/wand_of_final_light.png",
        "mod": "TravelOptics / Iron's Spells",
        "category": "Weapon",
        "stage": "Late",
        "classTags": ["Mage", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "holy_rune", "name": "Holy Rune", "name_vi": "Cổ Tự Thánh Quang", "count": 4},
            {"id": "divine_pearl", "name": "Divine Pearl", "name_vi": "Ngọc Trai Thánh", "count": 4},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 1}
        ],
        "recipe_desc_vi": "4x Cổ Tự Thánh + 4x Ngọc Trai Thánh + 1x Thỏi Netherite.",
        "recipe_desc_en": "4x Holy Rune + 4x Divine Pearl + 1x Netherite Ingot.",
        "effects_vi": "+35% Holy Spell Power, Phóng chùm tia laser Thánh Quang thiêu rụi mục tiêu với 120 DMG/giây!",
        "effects_en": "+35% Holy Spell Power, Fires continuous Holy Ray melting bosses!",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo ma thuật cấp cao.",
        "source_location_en": "High tier magic crafting."
    },
    {
        "id": "staff_of_the_storm_empress",
        "name": "Staff of the Storm Empress",
        "name_vi": "Quyền Trượng Nữ Hoàng Bão Tố",
        "icon": "images/items/staff_of_the_storm_empress.png",
        "mod": "TravelOptics / Iron's Spells",
        "category": "Weapon",
        "stage": "Late",
        "classTags": ["Mage", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "lightning_rune", "name": "Lightning Rune", "name_vi": "Cổ Tự Lôi Hệ", "count": 4},
            {"id": "cinder_essence", "name": "Cinder Essence", "name_vi": "Tinh Chất Tro Tàn", "count": 4},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 1}
        ],
        "recipe_desc_vi": "4x Cổ Tự Lôi + 4x Tinh Chất Tro Tàn + 1x Thỏi Netherite.",
        "recipe_desc_en": "4x Lightning Rune + 4x Cinder Essence + 1x Netherite Ingot.",
        "effects_vi": "+40% Lightning Spell Power, +20% Tốc độ di chuyển, Triệu hồi bão sấm sét cuồng nộ giật 8 mục tiêu cùng lúc!",
        "effects_en": "+40% Lightning Spell Power, +20% Speed, Calls massive chain thunderstorms!",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo sau khi có Cổ Tự Lôi Cấp Cao.",
        "source_location_en": "High tier Lightning crafting."
    },
    {
        "id": "pocket_black_hole",
        "name": "Pocket Black Hole",
        "name_vi": "Hố Đen Bỏ Túi (Pocket Black Hole)",
        "icon": "images/items/pocket_black_hole.png",
        "mod": "TravelOptics",
        "category": "Relic",
        "stage": "Late",
        "classTags": ["All Classes", "Mage"],
        "recipe_type": "Curios Drop / Crafting",
        "ingredients": [
            {"id": "ender_rune", "name": "Ender Rune", "name_vi": "Cổ Tự Hư Không", "count": 4},
            {"id": "resonarium_ingot", "name": "Resonarium Ingot", "name_vi": "Thỏi Resonarium", "count": 2}
        ],
        "recipe_desc_vi": "4x Cổ Tự Hư Không + 2x Thỏi Resonarium (The Otherside).",
        "recipe_desc_en": "4x Ender Rune + 2x Resonarium Ingot.",
        "effects_vi": "Tự động hút và triệt tiêu 100% tất cả đạn tên và quả cầu lửa nguy hiểm bắn về phía người chơi!",
        "effects_en": "Automatically absorbs and destroys 100% incoming projectiles and fireballs!",
        "source_type": "Crafting / The Otherside",
        "source_url": "magic.html",
        "source_location_vi": "Khai thác trong The Otherside kết hợp Cổ Tự Hư Không.",
        "source_location_en": "The Otherside dimension crafting."
    },

    # -------------------------------------------------------------
    # 2. FORBIDDEN & ARCANUS ARTIFACTS
    # -------------------------------------------------------------
    {
        "id": "slimec_pickaxe",
        "name": "Slimec Pickaxe",
        "name_vi": "Cuốc Nhầy Slimec (Slimec Pickaxe)",
        "icon": "images/items/slimec_pickaxe.png",
        "mod": "Forbidden and Arcanus",
        "category": "Tool",
        "stage": "Mid",
        "classTags": ["All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "deorum_ingot", "name": "Deorum Ingot", "name_vi": "Thỏi Vàng Thánh Deorum", "count": 3},
            {"id": "edelwood_stick", "name": "Edelwood Stick", "name_vi": "Gậy Gỗ Edelwood", "count": 2}
        ],
        "recipe_desc_vi": "3x Thỏi Vàng Thánh Deorum + 2x Gậy Gỗ Edelwood.",
        "recipe_desc_en": "3x Deorum Ingot + 2x Edelwood Stick.",
        "effects_vi": "Tích hợp sẵn Chạm Nhẹ (Silk Touch), Tốc độ đào nhanh hơn Cuốc Vàng và Độ bền vượt xa Netherite!",
        "effects_en": "Pre-enchanted with Silk Touch, faster mining than Gold, more durable than Netherite!",
        "source_type": "Crafting",
        "source_url": "progression.html",
        "source_location_vi": "Bàn chế tạo sau khi luyện thỏi Deorum.",
        "source_location_en": "Crafted with Deorum Ingots."
    },
    {
        "id": "quantum_catcher",
        "name": "Quantum Catcher",
        "name_vi": "Bẫy Lượng Tử (Quantum Catcher)",
        "icon": "images/items/quantum_catcher.png",
        "mod": "Forbidden and Arcanus",
        "category": "Tool",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "spawner_scrap", "name": "Spawner Scrap", "name_vi": "Mảnh Lồng Spawner", "count": 4},
            {"id": "arcane_crystal", "name": "Arcane Crystal", "name_vi": "Pha Lê Ma Thuật", "count": 2}
        ],
        "recipe_desc_vi": "4x Mảnh Lồng Spawner + 2x Pha Lê Ma Thuật Arcane Crystal.",
        "recipe_desc_en": "4x Spawner Scrap + 2x Arcane Crystal.",
        "effects_vi": "Bắt giữ và nhốt bất kỳ sinh vật hoặc quái vật nào (kể cả Dân Làng, Rồng nhỏ, Boss nhỏ) vào túi rồi thả ra tùy ý!",
        "effects_en": "Captures any mob (Villagers, mini-bosses) into inventory and releases freely!",
        "source_type": "Crafting",
        "source_url": "utilities.html",
        "source_location_vi": "Đào lồng Spawner lấy mảnh rồi ghép tại Bàn chế tạo.",
        "source_location_en": "Break Spawners for scraps and craft."
    },
    {
        "id": "sigil_of_socketing",
        "name": "Sigil of Socketing",
        "name_vi": "Phù Ấn Đục Lỗ (Sigil of Socketing)",
        "icon": "images/items/sigil_of_socketing.png",
        "mod": "Apotheosis",
        "category": "Consumable",
        "stage": "Mid",
        "classTags": ["All Classes", "Meta Build"],
        "recipe_type": "Smithing Table / Drop",
        "ingredients": [
            {"id": "gem_dust", "name": "Gem Dust", "name_vi": "Bụi Ngọc Gem Dust", "count": 4},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 1}
        ],
        "recipe_desc_vi": "4x Bụi Ngọc + 1x Thỏi Netherite trên Smithing Table.",
        "recipe_desc_en": "4x Gem Dust + 1x Netherite Ingot.",
        "effects_vi": "Đục thêm 1 ô khảm ngọc (Socket) trên bất kỳ vũ khí hoặc giáp trụ nào (Tối đa đục được 4 lỗ)! Bắt buộc cho Meta Build.",
        "effects_en": "Adds 1 Socket slot to any weapon/armor (Up to 4 sockets max)! Essential for Meta Build.",
        "source_type": "Crafting / Dungeons",
        "source_url": "magic.html",
        "source_location_vi": "Đập Đe lấy Gem Dust rồi rèn phù ấn trên Smithing Table.",
        "source_location_en": "Crush gems with Anvils for Gem Dust."
    }
]

# Read existing database
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\build_master_item_database.py", "r", encoding="utf-8") as f:
    code = f.read()

exec_globals = {}
exec(code, exec_globals)
master_items_list = exec_globals.get("all_master_items", [])

# Combine
item_dict = {it["id"]: it for it in master_items_list}
for it in expanded_items:
    item_dict[it["id"]] = it

final_items = list(item_dict.values())

# Recompute graph
items_map = {item["id"]: item for item in final_items}
for item in final_items:
    item["used_in"] = []

for item in final_items:
    for ing in item.get("ingredients", []):
        parent_id = ing.get("id")
        if parent_id in items_map:
            items_map[parent_id]["used_in"].append({
                "id": item["id"],
                "name": item["name"],
                "name_vi": item["name_vi"],
                "icon": item["icon"],
                "category": item["category"]
            })

print(f"Master Item Database: {len(final_items)} total items compiled!")

output_js = f"""/**
 * Terramity Awakened Wiki - Master Item & Graph Database (Encyclopedic Pro Edition)
 */
const ITEM_GRAPH_DATABASE = {json.dumps(final_items, ensure_ascii=False, indent=2)};
"""

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_items.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("Saved to data_items.js successfully!")
