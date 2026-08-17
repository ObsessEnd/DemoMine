import os
import glob
import json
import re

# Comprehensive Item Database Definitions with Full Graph Cross-Linking
items_db = [
    # -------------------------------------------------------------
    # 1. BASIC / INGREDIENT ROOTS (Tier 0 / Early Materials)
    # -------------------------------------------------------------
    {
        "id": "blank_rune",
        "name": "Blank Rune",
        "name_vi": "Cổ Tự Trắng (Blank Rune)",
        "icon": "images/items/blank_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Magic Material",
        "stage": "Early",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_essence", "name": "Arcane Essence", "name_vi": "Tinh Chất Ma Thuật", "count": 4},
            {"id": "stone", "name": "Stone", "name_vi": "Đá Thường", "count": 4}
        ],
        "recipe_desc_vi": "4x Arcane Essence + 4x Stone đặt xung quanh bàn chế tạo.",
        "recipe_desc_en": "4x Arcane Essence + 4x Stone in Crafting Table.",
        "effects_vi": "Phôi đá ma thuật trung tính dùng để khắc thành 8 loại Cổ Tự nguyên tố (Fire, Ice, Lightning, Holy, Ender, Blood, Evocation, Nature).",
        "effects_en": "Neutral arcane stone base used to inscribe 8 elemental runes.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Chế tạo từ Arcane Essence rơi ra từ quái vật ma thuật.",
        "source_location_en": "Crafted from Arcane Essence dropped by magical mobs."
    },
    {
        "id": "arcane_essence",
        "name": "Arcane Essence",
        "name_vi": "Tinh Chất Ma Thuật (Arcane Essence)",
        "icon": "images/items/arcane_essence.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Magic Material",
        "stage": "Early",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Mob Drop / Mining",
        "ingredients": [],
        "recipe_desc_vi": "Rơi từ phù thủy (Witch), Cryomancer, Pyromancer hoặc đào quặng Arcane Debris dưới lòng đất.",
        "recipe_desc_en": "Dropped by Witches, Cryomancers, Pyromancers or mined from Arcane Debris.",
        "effects_vi": "Bột tinh chất thuần khiết dùng để dệt Vải Ma Thuật (Arcane Cloth) và rèn Cổ Tự Trắng.",
        "effects_en": "Pure essence used to weave Arcane Cloth and forge Blank Runes.",
        "source_type": "Mob Drop / Mining",
        "source_url": "magic.html",
        "source_location_vi": "Đào quặng Arcane Debris ở tầng Y = 20 đến -40 hoặc tiêu diệt Phù thủy.",
        "source_location_en": "Mine Arcane Debris at Y = 20 to -40 or slay Witch mobs."
    },
    {
        "id": "arcane_cloth",
        "name": "Arcane Cloth",
        "name_vi": "Vải Ma Thuật (Arcane Cloth)",
        "icon": "images/items/arcane_cloth.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Magic Material",
        "stage": "Early",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_essence", "name": "Arcane Essence", "name_vi": "Tinh Chất Ma Thuật", "count": 4},
            {"id": "wool", "name": "Wool", "name_vi": "Len Cừu", "count": 4}
        ],
        "recipe_desc_vi": "4x Arcane Essence + 4x Wool (Len cừu).",
        "recipe_desc_en": "4x Arcane Essence + 4x Wool in Crafting Table.",
        "effects_vi": "Chất liệu dệt nên toàn bộ các bộ giáp Pháp Sư (Pyromancer, Cryomancer, Electromancer, Priest...).",
        "effects_en": "Textile used to tailor all Mage Armor sets.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Ghép tại Bàn chế tạo từ Len và Tinh chất Ma thuật.",
        "source_location_en": "Craft at Crafting Table with Wool and Arcane Essence."
    },
    {
        "id": "blaze_rod",
        "name": "Blaze Rod",
        "name_vi": "Que Lửa (Blaze Rod)",
        "icon": "images/items/blaze_rod.png",
        "mod": "Minecraft Vanilla",
        "category": "Ingredient",
        "stage": "Early",
        "classTags": ["All Classes", "Fire Mage"],
        "recipe_type": "Mob Drop",
        "ingredients": [],
        "recipe_desc_vi": "Rơi ra khi tiêu diệt quái Blaze trong Pháo đài Địa ngục Nether Fortress.",
        "recipe_desc_en": "Dropped by Blazes in Nether Fortresses.",
        "effects_vi": "Nguyên liệu chế tạo Cổ Tự Lửa, Bột Lửa nung lò và thuốc kháng lửa.",
        "effects_en": "Used to craft Fire Runes, Blaze Powder, and potions.",
        "source_type": "Nether Fortress",
        "source_url": "dimensions.html#dim-nether",
        "source_location_vi": "Pháo đài Nether Fortress giữa biển dung nham.",
        "source_location_en": "Nether Fortresses inside The Nether."
    },
    {
        "id": "cinder_essence",
        "name": "Cinder Essence",
        "name_vi": "Tinh Chất Tro Tàn (Cinder Essence)",
        "icon": "images/items/cinder_essence.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Magic Material",
        "stage": "Mid",
        "classTags": ["Fire Mage", "Mage"],
        "recipe_type": "Mob Drop (Nether)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi từ các pháp sư hỏa ngục và quái vật Nether.",
        "recipe_desc_en": "Dropped by Nether Pyromancers and fiery mobs.",
        "effects_vi": "Nguyên liệu nâng cấp Ngọc Cường Hóa Hỏa Hệ (Fire Upgrade Orb).",
        "effects_en": "Material to craft Fire Upgrade Orbs.",
        "source_type": "The Nether",
        "source_url": "dimensions.html#dim-nether",
        "source_location_vi": "Các pháo đài và hầm ngục trong Nether.",
        "source_location_en": "Nether dungeons and Pyromancer towers."
    },
    {
        "id": "frozen_bone",
        "name": "Frozen Bone",
        "name_vi": "Xương Băng Giá (Frozen Bone)",
        "icon": "images/items/frozen_bone.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Magic Material",
        "stage": "Early",
        "classTags": ["Ice Mage", "Mage"],
        "recipe_type": "Mob Drop (Stray)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi khi tiêu diệt quái xương Stray tại các vùng tuyết băng giá.",
        "recipe_desc_en": "Dropped by Strays in icy snowy biomes.",
        "effects_vi": "Dùng để khắc Cổ Tự Băng Ma (Ice Rune).",
        "effects_en": "Used to inscribe Ice Runes.",
        "source_type": "Snow Biomes",
        "source_url": "creatures.html",
        "source_location_vi": "Snowy Plains, Ice Spikes, Frozen Ocean.",
        "source_location_en": "Snowy Plains, Ice Spikes, Frozen Ocean."
    },
    {
        "id": "divine_pearl",
        "name": "Divine Pearl",
        "name_vi": "Ngọc Trai Thánh (Divine Pearl)",
        "icon": "images/items/divine_pearl.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Magic Material",
        "stage": "Early",
        "classTags": ["Paladin", "Mage"],
        "recipe_type": "Villager Trading / Drop",
        "ingredients": [],
        "recipe_desc_vi": "Đổi từ Dân Làng Mục Sư (Cleric Villager) hoặc nhặt trong Đền thờ Thánh.",
        "recipe_desc_en": "Traded from Cleric Villagers or found in Holy Temples.",
        "effects_vi": "Dùng để khắc Cổ Tự Thánh Quang (Holy Rune).",
        "effects_en": "Used to craft Holy Runes.",
        "source_type": "Villages / Churches",
        "source_url": "magic.html",
        "source_location_vi": "Nhà thờ làng Dân làng hoặc Đền thờ Thánh.",
        "source_location_en": "Villages and sacred chapels."
    },

    # -------------------------------------------------------------
    # 2. RUNES & SPELL MATERIALS
    # -------------------------------------------------------------
    {
        "id": "fire_rune",
        "name": "Fire Rune",
        "name_vi": "Cổ Tự Hỏa Ma (Fire Rune)",
        "icon": "images/items/fire_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Rune / Magic",
        "stage": "Early",
        "classTags": ["Mage", "Fire Mage", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "blank_rune", "name": "Blank Rune", "name_vi": "Cổ Tự Trắng", "count": 1},
            {"id": "blaze_rod", "name": "Blaze Rod", "name_vi": "Que Lửa", "count": 1}
        ],
        "recipe_desc_vi": "1x Blank Rune + 1x Blaze Rod (Bàn chế tạo).",
        "recipe_desc_en": "1x Blank Rune + 1x Blaze Rod (Crafting Table).",
        "effects_vi": "Nguyên liệu cốt lõi để rèn Áo Choàng Pyromancer, Cuộn Phép Hỏa Cầu, Kiếm Liễu Fireblossom Rapier và Ngọc Cường Hóa Lửa.",
        "effects_en": "Core material for Pyromancer Armor, Fireball scrolls, Fireblossom Rapier, and Fire Upgrade Orbs.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Chế tạo sau khi săn Blaze tại Nether Fortress.",
        "source_location_en": "Crafted after hunting Blazes in Nether Fortress."
    },
    {
        "id": "ice_rune",
        "name": "Ice Rune",
        "name_vi": "Cổ Tự Băng Ma (Ice Rune)",
        "icon": "images/items/ice_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Rune / Magic",
        "stage": "Early",
        "classTags": ["Mage", "Ice Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "blank_rune", "name": "Blank Rune", "name_vi": "Cổ Tự Trắng", "count": 1},
            {"id": "frozen_bone", "name": "Frozen Bone", "name_vi": "Xương Băng Giá", "count": 1}
        ],
        "recipe_desc_vi": "1x Blank Rune + 1x Frozen Bone (Bàn chế tạo).",
        "recipe_desc_en": "1x Blank Rune + 1x Frozen Bone (Crafting Table).",
        "effects_vi": "Rèn Áo Choàng Cryomancer, Cuộn Phép Đóng Băng Frost Step và Giáo Băng Ice Pike.",
        "effects_en": "Crafts Cryomancer Armor, Frost Step scrolls, and Ice Pike.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Săn Stray ở vùng tuyết lấy Frozen Bone rồi rèn cổ tự.",
        "source_location_en": "Hunt Strays in snowy biomes for Frozen Bones."
    },
    {
        "id": "holy_rune",
        "name": "Holy Rune",
        "name_vi": "Cổ Tự Thánh Quang (Holy Rune)",
        "icon": "images/items/holy_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Rune / Magic",
        "stage": "Early",
        "classTags": ["Paladin", "Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "blank_rune", "name": "Blank Rune", "name_vi": "Cổ Tự Trắng", "count": 1},
            {"id": "divine_pearl", "name": "Divine Pearl", "name_vi": "Ngọc Trai Thánh", "count": 1}
        ],
        "recipe_desc_vi": "1x Blank Rune + 1x Divine Pearl (Bàn chế tạo).",
        "recipe_desc_en": "1x Blank Rune + 1x Divine Pearl (Crafting Table).",
        "effects_vi": "Rèn Áo Choàng Priest Armor, Cuộn Phép Hồi Máu Heal & Divine Smite, và Kiếm Thánh Excalibur.",
        "effects_en": "Crafts Priest Armor, Heal & Divine Smite scrolls, and Excalibur.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Giao dịch với Dân làng Mục sư lấy Divine Pearl.",
        "source_location_en": "Trade with Cleric villagers for Divine Pearls."
    },
    {
        "id": "lightning_rune",
        "name": "Lightning Rune",
        "name_vi": "Cổ Tự Lôi Hệ (Lightning Rune)",
        "icon": "images/items/lightning_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Rune / Magic",
        "stage": "Early",
        "classTags": ["Mage", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "blank_rune", "name": "Blank Rune", "name_vi": "Cổ Tự Trắng", "count": 1},
            {"id": "copper_ingot", "name": "Copper Ingot", "name_vi": "Thỏi Đồng", "count": 1},
            {"id": "lightning_rod", "name": "Lightning Rod", "name_vi": "Cột Thu Lôi", "count": 1}
        ],
        "recipe_desc_vi": "1x Blank Rune + 1x Lightning Rod + 1x Copper Ingot.",
        "recipe_desc_en": "1x Blank Rune + 1x Lightning Rod + 1x Copper Ingot.",
        "effects_vi": "Rèn Áo Choàng Electromancer, Cuộn Phép Giật Sét Chain Lightning và Đại Đao Ionic Splitter.",
        "effects_en": "Crafts Electromancer Armor, Chain Lightning scrolls, and Ionic Splitter.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Chế tạo từ Cột thu lôi và Cổ Tự Trắng.",
        "source_location_en": "Crafted using Lightning Rods and Blank Runes."
    },
    {
        "id": "blood_rune",
        "name": "Blood Rune",
        "name_vi": "Cổ Tự Huyết Ma (Blood Rune)",
        "icon": "images/items/blood_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Rune / Magic",
        "stage": "Mid",
        "classTags": ["Mage", "Warrior"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "blank_rune", "name": "Blank Rune", "name_vi": "Cổ Tự Trắng", "count": 1},
            {"id": "blood_vial", "name": "Blood Vial", "name_vi": "Lọ Máu Hiến Tế", "count": 1}
        ],
        "recipe_desc_vi": "1x Blank Rune + 1x Blood Vial (Trích xuất máu quái vật).",
        "recipe_desc_en": "1x Blank Rune + 1x Blood Vial.",
        "effects_vi": "Rèn Áo Choàng Cultist Armor, Cuộn Phép Blood Slash và Đại Đao Devastator.",
        "effects_en": "Crafts Cultist Armor, Blood Slash scrolls, and Devastator Cleaver.",
        "source_type": "Crafting / Catacombs",
        "source_url": "magic.html",
        "source_location_vi": "Hầm mộ ngầm Catacombs hoặc trích máu hiến tế.",
        "source_location_en": "Catacombs underground or blood extraction rituals."
    },

    # -------------------------------------------------------------
    # 3. WORKSTATIONS & FORGES
    # -------------------------------------------------------------
    {
        "id": "scroll_forge",
        "name": "Scroll Forge",
        "name_vi": "Lò Rèn Cuộn Phép (Scroll Forge)",
        "icon": "images/items/scroll_forge.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Workstation",
        "stage": "Early",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "iron_ingot", "name": "Iron Ingot", "name_vi": "Thỏi Sắt", "count": 4},
            {"id": "stone", "name": "Stone", "name_vi": "Đá Thường", "count": 2},
            {"id": "arcane_essence", "name": "Arcane Essence", "name_vi": "Tinh Chất Ma Thuật", "count": 1}
        ],
        "recipe_desc_vi": "4x Sắt + 2x Đá + 1x Tinh Chất Ma Thuật.",
        "recipe_desc_en": "4x Iron Ingot + 2x Stone + 1x Arcane Essence.",
        "effects_vi": "Bàn chế tạo cho phép tạo ra tất cả các loại Cuộn Phép (Scrolls) từ nguyên liệu Cổ tự và Giấy trắng.",
        "effects_en": "Workstation enabling crafting of all spell scrolls using Runes and Paper.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Chế tạo ngay từ Ngày 1.",
        "source_location_en": "Craftable on Day 1."
    },
    {
        "id": "arcane_anvil",
        "name": "Arcane Anvil",
        "name_vi": "Đe Ma Thuật (Arcane Anvil)",
        "icon": "images/items/arcane_anvil.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Workstation",
        "stage": "Mid",
        "classTags": ["Mage", "All Classes", "Meta Build"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 4},
            {"id": "anvil", "name": "Anvil", "name_vi": "Đe Sắt Vanilla", "count": 1},
            {"id": "blank_rune", "name": "Blank Rune", "name_vi": "Cổ Tự Trắng", "count": 2}
        ],
        "recipe_desc_vi": "4x Arcane Cloth + 1x Anvil + 2x Blank Rune.",
        "recipe_desc_en": "4x Arcane Cloth + 1x Anvil + 2x Blank Rune.",
        "effects_vi": "Dùng để nâng cấp Sách Phép, gắn tối đa 10 Upgrade Orbs vào trang bị và Imbue ép chiêu thức phép thuật trực tiếp vào Vũ khí cận chiến!",
        "effects_en": "Used to upgrade Spellbooks, socket up to 10 Upgrade Orbs, and imbue spells into weapons!",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo ma thuật cấp trung.",
        "source_location_en": "Mid-game crafting table."
    },

    # -------------------------------------------------------------
    # 4. ARMOR SETS (MAGE / WARRIOR / PALADIN / RANGER)
    # -------------------------------------------------------------
    {
        "id": "pyromancer_chestplate",
        "name": "Pyromancer Chestplate",
        "name_vi": "Áo Choàng Hỏa Thuật Sư (Pyromancer)",
        "icon": "images/items/pyromancer_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Mage", "Fire Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 4},
            {"id": "fire_rune", "name": "Fire Rune", "name_vi": "Cổ Tự Hỏa Ma", "count": 3},
            {"id": "iron_chestplate", "name": "Iron Chestplate", "name_vi": "Áo Giáp Sắt", "count": 1}
        ],
        "recipe_desc_vi": "4x Arcane Cloth + 3x Fire Rune + 1x Iron Chestplate.",
        "recipe_desc_en": "4x Arcane Cloth + 3x Fire Rune + 1x Iron Chestplate.",
        "effects_vi": "+5% Sát thương Hỏa phép, +50 Mana tối đa, Kháng thiêu đốt 25%.",
        "effects_en": "+5% Fire Spell Power, +50 Max Mana, 25% Fire Resistance.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo sau khi có Fire Rune và Arcane Cloth.",
        "source_location_en": "Craft at Crafting Table with Fire Runes and Arcane Cloth."
    },
    {
        "id": "cryomancer_chestplate",
        "name": "Cryomancer Chestplate",
        "name_vi": "Áo Choàng Băng Thuật Sư (Cryomancer)",
        "icon": "images/items/cryomancer_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Mage", "Ice Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 4},
            {"id": "ice_rune", "name": "Ice Rune", "name_vi": "Cổ Tự Băng Ma", "count": 3},
            {"id": "iron_chestplate", "name": "Iron Chestplate", "name_vi": "Áo Giáp Sắt", "count": 1}
        ],
        "recipe_desc_vi": "4x Arcane Cloth + 3x Ice Rune + 1x Iron Chestplate.",
        "recipe_desc_en": "4x Arcane Cloth + 3x Ice Rune + 1x Iron Chestplate.",
        "effects_vi": "+5% Sát thương Băng phép, +50 Mana tối đa, Kháng làm chậm và giá buốt.",
        "effects_en": "+5% Ice Spell Power, +50 Max Mana, Freeze Resistance.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo sau khi có Ice Rune.",
        "source_location_en": "Craft at Crafting Table with Ice Runes."
    },
    {
        "id": "priest_chestplate",
        "name": "Priest Robe",
        "name_vi": "Áo Choàng Mục Sư (Priest Robe)",
        "icon": "images/items/priest_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Paladin", "Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 4},
            {"id": "holy_rune", "name": "Holy Rune", "name_vi": "Cổ Tự Thánh Quang", "count": 3},
            {"id": "iron_chestplate", "name": "Iron Chestplate", "name_vi": "Áo Giáp Sắt", "count": 1}
        ],
        "recipe_desc_vi": "4x Arcane Cloth + 3x Holy Rune + 1x Iron Chestplate.",
        "recipe_desc_en": "4x Arcane Cloth + 3x Holy Rune + 1x Iron Chestplate.",
        "effects_vi": "+5% Sát thương Thánh, +20% Hiệu quả hồi máu cho bản thân và đồng đội.",
        "effects_en": "+5% Holy Spell Power, +20% Healing effectiveness for party.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo sau khi có Holy Rune.",
        "source_location_en": "Craft at Crafting Table with Holy Runes."
    },
    {
        "id": "warden_chestplate",
        "name": "Warden Chestplate",
        "name_vi": "Áo Giáp Cai Ngục Warden",
        "icon": "images/items/warden_chestplate.png",
        "mod": "Deeper and Darker",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin", "All Classes"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "resonarium_ingot", "name": "Resonarium Ingot", "name_vi": "Thỏi Resonarium", "count": 4},
            {"id": "reinforced_echo_shard", "name": "Reinforced Echo Shard", "name_vi": "Mảnh Vọng Âm Cường Hóa", "count": 2},
            {"id": "netherite_chestplate", "name": "Netherite Chestplate", "name_vi": "Áo Giáp Netherite", "count": 1}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Netherite + Thỏi Resonarium trên Smithing Table.",
        "recipe_desc_en": "Upgrade Netherite Chestplate with Resonarium Ingot at Smithing Table.",
        "effects_vi": "+12 Điểm Giáp, +4 Kháng Đẩy Lùi, KHÁNG VĨNH VIỄN HIỆU ỨNG MÙ LÒA (Blindness/Darkness Immunity)!",
        "effects_en": "+12 Armor, +4 Knockback Resist, PERMANENT IMMUNITY TO BLINDNESS & DARKNESS!",
        "source_type": "The Otherside Crafting",
        "source_url": "dimensions.html#dim-otherside",
        "source_location_vi": "Khai thác quặng trong cõi âm The Otherside sau khi hạ Warden.",
        "source_location_en": "Mine in The Otherside dimension after slaying The Warden."
    },

    # -------------------------------------------------------------
    # 5. WEAPONS (MELEE, RANGED, SPELL WEAPONS)
    # -------------------------------------------------------------
    {
        "id": "fireblossom_rapier",
        "name": "Fireblossom Rapier",
        "name_vi": "Kiếm Liễu Hỏa Liên (Fireblossom Rapier)",
        "icon": "images/items/fireblossom_rapier.png",
        "mod": "Hazen 'n Stuff",
        "category": "Spell Weapon",
        "stage": "Early",
        "classTags": ["Mage", "Fire Mage", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "fire_rune", "name": "Fire Rune", "name_vi": "Cổ Tự Hỏa Ma", "count": 2},
            {"id": "iron_ingot", "name": "Iron Ingot", "name_vi": "Thỏi Sắt", "count": 2},
            {"id": "blaze_rod", "name": "Blaze Rod", "name_vi": "Que Lửa", "count": 1}
        ],
        "recipe_desc_vi": "2x Fire Rune + 2x Iron Ingot + 1x Blaze Rod.",
        "recipe_desc_en": "2x Fire Rune + 2x Iron Ingot + 1x Blaze Rod.",
        "effects_vi": "Tích hợp sẵn chiêu thức Flaming Strike Cấp 5; mỗi nhát đâm kích nổ ngọn lửa thiêu rụi mục tiêu.",
        "effects_en": "Pre-imbued with Flaming Strike Lv5; thrusting detonates fiery explosions on impact.",
        "source_type": "Crafting",
        "source_url": "creatures.html",
        "source_location_vi": "Bàn chế tạo sau khi có Fire Rune.",
        "source_location_en": "Craft at Crafting Table with Fire Runes."
    },
    {
        "id": "fire_upgrade_orb",
        "name": "Fire Upgrade Orb",
        "name_vi": "Ngọc Cường Hóa Hỏa Hệ (Fire Orb)",
        "icon": "images/items/fire_upgrade_orb.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Upgrade Material",
        "stage": "Mid",
        "classTags": ["Mage", "Fire Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "fire_rune", "name": "Fire Rune", "name_vi": "Cổ Tự Hỏa Ma", "count": 4},
            {"id": "cinder_essence", "name": "Cinder Essence", "name_vi": "Tinh Chất Tro Tàn", "count": 4},
            {"id": "gold_ingot", "name": "Gold Ingot", "name_vi": "Thỏi Vàng", "count": 1}
        ],
        "recipe_desc_vi": "4x Fire Rune + 4x Cinder Essence + 1x Gold Ingot.",
        "recipe_desc_en": "4x Fire Rune + 4x Cinder Essence + 1x Gold Ingot.",
        "effects_vi": "Khảm vào trang bị trên Đe Ma Thuật (Arcane Anvil), mỗi viên tăng vĩnh viễn +3% Sát thương Hỏa (tối đa 10 viên).",
        "effects_en": "Socket in Arcane Anvil to permanently add +3% Fire Spell Power per orb (Max 10).",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Bàn chế tạo sau khi săn quái Cinder trong Nether.",
        "source_location_en": "Crafted using Cinder Essence from Nether mobs."
    },
    {
        "id": "solaris",
        "name": "Solaris",
        "name_vi": "Đại Đao Thái Dương Solaris",
        "icon": "images/items/solaris.png",
        "mod": "Celestisynth",
        "category": "Mythical Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Starlit Factory",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "sunbird_feather", "name": "Sunbird Feather", "name_vi": "Lông Chim Mặt Trời", "count": 2},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 2}
        ],
        "recipe_desc_vi": "Rèn tại trạm Starlit Factory từ Lõi Thiên Thể + Lông chim Umvuthi + Thỏi Netherite.",
        "recipe_desc_en": "Forged in Starlit Factory with Heated Celestial Core, Sunbird Feathers, Netherite.",
        "effects_vi": "Kỹ năng [Solar Flare]: Chém liên hoàn tạo bão lửa thái dương quét sạch quái vật diện rộng.",
        "effects_en": "[Solar Flare]: Rapid combo cleaves unleashing solar shockwaves in wide area.",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory kết hợp Lông rơi từ Boss Umvuthi.",
        "source_location_en": "Starlit Factory using drops from Boss Umvuthi."
    },
    {
        "id": "frostbound",
        "name": "Frostbound",
        "name_vi": "Lưỡi Hái Băng Ngục Frostbound",
        "icon": "images/items/frostbound.png",
        "mod": "Celestisynth",
        "category": "Mythical Weapon",
        "stage": "Late",
        "classTags": ["Mage", "Ice Mage", "Warrior"],
        "recipe_type": "Starlit Factory",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "ice_dragon_blood", "name": "Ice Dragon Blood", "name_vi": "Máu Rồng Băng", "count": 2},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 2}
        ],
        "recipe_desc_vi": "Rèn tại trạm Starlit Factory từ Lõi Thiên Thể + Máu Rồng Băng + Thỏi Netherite.",
        "recipe_desc_en": "Forged in Starlit Factory with Heated Celestial Core, Ice Dragon Blood, Netherite.",
        "effects_vi": "Kỹ năng [Absolute Zero]: Chém quét đóng băng toàn bộ kẻ địch xung quanh và triệu hồi rừng chông băng khổng lồ.",
        "effects_en": "[Absolute Zero]: Freezes all nearby enemies and erupts a forest of massive ice spikes.",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory sau khi hạ Rồng Băng cấp 4.",
        "source_location_en": "Starlit Factory after slaying Stage 4 Ice Dragon."
    },
    {
        "id": "phoenix_bow",
        "name": "Phoenix Bow",
        "name_vi": "Cung Thần Phượng Hoàng (Phoenix Bow)",
        "icon": "images/items/phoenix_bow.png",
        "mod": "The Aether",
        "category": "Ranged Weapon",
        "stage": "Mid",
        "classTags": ["Ranger", "Sniper"],
        "recipe_type": "Boss Drop (Sun Spirit)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi từ trùm Sun Spirit trong Đền Vàng Gold Dungeon (The Aether).",
        "recipe_desc_en": "Dropped from Gold Dungeon Boss Sun Spirit (The Aether).",
        "effects_vi": "Tất cả mũi tên bắn ra tự động chuyển hóa thành Tên Lửa Phượng Hoàng thiêu đốt cực hạn.",
        "effects_en": "All fired arrows automatically transform into flaming Phoenix Blaze arrows.",
        "source_type": "Boss: Sun Spirit",
        "source_url": "bosses.html#boss-sun_spirit",
        "source_location_vi": "Gold Dungeon (The Aether).",
        "source_location_en": "Gold Dungeon (The Aether)."
    },
    {
        "id": "hammer_of_kingbdogz",
        "name": "Hammer of Kingbdogz",
        "name_vi": "Búa Thần Sấm Kingbdogz",
        "icon": "images/items/hammer_of_kingbdogz.png",
        "mod": "The Aether",
        "category": "Holy Weapon",
        "stage": "Mid",
        "classTags": ["Paladin", "Warrior"],
        "recipe_type": "Boss Drop (Slider)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi từ trùm Slider trong Hầm ngục Đồng Bronze Dungeon (The Aether).",
        "recipe_desc_en": "Dropped from Bronze Dungeon Boss Slider (The Aether).",
        "effects_vi": "Phóng sét giật lan và tạo sóng địa chấn đánh bật mọi kẻ địch khi nện xuống đất.",
        "effects_en": "Calls down chain lightning and seismic shockwaves when slammed into the ground.",
        "source_type": "Boss: Slider",
        "source_url": "bosses.html#boss-slider",
        "source_location_vi": "Bronze Dungeon (The Aether).",
        "source_location_en": "Bronze Dungeon (The Aether)."
    },

    # -------------------------------------------------------------
    # 7. CELESTISYNTH WEAPONS
    # -------------------------------------------------------------
    {
        "id": "celestial_core",
        "name": "Heated Celestial Core",
        "name_vi": "Lõi Thiên Thể Nung Đỏ (Celestial Core)",
        "icon": "images/items/heated_celestial_core.png",
        "mod": "Celestisynth",
        "category": "Key Material",
        "stage": "Mid",
        "classTags": ["All Classes", "Warrior", "Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "nether_star", "name": "Nether Star", "name_vi": "Sao Địa Ngục", "count": 1},
            {"id": "blaze_rod", "name": "Blaze Rod", "name_vi": "Que Lửa", "count": 4},
            {"id": "amethyst_shard", "name": "Amethyst Shard", "name_vi": "Mảnh Thạch Anh Tím", "count": 4}
        ],
        "recipe_desc_vi": "1x Sao Địa Ngục + 4x Que Lửa + 4x Thạch Anh Tím.",
        "recipe_desc_en": "1x Nether Star + 4x Blaze Rod + 4x Amethyst Shard.",
        "effects_vi": "Phôi hạt nhân năng lượng vũ trụ dùng để rèn toàn bộ 8 vũ khí Celestisynth tại trạm Starlit Factory.",
        "effects_en": "Cosmic energy core used to forge all 8 Celestisynth weapons in Starlit Factory.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Chế tạo sau khi tiêu diệt Wither lấy Nether Star.",
        "source_location_en": "Crafted after slaying the Wither for a Nether Star."
    },
    {
        "id": "breezebreaker",
        "name": "Breezebreaker",
        "name_vi": "Phong Ma Kiếm Breezebreaker",
        "icon": "images/items/breezebreaker.png",
        "mod": "Celestisynth",
        "category": "Mythical Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Ranger"],
        "recipe_type": "Starlit Factory",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "feathers", "name": "Feather", "name_vi": "Lông Vũ", "count": 4},
            {"id": "diamond_sword", "name": "Diamond Sword", "name_vi": "Kiếm Kim Cương", "count": 1}
        ],
        "recipe_desc_vi": "Rèn tại Starlit Factory từ Lõi Thiên Thể + Lông vũ + Kiếm Kim Cương.",
        "recipe_desc_en": "Forged in Starlit Factory with Celestial Core, Feathers, Diamond Sword.",
        "effects_vi": "Kỹ năng [Gale Dash]: Lướt gió với tốc độ âm thanh và tạo lốc xoáy chém nát kẻ thù trên đường lướt.",
        "effects_en": "[Gale Dash]: Lightspeed air dash generating cutting whirlwinds.",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory.",
        "source_location_en": "Starlit Factory workstation."
    },
    {
        "id": "keres",
        "name": "Keres",
        "name_vi": "Trảm Quỷ Kiếm Keres",
        "icon": "images/items/keres.png",
        "mod": "Celestisynth",
        "category": "Mythical Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Starlit Factory",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "wither_bone", "name": "Wither Bone", "name_vi": "Xương Wither", "count": 4},
            {"id": "netherite_ingot", "name": "Netherite Ingot", "name_vi": "Thỏi Netherite", "count": 2}
        ],
        "recipe_desc_vi": "Rèn tại Starlit Factory từ Lõi Thiên Thể + Xương Wither + Thỏi Netherite.",
        "recipe_desc_en": "Forged in Starlit Factory with Celestial Core, Wither Bones, Netherite.",
        "effects_vi": "Kỹ năng [Soul Siphon]: Đòn bổ quét gây sát thương hủy diệt và hút 20% sát thương thành máu hồi phục.",
        "effects_en": "[Soul Siphon]: Devastating heavy cleaves converting 20% damage dealt to player HP.",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory.",
        "source_location_en": "Starlit Factory workstation."
    },
    {
        "id": "crescentia",
        "name": "Crescentia",
        "name_vi": "Đại Đao Trăng Khuyết Crescentia",
        "icon": "images/items/crescentia.png",
        "mod": "Celestisynth",
        "category": "Mythical Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Starlit Factory",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "amethyst_shard", "name": "Amethyst Shard", "name_vi": "Mảnh Thạch Anh Tím", "count": 8}
        ],
        "recipe_desc_vi": "Rèn tại Starlit Factory từ Lõi Thiên Thể + Thạch Anh Tím.",
        "recipe_desc_en": "Forged in Starlit Factory with Celestial Core and Amethyst Shards.",
        "effects_vi": "Kỹ năng [Lunar Crescent]: Phóng ra 3 lưỡi liềm ánh trăng xoay tròn chém xuyên qua địa hình.",
        "effects_en": "[Lunar Crescent]: Launches 3 spinning lunar crescent waves penetrating walls.",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory.",
        "source_location_en": "Starlit Factory workstation."
    },
    {
        "id": "rainfall_serenity",
        "name": "Rainfall Serenity",
        "name_vi": "Cung Thần Vũ Khúc (Rainfall Serenity)",
        "icon": "images/items/rainfall_serenity.png",
        "mod": "Celestisynth",
        "category": "Ranged Weapon",
        "stage": "Late",
        "classTags": ["Ranger", "Sniper"],
        "recipe_type": "Starlit Factory",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "prismarine_crystals", "name": "Prismarine Crystal", "name_vi": "Pha Lê Biển", "count": 6}
        ],
        "recipe_desc_vi": "Rèn tại Starlit Factory từ Lõi Thiên Thể + Pha Lê Biển Prismarine.",
        "recipe_desc_en": "Forged in Starlit Factory with Celestial Core and Prismarine Crystals.",
        "effects_vi": "Kỹ năng [Shooting Star]: Bắn mũi tên tự động tách thành 12 tia laser ánh sao tìm mục tiêu chuẩn xác 100%.",
        "effects_en": "[Shooting Star]: Arrows split into 12 homing starlight lasers with 100% precision.",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory sau khi khám phá Đền thờ biển Ocean Monument.",
        "source_location_en": "Starlit Factory after raiding Ocean Monuments."
    },

    # -------------------------------------------------------------
    # 8. TERRAMITY, BRUTALITY & LETHALITY ENDGAME
    # -------------------------------------------------------------
    {
        "id": "unholy_lance",
        "name": "Unholy Lance",
        "name_vi": "Thương Bất Tịnh (Unholy Lance)",
        "icon": "images/items/unholy_lance.png",
        "mod": "Terramity",
        "category": "Key Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "profanum_ingot", "name": "Profanum Ingot", "name_vi": "Thỏi Bất Tịnh Profanum", "count": 2},
            {"id": "blaze_rod", "name": "Blaze Rod", "name_vi": "Que Lửa", "count": 1}
        ],
        "recipe_desc_vi": "2x Thỏi Profanum + 1x Que Lửa (Bàn chế tạo).",
        "recipe_desc_en": "2x Profanum Ingot + 1x Blaze Rod.",
        "effects_vi": "Khi ném thẳng lên trời cao sẽ triệu hồi Siêu Boss Virtue (450.000 HP). Đòn đâm gây sát thương nguyền rủa cực nặng.",
        "effects_en": "Throwing skyward summons Boss Virtue (450,000 HP). Inflicts curse on strike.",
        "source_type": "Crafting / Nether",
        "source_url": "bosses.html#boss-virtue",
        "source_location_vi": "Đào quặng Profanum trong Nether rồi rèn thành giáo.",
        "source_location_en": "Mine Profanum in Nether to craft."
    },
    {
        "id": "rhitta",
        "name": "Rhitta",
        "name_vi": "Thần Rìu Thái Dương Rhitta",
        "icon": "images/items/rhitta.png",
        "mod": "Brutality",
        "category": "Supreme Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "profanum_ingot", "name": "Profanum Ingot", "name_vi": "Thỏi Bất Tịnh Profanum", "count": 4},
            {"id": "sunbird_feather", "name": "Sunbird Feather", "name_vi": "Lông Chim Mặt Trời", "count": 2}
        ],
        "recipe_desc_vi": "4x Thỏi Profanum + 2x Lông Chim Mặt Trời Umvuthi.",
        "recipe_desc_en": "4x Profanum Ingot + 2x Sunbird Feather.",
        "effects_vi": "Kỹ năng [Cruel Sun]: Tích tụ năng lượng mặt trời tỏa ra vụ nổ hỏa tiễn khổng lồ tiêu diệt toàn bộ quái vật xung quanh.",
        "effects_en": "[Cruel Sun]: Charges solar flares triggering devastating explosions.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Rèn từ thỏi Profanum và lông chim Umvuthi.",
        "source_location_en": "Crafted from Profanum Ingots and Sunbird Feathers."
    },
    {
        "id": "hf_meowrasama",
        "name": "HF Meowrasama",
        "name_vi": "Tuyệt Tác Kiếm Katana HF Meowrasama",
        "icon": "images/items/hf_meowrasama.png",
        "mod": "Lethality",
        "category": "Supreme Weapon",
        "stage": "Endgame",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Anvil / Smithing",
        "ingredients": [
            {"id": "pixie_alloy", "name": "Pixie Alloy", "name_vi": "Hợp Kim Pixie", "count": 4},
            {"id": "reverium_ingot", "name": "Reverium Ingot", "name_vi": "Thỏi Thánh Reverium", "count": 2}
        ],
        "recipe_desc_vi": "Rèn kết hợp Hợp Kim Pixie + Thỏi Reverium + Cổ Vật Lethality.",
        "recipe_desc_en": "Crafted with Pixie Alloy, Reverium Ingot, Lethality Artifacts.",
        "effects_vi": "Katana cao tần chém với tốc độ ánh sáng, kích hoạt sóng xung kích âm thanh đỏ cắt đứt mọi loại giáp của Boss!",
        "effects_en": "High-frequency katana cleaving at lightspeed with red acoustic shockwaves bypassing armor!",
        "source_type": "Endgame Crafting",
        "source_url": "progression.html",
        "source_location_vi": "Rèn sau khi khai thác quặng Reverium tại chiều không gian The End.",
        "source_location_en": "Forged after harvesting Reverium ores in The End."
    },
    {
        "id": "reverium_paladin_chestplate",
        "name": "Reverium Paladin Chestplate",
        "name_vi": "Giáp Thánh Hiệp Sĩ Reverium",
        "icon": "images/items/reverium_paladin_chestplate.png",
        "mod": "Terramity",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["Paladin", "Warrior"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "reverium_ingot", "name": "Reverium Ingot", "name_vi": "Thỏi Thánh Reverium", "count": 4},
            {"id": "warden_chestplate", "name": "Warden Chestplate", "name_vi": "Áo Giáp Warden", "count": 1}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Warden + Thỏi Thánh Reverium trên Smithing Table.",
        "recipe_desc_en": "Upgrade Warden Chestplate with Reverium Ingot on Smithing Table.",
        "effects_vi": "+18 Điểm Giáp, +8 Kháng Đẩy Lùi, Hào quang Thánh hồi 5% Máu mỗi giây cho toàn bộ tổ đội!",
        "effects_en": "+18 Armor, +8 Knockback Resist, Holy Aura healing 5% Max HP/sec for party!",
        "source_type": "Endgame Crafting",
        "source_url": "classes.html",
        "source_location_vi": "Smithing Table kết hợp quặng The End Reverium.",
        "source_location_en": "Smithing Table using Outer End Reverium ores."
    },

    # -------------------------------------------------------------
    # 9. ALEX'S CAVES & ICE & FIRE ARSENAL
    # -------------------------------------------------------------
    {
        "id": "resistor_shield",
        "name": "Resistor Shield",
        "name_vi": "Khiên Từ Tính Resistor Shield",
        "icon": "images/items/resistor_shield.png",
        "mod": "Alex's Caves",
        "category": "Shield",
        "stage": "Mid",
        "classTags": ["Paladin", "Warrior"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "neodymium_ingot", "name": "Neodymium Ingot", "name_vi": "Thỏi Neodymium", "count": 4},
            {"id": "shield", "name": "Shield", "name_vi": "Khiên Gỗ Vanilla", "count": 1}
        ],
        "recipe_desc_vi": "4x Thỏi Neodymium + 1x Khiên Gỗ.",
        "recipe_desc_en": "4x Neodymium Ingot + 1x Shield.",
        "effects_vi": "Bật màng từ trường phản ngược 100% đạn tên và đẩy lùi tất cả kim loại xung quanh.",
        "effects_en": "Generates magnetic barrier reflecting 100% projectiles and repelling metals.",
        "source_type": "Alex's Caves: Magnetic Caves",
        "source_url": "creatures.html",
        "source_location_vi": "Đào quặng Neodymium trong hang từ tính Magnetic Caves.",
        "source_location_en": "Mine Neodymium in Magnetic Caves biome."
    },
    {
        "id": "galena_gauntlet",
        "name": "Galena Gauntlet",
        "name_vi": "Găng Tay Từ Trường Galena Gauntlet",
        "icon": "images/items/galena_gauntlet.png",
        "mod": "Alex's Caves",
        "category": "Gauntlet Weapon",
        "stage": "Mid",
        "classTags": ["Warrior", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "galena_ingot", "name": "Galena Ingot", "name_vi": "Thỏi Galena", "count": 4},
            {"id": "neodymium_ingot", "name": "Neodymium Ingot", "name_vi": "Thỏi Neodymium", "count": 2}
        ],
        "recipe_desc_vi": "4x Thỏi Galena + 2x Thỏi Neodymium.",
        "recipe_desc_en": "4x Galena Ingot + 2x Neodymium Ingot.",
        "effects_vi": "Hút và ném các khối đá/quái vật kim loại từ cự ly 30 block, đập nát kẻ địch từ xa.",
        "effects_en": "Magnetically grabs and throws blocks/mobs from 30 blocks away.",
        "source_type": "Alex's Caves: Magnetic Caves",
        "source_url": "creatures.html",
        "source_location_vi": "Hang từ tính Magnetic Caves.",
        "source_location_en": "Magnetic Caves biome."
    },
    {
        "id": "nuclear_bomb",
        "name": "Nuclear Bomb",
        "name_vi": "Bom Nguyên Tử (Nuclear Bomb)",
        "icon": "images/items/nuclear_bomb.png",
        "mod": "Alex's Caves",
        "category": "Explosive",
        "stage": "Late",
        "classTags": ["All Classes", "Ranger"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "uranium_rod", "name": "Uranium Rod", "name_vi": "Thanh Uranium", "count": 4},
            {"id": "heavy_metal_block", "name": "Heavy Metal Block", "name_vi": "Khối Kim Loại Nặng", "count": 4}
        ],
        "recipe_desc_vi": "4x Thanh Uranium + 4x Khối Kim Loại Nặng (Toxic Caves).",
        "recipe_desc_en": "4x Uranium Rod + 4x Heavy Metal Block (Toxic Caves).",
        "effects_vi": "Vụ nổ hạt nhân tận thế quét sạch bán kính 100 block và để lại bức xạ tử thần!",
        "effects_en": "Apocalyptic nuclear detonation wiping 100 blocks radius and radiating zone!",
        "source_type": "Alex's Caves: Toxic Caves",
        "source_url": "creatures.html",
        "source_location_vi": "Khai thác Uranium trong hang phóng xạ Toxic Caves.",
        "source_location_en": "Harvest Uranium inside Toxic Caves biome."
    },
    {
        "id": "raygun",
        "name": "Raygun",
        "name_vi": "Súng Tử Ngoại Raygun",
        "icon": "images/items/raygun.png",
        "mod": "Alex's Caves",
        "category": "Gun / Ranged",
        "stage": "Late",
        "classTags": ["Ranger", "Sniper"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "uranium_rod", "name": "Uranium Rod", "name_vi": "Thanh Uranium", "count": 2},
            {"id": "galena_ingot", "name": "Galena Ingot", "name_vi": "Thỏi Galena", "count": 3}
        ],
        "recipe_desc_vi": "2x Uranium Rod + 3x Galena Ingot.",
        "recipe_desc_en": "2x Uranium Rod + 3x Galena Ingot.",
        "effects_vi": "Bắn chùm tia tử ngoại năng lượng cao liên tục thiêu rụi thanh máu quái vật mà không cần nạp đạn.",
        "effects_en": "Fires continuous high-energy gamma laser melting boss health bars.",
        "source_type": "Alex's Caves: Toxic Caves",
        "source_url": "creatures.html",
        "source_location_vi": "Hang phóng xạ Toxic Caves.",
        "source_location_en": "Toxic Caves biome."
    },
    {
        "id": "dreadsteel_scythe",
        "name": "Dreadsteel Scythe",
        "name_vi": "Đại Lưỡi Hái Hủy Diệt Dreadsteel Scythe",
        "icon": "images/items/dreadsteel_scythe.png",
        "mod": "Dreadsteel",
        "category": "Supreme Weapon",
        "stage": "Late",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Anvil / Crafting",
        "ingredients": [
            {"id": "dreadsteel_ingot", "name": "Dreadsteel Ingot", "name_vi": "Thỏi Thép Dreadsteel", "count": 3},
            {"id": "wither_bone", "name": "Wither Bone", "name_vi": "Xương Wither", "count": 2}
        ],
        "recipe_desc_vi": "3x Thỏi Thép Dreadsteel + 2x Xương Wither.",
        "recipe_desc_en": "3x Dreadsteel Ingot + 2x Wither Bone.",
        "effects_vi": "35 Sát thương cơ bản, chém quét đa mục tiêu và kích hoạt cả 3 hiệu ứng Lửa thiêu + Băng đông + Sấm giật trên cùng 1 đòn đánh!",
        "effects_en": "35 Base DMG, cleaves all targets triggering Fire, Ice, and Lightning simultaneously!",
        "source_type": "Dragon Forge Crafting",
        "source_url": "creatures.html",
        "source_location_vi": "Luyện 3 loại Thép Rồng tại Dragon Forge rồi rèn lưỡi hái.",
        "source_location_en": "Smelt 3 Dragonsteels at Dragon Forge."
    },

    # -------------------------------------------------------------
    # 10. RELICS & HEART CANISTERS
    # -------------------------------------------------------------
    {
        "id": "red_heart_canister",
        "name": "Red Heart Canister",
        "name_vi": "Hộp Tim Đỏ (Red Heart Canister)",
        "icon": "images/items/red_heart_canister.png",
        "mod": "Baubley Heart Canisters",
        "category": "HP Upgrade",
        "stage": "Early",
        "classTags": ["All Classes", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "wither_bone", "name": "Wither Bone", "name_vi": "Xương Wither", "count": 1},
            {"id": "canister", "name": "Canister Base", "name_vi": "Hộp Rỗng Canister", "count": 1},
            {"id": "red_apple", "name": "Apple", "name_vi": "Quả Táo", "count": 1}
        ],
        "recipe_desc_vi": "1x Xương Wither + 1x Hộp Rỗng + 1x Quả Táo.",
        "recipe_desc_en": "1x Wither Bone + 1x Canister + 1x Apple.",
        "effects_vi": "Mỗi hộp gắn vào Heart Amulet tăng vĩnh viễn +2 Máu Tối Đa (1 Tim Đỏ). Tối đa gắn 10 hộp (+20 Máu).",
        "effects_en": "Permanently adds +2 Max HP (1 Red Heart). Max 10 canisters (+20 HP).",
        "source_type": "Crafting",
        "source_url": "utilities.html",
        "source_location_vi": "Săn Wither Skeleton tại Nether Fortress lấy xương.",
        "source_location_en": "Hunt Wither Skeletons in Nether Fortresses."
    },
    {
        "id": "yellow_heart_canister",
        "name": "Yellow Heart Canister",
        "name_vi": "Hộp Tim Vàng (Yellow Heart Canister)",
        "icon": "images/items/yellow_heart_canister.png",
        "mod": "Baubley Heart Canisters",
        "category": "HP Upgrade",
        "stage": "Mid",
        "classTags": ["All Classes", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "red_heart_canister", "name": "Red Heart Canister", "name_vi": "Hộp Tim Đỏ", "count": 1},
            {"id": "enchanted_golden_apple", "name": "Enchanted Golden Apple", "name_vi": "Táo Vàng Phù Phép", "count": 1}
        ],
        "recipe_desc_vi": "1x Hộp Tim Đỏ + 1x Táo Vàng Phù Phép.",
        "recipe_desc_en": "1x Red Heart Canister + 1x Enchanted Golden Apple.",
        "effects_vi": "Tăng thêm tầng Tim Vàng (+20 Máu Tối Đa thứ hai).",
        "effects_en": "Adds second layer of Yellow Hearts (+20 Max HP).",
        "source_type": "Crafting",
        "source_url": "utilities.html",
        "source_location_vi": "Ghép từ Hộp Tim Đỏ và Táo vàng enchanted.",
        "source_location_en": "Crafted with Red Canisters and Enchanted Apples."
    },
    {
        "id": "prismatic_jewel",
        "name": "Prismatic Jewel",
        "name_vi": "Ngọc Lục Giác Cầu Vồng (Prismatic Jewel)",
        "icon": "images/items/prismatic_jewel.png",
        "mod": "Terramity",
        "category": "Key Artifact",
        "stage": "Early",
        "classTags": ["All Classes", "Progression"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "topaz", "name": "Topaz Gem", "name_vi": "Hoàng Ngọc Topaz", "count": 1},
            {"id": "ruby", "name": "Ruby Gem", "name_vi": "Hồng Ngọc Ruby", "count": 1},
            {"id": "sapphire", "name": "Sapphire Gem", "name_vi": "Lam Ngọc Sapphire", "count": 1},
            {"id": "onyx", "name": "Onyx Gem", "name_vi": "Hắc Ngọc Onyx", "count": 1},
            {"id": "iridescent_shard", "name": "Iridescent Shard", "name_vi": "Mảnh Cầu Vồng", "count": 1}
        ],
        "recipe_desc_vi": "Kết hợp đủ 9 loại đá quý nguyên tố tại Bàn chế tạo.",
        "recipe_desc_en": "Combine all elemental gems in Crafting Table.",
        "effects_vi": "Chìa khóa mở khóa toàn bộ cây công nghệ Terramity Tier 1 (Dimlite, Cosmilite, Virentium).",
        "effects_en": "Key unlocking the entire Terramity Tier 1 progression tree.",
        "source_type": "Mining / Crafting",
        "source_url": "progression.html",
        "source_location_vi": "Khai thác các quặng ngầm ở từng biome theo bảng tọa độ Y-Levels.",
        "source_location_en": "Mine underground across biomes matching the Y-Levels chart."
    },
    {
        "id": "eternal_stella",
        "name": "Eternal Stella",
        "name_vi": "Bảo Vật Bất Tử Eternal Stella",
        "icon": "images/items/eternal_stella.png",
        "mod": "Forbidden and Arcanus",
        "category": "Godly Artifact",
        "stage": "Late",
        "classTags": ["All Classes", "Meta Build"],
        "recipe_type": "Hephaestus Forge",
        "ingredients": [
            {"id": "stellarite", "name": "Stellarite Piece", "name_vi": "Mảnh Sao Stellarite", "count": 1},
            {"id": "xpetrified_orb", "name": "Xpetrified Orb", "name_vi": "Ngọc Hóa Đá EXP", "count": 3}
        ],
        "recipe_desc_vi": "Đúc tại lò Hephaestus Forge: 1x Stellarite + 3x Xpetrified Orbs + 2000 Aureal + 10 Souls.",
        "recipe_desc_en": "Forged in Hephaestus Forge: 1x Stellarite + 3x Xpetrified Orbs + 2000 Aureal + 10 Souls.",
        "effects_vi": "Khi ép vào Đe với bất kỳ trang bị nào: Hồi phục 100% độ bền và nhận dòng thuộc tính INDESTRUCTIBLE (Không bao giờ hỏng).",
        "effects_en": "When applied in Anvil: Restores 100% durability and grants permanent INDESTRUCTIBLE trait.",
        "source_type": "Hephaestus Forge Ritual",
        "source_url": "magic.html",
        "source_location_vi": "Nạp 4 nguồn năng lượng vào Lò rèn Hephaestus Forge đa khối để đúc ngọc.",
        "source_location_en": "Feed 4 energy fuels into Hephaestus Forge multiblock to forge."
    },
    {
        "id": "the_judgement",
        "name": "The Judgement",
        "name_vi": "Thần Khí The Judgement",
        "icon": "images/items/the_judgement.png",
        "mod": "Terramity",
        "stage": "Endgame",
        "classTags": ["All Classes", "Supreme Trophy"],
        "category": "Supreme Relic",
        "recipe_type": "Boss Drop (Ultra Sniffer)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi 100% khi tiêu diệt Siêu Chúa Tể Ultra Sniffer 1.000.000 HP.",
        "recipe_desc_en": "Dropped 100% by Super-Boss Ultra Sniffer (1,000,000 HP).",
        "effects_vi": "Vật phẩm tối thượng minh chứng bạn đã phá đảo toàn diện Modpack Terramity Awakened!",
        "effects_en": "Supreme relic proving total conquest of the Terramity Awakened modpack!",
        "source_type": "Boss: Ultra Sniffer",
        "source_url": "bosses.html#boss-ultra_sniffer",
        "source_location_vi": "Đấu trường Vô Cực Tận Diệt.",
        "source_location_en": "Endgame Arena."
    }
]

# Compute the "used_in" reverse graph for every single item!
items_map = {item["id"]: item for item in items_db}
for item in items_db:
    item["used_in"] = []

for item in items_db:
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

print(f"Computed complete graph for {len(items_db)} items.")

# Write to output JS
output_js = f"""/**
 * Terramity Awakened Wiki - Item Graph & Cross-Linked Crafting Tree
 */
const ITEM_GRAPH_DATABASE = {json.dumps(items_db, ensure_ascii=False, indent=2)};
"""

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_items.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("Successfully generated data_items.js!")
