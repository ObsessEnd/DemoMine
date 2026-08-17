/**
 * Terramity Awakened Wiki - Complete Bilingual Data Repository (Pro Edition)
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
      dimensions: 5,
      itemsExtracted: 8726
    }
  },

  /* ==========================================================================
     PACKAGE 1: Deep Boss Mechanics, Phases & Combat Guide
     ========================================================================== */
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
      drops: ["Sunbird Feather (100%)", "Solar Staff (30%)", "3500 XP"],
      drops_vi: ["Lông vũ Chim Mặt Trời (100%)", "Trượng Thái Dương (30%)", "3500 Điểm EXP"],
      tips: "Use ranged attacks. Beware of dive bombs and fire trails.",
      tips_vi: "Nên dùng vũ khí tầm xa. Cẩn thận các đòn bổ nhào lao xuống và vệt lửa thiêu đốt.",
      phases: [
        {
          name_vi: "Pha 1 (100% - 40% HP): Lượn Bắn Cầu Lửa",
          name_en: "Phase 1 (100% - 40% HP): Aerial Fire Barrage",
          desc_vi: "Bay vòng tròn trên cao, bắn 3 quả cầu lửa liên tiếp và thả vệt lửa thiêu đốt mặt đất."
        },
        {
          name_vi: "Pha 2 (< 40% HP): Cuồng Nộ Lao Cảm Tử",
          name_en: "Phase 2 (< 40% HP): Enraged Dive Bombs",
          desc_vi: "Tốc độ bay tăng 50%, lao thẳng xuống đất tạo sóng chấn động lửa AOE bán kính 8 block."
        }
      ],
      attacks: [
        "🔥 Solar Fireball (Sát thương Hỏa tầm xa)",
        "⚡ Diving Shockwave (Sát thương Vật lý 16 Tim + Hất tung)",
        "☄️ Burning Trail (Thiêu đốt 5 Tim/giây)"
      ],
      immunities_vi: "Kháng 100% sát thương Lửa & Dung nham; Giảm 30% sát thương cận chiến khi đang bay.",
      recommended_gear_vi: "Giáp Sắt cường hóa Kháng Lửa + Cung Tên / Nỏ bắn tầm xa + 2 Bình Thuốc Kháng Lửa (Fire Resistance)."
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
      summon_vi: "Đánh thức trong phòng trùm hầm ngục Đồng",
      drops: ["Bronze Dungeon Key (100%)", "Hammer of Kingbdogz (33%)", "Neptune Armor Piece (33%)", "Valkyrie Cape (33%)"],
      drops_vi: ["Chìa khóa Hầm ngục Đồng (100%)", "Búa Thần Kingbdogz (33%)", "Mảnh Giáp Neptune (33%)", "Áo Choàng Valkyrie (33%)"],
      tips: "ONLY takes damage from Pickaxes! Switches from blue (slow) to red (fast enraged).",
      tips_vi: "CHỈ nhận sát thương từ Cuốc (Pickaxe)! Đổi màu từ xanh (chậm) sang đỏ (cuồng nộ siêu tốc).",
      phases: [
        {
          name_vi: "Pha Xanh Lam (> 50% HP): Phòng Thủ Chậm",
          name_en: "Blue Form (> 50% HP): Slow Ramming",
          desc_vi: "Mắt xanh, di chuyển thẳng theo trục 4 hướng, tốc độ chậm. Dễ dàng nhảy né và dùng Cuốc chém vào thân."
        },
        {
          name_vi: "Pha Đỏ Cuồng Nộ (< 50% HP): Húc Siêu Tốc & Đập Đất",
          name_en: "Red Form (< 50% HP): High-Speed Charge",
          desc_vi: "Mắt đỏ rực, tốc độ húc tăng gấp 3 lần, đâm liên tục vào tường làm rơi đá sập gây sát thương đè."
        }
      ],
      attacks: [
        "🔨 Heavy Collision (Húc trực diện 14 Tim + Đẩy lùi cực mạnh)",
        "💥 Cave In Rocks (Đá trần rơi gây 6 Tim)"
      ],
      immunities_vi: "MIỄN NHIỄM 100% kiếm, rìu, cung tên và phép thuật! CHỈ NHẬN SÁT THƯƠNG TỪ CUỐC (Pickaxes).",
      recommended_gear_vi: "Cuốc Kim Cương hoặc Cuốc Zanite (Zanite Pickaxe càng hỏng đánh càng đau) + Khiên chắn."
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
      drops: ["Silver Dungeon Key (100%)", "Valkyrie Lance (50%)", "Valkyrie Armor Set Piece (50%)"],
      drops_vi: ["Chìa khóa Hầm ngục Bạc (100%)", "Thương Valkyrie (50%)", "Mảnh Giáp Valkyrie (50%)"],
      tips: "Teleports frequently and strikes with lightning thrusts.",
      tips_vi: "Thường xuyên dịch chuyển tức thời và tung đòn đâm sét liên hoàn.",
      phases: [
        {
          name_vi: "Pha 1: Dịch Chuyển & Phóng Tia Sét",
          name_en: "Phase 1: Teleport & Lightning",
          desc_vi: "Dịch chuyển sau lưng người chơi mỗi 4 giây và tung 3 nhát đâm thương tầm xa."
        },
        {
          name_vi: "Pha 2 (< 30% HP): Triệu Hồi Hộ Vệ Valkyrie",
          name_en: "Phase 2 (< 30% HP): Guardian Summoning",
          desc_vi: "Bật khiên bất tử tạm thời và triệu hồi 4 nữ chiến binh Valkyrie phụ trợ."
        }
      ],
      attacks: [
        "⚡ Lightning Lance Thrust (Đâm thương giật sét 12 Tim)",
        "🌀 Teleport Ambush (Dịch chuyển tập kích sau lưng)"
      ],
      immunities_vi: "Kháng giật điện và hất tung.",
      recommended_gear_vi: "Giáp Neptune hoặc Kim Cương + Kiếm tốc độ đánh nhanh + Thuốc Tăng Tốc (Speed II)."
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
      drops: ["Dead King Helm (100%)", "Blood Staff (40%)", "Legendary Ink & Runes", "12000 XP"],
      drops_vi: ["Mũ Vua Bất Tử (100%)", "Trượng Huyết Ma (40%)", "Mực & Cổ Tự Huyền Thoại", "12000 Điểm EXP"],
      tips: "Has 2 phases. Summons hordes of undead mages and casts high-tier blood spells.",
      tips_vi: "Có 2 giai đoạn. Triệu hồi quái phép liên tục và thi triển huyết phép diện rộng.",
      phases: [
        {
          name_vi: "Pha 1 (1800 HP): Pháp Sư Huyết Ma Tối Cao",
          name_en: "Phase 1 (1800 HP): Blood Archmage",
          desc_vi: "Sử dụng gậy phép thi triển Blood Slash, Huyết Cầu và tạo vòng xoáy hút máu."
        },
        {
          name_vi: "Pha 2 (Hồi sinh 1800 HP): Cận Chiến Cuồng Bạo",
          name_en: "Phase 2 (Revives 1800 HP): Berserk Undead King",
          desc_vi: "Hồi sinh toàn bộ máu, rút đại kiếm bóng tối chém liên hoàn và triệu hồi 8 lính xác sống."
        }
      ],
      attacks: [
        "🩸 Blood Slash Barrage (3 nhát chém huyết kiếm 18 Tim)",
        "💀 Summon Undead Legion (Triệu hồi 8 lính xương phép)",
        "🌀 Life Drain Nova (Vòng xoáy hút máu hồi phục bản thân)"
      ],
      immunities_vi: "Miễn nhiễm sát thương Độc tố & Làm mù; Kháng 50% sát thương Huyết phép.",
      recommended_gear_vi: "Giáp Netherite hoặc Pyromancer + Cổ Tự Holy/Fire (Thánh/Lửa gây thêm 150% dmg vào boss)."
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
      drops: ["Monstrous Horn (100%)", "Infernal Forge Hammer (50%)", "Netherite Scrap x12", "Monstrous Armor Plate"],
      drops_vi: ["Sừng Quái Thú (100%)", "Búa Luyện Lửa Infernal (50%)", "Mảnh Netherite x12", "Tấm Giáp Quái Thú"],
      tips: "Massive ground slams. Jump or combat roll before impact. Avoid lava pools.",
      tips_vi: "Đòn đập đất cực mạnh. Nhảy lên hoặc lăn lộn (Combat Roll) né chấn động và dung nham.",
      phases: [
        {
          name_vi: "Pha 1: Quái Thú Luyện Kim Vung Búa",
          name_en: "Phase 1: Heavy Hammer Swings",
          desc_vi: "Vung búa khổng lồ đập đất tạo sóng xung kích và phun dung nham ra xung quanh."
        },
        {
          name_vi: "Pha 2 (< 50% HP): Nung Đỏ Toàn Thân & Hút Dung Nham",
          name_en: "Phase 2 (< 50% HP): Molten Rage & Siphon",
          desc_vi: "Thân quái thú rực sáng, hút dung nham từ sàn đấu để hồi máu và phóng tia laser hỏa ngục."
        }
      ],
      attacks: [
        "🔨 Earth Shatter Slam (Đập đất 28 Tim + Phá hủy địa hình)",
        "🌋 Lava Geyser (Cột dung nham phun từ dưới chân)",
        "🔥 Molten Charge (Lao thẳng húc nát người chơi)"
      ],
      immunities_vi: "Miễn nhiễm 100% Lửa, Kháng 70% sát thương Đẩy lùi.",
      recommended_gear_vi: "Giáp Dragonsteel Băng hoặc Giáp Fiery Boots có khảm ngọc + Vũ khí Celestisynth + Thuốc Kháng Lửa."
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
      drops: ["Incinerator Greatsword (100%)", "Ignitium Ingot x8 (100%)", "Profane Core (100%)", "Ignis Trophy"],
      drops_vi: ["Đại đao Incinerator (100%)", "Thỏi Kim Loại Ignitium x8 (100%)", "Lõi Bất Tịnh (100%)", "Cúp Ignis"],
      tips: "Extreme fire damage and armor penetration. Equip Fire Dragonsteel or Warden Armor.",
      tips_vi: "Sát thương thiêu đốt và xuyên giáp cực nặng. Cần trang bị giáp Warden hoặc Fire Dragonsteel.",
      phases: [
        {
          name_vi: "Pha 1 (1.000.000 - 500.000 HP): Đại Kiếm Incinerator",
          name_en: "Phase 1: Greatsword Slashes & Fire Waves",
          desc_vi: "Vung đại kiếm rực lửa chém ra các đường sóng lửa xuyên thấu mọi loại khiên chắn."
        },
        {
          name_vi: "Pha 2 (500.000 - 100.000 HP): Hỏa Ngục Toàn Phần",
          name_en: "Phase 2: Full Infernal Awakening",
          desc_vi: "Tốc độ chém tăng gấp đôi, nhảy lên không trung bổ nhát chém hủy diệt tạo vụ nổ 20 block."
        },
        {
          name_vi: "Pha 3 (< 100.000 HP): Tận Diệt Tro Tàn",
          name_en: "Phase 3: Ash Cataclysm",
          desc_vi: "Liên tục thiêu đốt 10% Max HP của người chơi mỗi 3 giây nếu không đứng trong vùng bảo hộ nước."
        }
      ],
      attacks: [
        "⚔️ Incinerator Cleave (Chém xuyên giáp 45 Tim)",
        "☄️ Hellfire Storm (Mưa thiên thạch bao phủ toàn bộ đấu trường)",
        "💥 Ground Detonation (Bổ kiếm kích nổ hạt nhân lửa)"
      ],
      immunities_vi: "Miễn nhiễm 100% Lửa, Kháng 90% sát thương Hỏa phép, Giảm 50% sát thương tầm xa.",
      recommended_gear_vi: "Giáp Warden Armor / Apocalyptium Cấp 100 + Vũ khí Băng Hệ + Full 40 Heart Canisters + Eternal Stella."
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
      drops: ["Ascension Halo (100%)", "Apocalyptium Ingot x4", "Seraph Bow", "Apocalypse Core"],
      drops_vi: ["Hào Quang Thăng Hoa (Ascension Halo - 100%)", "Thỏi Apocalyptium x4", "Cung Thiên Sứ", "Lõi Tận Thế"],
      tips: "Hellfire burns 6.66% Max HP. Cap damage per hit at 100. Bring Totems and high regen.",
      tips_vi: "Ngọn lửa địa ngục thiêu 6.66% Máu tối đa. Sát thương nhận vào bị giới hạn 100/hit. Chuẩn bị nhiều Totem.",
      phases: [
        {
          name_vi: "Pha 1: Đôi Cánh Thiên Sứ Rơi",
          name_en: "Phase 1: Seraph Wings & Judgement Bow",
          desc_vi: "Bay lượn trên không xả mưa tên thần thoại và phóng các tia sáng thánh khiết trừng phạt."
        },
        {
          name_vi: "Pha 2 (< 50% HP): Địa Ngục Sa Ngã (Hurt Limit 100 Dmg/Hit)",
          name_en: "Phase 2: Fallen Abyss (Hurt Limit 100/Hit)",
          desc_vi: "Hào quang chuyển sang đen tối, kích hoạt màng bảo hộ giới hạn sát thương nhận vào tối đa 100/hit và gây thiêu đốt 6.66% Max HP."
        }
      ],
      attacks: [
        "🏹 Judgement Arrow Barrage (Mưa tên 100% Xuyên giáp)",
        "🔥 Hellfire Immolation (Thiêu 6.66% Max HP mỗi giây)",
        "⚡ Divine Smite Strike (Sét thánh giáng nát mặt đất)"
      ],
      immunities_vi: "GIỚI HẠN SÁT THƯƠNG NHẬN VÀO TỐI ĐA 100 DMG/HIT. Không thể bị one-shot bởi bất kỳ vũ khí nào!",
      recommended_gear_vi: "Vũ khí tốc độ đánh cực nhanh (Dagger/Rapier) + Giáp hồi máu liên tục + 5+ Totem of Undying."
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
      drops: ["The Judgement (100%)", "Godly Essence (100%)", "Modpack Completion Badge (100%)"],
      drops_vi: ["Thần Khí The Judgement (100%)", "Tinh Chất Thần Thánh (100%)", "Huy Hiệu Phá Đảo (100%)"],
      tips: "The ultimate boss. Requires fully perfected Meta Build with Eternal Stella.",
      tips_vi: "Siêu trùm tối thượng. Bắt buộc có trang bị Meta Build hoàn thiện ép ngọc Eternal Stella.",
      phases: [
        {
          name_vi: "Pha 1 (1.000.000 HP): Sức Mạnh Thần Thú Tiền Sử",
          name_en: "Phase 1: Primal Ancient Roar",
          desc_vi: "Dậm chân tạo sóng địa chấn hất văng người chơi lên độ cao 50 block và gọi đàn Sniffer tiền sử."
        },
        {
          name_vi: "Pha 2 (Dưới 300.000 HP): Thần Phạt Tối Cao",
          name_en: "Phase 2: Divine Retribution",
          desc_vi: "Tỏa ra hào quang vũ trụ, bắn tia laser năng lượng hủy diệt và triệu hồi sấm sét liên hoàn khắp đấu trường."
        }
      ],
      attacks: [
        "🦏 Primal Trample (Đạp đất 60 Tim + Choáng 3s)",
        "🌌 Cosmic Laser Beam (Bắn tia laser vũ trụ 80 Tim/giây)",
        "⚡ Ancient Lightning Storm (Sấm sét cổ đại bao phủ)"
      ],
      immunities_vi: "Kháng 80% mọi loại sát thương nguyên tố; Kháng 100% hiệu ứng khống chế.",
      recommended_gear_vi: "Bộ Giáp Reverium Paladin Cấp 100 Bất Tử Eternal Stella + Đại Đao Solaris/Keres + Full Potions Buff."
    }
  ],

  /* ==========================================================================
     PACKAGE 3: Ore Spawning Y-Levels & Metallurgy Matrix
     ========================================================================== */
  ores: [
    {
      id: "topaz",
      name: "Topaz Ore",
      name_vi: "Quặng Hoàng Ngọc (Topaz)",
      tier: "Tier 0",
      y_level: "Y = 10 đến -32",
      biomes_vi: "Badlands, Rừng Rậm (Jungle), Savanna nóng",
      biomes_en: "Badlands, Jungle, Warm Savanna",
      pickaxe_tier: "Sắt (Iron Pickaxe) trở lên",
      vein_size: "4 - 8 khối mỗi mạch",
      smelting_vi: "Nung trong Lò hoặc đập bằng Cuốc Gia Tài (Fortune) rơi Topaz Gem.",
      uses_vi: "Ghép ngọc Prismatic Jewel, rèn công cụ Topaz tăng tốc độ đào."
    },
    {
      id: "ruby",
      name: "Ruby Ore",
      name_vi: "Quặng Hồng Ngọc (Ruby)",
      tier: "Tier 0",
      y_level: "Y = 15 đến -48",
      biomes_vi: "Nether Wastelands & Hang Scorched Caves (Overworld dưới sa mạc)",
      biomes_en: "Nether Wastelands & Scorched Caves (Overworld under deserts)",
      pickaxe_tier: "Sắt (Iron Pickaxe) trở lên",
      vein_size: "3 - 6 khối mỗi mạch",
      smelting_vi: "Đập bằng Cuốc Gia Tài rơi Ruby Gem.",
      uses_vi: "Ghép Prismatic Jewel, rèn trang bị tăng sát thương chí mạng."
    },
    {
      id: "sapphire",
      name: "Sapphire Ore",
      name_vi: "Quặng Lam Ngọc (Sapphire)",
      tier: "Tier 0",
      y_level: "Y = 40 đến -50",
      biomes_vi: "Vùng tuyết lạnh (Snowy Plains, Taiga, Frozen Ocean)",
      biomes_en: "Cold biomes (Snowy Plains, Taiga, Frozen Ocean)",
      pickaxe_tier: "Sắt (Iron Pickaxe) trở lên",
      vein_size: "4 - 8 khối mỗi mạch",
      smelting_vi: "Đập bằng Cuốc rơi Sapphire Gem.",
      uses_vi: "Ghép Prismatic Jewel, chế tạo vũ khí làm chậm mục tiêu."
    },
    {
      id: "onyx",
      name: "Onyx Ore",
      name_vi: "Quặng Hắc Ngọc (Onyx)",
      tier: "Tier 0",
      y_level: "Y = 10 đến 60 (Outer End Islands)",
      biomes_vi: "Các đảo The End ngoài không gian",
      biomes_en: "The End Outer Islands",
      pickaxe_tier: "Kim Cương (Diamond Pickaxe) trở lên",
      vein_size: "2 - 5 khối mỗi mạch",
      smelting_vi: "Đập bằng Cuốc rơi Onyx Gem.",
      uses_vi: "Ghép Prismatic Jewel, chế tạo trang bị tàng hình và dịch chuyển."
    },
    {
      id: "iridescent_shard",
      name: "Iridescent Shard",
      name_vi: "Mảnh Tinh Thể Cầu Vồng (Iridescent)",
      tier: "Tier 0",
      y_level: "Y = -40 đến -64 (Deepslate layer)",
      biomes_vi: "Tầng đá phiến sâu ngầm toàn thế giới Overworld",
      biomes_en: "Deepslate layer across Overworld underground",
      pickaxe_tier: "Kim Cương (Diamond Pickaxe) trở lên",
      vein_size: "2 - 4 khối mỗi mạch",
      smelting_vi: "Khai thác trực tiếp từ khối quặng lấp lánh.",
      uses_vi: "Nguyên liệu then chốt ghép viên ngọc Prismatic Jewel."
    },
    {
      id: "dimlite",
      name: "Dimlite Ore",
      name_vi: "Quặng Ánh Mờ (Dimlite)",
      tier: "Tier 1",
      y_level: "Y = -20 đến -58",
      biomes_vi: "Hang động ngầm sâu Overworld",
      biomes_en: "Deep Overworld Caves",
      pickaxe_tier: "Netherite Pickaxe",
      vein_size: "3 - 5 khối",
      smelting_vi: "Nung thỏi kết hợp Dimlite Smithing Template rơi từ Vua Lùn Gob.",
      uses_vi: "Rèn bộ giáp Dimlite Armor tăng tốc độ chạy và né đòn."
    },
    {
      id: "cosmilite",
      name: "Cosmilite Ore",
      name_vi: "Quặng Vũ Trụ (Cosmilite)",
      tier: "Tier 1",
      y_level: "Y = 120 đến 256 (Đỉnh núi cao / Tầng mây)",
      biomes_vi: "Đỉnh núi tuyết cao ngất Overworld & The Aether",
      biomes_en: "High Mountain Peaks & The Aether",
      pickaxe_tier: "Netherite Pickaxe",
      vein_size: "2 - 4 khối",
      smelting_vi: "Nung kết hợp Cosmilite Template từ Super Sniffer.",
      uses_vi: "Rèn vũ khí tầm xa và khiên chắn phản lực."
    },
    {
      id: "iridium",
      name: "Iridium Ore",
      name_vi: "Quặng Bạch Kim Cổ Đại (Iridium)",
      tier: "Tier 1.5",
      y_level: "Y = -50 đến -64",
      biomes_vi: "Gần lõi đá nền Bedrock Overworld",
      biomes_en: "Near Bedrock layer in Overworld",
      pickaxe_tier: "Dimlite / Cosmilite Pickaxe",
      vein_size: "1 - 3 khối (Cực hiếm)",
      smelting_vi: "Luyện thỏi trong Lò Luyện Kim Blast Furnace.",
      uses_vi: "Rèn vũ khí Tier 1.5 để đủ sức khiêu chiến Trial Guardian."
    },
    {
      id: "profanum",
      name: "Profanum Ore",
      name_vi: "Quặng Bất Tịnh (Profanum)",
      tier: "Tier 2.5",
      y_level: "Nether Y = 10 đến 35 (Gần hồ dung nham sâu)",
      biomes_vi: "Vùng tro tàn Basalt Deltas & Soul Sand Valley trong Nether",
      biomes_en: "Basalt Deltas & Soul Sand Valley in Nether",
      pickaxe_tier: "Iridium Pickaxe",
      vein_size: "2 - 4 khối",
      smelting_vi: "Luyện thỏi Profanum Ingot để rèn Rìu Mặt Trời Rhitta.",
      uses_vi: "Mở khóa khiêu chiến Hội Pháp Sư Bóng Tối Shadow Wizards."
    },
    {
      id: "reverium",
      name: "Reverium & Nyxium Ore",
      name_vi: "Quặng Thánh Reverium & Quặng Đêm Nyxium",
      tier: "Tier 4 (Endgame)",
      y_level: "The End Void Islands (Y = 20 đến 70)",
      biomes_vi: "Các hòn đảo ngoài rìa chiều không gian The End",
      biomes_en: "Outer End Dimension Islands",
      pickaxe_tier: "Profanum / Dreadsteel Pickaxe",
      vein_size: "1 - 2 khối",
      smelting_vi: "Kết hợp Antiprism từ Boss Archmage Gundalf.",
      uses_vi: "Rèn Giáp Reverium Paladin & Giáp Exodium Warlock tối thượng."
    }
  ],

  /* Metallurgy & Composite Materials */
  alloys: [
    {
      name: "Damascus Steel Ingot",
      name_vi: "Thép Damascus (Damascus Steel)",
      tier: "Composite Tier I",
      recipe: "1x Iron Ingot + 1x Coal + 1x Raw Copper (Alloy Smelter)",
      uses_vi: "Rèn vũ khí cận chiến có độ bền gấp đôi vũ khí sắt vanilla."
    },
    {
      name: "Dungeon Steel Ingot",
      name_vi: "Thép Hầm Ngục (Dungeon Steel)",
      tier: "Composite Tier II",
      recipe: "1x Damascus Steel + 2x Gold Ingot + 1x Lapis Lazuli",
      uses_vi: "Rèn vũ khí đĩa xoay Disc Weapons chém xuyên giáp quái vật hầm ngục."
    },
    {
      name: "Etherite Ingot",
      name_vi: "Thỏi Tinh Tú Etherite",
      tier: "Composite Tier III",
      recipe: "1x Netherite Ingot + 2x Zanite Gem + 2x Resonarium Ingot",
      uses_vi: "Chế tạo Totem Bất Tử Primitive Tenacity và Trượng Không Gian."
    },
    {
      name: "Dragonsteel (Fire/Ice/Lightning)",
      name_vi: "Thép Rồng 3 Hệ (Dragonsteel)",
      tier: "Mythical Alloy",
      recipe: "Dragon Forge (Thổi hơi thở rồng) + Iron Ingot + Dragon Blood",
      uses_vi: "Rèn vũ khí và bộ giáp có sức chống chịu nguyên tố cao nhất trước khi vào Endgame."
    },
    {
      name: "Dreadsteel Ingot",
      name_vi: "Thép Hủy Diệt Dreadsteel",
      tier: "Supreme Alloy",
      recipe: "1x Fire Dragonsteel + 1x Ice Dragonsteel + 1x Lightning Dragonsteel + 1x Dread Shard",
      uses_vi: "Hợp nhất 3 chủng rồng rèn nên Đại Lưỡi Hái Dreadsteel Scythe."
    },
    {
      name: "Apocalyptium Ingot",
      name_vi: "Thỏi Thiên Sứ Apocalyptium",
      tier: "Celestial Tier 5",
      recipe: "1x Ascension Halo (từ Boss Apollyon) + 4x Netherite + 4x Deorum Ingot",
      uses_vi: "Rèn bộ giáp Thiên Sứ kháng 6.66% ngọn lửa địa ngục và cung Seraph Bow."
    }
  ],

  /* Existing Items & Dimensions & Classes... */
  items: [
    {
      id: "fire_rune",
      name: "Fire Rune",
      name_vi: "Cổ Tự Hỏa Ma (Fire Rune)",
      icon: "images/items/fire_rune.png",
      mod: "Iron's Spells 'n Spellbooks",
      stage: "Early",
      classTags: ["Mage", "Fire Mage", "Battlemage"],
      category: "Magic Material",
      recipe: "1x Blank Rune + 1x Blaze Rod (Crafting Table)",
      effects_vi: "Nguyên liệu cốt lõi để rèn Sách phép Lửa, Cuộn phép Hỏa cầu và Bộ giáp Pyromancer Armor.",
      effects_en: "Core material for crafting Fire Spellbooks, Fireball scrolls, and Pyromancer Armor.",
      source_type: "Crafting / Nether Fortress",
      source_url: "dimensions.html#dim-nether",
      source_location_vi: "Săn Blaze lấy Blaze Rod tại Nether Fortress, ghép tại Bàn chế tạo.",
      source_location_en: "Harvest Blaze Rods from Nether Fortress Blazes, craft at Crafting Table."
    },
    {
      id: "pyromancer_chestplate",
      name: "Pyromancer Chestplate",
      name_vi: "Áo Choàng Hỏa Thuật Sư (Pyromancer)",
      icon: "images/items/pyromancer_chestplate.png",
      mod: "Iron's Spells 'n Spellbooks",
      stage: "Early",
      classTags: ["Mage", "Fire Mage"],
      category: "Armor",
      recipe: "1x Iron Chestplate + 4x Arcane Cloth + 3x Fire Rune",
      effects_vi: "+5% Sát thương Hỏa phép, +50 Mana tối đa, Kháng thiêu đốt 25%.",
      effects_en: "+5% Fire Spell Power, +50 Max Mana, 25% Fire Resistance.",
      source_type: "Crafting / Inscription",
      source_url: "magic.html",
      source_location_vi: "Chế tạo tại Bàn chế tạo sau khi có Arcane Cloth và Fire Rune.",
      source_location_en: "Craft at Crafting Table using Arcane Cloth and Fire Runes."
    },
    {
      id: "scroll_forge",
      name: "Scroll Forge",
      name_vi: "Lò Rèn Cuộn Phép (Scroll Forge)",
      icon: "images/items/scroll_forge.png",
      mod: "Iron's Spells 'n Spellbooks",
      stage: "Early",
      classTags: ["Mage", "All Classes"],
      category: "Workstation",
      recipe: "4x Iron Ingot + 2x Stone + 1x Blank Scroll + 1x Arcane Essence",
      effects_vi: "Bàn tạo ra mọi loại Cuộn phép (Scrolls) từ Hỏa Cầu (Fireball) đến Bão Sét và Mưa Thiên Thạch.",
      effects_en: "Crafts all spell scrolls from Fireball to Chain Lightning and Meteor Rain.",
      source_type: "Crafting",
      source_url: "magic.html",
      source_location_vi: "Bàn chế tạo cơ bản từ những phút đầu vào game.",
      source_location_en: "Basic workstation craftable from early resources on Day 1."
    },
    {
      id: "fireblossom_rapier",
      name: "Fireblossom Rapier",
      name_vi: "Kiếm Liễu Hỏa Liên (Fireblossom Rapier)",
      icon: "images/items/fireblossom_rapier.png",
      mod: "Hazen 'n Stuff",
      stage: "Early",
      classTags: ["Mage", "Fire Mage", "Battlemage"],
      category: "Spell Weapon",
      recipe: "1x Iron Rapier + 2x Fire Rune + 1x Fireblossom",
      effects_vi: "Tích hợp sẵn chiêu thức Flaming Strike Cấp 5; mỗi nhát đâm kích nổ ngọn lửa thiêu rụi mục tiêu.",
      effects_en: "Pre-imbued with Flaming Strike Lv5; thrusting detonates fiery explosions on impact.",
      source_type: "Crafting / Overworld Plants",
      source_url: "creatures.html",
      source_location_vi: "Thu hoạch hoa Fireblossom tại vùng đồi nóng kết hợp Fire Rune.",
      source_location_en: "Harvest Fireblossoms in warm biomes combined with Fire Runes."
    },
    {
      id: "rage_glove",
      name: "Rage Glove",
      name_vi: "Găng Tay Cuồng Nộ (Rage Glove)",
      icon: "images/items/rage_glove.png",
      mod: "Relics",
      stage: "Early",
      classTags: ["Warrior", "Berserker"],
      category: "Relic / Curio",
      recipe: "Raid Dungeons / Mineshafts Treasure Chests",
      effects_vi: "+15% Tốc độ đánh, +2 Sát thương cận chiến, càng đánh liên tiếp tốc độ chém càng tăng.",
      effects_en: "+15% Attack Speed, +2 Melee DMG, successive hits ramp up attack speed.",
      source_type: "Dungeon Chest",
      source_url: "utilities.html",
      source_location_vi: "Tìm thấy trong rương hầm mỏ bỏ hoang Mineshaft hoặc pháo đài Outpost.",
      source_location_en: "Found inside Mineshaft minecarts and Pillager Outpost chests."
    },
    {
      id: "solaris",
      name: "Solaris",
      name_vi: "Đại Đao Thái Dương Solaris",
      icon: "images/items/solaris.png",
      mod: "Celestisynth",
      stage: "Late",
      classTags: ["Warrior", "Berserker"],
      category: "Mythical Weapon",
      recipe: "Starlit Factory + Heated Celestial Core + Sunbird Feather + Netherite Ingot",
      effects_vi: "Kỹ năng [Solar Flare]: Chém liên hoàn tạo bão lửa thái dương quét sạch quái vật diện rộng.",
      effects_en: "[Solar Flare]: Rapid combo cleaves unleashing solar shockwaves in wide area.",
      source_type: "Starlit Factory Crafting",
      source_url: "magic.html",
      source_location_vi: "Rèn tại trạm Starlit Factory bằng Lông chim Umvuthi và Lõi Thiên Thể.",
      source_location_en: "Crafted at Starlit Factory with Sunbird Feathers and Celestial Core."
    },
    {
      id: "hammer_of_kingbdogz",
      name: "Hammer of Kingbdogz",
      name_vi: "Búa Thần Sấm Kingbdogz",
      icon: "images/items/hammer_of_kingbdogz.png",
      mod: "The Aether",
      stage: "Mid",
      classTags: ["Paladin", "Warrior"],
      category: "Holy Weapon",
      recipe: "Dropped from Bronze Dungeon Boss Slider (The Aether)",
      effects_vi: "Phóng sét giật lan và tạo sóng địa chấn đánh bật mọi kẻ địch khi nện xuống đất.",
      effects_en: "Calls down chain lightning and seismic shockwaves when slammed into the ground.",
      source_type: "Boss Drop: Slider",
      source_url: "bosses.html#boss-slider",
      source_location_vi: "Tiêu diệt trùm Slider trong Hầm ngục Đồng (The Aether).",
      source_location_en: "Defeat Boss Slider in Bronze Dungeon (The Aether)."
    },
    {
      id: "heart_amulet",
      name: "Heart Amulet",
      name_vi: "Dây Chuyền Trái Tim (Heart Amulet)",
      icon: "images/items/heart_amulet.png",
      mod: "Baubley Heart Canisters",
      stage: "Early",
      classTags: ["Paladin", "All Classes"],
      category: "Relic / Accessory",
      recipe: "4x Gold Ingot + 4x Diamond + 1x Heart Canister (Crafting Table)",
      effects_vi: "Chứa tối đa 40 hộp Heart Canisters (Đỏ, Vàng, Lục, Lam) tăng thêm đến +80 Máu Tối Đa vĩnh viễn!",
      effects_en: "Holds up to 40 Heart Canisters (Red, Yellow, Green, Blue) for up to +80 Max HP!",
      source_type: "Crafting",
      source_url: "utilities.html",
      source_location_vi: "Chế tạo sớm tại Bàn chế tạo và đeo vào ô Curios Amulet.",
      source_location_en: "Craft early at Crafting Table and equip into Curios Amulet slot."
    },
    {
      id: "phoenix_bow",
      name: "Phoenix Bow",
      name_vi: "Cung Thần Phượng Hoàng (Phoenix Bow)",
      icon: "images/items/phoenix_bow.png",
      mod: "The Aether",
      stage: "Mid",
      classTags: ["Ranger", "Sniper"],
      category: "Ranged Weapon",
      recipe: "Dropped from Gold Dungeon Boss Sun Spirit (The Aether)",
      effects_vi: "Tất cả mũi tên bắn ra tự động chuyển hóa thành Tên Lửa Phượng Hoàng thiêu đốt cực hạn.",
      effects_en: "All fired arrows automatically transform into flaming Phoenix Blaze arrows.",
      source_type: "Boss Drop: Sun Spirit",
      source_url: "bosses.html#boss-sun_spirit",
      source_location_vi: "Tiêu diệt trùm Sun Spirit tại Đền Vàng Thiên Giới Aether.",
      source_location_en: "Defeat Boss Sun Spirit in Gold Dungeon (The Aether)."
    },
    {
      id: "soul_elytra",
      name: "Soul Elytra",
      name_vi: "Cánh Linh Hồn (Soul Elytra)",
      icon: "images/items/soul_elytra.png",
      mod: "Deeper and Darker",
      stage: "Late",
      classTags: ["Ranger", "All Classes"],
      category: "Armor / Flight",
      recipe: "1x Elytra + 4x Soul Dust + 2x Resonarium Ingot (The Otherside)",
      effects_vi: "+3 Điểm giáp, tự động kích hoạt lực đẩy phản lực mỗi 30s bay lượn vô hạn không cần Pháo hoa.",
      effects_en: "+3 Armor, auto-boosts propulsion every 30s for infinite flight without fireworks.",
      source_type: "Crafting / The Otherside",
      source_url: "dimensions.html#dim-otherside",
      source_location_vi: "Khai thác thỏi Resonarium trong cõi âm The Otherside kết hợp cánh Elytra.",
      source_location_en: "Mine Resonarium in The Otherside dimension and upgrade Elytra."
    },
    {
      id: "eternal_stella",
      name: "Eternal Stella",
      name_vi: "Bảo Vật Bất Tử Eternal Stella",
      icon: "images/items/eternal_stella.png",
      mod: "Forbidden and Arcanus",
      stage: "Late",
      classTags: ["All Classes", "Meta Build"],
      category: "Godly Artifact",
      recipe: "Forged in Hephaestus Forge: 1x Stellarite + 3x Xpetrified Orbs + 2000 Aureal + 10 Souls",
      effects_vi: "Khi ép vào Đe với bất kỳ trang bị nào: Hồi phục 100% độ bền và nhận dòng thuộc tính INDESTRUCTIBLE (Không bao giờ hỏng).",
      effects_en: "When applied in Anvil: Restores 100% durability and grants permanent INDESTRUCTIBLE trait.",
      source_type: "Hephaestus Forge Ritual",
      source_url: "magic.html",
      source_location_vi: "Nạp 4 nguồn năng lượng vào Lò rèn Hephaestus Forge đa khối để đúc ngọc.",
      source_location_en: "Feed 4 energy fuels into Hephaestus Forge multiblock to forge."
    },
    {
      id: "the_judgement",
      name: "The Judgement",
      name_vi: "Thần Khí The Judgement",
      icon: "images/items/the_judgement.png",
      mod: "Terramity",
      stage: "Endgame",
      classTags: ["All Classes", "Supreme Trophy"],
      category: "Supreme Relic",
      recipe: "Dropped 100% by Super-Boss Ultra Sniffer (1,000,000 HP)",
      effects_vi: "Vật phẩm minh chứng bạn đã chinh phục hoàn toàn Modpack Terramity Awakened!",
      effects_en: "Supreme relic proving total conquest of the Terramity Awakened modpack!",
      source_type: "Super-Boss: Ultra Sniffer",
      source_url: "bosses.html#boss-ultra_sniffer",
      source_location_vi: "Đánh bại Chúa Tể Ultra Sniffer 1.000.000 HP tại Đấu trường Vô Cực.",
      source_location_en: "Slay the Supreme Ultra Sniffer (1,000,000 HP) in the Endgame Arena."
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
