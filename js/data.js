/**
 * Terramity Awakened Wiki - Complete Bilingual Data Repository
 */

const WIKI_DATA = {
  metadata: {
    name: "Terramity Awakened",
    version: "v1.0.5 Release",
    minecraft: "1.20.1",
    forge: "47.4.20",
    stats: {
      mods: 356,
      quests: 432,
      bosses: 70,
      dimensions: 5
    }
  },

  bosses: [
    {
      id: "umvuthi",
      name: "Umvuthi, The Sunbird",
      mod: "Born in Chaos",
      tier: 1,
      stars: "★☆☆☆☆",
      hp: 500,
      dimension: "Overworld",
      location: "Savanna / Umvuthana Groves",
      location_vi: "Đồng cỏ Xavan / Rừng Umvuthana",
      summon: "Found in Sunbird nest or summoned at Sun Altar",
      summon_vi: "Tìm thấy tại tổ chim mặt trời hoặc triệu hồi tại Tế đàn Mặt trời",
      drops: ["Sunbird Feather", "Solar Staff", "XP"],
      drops_vi: ["Lông vũ Chim Mặt Trời", "Trượng Thái Dương", "Kinh nghiệm"],
      tips: "Use ranged attacks. Beware of dive bombs and fire trails.",
      tips_vi: "Nên dùng vũ khí tầm xa. Cẩn thận các đòn bổ nhào lao xuống và vệt lửa thiêu đốt."
    },
    {
      id: "gob_king",
      name: "Gob, King of Gnomes",
      mod: "Terramity",
      tier: 1,
      stars: "★☆☆☆☆",
      hp: 120,
      dimension: "Overworld",
      location: "Court of Gnomes Structure",
      location_vi: "Cấu trúc Vương triều Gnome (Court of Gnomes)",
      summon: "Break the Gnome Throne in Court of Gnomes",
      summon_vi: "Đập vỡ Ngai vàng Gnome trong cấu trúc",
      drops: ["Blood Coins", "Gnome King Hat", "Dimlite Template"],
      drops_vi: ["Đồng xu Blood Coins", "Mũ Vua Gnome", "Bản rèn Dimlite"],
      tips: "Fast moving but low health. Clear the gnome guards first.",
      tips_vi: "Di chuyển rất nhanh nhưng máu ít. Nên tiêu diệt đám lính Gnome xung quanh trước."
    },
    {
      id: "slider",
      name: "Slider",
      mod: "The Aether",
      tier: 1,
      stars: "★☆☆☆☆",
      hp: 400,
      dimension: "The Aether",
      location: "Bronze Dungeon",
      location_vi: "Hầm ngục Đồng (Bronze Dungeon)",
      summon: "Awaken in boss chamber inside Bronze Dungeon",
      summon_vi: "Đánh thức trong phòng trùm hầm ngục",
      drops: ["Bronze Dungeon Key", "Hammer of Kingbdogz", "Neptune Armor"],
      drops_vi: ["Chìa khóa Hầm ngục Đồng", "Búa Thần Kingbdogz", "Giáp Neptune"],
      tips: "ONLY takes damage from Pickaxes! Switches from blue (slow) to red (fast enraged).",
      tips_vi: "CHỈ nhận sát thương từ Cuốc (Pickaxe)! Đổi màu từ xanh (chậm) sang đỏ (cuồng nộ siêu tốc)."
    },
    {
      id: "super_sniffer",
      name: "Super Sniffer",
      mod: "Terramity",
      tier: 1,
      stars: "★☆☆☆☆",
      hp: 350,
      dimension: "Overworld",
      location: "Plains / Forests",
      location_vi: "Đồng bằng / Rừng rậm",
      summon: "Feed a Sniffer a Profaned Berry or strike with lightning",
      summon_vi: "Cho Sniffer ăn quả Profaned Berry hoặc đánh sét vào Sniffer",
      drops: ["Ancient Fur", "Super Sniffer Horn", "Virentium Template"],
      drops_vi: ["Lông Cổ Đại", "Sừng Siêu Sniffer", "Bản rèn Virentium"],
      tips: "High knockback resistance. Keep moving in circles.",
      tips_vi: "Kháng đẩy lùi rất cao. Hãy vừa di chuyển vòng quanh vừa tấn công."
    },
    {
      id: "valkyrie_queen",
      name: "Valkyrie Queen",
      mod: "The Aether",
      tier: 2,
      stars: "★★☆☆☆",
      hp: 500,
      dimension: "The Aether",
      location: "Silver Dungeon (Temple in sky)",
      location_vi: "Hầm ngục Bạc (Đền mây)",
      summon: "Present 10 Valkyrie Medals to challenge her",
      summon_vi: "Giao nộp 10 Huy hiệu Valkyrie Medal để khiêu chiến",
      drops: ["Silver Dungeon Key", "Valkyrie Lance", "Valkyrie Armor"],
      drops_vi: ["Chìa khóa Hầm ngục Bạc", "Thương Valkyrie", "Giáp Valkyrie"],
      tips: "Teleports frequently and strikes with lightning thrusts.",
      tips_vi: "Thường xuyên dịch chuyển tức thời và tung đòn đâm sét liên hoàn."
    },
    {
      id: "sun_spirit",
      name: "Sun Spirit",
      mod: "The Aether",
      tier: 2,
      stars: "★★☆☆☆",
      hp: 1000,
      dimension: "The Aether",
      location: "Gold Dungeon (Sun Temple)",
      location_vi: "Hầm ngục Vàng (Đền Mặt Trời)",
      summon: "Interact in the lava core chamber",
      summon_vi: "Tương tác trong căn phòng dung nham hoàng kim",
      drops: ["Gold Dungeon Key", "Phoenix Bow", "Phoenix Armor"],
      drops_vi: ["Chìa khóa Hầm ngục Vàng", "Cung Phượng Hoàng", "Giáp Phượng Hoàng"],
      tips: "Immune to direct attacks! Hit his ice/fire orbs back at him.",
      tips_vi: "Miễn nhiễm sát thương trực tiếp! Phải đánh phản các quả cầu băng/lửa dội ngược vào người boss."
    },
    {
      id: "dead_king",
      name: "The Dead King",
      mod: "Iron's Spells",
      tier: 2,
      stars: "★★☆☆☆",
      hp: 1800,
      dimension: "Overworld",
      location: "Catacombs (Deep Underground)",
      location_vi: "Hầm mộ ngầm Catacombs",
      summon: "Locate with Wayward Compass in underground throne",
      summon_vi: "Dùng Wayward Compass định vị hầm ngục và đánh thức tại ngai vàng",
      drops: ["Dead King Helm", "Blood Staff", "Legendary Ink & Runes"],
      drops_vi: ["Mũ Vua Bất Tử", "Trượng Huyết Ma", "Mực & Cổ Tự Huyền Thoại"],
      tips: "Has 2 phases. Summons hordes of undead mages and casts high-tier blood spells.",
      tips_vi: "Có 2 giai đoạn. Triệu hồi quái phép liên tục và thi triển huyết phép diện rộng."
    },
    {
      id: "trial_guardian",
      name: "Trial Guardian",
      mod: "Terramity",
      tier: 3,
      stars: "★★★☆☆",
      hp: 1500,
      dimension: "Overworld",
      location: "Trial Spire (Height Y > 150)",
      location_vi: "Tháp Thử Thách Trial Spire (Độ cao Y > 150)",
      summon: "Activate the Spire Core at the top of Trial Spire",
      summon_vi: "Kích hoạt lõi Spire Core trên đỉnh tháp",
      drops: ["Iridium Shard", "Guardian Core", "Cosmilite Ingot"],
      drops_vi: ["Mảnh Iridium", "Lõi Hộ Vệ", "Thỏi Cosmilite"],
      tips: "Shielded against ranged attacks during barrier phase. Melee when vulnerable.",
      tips_vi: "Bật khiên phản đòn tầm xa trong pha tạo khiên. Lao vào cận chiến khi khiên vỡ."
    },
    {
      id: "netherite_monstrosity",
      name: "Netherite Monstrosity",
      mod: "Cataclysm",
      tier: 3,
      stars: "★★★☆☆",
      hp: 4800,
      dimension: "The Nether",
      location: "Soul Blacksmith Arena",
      location_vi: "Lò rèn Linh hồn (Soul Blacksmith Arena)",
      summon: "Place Monstrous Eye into the central altar block",
      summon_vi: "Đặt mắt Monstrous Eye vào bệ tế đàn trung tâm",
      drops: ["Monstrous Horn", "Infernal Forge Hammer", "Netherite Scrap x12"],
      drops_vi: ["Sừng Quái Thú", "Búa Luyện Lửa Infernal", "Mảnh Netherite x12"],
      tips: "Massive ground slams. Jump or combat roll before impact. Avoid lava pools.",
      tips_vi: "Đòn đập đất cực mạnh. Nhảy lên hoặc lăn lộn (Combat Roll) né chấn động và dung nham."
    },
    {
      id: "the_leviathan",
      name: "The Leviathan",
      mod: "Cataclysm",
      tier: 4,
      stars: "★★★★☆",
      hp: 180000,
      dimension: "Overworld",
      location: "Sunken City (Deep Ocean)",
      location_vi: "Thành phố Chìm Đáy Biển (Sunken City)",
      summon: "Place Tidal Claws on the altar of the Sunken City",
      summon_vi: "Đặt vuốt Tidal Claws lên tế đàn đáy biển",
      drops: ["Abyssal Sacrifice", "Tidal Claws", "Leviathan Armor Core"],
      drops_vi: ["Hiến Tế Vực Thẳm", "Vuốt Thủy Triều", "Lõi Giáp Leviathan"],
      tips: "Fought underwater. Must have Diving Armor or Conduit active.",
      tips_vi: "Trận chiến hoàn toàn dưới nước. Bắt buộc có Giáp Lặn (Diving Armor) hoặc Conduit."
    },
    {
      id: "ignis",
      name: "Ignis, The Profane",
      mod: "Cataclysm",
      tier: 5,
      stars: "★★★★★",
      hp: 1000000,
      dimension: "The Nether",
      location: "Burning Arena in Nether Wastes",
      location_vi: "Đấu trường Rực Lửa giữa biển dung nham Nether",
      summon: "Insert Ignis Heart into the Flame Altar",
      summon_vi: "Cắm Trái tim Ignis Heart vào Tế đàn Lửa",
      drops: ["Incinerator Greatsword", "Ignitium Ingot", "Profane Core"],
      drops_vi: ["Đại đao Incinerator", "Thỏi Kim Loại Ignitium", "Lõi Bất Tịnh"],
      tips: "Extreme fire damage and armor penetration. Equip Fire Dragonsteel or Warden Armor.",
      tips_vi: "Sát thương thiêu đốt và xuyên giáp cực nặng. Cần trang bị giáp Warden hoặc Fire Dragonsteel."
    },
    {
      id: "apollyon",
      name: "Apollyon (The Fallen Seraph)",
      mod: "Goety Revelation",
      tier: 5,
      stars: "★★★★★",
      hp: 6666,
      dimension: "Overworld / Nether",
      location: "Dark Altar Ritual",
      location_vi: "Nghi lễ Tế Đàn Tối Thượng (Dark Altar)",
      summon: "1% chance during Apostle Master Forge Ritual at midnight",
      summon_vi: "1% tỉ lệ xuất hiện khi thực hiện nghi lễ gọi Apostle lúc nửa đêm",
      drops: ["Ascension Halo", "Apocalyptium Ingot", "Seraph Bow"],
      drops_vi: ["Hào Quang Thăng Hoa (Ascension Halo)", "Thỏi Apocalyptium", "Cung Thiên Sứ"],
      tips: "Hellfire burns 6.66% Max HP. Cap damage per hit at 100. Bring Totems and high regen.",
      tips_vi: "Ngọn lửa địa ngục thiêu 6.66% Máu tối đa. Sát thương nhận vào bị giới hạn 100/hit. Chuẩn bị nhiều Totem."
    },
    {
      id: "ultra_sniffer",
      name: "Ultra Sniffer (Vua Thần Thú Cổ Đại)",
      mod: "Terramity",
      tier: 5,
      stars: "★★★★★",
      hp: 1000000,
      dimension: "Overworld / Custom Arena",
      location: "Endgame Arena",
      location_vi: "Đấu trường Vô Cực Tận Diệt",
      summon: "Lightning strike on Super Sniffer Phase 2 when under 10% HP with Reverium Ingot",
      summon_vi: "Đánh sét vào Super Sniffer giai đoạn 2 khi dưới 10% máu kèm thỏi Reverium",
      drops: ["The Judgement", "Godly Essence", "Modpack Completion Badge"],
      drops_vi: ["Thần Khí The Judgement", "Tinh Chất Thần Thánh", "Huy Hiệu Phá Đảo"],
      tips: "The ultimate boss. Requires fully perfected Meta Build with Eternal Stella.",
      tips_vi: "Siêu trùm tối thượng. Bắt buộc có trang bị Meta Build hoàn thiện ép ngọc Eternal Stella."
    }
  ],

  dimensions: [
    {
      id: "aether",
      name: "The Aether",
      name_vi: "Thiên Giới Đảo Mây (The Aether)",
      portal: "Glowstone Frame (like Nether Portal) + Water Bucket",
      portal_vi: "Khung đá phát sáng Glowstone + Đổ Xô Nước vào giữa",
      key_bosses: ["Slider", "Valkyrie Queen", "Sun Spirit"],
      key_resources: ["Zanite Ore", "Gravitite Ore", "Ambrosia", "Skyroot"],
      key_resources_vi: ["Quặng Zanite", "Quặng Gravitite (Phản trọng lực)", "Trái Ambrosia", "Gỗ Mây"],
      guide: "Floating sky islands with low gravity feel. Defeat 3 dungeons (Bronze, Silver, Gold) to conquer.",
      guide_vi: "Các hòn đảo bồng bềnh giữa tầng mây. Vượt qua 3 hầm ngục (Đồng, Bạc, Vàng) để chinh phục toàn bộ thiên giới."
    },
    {
      id: "otherside",
      name: "The Otherside",
      name_vi: "Cõi Âm Sâu Thẳm (The Otherside - Deeper & Darker)",
      portal: "Kill Warden -> Get Heart of the Deep -> Clear Sculk Veins in Ancient City Portal -> Right click frame",
      portal_vi: "Tiêu diệt Warden lấy Heart of the Deep -> Dọn sạch rễ Sculk quanh cổng Ancient City -> Nhấp chuột phải kích hoạt",
      key_bosses: ["The Warden", "The Stalker"],
      key_resources: ["Resonarium Ingot", "Soul Elytra", "Sonorous Staff", "Sculk Transmitter"],
      key_resources_vi: ["Thỏi Resonarium", "Cánh Soul Elytra", "Gậy Sóng Âm Sonorous", "Bộ truyền tin Sculk"],
      guide: "Dark, terrifying realm beyond the Deep Dark. Warden Armor grants complete blindness immunity.",
      guide_vi: "Chiều không gian hắc ám rùng rợn. Bộ giáp Warden chế tạo tại đây kháng vĩnh viễn hiệu ứng Mù lòa (Blindness)."
    },
    {
      id: "nether",
      name: "The Nether (Overhauled)",
      name_vi: "Địa Ngục Nâng Cấp (The Nether)",
      portal: "Obsidian Frame + Flint and Steel",
      portal_vi: "Khung Obsidian + Bật Lửa",
      key_bosses: ["Netherite Monstrosity", "The Harbinger", "Ignis", "Wither"],
      key_resources: ["Ancient Debris", "Ignitium", "Witherite", "Soul Alloys"],
      key_resources_vi: ["Mảnh Netherite Cổ", "Kim loại Ignitium", "Thỏi Witherite", "Hợp kim Linh hồn"],
      guide: "Host to massive dungeons: Soul Blacksmith, Ancient Factory, and the Burning Arena.",
      guide_vi: "Chứa nhiều pháo đài khổng lồ: Lò rèn Lửa, Nhà máy Cổ đại và Đấu trường Ignis giữa biển dung nham."
    },
    {
      id: "the_end",
      name: "The End & 12 Ancient Eyes",
      name_vi: "The End & 12 Mắt Thần Ma Thuật",
      portal: "Collect all 12 Unique End Remastered Eyes and place them in the Ancient Portal Frame",
      portal_vi: "Thu thập đủ 12 con Mắt Thần độc nhất từ các hầm ngục và cắm vào Khung Cổng Cổ Đại",
      key_bosses: ["Ender Dragon", "Ender Guardian", "Endersent", "Shulker Mimic", "Devourer of Gods"],
      key_resources: ["Enderite", "Void Core", "Dragon Breath", "Shulker Shells"],
      key_resources_vi: ["Thỏi Enderite", "Lõi Hư Không Void Core", "Hơi thở Rồng", "Vỏ Shulker Lớn"],
      guide: "End Remastered overhaul ensures you explore the whole world before accessing the dragon island.",
      guide_vi: "Cơ chế End Remastered yêu cầu khám phá toàn bộ thế giới trước khi có thể mở đường đến tổ rồng."
    }
  ],

  eyes: [
    { name: "Cursed Eye", loc: "Bastion Remnant Treasure Chest (Nether)", rate: "50%" },
    { name: "Black Eye", loc: "Buried Treasure Chest or Kill The Warden", rate: "30% / 10% (Drops 2)" },
    { name: "Lost Eye", loc: "Abandoned Mineshaft Minecart Chest", rate: "20%" },
    { name: "Cold Eye", loc: "Igloo Basement Secret Chest", rate: "70%" },
    { name: "Corrupted Eye", loc: "Pillager Outpost Top Chest", rate: "30%" },
    { name: "Nether Eye", loc: "Nether Fortress Corridor Chest", rate: "30%" },
    { name: "Old Eye", loc: "Desert Pyramid Secret Chamber", rate: "10%" },
    { name: "Rogue Eye", loc: "Jungle Pyramid Dispenser/Chest", rate: "40%" },
    { name: "Guardian Eye", loc: "Elder Guardian Kill (Ocean Monument)", rate: "30%" },
    { name: "Magical Eye", loc: "Woodland Mansion Chest / Evoker Kill", rate: "10% / 5%" },
    { name: "Wither Eye", loc: "Wither Boss Kill", rate: "100%" },
    { name: "Undead Eye", loc: "Craft: Phantom Membrane + Bone + Rotten Flesh + Ghast Tear + Undead Soul", rate: "Craftable" }
  ],

  meta_build: [
    {
      step: 1,
      title: "Choose Supreme Base Armor & Weapons",
      title_vi: "Chọn Phôi Trang Bị Thần Thoại",
      desc: "Warden Armor, Reverium Paladin, Apocalyptium, or Celestisynth Weapons (Solaris/Keres).",
      desc_vi: "Giáp Warden, Giáp Reverium, Apocalyptium hoặc Vũ khí Celestisynth (Solaris, Keres, Frostbound)."
    },
    {
      step: 2,
      title: "Enchant to Limit Level 100",
      title_vi: "Phù Phép Cực Hạn Cấp 100",
      desc: "Apotheosis setup with Draconic Endshelves and Rectifier T3 to achieve 100% Arcana and Lv100 enchants.",
      desc_vi: "Dùng bàn Apotheosis với kệ sách Draconic Endshelf và bộ điều phối Rectifier T3 đạt cấp 100 với 100% Arcana."
    },
    {
      step: 3,
      title: "Reforge Ancient/Mythic Affixes",
      title_vi: "Tái Rèn Dòng Thuộc Tính Cổ Đại",
      desc: "Use the Esoteric Reforging Table with Gem Dust to roll legendary red/orange bonus stats.",
      desc_vi: "Dùng bàn Esoteric Reforging Table với Bụi ngọc Gem Dust để ra các dòng chỉ số màu Đỏ/Cam mạnh nhất."
    },
    {
      step: 4,
      title: "Socket 4 Mythic Gems",
      title_vi: "Đục 4 Lỗ & Khảm Ngọc Thần Thoại",
      desc: "Use Sigil of Socketing to add 4 sockets, then socket Mythic/Ancient gems for lifesteal & armor penetration.",
      desc_vi: "Dùng Sigil of Socketing đục 4 lỗ trên Smithing Table, khảm 4 viên Ngọc Thần Thoại tăng Hút máu và Xuyên giáp."
    },
    {
      step: 5,
      title: "Imbue Spells & 10 Upgrade Orbs",
      title_vi: "Khảm 10 Upgrade Orbs & Imbue Phép",
      desc: "In Arcane Anvil, add 10 Upgrade Orbs of your chosen school and imbue a high-tier spell directly into your blade.",
      desc_vi: "Dùng Đe Ma Thuật Arcane Anvil gắn 10 viên ngọc Upgrade Orb và ép thẳng 1 chiêu phép cấp cao vào kiếm."
    },
    {
      step: 6,
      title: "Apply Eternal Stella (Indestructible)",
      title_vi: "Ép Ngọc Eternal Stella - BẤT TỬ 100%",
      desc: "Combine with Eternal Stella in an Anvil. Your gear will never break, never lose durability, and stays immortal forever.",
      desc_vi: "Kết hợp với viên ngọc Eternal Stella trong đe. Món đồ sẽ hồi phục 100% độ bền và KHÔNG BAO GIỜ HỎNG."
    }
  ],

  classes: [
    {
      id: "warrior",
      name: "Warrior / Berserker",
      name_vi: "Đấu Sĩ Cuồng Nộ (Warrior / Berserker)",
      role: "Melee Heavy DPS & Cleave",
      role_vi: "Cận chiến Sát thương lớn & Quét diện rộng",
      weapons: "Claymore, Greatsword, Solaris, Keres, Rhitta Axe",
      armor: "Dragonsteel Armor -> Warden Armor -> Reverium Armor",
      relics: "Rage Glove, Berserker Ring, Drowned Belt",
      gameplay_vi: "Lao vào đội hình địch, tận dụng Combat Roll né chiêu và bổ những nhát chém chí mạng quét sạch mục tiêu."
    },
    {
      id: "mage",
      name: "Mage / Elementalist",
      name_vi: "Pháp Sư Tối Cao (Mage / Elementalist)",
      role: "Ranged AOE Magic & Minion Army",
      role_vi: "Phép thuật tầm xa AOE & Binh đoàn đệ tớ",
      weapons: "Dragonskin Spellbook, Staff of Storm Empress, Wand of Final Light",
      armor: "Archevoker Robes -> TravelOptics Sovereign Sets -> Spider Darkmage",
      relics: "Midnight Robe, Cooldown Reduction Rings, Spell Power Amulets",
      gameplay_vi: "Giữ cự ly an toàn, liên tục xả bão sét, mưa sao băng và gọi bầy tôi quái vật từ Goety ra đỡ đòn."
    },
    {
      id: "paladin",
      name: "Paladin / Holy Tanker",
      name_vi: "Hiệp Sĩ Thánh (Paladin / Tanker)",
      role: "Invincible Defense & Team Regeneration",
      role_vi: "Phòng ngự bất khả xâm phạm & Hồi phục",
      weapons: "Hammer of Kingbdogz, Gauntlet of Guard, Holy Lances",
      armor: "Neptune Armor -> Draco Arcanus -> Apocalyptium Armor",
      relics: "Holy Locket, Heart Amulet (Full 40 Canisters), Aegis Shield",
      gameplay_vi: "Hút toàn bộ sát thương từ Boss lớn, che chắn cho đồng đội và liên tục hồi phục sinh lực cho toàn đội."
    },
    {
      id: "ranger",
      name: "Ranger / Sniper",
      name_vi: "Xạ Thủ Du Mục (Ranger / Sniper)",
      role: "Extreme Mobility & Rapid Ranged Precision",
      role_vi: "Cực kỳ cơ động & Bắn tỉa tầm xa chuẩn xác",
      weapons: "Phoenix Bow, Dreadbow, Raygun, Nuclear Rocket Launcher",
      armor: "Valkyrie Armor -> Hazmat Reinforced -> Void Walker Set",
      relics: "Space Dissector, Quiver of Endless Arrows, Mobility Rings",
      gameplay_vi: "Bay lượn trên không với cánh Soul Elytra, xả mưa tên lửa và tia tử ngoại từ độ cao an toàn."
    }
  ],

  tips: [
    {
      type: "danger",
      title: "CRASH BUG WARNING: Sugar Rush Effect",
      title_vi: "CẢNH BÁO LỖI CRASH WORLD: Hiệu ứng Sugar Rush",
      desc: "DO NOT use potions or foods granting the Sugar Rush effect. A known mod conflict causes infinite mob multiplication which freezes and crashes the world permanently.",
      desc_vi: "TUYỆT ĐỐI KHÔNG sử dụng thuốc hay thức ăn có hiệu ứng Sugar Rush. Xung đột mã nguồn sẽ nhân bản quái vật vô hạn khiến world bị đóng băng và hỏng file save vĩnh viễn."
    },
    {
      type: "warning",
      title: "Ring of Seven Curses (Enigmatic Legacy)",
      title_vi: "Lời Nguyền Chiếc Nhẫn (Ring of Seven Curses)",
      desc: "If chosen at world start, monsters deal 200% damage and you take amplified hurt from all sources. The ring CANNOT be unequipped. Only for hardcore masochists!",
      desc_vi: "Nếu chọn nhẫn này lúc đầu game, quái vật tăng 200% sát thương và bạn chịu thêm sát thương từ mọi nguồn. Nhẫn KHÔNG THỂ tháo ra. Chỉ dành cho người chơi thích thử thách cực hạn!"
    },
    {
      type: "info",
      title: "Explorer's Compass & Nature's Compass",
      title_vi: "Dùng La Bàn Định Vị Dungeon & Biome",
      desc: "Craft these 2 compasses right away on Day 1. They point directly to any structure (Dungeons, Towers, Catacombs) and any Biome instantly.",
      desc_vi: "Hãy chế tạo 2 la bàn này ngay từ Ngày 1. Chúng sẽ chỉ đường thẳng đến bất kỳ hầm ngục, cấu trúc đền đài hay biome nào mà bạn muốn tìm."
    },
    {
      type: "success",
      title: "Gob's Shop Currency: Blood Coins",
      title_vi: "Đừng vứt Blood Coins rơi từ Boss",
      desc: "Bosses drop red Blood Coins. Bring them to Gob in the Court of Gnomes to purchase endgame legendary weapons like Whisperwind and Sunfire.",
      desc_vi: "Các Boss sẽ rơi ra đồng xu đỏ Blood Coins. Hãy mang đến đổi với thương nhân Gob để lấy vũ khí thần thoại như Whisperwind và Sunfire."
    }
  ]
};
