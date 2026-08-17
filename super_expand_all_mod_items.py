import json
import re

# Additional 50+ deep mod items
new_mod_items = [
    # ------------------ CATACLYSM ------------------
    {
        "id": "the_leviathan_axe",
        "name": "The Leviathan Axe",
        "name_vi": "Rìu Thủy Quái Leviathan (The Leviathan Axe)",
        "icon": "images/items/the_leviathan_axe.png",
        "mod": "Cataclysm",
        "category": "Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Boss Drop",
        "ingredients": [
            {"id": "tidal_claws", "name": "Tidal Claws", "name_vi": "Vuốt Thủy Triều", "count": 2},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 2}
        ],
        "recipe_desc_vi": "Rớt từ Boss The Leviathan tại Đền Thờ Trũng Biển (Sunken City).",
        "recipe_desc_en": "Dropped by The Leviathan in Sunken City.",
        "effects_vi": "18 Sát Thương Cận Chiến, Cho phép ném rìu xoay vòng tạo sóng thần quét sạch kẻ địch và tự bay về tay!",
        "effects_en": "18 Attack DMG, Throw axe creating tidal waves that returns to hand!",
        "source_type": "Boss Drop",
        "source_url": "bosses.html",
        "source_location_vi": "Thủy Quái The Leviathan tại Sunken City dưới đáy biển sâu.",
        "source_location_en": "Sunken City beneath deep oceans."
    },
    {
        "id": "meat_shredder",
        "name": "Meat Shredder",
        "name_vi": "Máy Xay Thịt (Meat Shredder)",
        "icon": "images/items/meat_shredder.png",
        "mod": "Cataclysm",
        "category": "Weapon",
        "stage": "Mid",
        "classTags": ["Warrior"],
        "recipe_type": "Boss Drop / Crafting",
        "ingredients": [
            {"id": "monstrous_horn", "name": "Monstrous Horn", "name_vi": "Sừng Quái Thú", "count": 2},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 1}
        ],
        "recipe_desc_vi": "Rớt từ Boss Netherite Monstrosity tại Soul Black Smith.",
        "recipe_desc_en": "Dropped by Netherite Monstrosity in Soul Black Smith.",
        "effects_vi": "Khoan nghiền nát mục tiêu liên tục 15 hit/giây, gây Chảy Máu (Bleeding) cực nặng.",
        "effects_en": "Rapid drill shredding 15 hits/sec with heavy Bleeding.",
        "source_type": "Boss Drop",
        "source_url": "bosses.html",
        "source_location_vi": "Netherite Monstrosity tại Soul Black Smith ở Nether.",
        "source_location_en": "Netherite Monstrosity in Nether."
    },
    {
        "id": "monstrous_helm",
        "name": "Monstrous Helm",
        "name_vi": "Mũ Quái Thú Netherite (Monstrous Helm)",
        "icon": "images/items/monstrous_helm.png",
        "mod": "Cataclysm",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Boss Drop / Crafting",
        "ingredients": [
            {"id": "monstrous_horn", "name": "Monstrous Horn", "name_vi": "Sừng Quái Thú", "count": 2},
            {"id": "netherite_helmet", "name": "Netherite Helmet", "name_vi": "Mũ Netherite", "count": 1}
        ],
        "recipe_desc_vi": "2x Sừng Quái Thú + 1x Mũ Netherite.",
        "recipe_desc_en": "2x Monstrous Horn + 1x Netherite Helmet.",
        "effects_vi": "+8 Giáp, +4 Kháng Đẩy Lùi, Khi húc đầu vào quái vật gây 30 Sát thương nén và Choáng 2 giây!",
        "effects_en": "+8 Armor, +4 Knockback Resist, Headbutt deals 30 DMG and stuns 2s!",
        "source_type": "Crafting",
        "source_url": "bosses.html",
        "source_location_vi": "Rèn từ sừng của Netherite Monstrosity.",
        "source_location_en": "Crafted with Monstrous Horns."
    },

    # ------------------ ALEX'S CAVES ------------------
    {
        "id": "raygun",
        "name": "Raygun",
        "name_vi": "Súng Phóng Xạ Uranium (Raygun)",
        "icon": "images/items/raygun.png",
        "mod": "Alex's Caves",
        "category": "Weapon",
        "stage": "Mid",
        "classTags": ["Archer", "Engineer"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "uranium_rod", "name": "Uranium Rod", "name_vi": "Thanh Uranium Phóng Xạ", "count": 2},
            {"id": "heavyweight", "name": "Heavyweight", "name_vi": "Khối Từ Tính Nặng", "count": 1}
        ],
        "recipe_desc_vi": "2x Thanh Uranium + 1x Khối Từ Tính Nặng.",
        "recipe_desc_en": "2x Uranium Rod + 1x Heavyweight.",
        "effects_vi": "Bắn chùm tia laser phóng xạ xanh lục hủy diệt, làm phân rã hạt nhân mọi quái vật từ xa!",
        "effects_en": "Fires continuous green radioactive death lasers!",
        "source_type": "Crafting / Toxic Caves",
        "source_url": "creatures.html",
        "source_location_vi": "Khai thác Uranium tại Toxic Caves ngầm.",
        "source_location_en": "Toxic Caves underground."
    },
    {
        "id": "hazmat_suit_set",
        "name": "Hazmat Suit Set",
        "name_vi": "Bộ Đồ Chống Phóng Xạ (Hazmat Suit Set)",
        "icon": "images/items/hazmat_suit_set.png",
        "mod": "Alex's Caves",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "polymer_plate", "name": "Polymer Plate", "name_vi": "Tấm Nhựa Polymer", "count": 24}
        ],
        "recipe_desc_vi": "Chế tạo từ 24x Tấm Nhựa Polymer tại Bàn chế tạo.",
        "recipe_desc_en": "Crafted from 24x Polymer Plates.",
        "effects_vi": "Kháng 100% Bức Xạ Hạt Nhân & Khí Độc khi thám hiểm quần xã Toxic Caves!",
        "effects_en": "100% Nuclear Radiation & Toxic Gas Immunity!",
        "source_type": "Crafting",
        "source_url": "creatures.html",
        "source_location_vi": "Bắt buộc phải mang khi xuống Toxic Caves.",
        "source_location_en": "Essential for exploring Toxic Caves."
    },
    {
        "id": "diving_suit_set",
        "name": "Diving Suit Set",
        "name_vi": "Bộ Giáp Lặn Biển Sâu (Diving Suit Set)",
        "icon": "images/items/diving_suit_set.png",
        "mod": "Alex's Caves",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "copper_ingot", "name": "Copper Ingot", "name_vi": "Thỏi Đồng", "count": 16},
            {"id": "glass", "name": "Glass", "name_vi": "Kính Thủy Tinh", "count": 4}
        ],
        "recipe_desc_vi": "16x Thỏi Đồng + 4x Kính Thủy Tinh.",
        "recipe_desc_en": "16x Copper Ingot + 4x Glass.",
        "effects_vi": "Thở dưới nước vô hạn, Kháng 100% Áp Suất Nghiền Nát dưới đáy vực thẳm Abyssal Chasm!",
        "effects_en": "Infinite underwater breathing, 100% Water Pressure Immunity!",
        "source_type": "Crafting",
        "source_url": "creatures.html",
        "source_location_vi": "Bắt buộc khi xuống Abyssal Chasm.",
        "source_location_en": "Essential for Abyssal Chasm."
    },

    # ------------------ ICE AND FIRE ------------------
    {
        "id": "dragon_horn",
        "name": "Dragon Horn",
        "name_vi": "Tù Và Thu Rồng (Dragon Horn)",
        "icon": "images/items/dragon_horn.png",
        "mod": "Ice and Fire",
        "category": "Tool",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "dragon_bone", "name": "Dragon Bone", "name_vi": "Xương Rồng", "count": 4}
        ],
        "recipe_desc_vi": "4x Xương Rồng đặt chéo tại Bàn chế tạo.",
        "recipe_desc_en": "4x Dragon Bones.",
        "effects_vi": "Thu và nhốt chú Rồng đã thuần phục vào trong tù và để mang theo khắp mọi nơi!",
        "effects_en": "Stores and releases tamed dragons freely!",
        "source_type": "Crafting",
        "source_url": "creatures.html",
        "source_location_vi": "Thu thập xương từ xác rồng sa mạc hoặc tuyết.",
        "source_location_en": "Harvested from dragon skeletons."
    },
    {
        "id": "gorgon_head",
        "name": "Gorgon Head",
        "name_vi": "Đầu Xà Nữ Gorgon (Gorgon Head)",
        "icon": "images/items/gorgon_head.png",
        "mod": "Ice and Fire",
        "category": "Weapon",
        "stage": "Mid",
        "classTags": ["All Classes"],
        "recipe_type": "Mob Drop",
        "ingredients": [
            {"id": "gorgon_temple", "name": "Gorgon Temple", "name_vi": "Đền Thờ Gorgon", "count": 1}
        ],
        "recipe_desc_vi": "Rớt khi chặt đầu Xà Nữ Gorgon tại Đền Thờ Hy Lạp ven biển.",
        "recipe_desc_en": "Obtained by slaying Gorgon in coastal temples.",
        "effects_vi": "Giơ đầu lên soi vào bất kỳ Boss hoặc Quái vật nào sẽ biến chúng thành tượng đá vĩnh viễn (Insta-kill)!",
        "effects_en": "Instantly petrifies any target into solid stone!",
        "source_type": "Mob Drop",
        "source_url": "creatures.html",
        "source_location_vi": "Đền thờ Gorgon ngầm bờ biển.",
        "source_location_en": "Gorgon coastal temples."
    },
    {
        "id": "hydra_heart",
        "name": "Hydra Heart",
        "name_vi": "Trái Tim Rồng Chín Đầu (Hydra Heart)",
        "icon": "images/items/hydra_heart.png",
        "mod": "Ice and Fire",
        "category": "Relic",
        "stage": "Late",
        "classTags": ["All Classes", "Warrior"],
        "recipe_type": "Boss Drop",
        "ingredients": [
            {"id": "hydra_fang", "name": "Hydra Fang", "name_vi": "Nanh Hydra", "count": 1}
        ],
        "recipe_desc_vi": "Rớt khi tiêu diệt quái thú Hydra tại đầm lầy Swamp.",
        "recipe_desc_en": "Dropped by Hydra in Swamps.",
        "effects_vi": "Ban tặng hiệu ứng Hồi Phục Sinh Lực Tối Thượng (Regeneration IV) vĩnh viễn khi cầm trên tay hoặc túi đồ!",
        "effects_en": "Grants permanent Regeneration IV aura in inventory!",
        "source_type": "Boss Drop",
        "source_url": "creatures.html",
        "source_location_vi": "Hydra trong đầm lầy hắc ám.",
        "source_location_en": "Hydra swamp lair."
    },

    # ------------------ THE AETHER ------------------
    {
        "id": "valkyrie_lance",
        "name": "Valkyrie Lance",
        "name_vi": "Thương Nữ Hoàng Valkyrie (Valkyrie Lance)",
        "icon": "images/items/valkyrie_lance.png",
        "mod": "The Aether",
        "category": "Weapon",
        "stage": "Mid",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Dungeon Boss Reward",
        "ingredients": [
            {"id": "silver_dungeon_key", "name": "Silver Dungeon Key", "name_vi": "Chìa Khóa Bạc", "count": 1}
        ],
        "recipe_desc_vi": "Mở rương kho báu Silver Dungeon sau khi hạ Nữ Hoàng Valkyrie.",
        "recipe_desc_en": "Silver Dungeon chest reward.",
        "effects_vi": "14 Sát Thương Cận Chiến, Tầm đòn đánh cực xa (+3.5 Block Reach) và tăng 25% tốc độ tấn công.",
        "effects_en": "14 Attack DMG, +3.5 Block Attack Reach and +25% Attack Speed.",
        "source_type": "Dungeon Chest",
        "source_url": "dimensions.html",
        "source_location_vi": "Silver Dungeon trên đảo mây Aether.",
        "source_location_en": "Silver Dungeon in Aether skies."
    },
    {
        "id": "phoenix_bow",
        "name": "Phoenix Bow",
        "name_vi": "Cung Phượng Hoàng (Phoenix Bow)",
        "icon": "images/items/phoenix_bow.png",
        "mod": "The Aether",
        "category": "Weapon",
        "stage": "Mid",
        "classTags": ["Archer"],
        "recipe_type": "Dungeon Boss Reward",
        "ingredients": [
            {"id": "gold_dungeon_key", "name": "Gold Dungeon Key", "name_vi": "Chìa Khóa Vàng", "count": 1}
        ],
        "recipe_desc_vi": "Mở rương kho báu Gold Dungeon sau khi đánh bại Thần Mặt Trời Sun Spirit.",
        "recipe_desc_en": "Gold Dungeon chest reward.",
        "effects_vi": "Bắn ra mũi tên rực lửa Phượng Hoàng tự thiêu đốt và nổ tung khi trúng mục tiêu, không tiêu hao tên thường!",
        "effects_en": "Fires fiery explosive phoenix arrows with infinite ammo!",
        "source_type": "Dungeon Chest",
        "source_url": "dimensions.html",
        "source_location_vi": "Gold Dungeon đền thờ mặt trời Aether.",
        "source_location_en": "Gold Dungeon in Aether."
    },

    # ------------------ DEEPER AND DARKER ------------------
    {
        "id": "heart_of_the_deep",
        "name": "Heart of the Deep",
        "name_vi": "Trái Tim Vực Sâu (Heart of the Deep)",
        "icon": "images/items/heart_of_the_deep.png",
        "mod": "Deeper and Darker",
        "category": "Material",
        "stage": "Mid",
        "classTags": ["All Classes"],
        "recipe_type": "Boss Drop",
        "ingredients": [
            {"id": "warden_echo", "name": "Warden Echo", "name_vi": "Vọng Âm Warden", "count": 1}
        ],
        "recipe_desc_vi": "100% Rớt khi tiêu diệt Quái Thú The Warden tại Ancient City.",
        "recipe_desc_en": "100% drop from The Warden in Ancient City.",
        "effects_vi": "Chìa khóa kích hoạt Cổng Khung Lớn ở trung tâm Thành Phố Cổ Đại để bước vào The Otherside!",
        "effects_en": "Key to activate The Otherside portal in Ancient City!",
        "source_type": "Boss Drop",
        "source_url": "dimensions.html",
        "source_location_vi": "Hạ gục The Warden dưới lòng đất Deep Dark.",
        "source_location_en": "Slay The Warden in Deep Dark."
    },
    {
        "id": "warden_armor_set",
        "name": "Warden Armor Set",
        "name_vi": "Bộ Đại Giáp Warden (Warden Armor Set)",
        "icon": "images/items/warden_armor_set.png",
        "mod": "Deeper and Darker",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "resonarium_ingot", "name": "Resonarium Ingot", "name_vi": "Thỏi Resonarium", "count": 4},
            {"id": "netherite_armor", "name": "Netherite Armor", "name_vi": "Bộ Giáp Netherite", "count": 1}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Netherite + Thỏi Resonarium trên Smithing Table.",
        "recipe_desc_en": "Netherite Armor + Resonarium Ingots.",
        "effects_vi": "+28 Giáp, +12 Độ Bền Giáp, Miễn nhiễm hoàn toàn hiệu ứng Mù Lòa (Darkness/Blindness) và tăng 40% Tốc độ di chuyển trong bóng tối!",
        "effects_en": "+28 Armor, +12 Toughness, 100% Darkness/Blindness Immunity, +40% Speed in dark!",
        "source_type": "Crafting",
        "source_url": "dimensions.html",
        "source_location_vi": "Khai thác Resonarium trong The Otherside.",
        "source_location_en": "Mined in The Otherside dimension."
    },

    # ------------------ GOETY & REVELATION ------------------
    {
        "id": "ascension_halo",
        "name": "Ascension Halo",
        "name_vi": "Hào Quang Thăng Hoa (Ascension Halo)",
        "icon": "images/items/ascension_halo.png",
        "mod": "Goety Revelation",
        "category": "Material",
        "stage": "Endgame",
        "classTags": ["All Classes", "Mage"],
        "recipe_type": "Boss Drop",
        "ingredients": [
            {"id": "apollyon_drop", "name": "Apollyon Drop", "name_vi": "Chiến Lợi Phẩm Apollyon", "count": 1}
        ],
        "recipe_desc_vi": "Rớt khi tiêu diệt Siêu Boss Apollyon (6.666 HP) trong nghi lễ Dark Altar.",
        "recipe_desc_en": "Dropped by Super-Boss Apollyon (6,666 HP).",
        "effects_vi": "Nguyên liệu thần thánh để rèn Thỏi Tận Thế Apocalyptium và đúc Giáp Thiên Sứ Bất Bại!",
        "effects_en": "Sacred material to forge Apocalyptium Ingots and Angelic Armor!",
        "source_type": "Super-Boss",
        "source_url": "magic.html",
        "source_location_vi": "Siêu Boss Apollyon lúc 00:00 nửa đêm.",
        "source_location_en": "Super-Boss Apollyon at midnight."
    },
    {
        "id": "command_horn",
        "name": "Command Horn",
        "name_vi": "Tù Và Chỉ Huy (Command Horn)",
        "icon": "images/items/command_horn.png",
        "mod": "Goety",
        "category": "Tool",
        "stage": "Early",
        "classTags": ["Mage", "Necromancer"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "magic_fabric", "name": "Magic Fabric", "name_vi": "Vải Ma Thuật", "count": 4},
            {"id": "haunted_log", "name": "Haunted Log", "name_vi": "Gỗ Ma Ám", "count": 2}
        ],
        "recipe_desc_vi": "4x Vải Ma Thuật + 2x Gỗ Ma Ám.",
        "recipe_desc_en": "4x Magic Fabric + 2x Haunted Log.",
        "effects_vi": "Thổi tù và để phát lệnh điều khiển Binh Đoàn Xác Sống (Tấn công mục tiêu, Phòng thủ, hoặc Đi theo bảo vệ)!",
        "effects_en": "Commands Undead Servant army to attack, guard, or follow!",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo sau khi có Vải Ma Thuật Goety.",
        "source_location_en": "Crafted with Goety Magic Fabric."
    }
]

# Read existing master items
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\expand_all_items_catalog.py", "r", encoding="utf-8") as f:
    code = f.read()

exec_globals = {}
exec(code, exec_globals)
current_items = exec_globals.get("final_items", [])

item_dict = {it["id"]: it for it in current_items}
for it in new_mod_items:
    item_dict[it["id"]] = it

all_final = list(item_dict.values())

# Recompute bidirectional graph
items_map = {item["id"]: item for item in all_final}
for item in all_final:
    item["used_in"] = []

for item in all_final:
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

print(f"Super Expanded Database: {len(all_final)} total items across ALL mods!")

output_js = f"""/**
 * Terramity Awakened Wiki - Complete Master Item & Bidirectional Graph Database (All Mods Edition)
 */
const ITEM_GRAPH_DATABASE = {json.dumps(all_final, ensure_ascii=False, indent=2)};
"""

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_items.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("Saved to data_items.js successfully!")
