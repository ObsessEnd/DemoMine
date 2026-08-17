import os
import json

# Master Armor Sets & Weapons Catalog for Terramity Awakened
armor_sets = [
    # -------------------------------------------------------------
    # 1. IRON'S SPELLS 'N SPELLBOOKS (8 Elemental Schools)
    # -------------------------------------------------------------
    {
        "id": "pyromancer_armor_set",
        "name": "Pyromancer Armor Set",
        "name_vi": "Bộ Giáp Hỏa Thuật Sư (Pyromancer Set)",
        "icon": "images/items/pyromancer_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Mage", "Fire Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "fire_rune", "name": "Fire Rune", "name_vi": "Cổ Tự Hỏa Ma", "count": 10},
            {"id": "iron_ingot", "name": "Iron Ingot", "name_vi": "Thỏi Sắt", "count": 10}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Hỏa Ma + 10x Thỏi Sắt (4 món: Mũ, Áo, Quần, Giày).",
        "recipe_desc_en": "16x Arcane Cloth + 10x Fire Rune + 10x Iron Ingot (Full Set).",
        "effects_vi": "Set Bonus: +20% Sát thương Hỏa Phép, +200 Mana tối đa, Kháng 100% Thiêu Đốt và bốc cháy xung quanh khi bị đánh.",
        "effects_en": "Set Bonus: +20% Fire Spell Power, +200 Max Mana, 100% Fire Immunity.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Dệt từ Arcane Cloth và Cổ Tự Lửa tại Bàn chế tạo.",
        "source_location_en": "Crafted with Arcane Cloth and Fire Runes."
    },
    {
        "id": "cryomancer_armor_set",
        "name": "Cryomancer Armor Set",
        "name_vi": "Bộ Giáp Băng Thuật Sư (Cryomancer Set)",
        "icon": "images/items/cryomancer_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Mage", "Ice Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "ice_rune", "name": "Ice Rune", "name_vi": "Cổ Tự Băng Ma", "count": 10},
            {"id": "iron_ingot", "name": "Iron Ingot", "name_vi": "Thỏi Sắt", "count": 10}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Băng Ma + 10x Thỏi Sắt.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Ice Rune + 10x Iron Ingot.",
        "effects_vi": "Set Bonus: +20% Sát thương Băng Phép, +200 Mana, Miễn nhiễm đóng băng tuyết lạnh và tạo hào quang làm chậm quái xung quanh.",
        "effects_en": "Set Bonus: +20% Ice Spell Power, +200 Max Mana, Freeze Immunity.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Dệt từ Arcane Cloth và Cổ Tự Băng.",
        "source_location_en": "Crafted with Arcane Cloth and Ice Runes."
    },
    {
        "id": "electromancer_armor_set",
        "name": "Electromancer Armor Set",
        "name_vi": "Bộ Giáp Lôi Thuật Sư (Electromancer Set)",
        "icon": "images/items/electromancer_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Mage", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "lightning_rune", "name": "Lightning Rune", "name_vi": "Cổ Tự Lôi Hệ", "count": 10},
            {"id": "copper_ingot", "name": "Copper Ingot", "name_vi": "Thỏi Đồng", "count": 10}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Lôi Hệ + 10x Thỏi Đồng.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Lightning Rune + 10x Copper Ingot.",
        "effects_vi": "Set Bonus: +20% Sát thương Lôi Phép, +200 Mana, +15% Tốc độ di chuyển, đòn đánh kích hoạt sét phụ giật lan.",
        "effects_en": "Set Bonus: +20% Lightning Spell Power, +200 Mana, +15% Speed.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Dệt từ Arcane Cloth và Cổ Tự Lôi.",
        "source_location_en": "Crafted with Arcane Cloth and Lightning Runes."
    },
    {
        "id": "priest_armor_set",
        "name": "Priest Robe Set",
        "name_vi": "Bộ Áo Choàng Mục Sư (Priest Set)",
        "icon": "images/items/priest_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Paladin", "Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "holy_rune", "name": "Holy Rune", "name_vi": "Cổ Tự Thánh Quang", "count": 10}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Thánh Quang.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Holy Rune.",
        "effects_vi": "Set Bonus: +20% Sát thương Thánh, +50% Hiệu quả hồi máu cho tổ đội, Trừ tà tăng 50% sát thương lên quái Undead.",
        "effects_en": "Set Bonus: +20% Holy Power, +50% Team Healing, Smites Undead.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Dệt từ Cổ Tự Thánh Quang.",
        "source_location_en": "Crafted with Holy Runes."
    },
    {
        "id": "shadowwalker_armor_set",
        "name": "Shadow-Walker Armor Set",
        "name_vi": "Bộ Giáp Bóng Ma Hư Không (Shadow-Walker)",
        "icon": "images/items/shadowwalker_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Mage", "Ranger"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "ender_rune", "name": "Ender Rune", "name_vi": "Cổ Tự Hư Không", "count": 10},
            {"id": "ender_pearl", "name": "Ender Pearl", "name_vi": "Ngọc Ender", "count": 4}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Hư Không + 4x Ngọc Ender.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Ender Rune + 4x Ender Pearl.",
        "effects_vi": "Set Bonus: +20% Sát thương Hư Không, Cho phép dịch chuyển tức thời khi bấm nút kỹ năng và tàng hình khi lén lút (Sneak).",
        "effects_en": "Set Bonus: +20% Ender Spell Power, Blink Teleportation on hotkey, Stealth on sneak.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Dệt từ Cổ Tự Hư Không sau khi săn Enderman.",
        "source_location_en": "Crafted with Ender Runes after hunting Endermen."
    },
    {
        "id": "cultist_armor_set",
        "name": "Cultist Armor Set",
        "name_vi": "Bộ Giáp Tà Giáo Huyết Ma (Cultist Set)",
        "icon": "images/items/cultist_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Mage", "Warrior"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "blood_rune", "name": "Blood Rune", "name_vi": "Cổ Tự Huyết Ma", "count": 10}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Huyết Ma.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Blood Rune.",
        "effects_vi": "Set Bonus: +20% Sát thương Huyết Ma, Hút 15% lượng máu của kẻ thù khi tung đòn phép, Tăng 30% sát thương khi máu bản thân dưới 50%.",
        "effects_en": "Set Bonus: +20% Blood Spell Power, 15% Lifesteal, 30% Damage bonus below 50% HP.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Hầm mộ ngầm Catacombs hoặc trích máu hiến tế.",
        "source_location_en": "Catacombs underground or blood extraction rituals."
    },
    {
        "id": "archevoker_armor_set",
        "name": "Archevoker Robe Set",
        "name_vi": "Bộ Áo Choàng Đại Triệu Hoán (Archevoker)",
        "icon": "images/items/archevoker_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "evocation_rune", "name": "Evocation Rune", "name_vi": "Cổ Tự Triệu Hoán", "count": 10},
            {"id": "emerald", "name": "Emerald", "name_vi": "Ngọc Lục Bảo", "count": 12}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Triệu Hoán + 12x Ngọc Lục Bảo.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Evocation Rune + 12x Emerald.",
        "effects_vi": "Set Bonus: +20% Sát thương Triệu Hoán, Tự động triệu hồi đàn đệ tử Vex bảo vệ chủ nhân và tăng 50% thời gian tồn tại của linh thú.",
        "effects_en": "Set Bonus: +20% Evocation Power, Summons Vex minions, +50% Minion duration.",
        "source_type": "Woodland Mansion / Raids",
        "source_url": "dimensions.html",
        "source_location_vi": "Biệt thự Rừng Rậm Woodland Mansion hoặc càn quét Raid.",
        "source_location_en": "Woodland Mansions and Pillager Raids."
    },
    {
        "id": "plagued_armor_set",
        "name": "Plagued Armor Set",
        "name_vi": "Bộ Giáp Dịch Bệnh Tự Nhiên (Plagued Set)",
        "icon": "images/items/plagued_chestplate.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Mage", "Ranger"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_cloth", "name": "Arcane Cloth", "name_vi": "Vải Ma Thuật", "count": 16},
            {"id": "nature_rune", "name": "Nature Rune", "name_vi": "Cổ Tự Tự Nhiên", "count": 10}
        ],
        "recipe_desc_vi": "16x Vải Ma Thuật + 10x Cổ Tự Tự Nhiên.",
        "recipe_desc_en": "16x Arcane Cloth + 10x Nature Rune.",
        "effects_vi": "Set Bonus: +20% Sát thương Tự Nhiên, Đầu độc lan truyền diện rộng, Kháng 100% mọi hiệu ứng trúng độc và héo mòn.",
        "effects_en": "Set Bonus: +20% Nature Spell Power, Spreading Poison AOE, 100% Poison & Wither Immunity.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Dệt từ Cổ Tự Tự Nhiên sau khi khám phá Đầm lầy Swamps.",
        "source_location_en": "Crafted with Nature Runes from Swamps."
    },

    # -------------------------------------------------------------
    # 2. THE AETHER DIMENSION ARMOR SETS
    # -------------------------------------------------------------
    {
        "id": "zanite_armor_set",
        "name": "Zanite Armor Set",
        "name_vi": "Bộ Giáp Quặng Zanite (Zanite Set)",
        "icon": "images/items/zanite_chestplate.png",
        "mod": "The Aether",
        "category": "Armor",
        "stage": "Early",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "zanite_gemstone", "name": "Zanite Gemstone", "name_vi": "Đá Quý Zanite", "count": 24}
        ],
        "recipe_desc_vi": "24x Đá Quý Zanite đúc thành 4 món giáp.",
        "recipe_desc_en": "24x Zanite Gemstone in Crafting Table.",
        "effects_vi": "Đặc tính [Resilience]: Giáp càng bị tụt độ bền thì phòng ngự càng tăng mạnh!",
        "effects_en": "Special [Resilience]: Grants higher defense as durability decreases!",
        "source_type": "The Aether Mining",
        "source_url": "dimensions.html#dim-aether",
        "source_location_vi": "Đào quặng Zanite trên các hòn đảo mây The Aether.",
        "source_location_en": "Mine Zanite ores on floating Aether islands."
    },
    {
        "id": "gravitite_armor_set",
        "name": "Gravitite Armor Set",
        "name_vi": "Bộ Giáp Phản Trọng Lực Gravitite",
        "icon": "images/items/gravitite_chestplate.png",
        "mod": "The Aether",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Warrior", "Ranger"],
        "recipe_type": "Enchanter / Crafting",
        "ingredients": [
            {"id": "enchanted_gravitite", "name": "Enchanted Gravitite", "name_vi": "Thỏi Gravitite Phù Phép", "count": 24}
        ],
        "recipe_desc_vi": "Nung quặng Gravitite trong lò Enchanter (Aether) để kích hoạt từ trường.",
        "recipe_desc_en": "Smelt Gravitite in Aether Enchanter to activate.",
        "effects_vi": "Set Bonus: Nhảy siêu cao (High Jump), Giảm 100% sát thương rơi ngã và lơ lửng giữa không trung khi giữ nút nhảy!",
        "effects_en": "Set Bonus: Super High Jump, 100% Fall Damage Immunity, Hover in mid-air!",
        "source_type": "The Aether Mining",
        "source_url": "dimensions.html#dim-aether",
        "source_location_vi": "Đào quặng Gravitite ở đáy dưới các hòn đảo mây The Aether.",
        "source_location_en": "Mine Gravitite under floating Aether islands."
    },
    {
        "id": "neptune_armor_set",
        "name": "Neptune Armor Set",
        "name_vi": "Bộ Giáp Hải Vương Neptune",
        "icon": "images/items/neptune_chestplate.png",
        "mod": "The Aether",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Paladin", "All Classes"],
        "recipe_type": "Bronze Dungeon Drop",
        "ingredients": [],
        "recipe_desc_vi": "Mở rương phần thưởng sau khi diệt Boss Slider trong Bronze Dungeon (The Aether).",
        "recipe_desc_en": "Bronze Dungeon reward chest after defeating Boss Slider.",
        "effects_vi": "Set Bonus: Bơi lội siêu tốc dưới nước, Thở dưới nước vĩnh viễn và di chuyển tự do trong bùn lầy/vực biển.",
        "effects_en": "Set Bonus: Ultra fast swimming, Infinite underwater breathing.",
        "source_type": "Boss: Slider",
        "source_url": "bosses.html#boss-slider",
        "source_location_vi": "Bronze Dungeon (The Aether).",
        "source_location_en": "Bronze Dungeon (The Aether)."
    },
    {
        "id": "valkyrie_armor_set",
        "name": "Valkyrie Armor Set",
        "name_vi": "Bộ Giáp Nữ Thần Valkyrie",
        "icon": "images/items/valkyrie_chestplate.png",
        "mod": "The Aether",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Ranger", "Warrior"],
        "recipe_type": "Silver Dungeon Drop",
        "ingredients": [],
        "recipe_desc_vi": "Rơi từ Nữ Hoàng Valkyrie Queen trong đền mây Silver Dungeon (The Aether).",
        "recipe_desc_en": "Dropped by Valkyrie Queen in Silver Dungeon (The Aether).",
        "effects_vi": "Set Bonus: +30% Tốc độ di chuyển, Cho phép lướt gió trên không liên tục 5 giây không cần Elytra!",
        "effects_en": "Set Bonus: +30% Movement Speed, Air Gliding for 5 seconds without Elytra!",
        "source_type": "Boss: Valkyrie Queen",
        "source_url": "bosses.html#boss-valkyrie_queen",
        "source_location_vi": "Silver Dungeon (The Aether).",
        "source_location_en": "Silver Dungeon (The Aether)."
    },
    {
        "id": "phoenix_armor_set",
        "name": "Phoenix Armor Set",
        "name_vi": "Bộ Giáp Phượng Hoàng Bất Tử (Phoenix Set)",
        "icon": "images/items/phoenix_chestplate.png",
        "mod": "The Aether",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Paladin", "Fire Mage"],
        "recipe_type": "Gold Dungeon Drop",
        "ingredients": [],
        "recipe_desc_vi": "Rơi từ trùm Sun Spirit trong Đền Vàng Gold Dungeon (The Aether).",
        "recipe_desc_en": "Dropped from Sun Spirit in Gold Dungeon (The Aether).",
        "effects_vi": "Set Bonus: KHÁNG 100% LỬA & DUNG NHAM, Tự do bơi lội và lặn trong biển dung nham Nether mà không mất máu!",
        "effects_en": "Set Bonus: 100% FIRE & LAVA IMMUNITY, Swim freely inside Nether lava lakes!",
        "source_type": "Boss: Sun Spirit",
        "source_url": "bosses.html#boss-sun_spirit",
        "source_location_vi": "Gold Dungeon (The Aether).",
        "source_location_en": "Gold Dungeon (The Aether)."
    },

    # -------------------------------------------------------------
    # 3. DEEPER AND DARKER (THE OTHERSIDE)
    # -------------------------------------------------------------
    {
        "id": "resonarium_armor_set",
        "name": "Resonarium Armor Set",
        "name_vi": "Bộ Giáp Quặng Vọng Âm Resonarium",
        "icon": "images/items/resonarium_chestplate.png",
        "mod": "Deeper and Darker",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "resonarium_ingot", "name": "Resonarium Ingot", "name_vi": "Thỏi Resonarium", "count": 24}
        ],
        "recipe_desc_vi": "24x Thỏi Resonarium khai thác tại cõi âm The Otherside.",
        "recipe_desc_en": "24x Resonarium Ingot mined in The Otherside.",
        "effects_vi": "Chỉ số cao hơn Kim Cương 30%, +8 Kháng Sóng Âm (Sonic Boom Resistance).",
        "effects_en": "30% higher stats than Diamond, +8 Sonic Boom Resistance.",
        "source_type": "The Otherside Mining",
        "source_url": "dimensions.html#dim-otherside",
        "source_location_vi": "Quần xã Deeplands trong cõi âm The Otherside.",
        "source_location_en": "Deeplands biome in The Otherside."
    },
    {
        "id": "warden_armor_set",
        "name": "Warden Armor Set",
        "name_vi": "Bộ Giáp Cai Ngục Warden Tối Thượng",
        "icon": "images/items/warden_chestplate.png",
        "mod": "Deeper and Darker",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin", "All Classes"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "netherite_armor_set", "name": "Netherite Armor Piece", "name_vi": "Mảnh Giáp Netherite", "count": 4},
            {"id": "reinforced_echo_shard", "name": "Reinforced Echo Shard", "name_vi": "Mảnh Vọng Âm Cường Hóa", "count": 8},
            {"id": "resonarium_ingot", "name": "Resonarium Ingot", "name_vi": "Thỏi Resonarium", "count": 16}
        ],
        "recipe_desc_vi": "Nâng cấp từ trọn bộ Giáp Netherite + Thỏi Resonarium + Mảnh Vọng Âm trên Smithing Table.",
        "recipe_desc_en": "Upgrade full Netherite set with Resonarium Ingots and Echo Shards on Smithing Table.",
        "effects_vi": "Set Bonus: +30 Điểm Giáp, +12 Kháng Đẩy Lùi, KHÁNG VĨNH VIỄN HIỆU ỨNG MÙ LÒA (Blindness/Darkness Immunity), Nhìn thấu bóng đêm!",
        "effects_en": "Set Bonus: +30 Armor, +12 Knockback Resist, PERMANENT BLINDNESS/DARKNESS IMMUNITY, Night Vision!",
        "source_type": "The Otherside Smithing",
        "source_url": "dimensions.html#dim-otherside",
        "source_location_vi": "Đền thờ cổ đại trong cõi âm The Otherside.",
        "source_location_en": "Ancient Temples in The Otherside."
    },

    # -------------------------------------------------------------
    # 4. ICE AND FIRE (DRAGONSCALE & DRAGONSTEEL)
    # -------------------------------------------------------------
    {
        "id": "fire_dragonscale_armor_set",
        "name": "Fire Dragonscale Armor Set",
        "name_vi": "Bộ Giáp Vảy Hỏa Long (Fire Dragonscale)",
        "icon": "images/items/dragonscale_red_chestplate.png",
        "mod": "Ice and Fire",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Warrior", "Fire Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "dragonscale_fire", "name": "Fire Dragon Scales", "name_vi": "Vảy Rồng Lửa", "count": 24}
        ],
        "recipe_desc_vi": "24x Vảy Rồng Lửa (Lột da từ xác Hỏa Long cấp 3-5).",
        "recipe_desc_en": "24x Fire Dragon Scales harvested from Fire Dragons.",
        "effects_vi": "Kháng 100% Hơi thở Hỏa Long, Tăng 20% sát thương vũ khí lửa, Đẩy lùi quái vật khi bị tấn công.",
        "effects_en": "100% Fire Dragon Breath Immunity, +20% Fire Damage, Reflects attacks.",
        "source_type": "Dragon Hunting",
        "source_url": "creatures.html",
        "source_location_vi": "Tổ rồng lửa tại vùng núi nóng Overworld.",
        "source_location_en": "Fire Dragon roosts in warm mountains."
    },
    {
        "id": "ice_dragonscale_armor_set",
        "name": "Ice Dragonscale Armor Set",
        "name_vi": "Bộ Giáp Vảy Băng Long (Ice Dragonscale)",
        "icon": "images/items/dragonscale_blue_chestplate.png",
        "mod": "Ice and Fire",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Warrior", "Ice Mage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "dragonscale_ice", "name": "Ice Dragon Scales", "name_vi": "Vảy Rồng Băng", "count": 24}
        ],
        "recipe_desc_vi": "24x Vảy Rồng Băng (Lột da từ xác Băng Long).",
        "recipe_desc_en": "24x Ice Dragon Scales.",
        "effects_vi": "Kháng 100% Hơi thở Băng Long, Đóng băng kẻ địch tấn công vào giáp.",
        "effects_en": "100% Ice Dragon Breath Immunity, Freezes attackers on hit.",
        "source_type": "Dragon Hunting",
        "source_url": "creatures.html",
        "source_location_vi": "Hang rồng băng tại vùng núi tuyết.",
        "source_location_en": "Ice Dragon caves in snowy biomes."
    },
    {
        "id": "fire_dragonsteel_armor_set",
        "name": "Fire Dragonsteel Armor Set",
        "name_vi": "Bộ Giáp Thép Hỏa Long (Fire Dragonsteel)",
        "icon": "images/items/dragonsteel_fire_chestplate.png",
        "mod": "Ice and Fire",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Dragon Forge",
        "ingredients": [
            {"id": "dragonsteel_fire_ingot", "name": "Fire Dragonsteel Ingot", "name_vi": "Thỏi Thép Hỏa Long", "count": 24}
        ],
        "recipe_desc_vi": "Luyện thỏi tại lò Dragon Forge dùng hơi thở Hỏa Long cấp 5 rồi rèn giáp.",
        "recipe_desc_en": "Smelted in Dragon Forge with Stage 5 Fire Dragon breath.",
        "effects_vi": "+36 Điểm Giáp, +16 Kháng Đẩy Lùi, Kháng 100% mọi loại lửa, Tự động thiêu rụi kẻ địch xung quanh.",
        "effects_en": "+36 Armor, +16 Knockback Resist, 100% Fire Immunity, Immolation aura.",
        "source_type": "Dragon Forge",
        "source_url": "creatures.html",
        "source_location_vi": "Lò luyện Dragon Forge xây từ Gạch Lò Rồng.",
        "source_location_en": "Dragon Forge multiblock."
    },
    {
        "id": "dreadsteel_armor_set",
        "name": "Dreadsteel Armor Set",
        "name_vi": "Bộ Giáp Vô Địch Dreadsteel (Dreadsteel Set)",
        "icon": "images/items/dreadsteel_chestplate.png",
        "mod": "Dreadsteel / Ice & Fire",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["Warrior", "Paladin", "All Classes"],
        "recipe_type": "Anvil / Dragon Forge",
        "ingredients": [
            {"id": "dreadsteel_ingot", "name": "Dreadsteel Ingot", "name_vi": "Thỏi Thép Dreadsteel", "count": 24}
        ],
        "recipe_desc_vi": "Hợp nhất 3 loại Thép Rồng (Lửa + Băng + Sét) cùng Mảnh Dread Shard để rèn.",
        "recipe_desc_en": "Combines Fire, Ice, Lightning Dragonsteel with Dread Shard.",
        "effects_vi": "Set Bonus: +45 Điểm Giáp, +20 Kháng Đẩy Lùi, Hồi phục 3% Máu mỗi giây, Miễn nhiễm 100% mọi sát thương nguyên tố!",
        "effects_en": "Set Bonus: +45 Armor, +20 Knockback Resist, 3% HP Regen/sec, 100% Elemental Immunity!",
        "source_type": "Supreme Metallurgy",
        "source_url": "creatures.html",
        "source_location_vi": "Rèn hợp kim Dreadsteel tại Lò rèn Rồng tối cao.",
        "source_location_en": "Supreme Dragon Forge."
    },

    # -------------------------------------------------------------
    # 5. ALEX'S CAVES SPECIAL SUITS
    # -------------------------------------------------------------
    {
        "id": "hazmat_suit_set",
        "name": "Hazmat Armor Suit",
        "name_vi": "Bộ Đồ Bảo Hộ Phóng Xạ Hazmat Suit",
        "icon": "images/items/hazmat_chestplate.png",
        "mod": "Alex's Caves",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Ranger", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "rubber", "name": "Polymer Plate", "name_vi": "Tấm Cao Su Polymer", "count": 24},
            {"id": "lead_ingot", "name": "Lead Ingot", "name_vi": "Thỏi Chì", "count": 8}
        ],
        "recipe_desc_vi": "24x Tấm Polymer + 8x Thỏi Chì chống phóng xạ.",
        "recipe_desc_en": "24x Polymer Plate + 8x Lead Ingot.",
        "effects_vi": "KHÁNG 100% BỨC XẠ HẠT NHÂN & AXÍT! Bắt buộc phải mặc khi khám phá hang phóng xạ Toxic Caves.",
        "effects_en": "100% RADIATION & ACID IMMUNITY! Mandatory for exploring Toxic Caves.",
        "source_type": "Alex's Caves: Toxic Caves",
        "source_url": "creatures.html",
        "source_location_vi": "Bàn chế tạo sau khi khai thác Chì và Polymer.",
        "source_location_en": "Crafted with Lead and Polymer."
    },
    {
        "id": "diving_suit_set",
        "name": "Diving Armor Suit",
        "name_vi": "Bộ Đồ Lặn Biển Sâu (Diving Suit)",
        "icon": "images/items/diving_chestplate.png",
        "mod": "Alex's Caves",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["All Classes", "Paladin"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "copper_ingot", "name": "Copper Ingot", "name_vi": "Thỏi Đồng", "count": 16},
            {"id": "glass", "name": "Glass", "name_vi": "Kính Cường Lực", "count": 4}
        ],
        "recipe_desc_vi": "16x Thỏi Đồng + 4x Kính Cường Lực.",
        "recipe_desc_en": "16x Copper Ingot + 4x Glass.",
        "effects_vi": "KHÁNG ÁP SUẤT NƯỚC SÂU & Thở oxy dưới đáy vực Abyssal Chasm. Bắt buộc để đánh trùm Thủy Quái The Leviathan!",
        "effects_en": "CRUSHING DEPTH PRESSURE IMMUNITY! Mandatory for slaying The Leviathan!",
        "source_type": "Alex's Caves: Abyssal Chasm",
        "source_url": "creatures.html",
        "source_location_vi": "Vực biển Abyssal Chasm.",
        "source_location_en": "Abyssal Chasm deep ocean."
    },

    # -------------------------------------------------------------
    # 7. CATACLYSM BOSS ARMORS
    # -------------------------------------------------------------
    {
        "id": "ignitium_armor_set",
        "name": "Ignitium Armor Set",
        "name_vi": "Bộ Giáp Hỏa Thần Ignitium (Ignitium Set)",
        "icon": "images/items/ignitium_chestplate.png",
        "mod": "Cataclysm",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["Warrior", "Paladin"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "ignitium_ingot", "name": "Ignitium Ingot", "name_vi": "Thỏi Kim Loại Ignitium", "count": 16},
            {"id": "netherite_armor_set", "name": "Netherite Armor Piece", "name_vi": "Mảnh Giáp Netherite", "count": 4}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Netherite + Thỏi Ignitium (rơi từ Siêu Boss Ignis 1.000.000 HP) trên Smithing Table.",
        "recipe_desc_en": "Upgrade Netherite with Ignitium Ingots (dropped by Boss Ignis) on Smithing Table.",
        "effects_vi": "Set Bonus: +40 Điểm Giáp, Kháng 100% Lửa/Dung Nham, Phóng ra sóng xung kích Hỏa Ngục thiêu rụi kẻ tấn công!",
        "effects_en": "Set Bonus: +40 Armor, 100% Fire Immunity, Hellfire shockwave retaliation.",
        "source_type": "Boss: Ignis",
        "source_url": "bosses.html#boss-ignis",
        "source_location_vi": "Đấu trường Burning Arena giữa biển dung nham Nether.",
        "source_location_en": "Burning Arena inside Nether Wastes."
    },
    {
        "id": "monstrous_armor_set",
        "name": "Monstrous Armor Set",
        "name_vi": "Bộ Giáp Quái Thú Netherite (Monstrous Set)",
        "icon": "images/items/monstrous_helm.png",
        "mod": "Cataclysm",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "monstrous_horn", "name": "Monstrous Horn", "name_vi": "Sừng Quái Thú", "count": 2},
            {"id": "netherite_scrap", "name": "Netherite Scrap", "name_vi": "Mảnh Netherite", "count": 8}
        ],
        "recipe_desc_vi": "Rèn từ Sừng Quái Thú (rơi từ Boss Netherite Monstrosity) + Mảnh Netherite.",
        "recipe_desc_en": "Crafted from Monstrous Horns + Netherite Scraps.",
        "effects_vi": "Đặc tính [Monstrous Roar]: Khi chạy đà sẽ húc văng tất cả quái vật trên đường đi và tăng 25% Sát thương đập búa!",
        "effects_en": "[Monstrous Roar]: Charges ramming enemies aside, +25% Hammer Damage!",
        "source_type": "Boss: Netherite Monstrosity",
        "source_url": "bosses.html#boss-netherite_monstrosity",
        "source_location_vi": "Lò rèn Linh Hồn Soul Blacksmith trong Nether.",
        "source_location_en": "Soul Blacksmith in The Nether."
    },

    # -------------------------------------------------------------
    # 8. HAZEN 'N STUFF BATTLEMAGE SETS
    # -------------------------------------------------------------
    {
        "id": "mithril_armor_set",
        "name": "Mithril Battlemage Armor Set",
        "name_vi": "Bộ Giáp Chiến Pháp Mithril (Mithril Set)",
        "icon": "images/items/mithril_chestplate.png",
        "mod": "Hazen 'n Stuff",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Mage", "Warrior", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "mithril_ingot", "name": "Mithril Ingot", "name_vi": "Thỏi Mithril", "count": 24}
        ],
        "recipe_desc_vi": "24x Thỏi Mithril (Luyện từ quặng Mithril sâu dưới lòng đất).",
        "recipe_desc_en": "24x Mithril Ingot mined deep underground.",
        "effects_vi": "Cân bằng hoàn hảo giữa Giáp Vật Lý (+22 Giáp) và +15% Sát Thương Ma Thuật Mọi Hệ!",
        "effects_en": "Perfect balance: +22 Physical Armor and +15% Universal Spell Power!",
        "source_type": "Deep Underground Mining",
        "source_url": "progression.html",
        "source_location_vi": "Tầng đá phiến sâu Y = -30 đến -55.",
        "source_location_en": "Deepslate caves Y = -30 to -55."
    },
    {
        "id": "pyrium_armor_set",
        "name": "Pyrium Heavy Battlemage Set",
        "name_vi": "Bộ Giáp Trọng Chiến Pháp Pyrium",
        "icon": "images/items/pyrium_chestplate.png",
        "mod": "Hazen 'n Stuff",
        "category": "Armor",
        "stage": "Late",
        "classTags": ["Warrior", "Fire Mage", "Battlemage"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "pyrium_ingot", "name": "Pyrium Ingot", "name_vi": "Thỏi Pyrium", "count": 24}
        ],
        "recipe_desc_vi": "24x Thỏi Hợp Kim Pyrium (Nung kết hợp Mithril và Lửa Nether).",
        "recipe_desc_en": "24x Pyrium Ingot forged with Mithril and Nether Fire.",
        "effects_vi": "+28 Điểm Giáp, +35% Sát thương Hỏa Phép và tăng 20% Tốc độ chém kiếm liễu Rapier.",
        "effects_en": "+28 Armor, +35% Fire Spell Power, +20% Rapier Attack Speed.",
        "source_type": "Nether Metallurgy",
        "source_url": "magic.html",
        "source_location_vi": "Luyện kim nâng cao kết hợp nguyên liệu Nether.",
        "source_location_en": "Advanced Metallurgy using Nether materials."
    },

    # -------------------------------------------------------------
    # 9. GOETY & DARK ARTS NECROMANCY
    # -------------------------------------------------------------
    {
        "id": "apostle_robes_set",
        "name": "Apostle Dark Robes Set",
        "name_vi": "Bộ Áo Choàng Tông Đồ Bóng Tối (Apostle Robes)",
        "icon": "images/items/apostle_chestplate.png",
        "mod": "Goety",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Dark Altar Ritual",
        "ingredients": [
            {"id": "apocalypse_core", "name": "Apocalypse Core", "name_vi": "Lõi Tận Thế", "count": 1},
            {"id": "dark_cloth", "name": "Dark Cloth", "name_vi": "Vải Hắc Ám", "count": 16}
        ],
        "recipe_desc_vi": "Nghi lễ Tế đàn hắc ám kết hợp Lõi Tận Thế từ Boss Apostle / Apollyon.",
        "recipe_desc_en": "Dark Altar Ritual with Apocalypse Core from Boss Apostle/Apollyon.",
        "effects_vi": "Set Bonus: Triệu hồi Binh đoàn Xác sống Vô hạn (Necromancy Army), Kháng 100% Lời nguyền và sát thương Hư không!",
        "effects_en": "Set Bonus: Infinite Necromancy Undead Army, 100% Curse & Void Immunity!",
        "source_type": "Boss: Apostle / Apollyon",
        "source_url": "bosses.html#boss-apollyon",
        "source_location_vi": "Tế đàn hắc ám Dark Altar lúc nửa đêm.",
        "source_location_en": "Dark Altar Ritual at midnight."
    },
    {
        "id": "apocalyptium_armor_set",
        "name": "Apocalyptium Celestial Armor Set",
        "name_vi": "Bộ Giáp Thiên Sứ Tận Thế (Apocalyptium)",
        "icon": "images/items/apocalyptium_chestplate.png",
        "mod": "Goety Revelation / Terramity",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["All Classes", "Paladin", "Meta Build"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "apocalyptium_ingot", "name": "Apocalyptium Ingot", "name_vi": "Thỏi Apocalyptium", "count": 16},
            {"id": "ascension_halo", "name": "Ascension Halo", "name_vi": "Hào Quang Thăng Hoa", "count": 1}
        ],
        "recipe_desc_vi": "Rèn từ Hào Quang Thăng Hoa (100% rơi từ Boss Apollyon) + Thỏi Apocalyptium.",
        "recipe_desc_en": "Forged from Ascension Halo (dropped by Boss Apollyon) + Apocalyptium Ingots.",
        "effects_vi": "Set Bonus: +65 ĐIỂM GIÁP (BẢO VỆ TUYỆT ĐỐI), HỒI SINH TỰ ĐỘNG KHÔNG CẦN TOTEM, MIỄN NHIỄM 100% NGỌN LỬA ĐỊA NGỤC!",
        "effects_en": "Set Bonus: +65 ARMOR (ABSOLUTE DEFENSE), AUTO-REVIVE WITHOUT TOTEM, 100% HELLFIRE IMMUNITY!",
        "source_type": "Boss: Apollyon",
        "source_url": "bosses.html#boss-apollyon",
        "source_location_vi": "Nghi lễ triệu hồi Boss Apollyon.",
        "source_location_en": "Summoning Ritual of Boss Apollyon."
    },
    {
        "id": "dimlite_armor_set",
        "name": "Dimlite Armor Set",
        "name_vi": "Bộ Giáp Ánh Mờ (Dimlite Set)",
        "icon": "images/items/dimlite_chestplate.png",
        "mod": "Terramity",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Warrior", "Ranger"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "dimlite_ingot", "name": "Dimlite Ingot", "name_vi": "Thỏi Dimlite", "count": 4},
            {"id": "dimlite_template", "name": "Dimlite Template", "name_vi": "Bản Rèn Dimlite", "count": 4},
            {"id": "diamond_armor_piece", "name": "Diamond Armor", "name_vi": "Giáp Kim Cương", "count": 4}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Kim Cương + Bản rèn Dimlite (rơi từ Vua Lùn Gob) + Thỏi Dimlite.",
        "recipe_desc_en": "Upgrade Diamond Armor with Dimlite Template and Ingots on Smithing Table.",
        "effects_vi": "+25% Tốc độ di chuyển, +10% Tỉ lệ né tránh đòn đánh cận chiến.",
        "effects_en": "+25% Speed, +10% Dodge chance.",
        "source_type": "Boss: Gob King / Mining",
        "source_url": "bosses.html#boss-gob_king",
        "source_location_vi": "Court of Gnomes và đào quặng Dimlite Y = -20 đến -58.",
        "source_location_en": "Court of Gnomes and Dimlite Mining."
    },
    {
        "id": "cosmilite_armor_set",
        "name": "Cosmilite Armor Set",
        "name_vi": "Bộ Giáp Vũ Trụ (Cosmilite Set)",
        "icon": "images/items/cosmilite_chestplate.png",
        "mod": "Terramity",
        "category": "Armor",
        "stage": "Mid",
        "classTags": ["Ranger", "Mage"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "cosmilite_ingot", "name": "Cosmilite Ingot", "name_vi": "Thỏi Cosmilite", "count": 4},
            {"id": "cosmilite_template", "name": "Cosmilite Template", "name_vi": "Bản Rèn Cosmilite", "count": 4}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Kim Cương + Bản rèn Cosmilite + Thỏi Cosmilite (Đỉnh núi cao).",
        "recipe_desc_en": "Upgrade with Cosmilite Template and Ingots on Smithing Table.",
        "effects_vi": "Set Bonus: Bật khiên chắn phản lực, Giảm 50% sát thương tầm xa từ cung tên.",
        "effects_en": "Set Bonus: Kinetic barrier, 50% Projectile Damage Reduction.",
        "source_type": "Mountain Mining / Aether",
        "source_url": "progression.html",
        "source_location_vi": "Đỉnh núi tuyết cao Y > 120 và The Aether.",
        "source_location_en": "High mountain peaks Y > 120."
    },
    {
        "id": "reverium_paladin_armor_set",
        "name": "Reverium Paladin Armor Set",
        "name_vi": "Bộ Giáp Thánh Hiệp Sĩ Reverium",
        "icon": "images/items/reverium_paladin_chestplate.png",
        "mod": "Terramity",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["Paladin", "Warrior"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "reverium_ingot", "name": "Reverium Ingot", "name_vi": "Thỏi Thánh Reverium", "count": 16},
            {"id": "warden_armor_set", "name": "Warden Armor Piece", "name_vi": "Mảnh Giáp Warden", "count": 4}
        ],
        "recipe_desc_vi": "Nâng cấp từ trọn bộ Giáp Warden + Thỏi Thánh Reverium (The End) trên Smithing Table.",
        "recipe_desc_en": "Upgrade full Warden Armor set with Reverium Ingots on Smithing Table.",
        "effects_vi": "Set Bonus: +55 Điểm Giáp, +25 Kháng Đẩy Lùi, Hào quang Thánh hồi phục 5% Max HP mỗi giây cho toàn đội, Miễn nhiễm nguyền rủa!",
        "effects_en": "Set Bonus: +55 Armor, +25 Knockback Resist, 5% Max HP/sec Team Regen, Curse Immunity!",
        "source_type": "Endgame Outer Islands",
        "source_url": "progression.html",
        "source_location_vi": "Khai thác quặng Reverium tại các đảo ngoài cùng The End.",
        "source_location_en": "Mine Reverium in Outer End Islands."
    },
    {
        "id": "exodium_warlock_armor_set",
        "name": "Exodium Warlock Armor Set",
        "name_vi": "Bộ Giáp Pháp Sư Tối Cao Exodium Warlock",
        "icon": "images/items/exodium_warlock_chestplate.png",
        "mod": "Terramity",
        "category": "Armor",
        "stage": "Endgame",
        "classTags": ["Mage", "Battlemage"],
        "recipe_type": "Smithing Table",
        "ingredients": [
            {"id": "exodium_ingot", "name": "Exodium Ingot", "name_vi": "Thỏi Exodium", "count": 16},
            {"id": "reverium_ingot", "name": "Reverium Ingot", "name_vi": "Thỏi Reverium", "count": 8}
        ],
        "recipe_desc_vi": "Nâng cấp từ Giáp Ma Thuật Cấp Cao + Thỏi Exodium kết hợp thỏi Reverium.",
        "recipe_desc_en": "Upgrade Archmage robes with Exodium and Reverium Ingots on Smithing Table.",
        "effects_vi": "Set Bonus: +60% SÁT THƯƠNG PHÉP MỌI HỆ THỐNG, +1000 Mana tối đa, Giảm 50% thời gian hồi chiêu của tất cả các phép!",
        "effects_en": "Set Bonus: +60% ALL SPELL DAMAGE, +1000 Max Mana, 50% Cooldown Reduction on all spells!",
        "source_type": "Endgame Outer Islands",
        "source_url": "magic.html",
        "source_location_vi": "Khai thác quặng Exodium tại The End sau khi hạ Archmage Gundalf.",
        "source_location_en": "Outer End Islands after slaying Archmage Gundalf."
    }
]

# Read existing items_db from build_item_graph.py
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\build_item_graph.py", "r", encoding="utf-8") as f:
    code = f.read()

# Merge all armor sets into items_db
full_items = armor_sets

# Add all weapons, materials, and ingredients
# Re-import existing items_db definitions
exec_globals = {}
exec(code, exec_globals)
old_items = exec_globals.get("items_db", [])

# Combine and deduplicate
combined_map = {}
for it in old_items:
    combined_map[it["id"]] = it
for it in armor_sets:
    combined_map[it["id"]] = it

all_items = list(combined_map.values())

# Compute bidirectional graph
items_map = {item["id"]: item for item in all_items}
for item in all_items:
    item["used_in"] = []

for item in all_items:
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

print(f"Generated {len(all_items)} total items with complete bidirectional graph!")

output_js = f"""/**
 * Terramity Awakened Wiki - Item & Armor Graph Database (Expanded Edition)
 */
const ITEM_GRAPH_DATABASE = {json.dumps(all_items, ensure_ascii=False, indent=2)};
"""

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_items.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("Saved to data_items.js successfully!")
