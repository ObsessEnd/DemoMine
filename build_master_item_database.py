import os
import json

# =============================================================================
# TERRAMITY AWAKENED WIKI - MASTER ITEM & RECIPE GRAPH DATABASE
# Categories:
# 1. 🗡️ Weapon (Vũ Khí)
# 2. 🛡️ Armor (Giáp Trụ)
# 3. 🧪 Potion (Thuốc & Độc Dược)
# 4. 🍖 Food (Thực Phẩm & Món Ăn Bổ Dưỡng)
# 5. 📜 Consumable (Đồ Dùng 1 Lần / Cuộn Phép / Vật Phẩm Triệu Hồi / Totems)
# 6. 💍 Relic (Cổ Vật, Trang Sức & Curios)
# 7. ⚒️ Material (Nguyên Liệu, Quặng & Hợp Kim)
# =============================================================================

master_items = [
    # =========================================================================
    # 1. 🗡️ WEAPONS (VŨ KHÍ)
    # =========================================================================
    {
        "id": "solaris",
        "name": "Solaris",
        "name_vi": "Đại Đao Thái Dương Solaris",
        "icon": "images/items/solaris.png",
        "mod": "Celestisynth",
        "category": "Weapon",
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
        "id": "breezebreaker",
        "name": "Breezebreaker",
        "name_vi": "Phong Ma Kiếm Breezebreaker",
        "icon": "images/items/breezebreaker.png",
        "mod": "Celestisynth",
        "category": "Weapon",
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
        "category": "Weapon",
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
        "category": "Weapon",
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
        "id": "frostbound",
        "name": "Frostbound",
        "name_vi": "Lưỡi Hái Băng Ngục Frostbound",
        "icon": "images/items/frostbound.png",
        "mod": "Celestisynth",
        "category": "Weapon",
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
        "id": "rainfall_serenity",
        "name": "Rainfall Serenity",
        "name_vi": "Cung Thần Vũ Khúc (Rainfall Serenity)",
        "icon": "images/items/rainfall_serenity.png",
        "mod": "Celestisynth",
        "category": "Weapon",
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
    {
        "id": "incinerator",
        "name": "Incinerator",
        "name_vi": "Đại Đao Hỏa Thần Incinerator",
        "icon": "images/items/incinerator.png",
        "mod": "Cataclysm",
        "category": "Weapon",
        "stage": "Endgame",
        "classTags": ["Warrior", "Berserker"],
        "recipe_type": "Boss Drop (Ignis)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi 100% khi tiêu diệt Siêu Boss Ignis (1.000.000 HP) tại Burning Arena.",
        "recipe_desc_en": "Dropped 100% by Boss Ignis (1,000,000 HP) in Burning Arena.",
        "effects_vi": "40 Sát thương cơ bản, Chém xuyên thấu mọi loại khiên chắn và tung ra sóng lửa thiêu đốt 45 Tim!",
        "effects_en": "40 Base DMG, shield piercing, unleashes hellfire waves for 45 Hearts!",
        "source_type": "Boss: Ignis",
        "source_url": "bosses.html#boss-ignis",
        "source_location_vi": "Burning Arena (The Nether).",
        "source_location_en": "Burning Arena (The Nether)."
    },
    {
        "id": "dreadsteel_scythe",
        "name": "Dreadsteel Scythe",
        "name_vi": "Đại Lưỡi Hái Hủy Diệt Dreadsteel Scythe",
        "icon": "images/items/dreadsteel_scythe.png",
        "mod": "Dreadsteel",
        "category": "Weapon",
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
    {
        "id": "hf_meowrasama",
        "name": "HF Meowrasama",
        "name_vi": "Tuyệt Tác Kiếm Katana HF Meowrasama",
        "icon": "images/items/hf_meowrasama.png",
        "mod": "Lethality",
        "category": "Weapon",
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
        "id": "rhitta",
        "name": "Rhitta",
        "name_vi": "Thần Rìu Thái Dương Rhitta",
        "icon": "images/items/rhitta.png",
        "mod": "Brutality",
        "category": "Weapon",
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
        "id": "phoenix_bow",
        "name": "Phoenix Bow",
        "name_vi": "Cung Thần Phượng Hoàng (Phoenix Bow)",
        "icon": "images/items/phoenix_bow.png",
        "mod": "The Aether",
        "category": "Weapon",
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
        "category": "Weapon",
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
    {
        "id": "fireblossom_rapier",
        "name": "Fireblossom Rapier",
        "name_vi": "Kiếm Liễu Hỏa Liên (Fireblossom Rapier)",
        "icon": "images/items/fireblossom_rapier.png",
        "mod": "Hazen 'n Stuff",
        "category": "Weapon",
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
        "id": "raygun",
        "name": "Raygun",
        "name_vi": "Súng Tử Ngoại Raygun",
        "icon": "images/items/raygun.png",
        "mod": "Alex's Caves",
        "category": "Weapon",
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

    # =========================================================================
    # 2. 🧪 POTIONS & ELIXIRS (THUỐC & ĐỘC DƯỢC)
    # =========================================================================
    {
        "id": "life_bottle",
        "name": "Life Bottle",
        "name_vi": "Bình Sinh Mệnh (Life Bottle)",
        "icon": "images/items/life_bottle.png",
        "mod": "Terramity",
        "category": "Potion",
        "stage": "Early",
        "classTags": ["All Classes", "Paladin"],
        "recipe_type": "Brewing Stand / Crafting",
        "ingredients": [
            {"id": "red_apple", "name": "Apple", "name_vi": "Quả Táo", "count": 1},
            {"id": "glistering_melon_slice", "name": "Glistering Melon", "name_vi": "Dưa Hấu Vàng", "count": 1},
            {"id": "ghast_tear", "name": "Ghast Tear", "name_vi": "Nước Mắt Ma Địa Ngục", "count": 1}
        ],
        "recipe_desc_vi": "Pha chế từ Táo + Dưa hấu vàng + Nước mắt Ghast.",
        "recipe_desc_en": "Brewed with Apple + Glistering Melon + Ghast Tear.",
        "effects_vi": "Khi uống: Tăng vĩnh viễn +2 Máu Tối Đa (Tối đa uống 10 bình để nhận +20 Máu cơ bản)!",
        "effects_en": "When consumed: Permanently increases Max HP by +2 (Max 10 bottles for +20 HP)!",
        "source_type": "Brewing / Alchemy",
        "source_url": "utilities.html",
        "source_location_vi": "Pha chế tại Giàn pha thuốc Brewing Stand.",
        "source_location_en": "Brewed at Brewing Stand."
    },
    {
        "id": "mana_flask_greater",
        "name": "Greater Mana Flask",
        "name_vi": "Bình Mana Siêu Cấp (Greater Mana Flask)",
        "icon": "images/items/greater_mana_flask.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Potion",
        "stage": "Mid",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Brewing Stand",
        "ingredients": [
            {"id": "arcane_essence", "name": "Arcane Essence", "name_vi": "Tinh Chất Ma Thuật", "count": 2},
            {"id": "nether_wart", "name": "Nether Wart", "name_vi": "Bướu Địa Ngục", "count": 1}
        ],
        "recipe_desc_vi": "Pha chế Tinh Chất Ma Thuật với Thuốc Kỳ Lạ (Awkward Potion).",
        "recipe_desc_en": "Brew Arcane Essence into Awkward Potion.",
        "effects_vi": "Hồi phục tức thì 250 Mana và tăng 50% tốc độ hồi mana trong 3 phút.",
        "effects_en": "Instantly restores 250 Mana and grants +50% Mana Regen for 3 mins.",
        "source_type": "Alchemy",
        "source_url": "magic.html",
        "source_location_vi": "Giàn pha thuốc Brewing Stand.",
        "source_location_en": "Brewing Stand."
    },
    {
        "id": "fire_resistance_potion",
        "name": "Fire Resistance Potion (8:00)",
        "name_vi": "Thuốc Kháng Lửa Cấp Cao (8 Phút)",
        "icon": "images/items/potion_fire_res.png",
        "mod": "Minecraft Vanilla",
        "category": "Potion",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Brewing Stand",
        "ingredients": [
            {"id": "magma_cream", "name": "Magma Cream", "name_vi": "Kem Dung Nham", "count": 1},
            {"id": "redstone", "name": "Redstone Dust", "name_vi": "Bột Đá Đỏ", "count": 1}
        ],
        "recipe_desc_vi": "Kem Dung Nham + Bột Đá Đỏ (Giàn pha thuốc).",
        "recipe_desc_en": "Magma Cream + Redstone Dust at Brewing Stand.",
        "effects_vi": "Miễn nhiễm 100% sát thương Lửa và Dung nham trong 8 phút. Bắt buộc chuẩn bị khi đánh Netherite Monstrosity!",
        "effects_en": "100% Fire and Lava damage immunity for 8 minutes.",
        "source_type": "Brewing",
        "source_url": "dimensions.html#dim-nether",
        "source_location_vi": "Giàn pha thuốc Brewing Stand.",
        "source_location_en": "Brewing Stand."
    },
    {
        "id": "starlight_elixir",
        "name": "Starlight Elixir",
        "name_vi": "Thần Dược Ánh Sao (Starlight Elixir)",
        "icon": "images/items/starlight_elixir.png",
        "mod": "Celestisynth",
        "category": "Potion",
        "stage": "Late",
        "classTags": ["All Classes", "Warrior", "Mage"],
        "recipe_type": "Starlit Alchemy",
        "ingredients": [
            {"id": "celestial_core", "name": "Heated Celestial Core", "name_vi": "Lõi Thiên Thể Nung Đỏ", "count": 1},
            {"id": "ambrosia", "name": "Ambrosia", "name_vi": "Trái Ambrosia", "count": 2}
        ],
        "recipe_desc_vi": "Chưng cất Lõi Thiên Thể với Trái Ambrosia Thiên Giới.",
        "recipe_desc_en": "Distill Celestial Core with Aether Ambrosia.",
        "effects_vi": "+50% Sát thương vật lý, +50% Sát thương phép thuật, +30% Tốc độ di chuyển và Bất tử trong 10 giây đầu tiên!",
        "effects_en": "+50% Melee DMG, +50% Spell Power, +30% Speed, 10s Invulnerability!",
        "source_type": "Starlit Factory",
        "source_url": "magic.html",
        "source_location_vi": "Trạm Starlit Factory.",
        "source_location_en": "Starlit Factory."
    },

    # =========================================================================
    # 3. 🍖 FOOD & SUSTENANCE (THỰC PHẨM & MÓN ĂN)
    # =========================================================================
    {
        "id": "ambrosia",
        "name": "Ambrosia",
        "name_vi": "Thần Quả Ambrosia",
        "icon": "images/items/ambrosia.png",
        "mod": "The Aether",
        "category": "Food",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Harvesting / Dungeons",
        "ingredients": [],
        "recipe_desc_vi": "Hái từ cây Skyroot mọc trên thiên giới The Aether hoặc mở rương đền Bronze Dungeon.",
        "recipe_desc_en": "Harvested from Aether Skyroot trees or found in Bronze Dungeons.",
        "effects_vi": "Hồi 10 Thanh thức ăn, Cấp hiệu ứng Hồi Máu Siêu Tốc (Regeneration III) trong 15 giây và Kháng mọi debuff!",
        "effects_en": "Restores 10 Hunger, grants Regeneration III for 15s and cleanses debuffs!",
        "source_type": "The Aether",
        "source_url": "dimensions.html#dim-aether",
        "source_location_vi": "Tầng mây The Aether.",
        "source_location_en": "The Aether dimension."
    },
    {
        "id": "enchanted_golden_apple",
        "name": "Enchanted Golden Apple",
        "name_vi": "Táo Vàng Phù Phép (God Apple)",
        "icon": "images/items/enchanted_golden_apple.png",
        "mod": "Minecraft Vanilla",
        "category": "Food",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Dungeon Loot",
        "ingredients": [],
        "recipe_desc_vi": "Tìm thấy trong rương Dungeon, Ancient City, Bastion Remnant, Desert Temple.",
        "recipe_desc_en": "Found inside Dungeon, Ancient City, and Bastion chests.",
        "effects_vi": "Cấp hiệu ứng Hấp Thụ (Absorption IV +8 Tim Vàng), Hồi Phục II, Kháng Sát Thương I và Kháng Lửa trong 5 phút!",
        "effects_en": "Absorption IV (+8 Hearts), Regeneration II, Resistance I, Fire Resistance for 5m.",
        "source_type": "Dungeon Chests",
        "source_url": "progression.html",
        "source_location_vi": "Rương hầm ngục toàn thế giới.",
        "source_location_en": "World dungeon loot chests."
    },
    {
        "id": "starcatcher_cooked_tuna",
        "name": "Starlight Seared Tuna",
        "name_vi": "Cá Ngừ Nướng Ánh Sao (Starlight Tuna)",
        "icon": "images/items/cooked_starlight_tuna.png",
        "mod": "Starcatcher / Fishing",
        "category": "Food",
        "stage": "Mid",
        "classTags": ["All Classes", "Ranger"],
        "recipe_type": "Campfire / Smoker",
        "ingredients": [
            {"id": "raw_starlight_tuna", "name": "Raw Starlight Tuna", "name_vi": "Cá Ngừ Ánh Sao Sống", "count": 1}
        ],
        "recipe_desc_vi": "Câu cá tại Biển sâu vào ban đêm trời mưa bão rồi nướng trên Lửa trại Campfire.",
        "recipe_desc_en": "Fished in deep oceans during night storms, cooked on Campfire.",
        "effects_vi": "Hồi 12 Thanh Thức Ăn, Cấp hiệu ứng Tăng Tầm Nhìn Đêm (Night Vision) và +10% Tốc độ rút cung trong 10 phút!",
        "effects_en": "Restores 12 Hunger, grants Night Vision and +10% Bow Draw Speed for 10m!",
        "source_type": "Fishing / Ocean",
        "source_url": "utilities.html",
        "source_location_vi": "Biển sâu Deep Ocean ban đêm.",
        "source_location_en": "Deep Oceans at night."
    },

    # =========================================================================
    # 4. 📜 CONSUMABLES & 1-TIME USE (ĐỒ DÙNG 1 LẦN / CUỘN PHÉP / TOTEMS)
    # =========================================================================
    {
        "id": "scroll_fireball",
        "name": "Scroll of Fireball",
        "name_vi": "Cuộn Phép Hỏa Cầu (Fireball Scroll)",
        "icon": "images/items/scroll_fireball.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Consumable",
        "stage": "Early",
        "classTags": ["Mage", "Fire Mage", "All Classes"],
        "recipe_type": "Scroll Forge",
        "ingredients": [
            {"id": "blank_scroll", "name": "Blank Scroll", "name_vi": "Cuộn Giấy Trắng", "count": 1},
            {"id": "fire_rune", "name": "Fire Rune", "name_vi": "Cổ Tự Hỏa Ma", "count": 1},
            {"id": "common_ink", "name": "Common Ink", "name_vi": "Mực Thường", "count": 1}
        ],
        "recipe_desc_vi": "Khắc tại Lò Scroll Forge từ Cuộn giấy trắng + Cổ Tự Lửa + Lọ Mực.",
        "recipe_desc_en": "Inscribed at Scroll Forge with Blank Scroll + Fire Rune + Ink.",
        "effects_vi": "Sử dụng 1 lần: Phóng quả cầu lửa khổng lồ phát nổ gây 25 Sát thương Hỏa và thiêu rụi mục tiêu.",
        "effects_en": "Single use: Launches blazing fireball exploding for 25 Fire DMG.",
        "source_type": "Scroll Forge",
        "source_url": "magic.html",
        "source_location_vi": "Lò rèn Scroll Forge.",
        "source_location_en": "Scroll Forge."
    },
    {
        "id": "totem_of_undying",
        "name": "Totem of Undying",
        "name_vi": "Bùa Hộ Mệnh Bất Tử (Totem of Undying)",
        "icon": "images/items/totem_of_undying.png",
        "mod": "Minecraft Vanilla",
        "category": "Consumable",
        "stage": "Mid",
        "classTags": ["All Classes", "Paladin"],
        "recipe_type": "Mob Drop (Evoker)",
        "ingredients": [],
        "recipe_desc_vi": "Rơi ra khi tiêu diệt Evoker trong Woodland Mansion hoặc các đợt Pillager Raid.",
        "recipe_desc_en": "Dropped by Evokers in Woodland Mansions or Raids.",
        "effects_vi": "Khi nhận đòn chí tử: Ngay lập tức cứu sống người chơi, hồi 1 Tim máu, cấp Hồi Phục II, Hấp Thụ II và Kháng Lửa.",
        "effects_en": "Prevents death on lethal blow, restores 1 Heart, grants Regen II and Absorption.",
        "source_type": "Raids / Evokers",
        "source_url": "dimensions.html",
        "source_location_vi": "Woodland Mansion và Pillager Raids.",
        "source_location_en": "Woodland Mansions."
    },
    {
        "id": "primitive_tenacity_totem",
        "name": "Primitive Tenacity Totem",
        "name_vi": "Bảo Vật Bất Khuất Primitive Tenacity",
        "icon": "images/items/totem_primitive_tenacity.png",
        "mod": "Relics",
        "category": "Consumable",
        "stage": "Late",
        "classTags": ["All Classes", "Warrior"],
        "recipe_type": "Dungeon Chest / Nether",
        "ingredients": [],
        "recipe_desc_vi": "Tìm thấy trong rương kho báu Soul Blacksmith Arena hoặc Burning Arena.",
        "recipe_desc_en": "Found inside Soul Blacksmith or Burning Arena chests.",
        "effects_vi": "Cứu sống người chơi khi chết và kích hoạt CUỒNG NỘ BẤT TỬ trong 6 giây (Không thể mất máu trong 6s đó)!",
        "effects_en": "Saves player from death and grants 6 SECONDS OF ABSOLUTE INVINCIBILITY!",
        "source_type": "Cataclysm Dungeons",
        "source_url": "bosses.html",
        "source_location_vi": "Hầm ngục Cataclysm trong Nether.",
        "source_location_en": "Cataclysm Dungeons in Nether."
    },
    {
        "id": "recall_potion",
        "name": "Recall Potion",
        "name_vi": "Thuốc Dịch Chuyển Về Nhà (Recall Potion)",
        "icon": "images/items/recall_potion.png",
        "mod": "Terramity",
        "category": "Consumable",
        "stage": "Early",
        "classTags": ["All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "ender_pearl", "name": "Ender Pearl", "name_vi": "Ngọc Ender", "count": 1},
            {"id": "glass_bottle", "name": "Glass Bottle", "name_vi": "Chai Thủy Tinh", "count": 1},
            {"id": "gold_nugget", "name": "Gold Nugget", "name_vi": "Hạt Vàng", "count": 4}
        ],
        "recipe_desc_vi": "1x Ngọc Ender + 1x Chai Thủy Tinh + 4x Hạt Vàng.",
        "recipe_desc_en": "1x Ender Pearl + 1x Bottle + 4x Gold Nuggets.",
        "effects_vi": "Sử dụng 1 lần: Tức thì dịch chuyển người chơi về lại Giường ngủ hoặc Điểm hồi sinh ban đầu từ bất kỳ đâu!",
        "effects_en": "Single use: Instantly teleports player back to spawn bed from anywhere!",
        "source_type": "Crafting",
        "source_url": "utilities.html",
        "source_location_vi": "Bàn chế tạo.",
        "source_location_en": "Crafting Table."
    },
    {
        "id": "ignis_heart",
        "name": "Heart of Ignis",
        "name_vi": "Trái Tim Hỏa Thần Ignis (Summon Item)",
        "icon": "images/items/ignis_heart.png",
        "mod": "Cataclysm",
        "category": "Consumable",
        "stage": "Endgame",
        "classTags": ["All Classes", "Boss Summon"],
        "recipe_type": "Burning Arena Altar",
        "ingredients": [],
        "recipe_desc_vi": "Tìm thấy trong rương trung tâm Đấu trường Burning Arena.",
        "recipe_desc_en": "Found inside Burning Arena central chest.",
        "effects_vi": "Cắm vào Tế Đàn Lửa (Flame Altar) để triệu hồi Siêu Boss Ignis (1.000.000 HP).",
        "effects_en": "Place on Flame Altar to summon Boss Ignis (1,000,000 HP).",
        "source_type": "Burning Arena",
        "source_url": "bosses.html#boss-ignis",
        "source_location_vi": "Đấu trường rực lửa Burning Arena trong Nether.",
        "source_location_en": "Burning Arena in Nether."
    },

    # =========================================================================
    # 5. 💍 RELICS, CURIOS & BAUBLES (CỔ VẬT, TRANG SỨC & PHỤ KIỆN)
    # =========================================================================
    {
        "id": "heart_amulet",
        "name": "Heart Amulet",
        "name_vi": "Dây Chuyền Trái Tim (Heart Amulet)",
        "icon": "images/items/heart_amulet.png",
        "mod": "Baubley Heart Canisters",
        "stage": "Early",
        "classTags": ["Paladin", "All Classes"],
        "category": "Relic",
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "gold_ingot", "name": "Gold Ingot", "name_vi": "Thỏi Vàng", "count": 4},
            {"id": "diamond", "name": "Diamond", "name_vi": "Kim Cương", "count": 4}
        ],
        "recipe_desc_vi": "4x Thỏi Vàng + 4x Kim Cương.",
        "recipe_desc_en": "4x Gold Ingot + 4x Diamond.",
        "effects_vi": "Chứa tối đa 40 hộp Heart Canisters (Đỏ, Vàng, Lục, Lam) tăng thêm đến +80 Máu Tối Đa vĩnh viễn!",
        "effects_en": "Holds up to 40 Heart Canisters (Red, Yellow, Green, Blue) for up to +80 Max HP!",
        "source_type": "Crafting",
        "source_url": "utilities.html",
        "source_location_vi": "Chế tạo sớm tại Bàn chế tạo và đeo vào ô Curios Amulet.",
        "source_location_en": "Craft early at Crafting Table and equip into Curios Amulet slot."
    },
    {
        "id": "rage_glove",
        "name": "Rage Glove",
        "name_vi": "Găng Tay Cuồng Nộ (Rage Glove)",
        "icon": "images/items/rage_glove.png",
        "mod": "Relics",
        "stage": "Early",
        "classTags": ["Warrior", "Berserker"],
        "category": "Relic",
        "recipe_type": "Dungeon Chest",
        "ingredients": [],
        "recipe_desc_vi": "Raid Dungeons / Mineshafts Treasure Chests.",
        "recipe_desc_en": "Raid Dungeons / Mineshafts Treasure Chests.",
        "effects_vi": "+15% Tốc độ đánh, +2 Sát thương cận chiến, càng đánh liên tiếp tốc độ chém càng tăng.",
        "effects_en": "+15% Attack Speed, +2 Melee DMG, successive hits ramp up attack speed.",
        "source_type": "Dungeon Chest",
        "source_url": "utilities.html",
        "source_location_vi": "Tìm thấy trong rương hầm mỏ bỏ hoang Mineshaft hoặc pháo đài Outpost.",
        "source_location_en": "Found inside Mineshaft minecarts and Pillager Outpost chests."
    },
    {
        "id": "soul_elytra",
        "name": "Soul Elytra",
        "name_vi": "Cánh Linh Hồn (Soul Elytra)",
        "icon": "images/items/soul_elytra.png",
        "mod": "Deeper and Darker",
        "stage": "Late",
        "classTags": ["Ranger", "All Classes"],
        "category": "Relic",
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "elytra", "name": "Elytra", "name_vi": "Cánh Côn Trùng Elytra", "count": 1},
            {"id": "resonarium_ingot", "name": "Resonarium Ingot", "name_vi": "Thỏi Resonarium", "count": 2},
            {"id": "soul_dust", "name": "Soul Dust", "name_vi": "Bụi Linh Hồn", "count": 4}
        ],
        "recipe_desc_vi": "1x Elytra + 4x Soul Dust + 2x Resonarium Ingot (The Otherside).",
        "recipe_desc_en": "1x Elytra + 4x Soul Dust + 2x Resonarium Ingot (The Otherside).",
        "effects_vi": "+3 Điểm giáp, tự động kích hoạt lực đẩy phản lực mỗi 30s bay lượn vô hạn không cần Pháo hoa.",
        "effects_en": "+3 Armor, auto-boosts propulsion every 30s for infinite flight without fireworks.",
        "source_type": "Crafting / The Otherside",
        "source_url": "dimensions.html#dim-otherside",
        "source_location_vi": "Khai thác thỏi Resonarium trong cõi âm The Otherside kết hợp cánh Elytra.",
        "source_location_en": "Mine Resonarium in The Otherside dimension and upgrade Elytra."
    },
    {
        "id": "eternal_stella",
        "name": "Eternal Stella",
        "name_vi": "Bảo Vật Bất Tử Eternal Stella",
        "icon": "images/items/eternal_stella.png",
        "mod": "Forbidden and Arcanus",
        "stage": "Late",
        "classTags": ["All Classes", "Meta Build"],
        "category": "Relic",
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
        "category": "Relic",
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
    },

    # =========================================================================
    # 6. ⚒️ MATERIALS, ORES & ALLOYS (NGUYÊN LIỆU, QUẶNG & HỢP KIM)
    # =========================================================================
    {
        "id": "blank_rune",
        "name": "Blank Rune",
        "name_vi": "Cổ Tự Trắng (Blank Rune)",
        "icon": "images/items/blank_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Material",
        "stage": "Early",
        "classTags": ["Mage", "All Classes"],
        "recipe_type": "Crafting Table",
        "ingredients": [
            {"id": "arcane_essence", "name": "Arcane Essence", "name_vi": "Tinh Chất Ma Thuật", "count": 4},
            {"id": "stone", "name": "Stone", "name_vi": "Đá Thường", "count": 4}
        ],
        "recipe_desc_vi": "4x Arcane Essence + 4x Stone đặt xung quanh bàn chế tạo.",
        "recipe_desc_en": "4x Arcane Essence + 4x Stone in Crafting Table.",
        "effects_vi": "Phôi đá ma thuật trung tính dùng để khắc thành 8 loại Cổ Tự nguyên tố.",
        "effects_en": "Neutral arcane stone base used to inscribe 8 elemental runes.",
        "source_type": "Crafting",
        "source_url": "magic.html",
        "source_location_vi": "Chế tạo từ Arcane Essence rơi ra từ quái vật ma thuật.",
        "source_location_en": "Crafted from Arcane Essence dropped by magical mobs."
    },
    {
        "id": "fire_rune",
        "name": "Fire Rune",
        "name_vi": "Cổ Tự Hỏa Ma (Fire Rune)",
        "icon": "images/items/fire_rune.png",
        "mod": "Iron's Spells 'n Spellbooks",
        "category": "Material",
        "stage": "Early",
        "classTags": ["Mage", "Fire Mage"],
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
        "id": "prismatic_jewel",
        "name": "Prismatic Jewel",
        "name_vi": "Ngọc Lục Giác Cầu Vồng (Prismatic Jewel)",
        "icon": "images/items/prismatic_jewel.png",
        "mod": "Terramity",
        "category": "Material",
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
    }
]

# Read existing armor sets from expand_armor_catalog.py
with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\expand_armor_catalog.py", "r", encoding="utf-8") as f:
    code = f.read()

exec_globals = {}
exec(code, exec_globals)
old_armors = exec_globals.get("armor_sets", [])
old_items = exec_globals.get("old_items", [])

# Combine all items into a single master dictionary
combined_dict = {}

for it in old_items:
    combined_dict[it["id"]] = it
for it in old_armors:
    combined_dict[it["id"]] = it
for it in master_items:
    combined_dict[it["id"]] = it

all_master_items = list(combined_dict.values())

# Compute bidirectional graph
items_map = {item["id"]: item for item in all_master_items}
for item in all_master_items:
    item["used_in"] = []

for item in all_master_items:
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

print(f"Computed Master Item Database: {len(all_master_items)} total items!")

output_js = f"""/**
 * Terramity Awakened Wiki - Complete Master Item & Graph Database
 */
const ITEM_GRAPH_DATABASE = {json.dumps(all_master_items, ensure_ascii=False, indent=2)};
"""

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_items.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("Master database successfully compiled and written to data_items.js!")
