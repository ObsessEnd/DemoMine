const CREATURES_DATABASE = [
  {
    "name": "Magnetron",
    "type": "Boss / Mini-boss",
    "biome": "alexscaves:magnetic_caves",
    "drops": "alexscaves:heart_of_iron",
    "notes": "Boss từ tính, điều khiển kim loại và Neodymium."
  },
  {
    "name": "Boundroid",
    "type": "Quái vật thường",
    "biome": "alexscaves:magnetic_caves",
    "drops": "alexscaves:heavyweight",
    "notes": "Quái vật từ trường cơ khí."
  },
  {
    "name": "Tremorsaurus / Dinosaurs",
    "type": "Quái vật lớn / Mini-boss",
    "biome": "alexscaves:primordial_caves",
    "drops": "alexscaves:heavy_bone, Trứng khủng long",
    "notes": "Khủng long bạo chúa tiền sử hung dữ, sát thương cắn cực lớn."
  },
  {
    "name": "Underzealot",
    "type": "Quái vật giáo phái",
    "biome": "alexscaves:forlorn_hollows",
    "drops": "alexscaves:occult_gem, Hiến tế",
    "notes": "Tộc người chuột chũi thờ phụng bóng tối, thực hiện nghi lễ hiến tế."
  },
  {
    "name": "Corrodent",
    "type": "Quái vật",
    "biome": "alexscaves:forlorn_hollows",
    "drops": "alexscaves:corrodent_teeth",
    "notes": "Dùng răng để chế tạo Burrowing Arrow phá block."
  },
  {
    "name": "Gammaroach",
    "type": "Quái vật đột biến",
    "biome": "alexscaves:toxic_caves",
    "drops": "Đột biến phóng xạ",
    "notes": "Gián phóng xạ khổng lồ, có thể thuần phục/cho ăn bằng Spelunkie."
  },
  {
    "name": "Licowitch",
    "type": "Boss / Phù thủy",
    "biome": "alexscaves:candy_cavity (Licowitch Tower)",
    "drops": "alexscaves:radiant_essence",
    "notes": "Trùm tháp kẹo Licorice, nguồn cung cấp Tinh chất Rực rỡ chế tạo Vạc Chuyển Đổi Sinh Thái."
  },
  {
    "name": "Gingerbread Man",
    "type": "Quái vật / NPC",
    "biome": "alexscaves:candy_cavity (Gingerbread Town)",
    "drops": "alexscaves:gingerbread_crumbs",
    "notes": "Người bánh gừng trong thị trấn bánh kẹo."
  },
  {
    "name": "Mine Guardian",
    "type": "Quái vật biển sâu",
    "biome": "alexscaves:abyssal_chasm",
    "drops": "alexscaves:depth_charge",
    "notes": "Guardian mang thủy lôi phát nổ dưới đáy vực thẳm."
  },
  {
    "name": "Deep Ones",
    "type": "Tộc người biển sâu",
    "biome": "alexscaves:abyssal_chasm",
    "drops": "Giao dịch ngọc trai, phép thuật biển",
    "notes": "Tộc người dưới đáy biển sâu, có thể giao dịch và trở thành đồng minh."
  },
  {
    "name": "Shape: Default\n- Subtitle: Defeat a Magnetron\n- Dependencies: 79131E308CAC0660\n- Yêu cầu: Thu thập alexscaves:heart_of_iron (rơi từ trùm Magnetron)\n- Boss/Mob: Magnetron (Boss)\n- Phần thưởng: 20 XP, 1x Coin\n\n##### 7. A Magnetic Defender\n- ID: 4749EBE31B7C9FA1",
    "type": "Shape: Default\n- Subtitle: A Magnetic Defender\n- Dependencies: 4A63A3FBD4792738\n- Yêu cầu: Sở hữu alexscaves:resistor_shield (Khiên điện trở từ tính)\n- Phần thưởng: 1x Nam châm đỏ (alexscaves:scarlet_magnet), 10 XP, 1x Coin\n\n##### 8. Mind Over Magnet\n- ID: 7E05A4F64F9A9EFD",
    "biome": "Shape: Default\n- Subtitle: Slay a Creature with the Galena Gauntlet from over 20 Blocks Away\n- Dependencies: 13568C79A039E88D, 4749EBE31B7C9FA1\n- Yêu cầu: Hoàn thành Advancement alexscaves:alexscaves/galena_gauntlet_challenge (Hạ gục quái vật bằng Găng tay Galena từ khoảng cách trên 20 khối)\n- Phần thưởng: 1x Phôi rèn Polarity Armor Trim (alexscaves:polarity_armor_trim_smithing_template), 1x Coin\n\n---\n\n#### Nhánh 2: Primordial Caves (Hang Tiền Sử)\n\n##### 9. The Cave that Time Forgot\n- ID: 7996507FE1F8709F",
    "drops": "Shape: Default (Size 1.5)\n- Subtitle: The Cave that Time Forgot\n- Dependencies: 7CCCBC0188A03C32\n- Mô tả: Tìm kiếm quần xã Primordial Caves.\n- Yêu cầu: Khám phá Biome alexscaves:primordial_caves\n- Phần thưởng: 20 XP, 1x Coin\n\n##### 10. Re-Extinct\n- ID: 1D86377C62795FC9",
    "notes": "Shape: Default\n- Subtitle: Slay a Large Dinosaur within the Cave\n- Dependencies: 7996507FE1F8709F\n- Mô tả: Khuyến nghị trang bị đồ mạnh trước khi chiến đấu. Chúng cắn rất đau!\n- Yêu cầu: Đạt Advancement alexscaves:alexscaves/defeat_big_dinosaur (Tiêu diệt khủng long khổng lồ)\n- Boss/Mob: Tremorsaurus / Luxtructosaurus\n- Phần thưởng: 15 XP, 1x Coin\n\n##### 11. Craft an Ominous Catalyst\n- ID: 0A6BFF07EDE10A6E"
  },
  {
    "name": "Shape: Default\n- Subtitle: A primal weapon.\n- Dependencies: 7996507FE1F8709F\n- Yêu cầu: Chế tạo Giáo đá vôi alexscaves:limestone_spear\n- Phần thưởng: 1x Hổ phách tò mò (alexscaves:amber_curiosity), 20 XP, 1x Coin\n\n##### 13. Extinction spear?\n- ID: 3D7335089B69354F",
    "type": "Shape: Default\n- Mô tả: Giáo Tuyệt Chủng - ngọn giáo đã hủy diệt tất cả...\n- Dependencies: 0A6BFF07EDE10A6E, 45C34B8DDA15563F\n- Yêu cầu: Sở hữu Giáo tuyệt chủng alexscaves:extinction_spear\n- Phần thưởng: 20 XP, 1x Coin\n\n##### 14. Even more primal..\n- ID: 428ACDCCDC29708A",
    "biome": "Shape: Default\n- Subtitle: Even more primal..\n- Dependencies: 45C34B8DDA15563F\n- Yêu cầu: Sở hữu Dùi cui nguyên thủy alexscaves:primitive_club\n- Phần thưởng: 40 XP, 1x Coin\n\n---\n\n#### Nhánh 3: Forlorn Hollows (Hang Hư Vô & Bóng Tối)\n\n##### 15. &8&lForlorn Hollows\n- ID: 77161FAA53643F22",
    "drops": "Shape: Gear (Size 1.5)\n- Subtitle: Forlornliest Day of My Life\n- Dependencies: 7CCCBC0188A03C32\n- Mô tả: Tìm kiếm quần xã Forlorn Hollows chìm trong bóng tối vĩnh cửu.\n- Yêu cầu: Khám phá Biome alexscaves:forlorn_hollows\n- Phần thưởng: 100 XP, 1x Coin\n\n##### 16. The Underzealots\n- ID: 04C3320A5EDCBFF1",
    "notes": "Shape: Square\n- Dependencies: 77161FAA53643F22\n- Mô tả: Phát hiện Underzealot - những kẻ tôi tớ hình chuột chũi phục vụ chúa tể bóng tối.\n- Yêu cầu: Đạt Advancement alexscaves:alexscaves/discover_underzealot\n- Boss/Mob: Underzealot\n- Phần thưởng: 20 XP, 1x Coin\n\n##### 17. The Black Parade\n- ID: 3849A2E20966ED4E"
  },
  {
    "name": "Shape: Square\n- Dependencies: 77161FAA53643F22\n- Mô tả: Chế tạo Mũi tên Đào bới, có khả năng xuyên và phá hủy tới 5 khối block khi bắn bằng cung.\n- Yêu cầu: Sở hữu alexscaves:burrowing_arrow\n- Phần thưởng: 1x Răng Corrodent (alexscaves:corrodent_teeth), 15 XP, 1x Coin\n\n##### 19. You are under my control now!\n- ID: 4E8CC910E436EAF7",
    "type": "Shape: Square\n- Subtitle: You are under my control now!\n- Dependencies: 6E23D9E092DE5A10\n- Mô tả: Totem of Possession có thể tạm thời khống chế tâm trí của một quái vật bạn chọn.\n- Yêu cầu: Sở hữu alexscaves:totem_of_possession\n- Phần thưởng: 1x Tơ bóng tối (alexscaves:shadow_silk), 15 XP, 1x Coin\n\n##### 20. &l&7Dreadbow\n- ID: 55FDC375B83CB18A",
    "biome": "Shape: Gear\n- Subtitle: Blot Out the Sun\n- Dependencies: 4E8CC910E436EAF7\n- Mô tả: Dreadbow là cây cung cực mạnh có thể bắn ra một cơn mưa tên cùng lúc!\n- Yêu cầu: Sở hữu Cung Dreadbow alexscaves:dreadbow\n- Phần thưởng: 5 Cấp độ kinh nghiệm (XP Levels), 1x Coin\n\n##### 21. Darkness Incarnate\n- ID: 198DA29A3677241D",
    "drops": "Shape: RSquare\n- Subtitle: [Click to read]\n- Dependencies: 77161FAA53643F22\n- Mô tả: Chế tạo Mũ trùm và Áo choàng bóng tối để tạm thời hóa thân thành Hiện Thân Bóng Tối (Darkness Incarnate).\n- Yêu cầu: Thu thập Bóng tối thuần khiết alexscaves:pure_darkness\n- Phần thưởng: 27 XP, 1x Coin\n\n##### 22. &7&lThe Hood of Darkness\n- ID: 0EFC5FD9DFF010A0",
    "notes": "Dependencies: 198DA29A3677241D\n- Yêu cầu: Chế tạo alexscaves:hood_of_darkness\n- Phần thưởng: 1x alexscaves:pure_darkness, 20 XP, 1x Coin\n\n##### 23. &l&7The Cloak of Darkness\n- ID: 66E61FBA03E135FA"
  },
  {
    "name": "Shape: Square (Size 1.5)\n- Subtitle: Radiation Vibe\n- Dependencies: 7CCCBC0188A03C32\n- Mô tả: Tìm kiếm quần xã hang độc hại và nhiễm phóng xạ Toxic Caves.\n- Yêu cầu: Khám phá Biome alexscaves:toxic_caves\n- Phần thưởng: 100 XP, 1x Coin\n\n##### 25. Tank a acid bath\n- ID: 70D6BA3908F691A8",
    "type": "Shape: Default\n- Subtitle: Enter Acid While Wearing Armour\n- Dependencies: 12251DF6B529B713\n- Yêu cầu: Đạt Advancement alexscaves:alexscaves/enter_acid_with_armor (Nhảy vào hồ axit khi đang mặc giáp bảo hộ)\n- Phần thưởng: 1x Giày Hazmat (alexscaves:hazmat_boots), 10 XP, 1x Coin\n\n##### 26. Sulfur Dust\n- ID: 635E15DCD1640A07",
    "biome": "Dependencies: 12251DF6B529B713\n- Subtitle: Can be obtained from sulfur clusts.\n- Yêu cầu: Thu thập Bụi lưu huỳnh alexscaves:sulfur_dust\n- Phần thưởng: 100 XP, 1x Coin\n\n##### 27. Radon in Geothermal Vents\n- ID: 3F65CB6279E012E2",
    "drops": "Dependencies: 12251DF6B529B713\n- Subtitle: Found in Geothermal Vents\n- Yêu cầu: Thu thập Bình khí Radon alexscaves:radon_bottle\n- Phần thưởng: 1x Quần Hazmat (alexscaves:hazmat_leggings), 5 XP, 1x Coin\n\n##### 28. Toxic goo\n- ID: 7590BEDEE02367A1",
    "notes": "Dependencies: 12251DF6B529B713\n- Subtitle: Obtain Toxic Paste\n- Yêu cầu: Thu thập Chất dính độc hại alexscaves:toxic_paste\n- Phần thưởng: 20 XP, 1x Coin\n\n##### 29. Radioactive Friend\n- ID: 17AFD44F8D796840"
  },
  {
    "name": "Shape: Goldtier\n- Subtitle: Craft a Nuclear Bomb\n- Mô tả: Sức mạnh hủy diệt tối thượng nằm ngay trong tầm tay bạn. BÙMMM...!\n- Dependencies: 12251DF6B529B713\n- Yêu cầu: Chế tạo Bom hạt nhân alexscaves:nuclear_bomb\n- Phần thưởng: 1x Đĩa nhạc Fusion (alexscaves:music_disc_fusion), 1x Coin\n\n##### 31. Raygun\n- ID: 15C843788077D8FE",
    "type": "Dependencies: 12251DF6B529B713\n- Subtitle: A fucking raygun\n- Yêu cầu: Chế tạo Súng bắn tia tử ngoại alexscaves:raygun\n- Phần thưởng: 5 XP Levels, 1x Coin\n\n##### 32. Polymer Plate & Hazmat Armor\n- Quest 1 (ID: 6F437C9CC017AAB9): Polymer Plate (alexscaves:polymer_plate)",
    "biome": "Thưởng: 100 XP, 1x Coin.\n- Quest 2 (ID: 1D12B51CBE25A5AA): Chế tạo trọn bộ giáp Hazmat Suit (Mặt nạ, Giáp thân, Quần, Giày)",
    "drops": "Thưởng: 100 XP, 1x Coin",
    "notes": "Dep: 6F437C9CC017AAB9.\n\n---\n\n#### Nhánh 5: Candy Cavity (Hang Bánh Kẹo & Phù Thủy)\n\n##### 33. Candy Cavity!\n- ID: 67743B706D4142D5"
  },
  {
    "name": "Thưởng: 2x Kẹo gậy, 25 XP, 1x Coin.\n- Quest 2 (ID: 070201A579C266F6): Khám phá Thị trấn Bánh gừng (alexscaves:gingerbread_town)",
    "type": "Thưởng: 15 XP, 1x Coin.\n- Quest 3 (ID: 38B7B1FADE6BC4B0): Tiêu diệt người bánh gừng nhặt Vụn bánh gừng (alexscaves:gingerbread_crumbs)",
    "biome": "Thưởng: 20 XP, 1x Coin.\n- Quest 4 (ID: 339C9BCAD0865692): Spear Mint (alexscaves:frostmint_spear)",
    "drops": "Thưởng: 30 XP, 1x Coin.\n- Bộ Giáp Gingerbread Armor (ID: 33BA359B116305D1, 501771BFDA9735B3, 4AEC431A08AF0C2C, 291B0D3426A1EF98, 74EC39754A1701B9): Chế tạo từng mảnh giáp bánh gừng",
    "notes": "Thưởng: Kẹo kẹo ngọt Supplementaries, XP và Coin.\n\n##### 35. The Dark (Chocolate) Tower & Licowitch\n- Quest 1 (ID: 78D5702DE3FF6CA2): Khám phá Tháp Licowitch (alexscaves:licowitch_tower)"
  },
  {
    "name": "Thưởng: 30 XP, 1x Coin.\n- Quest 3 (ID: 3181A05FFB5D465C): Biome Reactors - Chế tạo Vạc Chuyển Đổi Sinh Thái (alexscaves:conversion_crucible)",
    "type": "Thưởng: 1x Gậy đường (alexscaves:sugar_staff), 20 XP, 1x Coin.\n\n---\n\n#### Nhánh 6: Abyssal Chasm (Vực Thẳm Đại Dương & Deep Ones)\n\n##### 36. Beyond the Ocean\n- ID: 06477537EAFC321F",
    "biome": "Shape: Default (Size 1.5)\n- Subtitle: Beyond the Ocean\n- Dependencies: 7CCCBC0188A03C32\n- Yêu cầu: Khám phá Biome rãnh biển sâu alexscaves:abyssal_chasm\n- Phần thưởng: 20 XP, 1x Coin\n\n##### 37. Mine Guardian\n- ID: 198DEF6C9D3ACCC7",
    "drops": "Dependencies: 06477537EAFC321F\n- Subtitle: Slay an Explosive Foe\n- Yêu cầu: Tiêu diệt 1x alexscaves:mine_guardian\n- Boss/Mob: Mine Guardian\n- Phần thưởng: 10 XP, 1x Coin\n\n##### 38. Powers Of The Deep Ocean!\n- ID: 4A1C1CCA25648B59",
    "notes": "Dependencies: 06477537EAFC321F\n- Mô tả: Thu thập các cổ vật thông qua giao dịch với sinh vật đáy biển:\n  1. Ốc xà cừ ma thuật alexscaves:magic_conch\n  2. Giáo Ortholance alexscaves:ortholance\n  3. Gậy biển sâu alexscaves:sea_staff\n  4. Ngọc nhìn thấu alexscaves:gazing_pearl\n- Phần thưởng: 1x Floater, 1x Tide Armor Trim, 10 XP, 1x Coin\n\n##### 39. Ngọc trai, Bàn thờ Thần Biển & Đồng minh Deep Ones\n- Quest 1 (ID: 7E646765E175FE1C): Tìm Ngọc trai alexscaves:pearl"
  },
  {
    "name": "Thưởng: 50 XP, 1x Coin.\n- Quest 3 (ID: 71CED34A1AE4ABEA): Giao dịch với tộc Deep Ones (alexscaves:trade_with_deep_one)",
    "type": "Thưởng: 50 XP, 1x Coin.\n- Quest 4 (ID: 0FC75DE56C010977): Buddies Now - Biến Deep Ones thành đồng minh bảo vệ bạn (alexscaves:deep_ones_become_helpful)",
    "biome": "Thưởng: 50 XP, 1x Coin.\n- Bộ Giáp Lặn Diving Armor (ID: 63D448A24B35381B): Sở hữu trọn bộ Giáp lặn Diving Armor",
    "drops": "Thưởng: 100 XP, 1x Coin.\n\n---\n\n## 2. ICE AND FIRE (ice__fire.snbt)\n\n- Chủ đề: Thợ săn rồng thần thoại, thuần hóa rồng, chiến đấu với các sinh vật huyền thoại (Gorgon, Hydra, Cyclops, Sea Serpent, Dread Army) và luyện kim Thép Rồng (Dragonsteel & Dreadsteel).\n- Biểu tượng: Đầu rồng lửa (iceandfire:dragon_skull_fire)\n- Tổng số Quest: 27 Quest\n\n### 2.1. Bảng Tổng Hợp Boss & Quái Vật Thần Thoại Trong Ice and Fire",
    "notes": "Tên Quái vật / Boss"
  },
  {
    "name": "Vật phẩm đặc trưng",
    "type": "Công dụng & Chiến thuật",
    "biome": "",
    "drops": ":---",
    "notes": ":---"
  },
  {
    "name": "Lightning Dragon (Rồng Sét)",
    "type": "Biome rừng nhiệt đới / Savanna giông bão",
    "biome": "Tim rồng sét, Vảy rồng (4 màu: Xanh điện, Thạch anh tím, Đồng, Đen), Máu rồng sét",
    "drops": "Phóng sét hủy diệt tầm xa. Dùng để vận hành Lightning Dragon Forge.",
    "notes": ""
  },
  {
    "name": "Gorgon Temple (Beach Biome)",
    "type": "iceandfire:gorgon_head (Đầu Gorgon)",
    "biome": "Có ánh nhìn hóa đá ngay lập tức. Bắt buộc phải đeo Blindfold (bịt mắt) để không bị hóa đá. Đầu Gorgon dùng hóa đá 1 mục tiêu duy nhất.",
    "drops": "",
    "notes": "Cyclops (Khổng Lồ Một Mắt)"
  },
  {
    "name": "Đầu lâu Cyclops, Rương kho báu",
    "type": "Sức mạnh vật lý khủng khiếp, có thể nhấc bổng người chơi và dẫm nát.",
    "biome": "",
    "drops": "Hydra (Rồng 9 Đầu)",
    "notes": "Đầm lầy (Swamp Biome)"
  },
  {
    "name": "Mọc thêm đầu khi bị chém nếu không dùng lửa/độc để đốt vết thương.",
    "type": "",
    "biome": "Sea Serpent (Thủy Quái Biển)",
    "drops": "Đại dương sâu (Deep Ocean)",
    "notes": "Vảy thủy quái, Răng thủy quái, Đầu lâu"
  },
  {
    "name": "Shape: Default (Size 2.0)\n- Subtitle: Explore, fight, and kill dragons!\n- Dependencies: Không có (Root quest)\n- Mô tả: Đánh bại những con rồng hùng mạnh, thu thập xương và sức mạnh của chúng để chế tạo các trang bị tối thượng. Tìm tổ rồng và trở thành thợ săn rồng vĩ đại nhất!\n- Yêu cầu: Checkmark (\"silver is the dragons best friend\")\n- Phần thưởng: 50 XP\n\n#### 2. Trang Bị Khởi Đầu & Sách Hướng Dẫn\n- Quest Manuscripts (ID: 216A6EC6FE4E436E): Thu thập Bản thảo iceandfire:manuscript (tìm thấy trong tổ rồng, hang Cyclops, đầm lầy Hydra, làng mạc)",
    "type": "Thưởng: 20 XP",
    "biome": "Dep: 4617A1C9669B5909.\n- Quest Bestiary (ID: 4EDEB83B4BDA8CD6): Sở hữu Sách bách khoa quái vật iceandfire:bestiary và Bục đọc sách iceandfire:lectern",
    "drops": "Thưởng: 20 XP",
    "notes": "Dep: 216A6EC6FE4E436E.\n- Quest Bone Collector [Optional] (ID: 0DB417906F96C009): Thu thập toàn bộ 9 đầu lâu quái vật thần thoại (Fire Dragon, Hippogryph, Cyclops, Cockatrice, Stymphalian, Troll, Amphithere, Sea Serpent, Hydra)"
  },
  {
    "name": "Dep: 4EDEB83B4BDA8CD6.\n- Quest Bạc (ID: 72D9BC2BB748D2D4): Thu thập 3x Quặng bạc thô iceandfire:raw_silver",
    "type": "Thưởng: 3x Thỏi bạc, 1 XP Level.\n- Quest Giáp Bạc (ID: 67967612384A7AAD): Chế tạo trọn bộ giáp bạc Silver Armor (vũ khí bạc gây thêm sát thương lên Undead)",
    "biome": "Thưởng: 1x Kiếm bạc iceandfire:silver_sword, 1 XP Level",
    "drops": "Dep: 72D9BC2BB748D2D4.\n- Quest Giáp Đồng (ID: 5795ECD75ACACD71, 540C3501EC273441): Lựa chọn thay thế bằng trang bị đồng",
    "notes": "Thưởng: Kiếm đồng, XP Levels.\n\n#### 3. Thu Hoạch Xác Rồng (Dragon Harvesting)\n- Quest Dragon Heart (ID: 45F0280E0EE75C7B): Thu thập Tim rồng (Fire / Ice / Lightning Dragon Heart). Tim rồng là nguyên liệu bắt buộc để chế tạo Lõi Lò Rèn Rồng (Dragon Forge Core)"
  },
  {
    "name": "Dep: 67967612384A7AAD.\n- Quest Scales (ID: 3B4DA7EF08D1EC2F): Chuột phải tay không vào xác rồng để lột vảy rồng (dùng xây lò rèn rồng)",
    "type": "Thưởng: 100 XP",
    "biome": "Dep: 45F0280E0EE75C7B.\n- Quest Dragon Flesh (ID: 13F8BD59613AC3FE): Thịt rồng từ rồng cấp 3 trở lên",
    "drops": "Thưởng: 1x Táo vàng phù phép (minecraft:enchanted_golden_apple)",
    "notes": "Dep: 45F0280E0EE75C7B.\n- Quest Dragon Blood (ID: 7DF4BD144CB89FB7): Dùng chai thủy tinh chuột phải vào xác rồng để lấy máu rồng (sẽ làm biến mất xác, không thể lấy cả vảy lẫn máu cùng lúc)"
  },
  {
    "name": "Dep: 45F0280E0EE75C7B.\n- Quest Dragon Bones (ID: 54306E8AB3574BC3): Lấy xương rồng từ bộ xương",
    "type": "Thưởng: 8x iceandfire:dragonbone",
    "biome": "Dep: 45F0280E0EE75C7B.\n- Quest Dragon Skulls (ID: 11512722F976909C): Lấy Đầu lâu rồng cấp 4+",
    "drops": "Thưởng: 5 XP Levels",
    "notes": "Dep: 54306E8AB3574BC3.\n\n#### 4. Pha Lê Triệu Hồi Rồng (Summoning Crystals)\n- Pha lê Rồng Lửa (ID: 683BE7D5D9706983): iceandfire:summoning_crystal_fire"
  },
  {
    "name": "Thưởng: 7 XP Levels.\n- Pha lê Rồng Sét (ID: 62E2BFFEA137AA6C): iceandfire:summoning_crystal_lightning",
    "type": "Thưởng: 7 XP Levels.\n\n#### 5. Màu Sắc Của Rồng & Xây Dựng Lò Rèn Rồng (Dragon Forge)\n- Quest Colors of Dragons (ID: 03D776E331D95114): Checkmark tìm hiểu về 4 màu sắc của mỗi chủng loại rồng",
    "biome": "Thưởng: 100 XP",
    "drops": "Dep: 13F8BD59613AC3FE, 3B4DA7EF08D1EC2F, 7DF4BD144CB89FB7.\n- Fire Dragon Colors (ID: 61C2732DC98234AD): Thu thập đủ 4 màu vảy rồng lửa (Đỏ, Xanh lá, Đồng, Xám)",
    "notes": "Thưởng: 5x Gạch lò rèn lửa iceandfire:dragonforge_fire_brick, 5 XP Levels.\n- Ice Dragon Colors (ID: 6D572E185AD81408): Thu thập đủ 4 màu vảy rồng băng (Xanh dương, Trắng, Sapphire, Bạc)"
  },
  {
    "name": "Thưởng: 5x Gạch lò rèn sét iceandfire:dragonforge_lightning_brick, 5 XP Levels.\n\n#### 6. Luyện Kim Thép Rồng (Dragonsteel & Dreadsteel)\n- Lò Rèn Rồng Lửa & Dragonsteel Lửa:\n  - Quest Lõi lò lửa (ID: 692DF9395BF63138): iceandfire:dragonforge_fire_core_disabled",
    "type": "Thưởng: 100 XP.\n  - Quest Thỏi thép rồng lửa (ID: 53EC8131D2AC55AE): iceandfire:dragonsteel_fire_ingot",
    "biome": "Thưởng: 5 XP Levels.\n- Lò Rèn Rồng Băng & Dragonsteel Băng:\n  - Quest Lõi lò băng (ID: 0451E3C9CB20A121): iceandfire:dragonforge_ice_core_disabled",
    "drops": "Thưởng: 100 XP.\n  - Quest Thỏi thép rồng băng (ID: 69B1A4E3EF7DFC16): iceandfire:dragonsteel_ice_ingot",
    "notes": "Thưởng: 5 XP Levels.\n- Lò Rèn Rồng Sét & Dragonsteel Sét:\n  - Quest Lõi lò sét (ID: 002B2CF0A1A2EC06): iceandfire:dragonforge_lightning_core_disabled"
  },
  {
    "name": "Thưởng: 5 XP Levels.\n- Thép Dreadsteel Tối Thượng (ID: 6F8F09FBA4FFAB39):\n  - Mô tả: Kim loại tối thượng kết hợp cả 3 loại thép rồng cùng mảnh Dread Shard!\n  - Yêu cầu: Chế tạo dreadsteel:dreadsteel_ingot\n  - Dependencies: 5DAC21343CEEE1BF, 53EC8131D2AC55AE, 69B1A4E3EF7DFC16, 72B06E6D54BF1FD6\n  - Phần thưởng: 10 XP Levels\n- Dread Warrior (ID: 41BAE25D02C10F3D):\n  - Mô tả: Trở thành Chiến Binh Dread Vĩ Đại!\n  - Yêu cầu: Chế tạo trọn bộ trang bị Dreadsteel: Khiên, Lưỡi hái (dreadsteel:dreadsteel_scythe), Mũ, Giáp thân, Quần, Giày.\n  - Phần thưởng: 30 XP Levels\n\n#### 7. Đền Thờ Gorgon & Quái Vật Lăng Mộ (Dread Mausoleum)\n- Nhánh Gorgon:\n  - Quest Giới thiệu Gorgon (ID: 568DFAA06F431D4B): Checkmark",
    "type": "Thưởng: 5 XP Levels.\n  - Quest Tìm Đền Gorgon (ID: 37060BF95E5DE1E0): Tìm cấu trúc iceandfire:gorgon_temple ở bờ biển",
    "biome": "Thưởng: 2x Dây chỉ, 1x Da thuộc (làm bịt mắt Blindfold).\n  - Quest Trảm Đầu Gorgon (ID: 07739E12766B9A0A): Thu thập Đầu Medusa iceandfire:gorgon_head",
    "drops": "Thưởng: 100 XP.\n- Nhánh Quái Vật Lăng Mộ (Mausoleum & Dread Army):\n  - Quest The Undeads (ID: 42DEAEAAEEF5424D): Checkmark",
    "notes": "Thưởng: 20 XP.\n  - Quest Tìm Lăng Mộ (ID: 2957649C45311405): Tìm cấu trúc iceandfire:mausoleum trong vùng tuyết lạnh"
  },
  {
    "name": "Thưởng: 5x Dread Shard, 2 XP Levels.\n  - Quest Dẹp Loạn Quân Đoàn Dread (ID: 688F140757A418D0): Tiêu diệt 3x Dread Scuttler, 3x Dread Knight, 9x Dread Beast",
    "type": "Thưởng: 64x Gạch đá Dreadstone, 5 XP Levels.\n\n---\n\n## 3. LEGENDARY MONSTERS (legendary_monsters_2.snbt)\n\n- Chủ đề: Thử thách săn lùng các Trùm Huyền Thoại rải rác khắp 3 chiều không gian (Overworld, The Nether, The End) bằng các Con Mắt Sinh Vật đặc chế để định vị.\n- Biểu tượng: Chìa Khóa U Ám (legendary_monsters:somber_key)\n- Tổng số Quest: 16 Quest\n\n### 3.1. Bảng Tổng Hợp Boss Huyền Thoại Theo Từng Chiều Không Gian",
    "biome": "Chiều không gian",
    "drops": "Tên Boss Huyền Thoại",
    "notes": "Con mắt dùng để định vị"
  },
  {
    "name": "Phần thưởng Quest",
    "type": "",
    "biome": ":---",
    "drops": ":---",
    "notes": ":---"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "Overworld",
    "drops": "Possessed Paladin",
    "notes": "legendary_monsters:eye_of_ghost"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "Overworld",
    "drops": "Ancient Guardian",
    "notes": "legendary_monsters:eye_of_many_ribs"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "Overworld",
    "drops": "Cloud Golem",
    "notes": "legendary_monsters:eye_of_air"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "Overworld",
    "drops": "Dune Sentinel",
    "notes": "legendary_monsters:eye_of_sandstorm"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "Overworld",
    "drops": "Overgrown Colossus",
    "notes": "legendary_monsters:eye_of_moss"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The Nether",
    "drops": "Skeletosaurus",
    "notes": "legendary_monsters:eye_of_bones"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The Nether",
    "drops": "Withered Abomination",
    "notes": "legendary_monsters:eye_of_soul"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The Nether",
    "drops": "Lava Eater",
    "notes": "legendary_monsters:eye_of_magma"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The End",
    "drops": "Annihilation Pursuer",
    "notes": "legendary_monsters:eye_of_annihilation"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The End",
    "drops": "The Obliterator",
    "notes": "Cấu trúc / Mắt End"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The End",
    "drops": "Shulker Mimic",
    "notes": "legendary_monsters:eye_of_shulker"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "",
    "biome": "The End",
    "drops": "Endersent",
    "notes": "legendary_monsters:eye_of_chorus"
  },
  {
    "name": "1x Coin, 1x Boss Loot Box, 5 XP Levels",
    "type": "---\n\n### 3.2. Danh Sách Chi Tiết Toàn Bộ Quest Trong Legendary Monsters\n\n#### Nhánh 1: Overworld Challenges\n- Quest Root Overworld (ID: 6CCC0D919C339A9D): Đến Overworld",
    "biome": "Thưởng: 100 XP, 1x Coin.\n- Quest 1: Frosty (ID: 1C468768243CE551): Chế tạo eye_of_frost và tiêu diệt legendary_monsters:frostbitten_golem.\n- Quest 2: Possessed (ID: 14548E0E21A7E283): Chế tạo eye_of_ghost, tiêu diệt legendary_monsters:posessed_paladin và thu thập somber_key.\n- Quest 3: Sunky (ID: 32EE49E726B81C86): Chế tạo eye_of_many_ribs và tiêu diệt legendary_monsters:ancient_guardian.\n- Quest 4: Cloudy (ID: 2A347F37517380FF): Chế tạo eye_of_air và tiêu diệt legendary_monsters:cloud_golem.\n- Quest 5: Sandy (ID: 703EE69C5D8050DC): Chế tạo eye_of_sandstorm và tiêu diệt legendary_monsters:dune_sentinel.\n- Quest 6: Mossy (ID: 7BEB2CEFD962AF91): Chế tạo eye_of_moss và tiêu diệt legendary_monsters:overgrown_colossus.\n\n#### Nhánh 2: Nether Challenges\n- Quest Root Nether (ID: 3A434E6D6C87249F): Bước chân vào Nether",
    "drops": "Thưởng: 100 XP, 1x Coin",
    "notes": "Dep: 6CCC0D919C339A9D.\n- Quest 7: Bones (ID: 179CA1964C40F7CF): Chế tạo eye_of_bones và tiêu diệt legendary_monsters:skeletosaurus.\n- Quest 8: Soul (ID: 159680B9EF82CBD3): Chế tạo eye_of_soul và tiêu diệt legendary_monsters:withered_abomination.\n- Quest 9: Magma (ID: 23E1D5A84854309F): Chế tạo eye_of_magma và tiêu diệt legendary_monsters:lava_eater.\n\n#### Nhánh 3: End Challenges\n- Quest Root End (ID: 697A6EC01C2C4A61): Đặt chân đến The End"
  },
  {
    "name": "Băng Thuật (Ice Magic)",
    "type": "Tăng sát thương Băng, kháng đông lạnh",
    "biome": "",
    "drops": "Creaking Sorcerer Set",
    "notes": "Tự Nhiên & Cổ Xưa (Nature/Eldritch)"
  },
  {
    "name": "Ender Magic",
    "type": "Tăng sát thương dịch chuyển & không gian",
    "biome": "",
    "drops": "Flesh Mass Set",
    "notes": "Huyết Thuật (Blood Magic)"
  },
  {
    "name": "Thánh Thuật (Holy Magic)",
    "type": "Tăng hồi máu và sát thương lên Undead",
    "biome": "",
    "drops": "Infestation Set",
    "notes": "Triệu Hồi Côn Trùng (Evocation)"
  },
  {
    "name": "Chiến Binh Hỏa Ma Pháp",
    "type": "Cân bằng hoàn hảo giữa giáp nặng và sức mạnh phép",
    "biome": "",
    "drops": "Mithril Battlemage Set",
    "notes": "Chiến Binh Bí Thuật (Mithril)"
  },
  {
    "name": "Chỉ Huy Quân Đoàn Ma Thuật",
    "type": "Hỗ trợ sát thương diện rộng và đồng minh",
    "biome": "",
    "drops": "Fireblossom Battlemage Set",
    "notes": "Hoa Lửa Tối Thượng"
  },
  {
    "name": "Thưởng: 1x Coin, 100 XP",
    "type": "Dep: 0D7DF8B8FFBCDFDD.\n3. Zenalite Ingot (ID: 3B6C07A361FC4989): Thỏi kim loại Zenalite tinh luyện dùng để chế tạo trang bị tối thượng",
    "biome": "Thưởng: 1x Coin, 100 XP",
    "drops": "Dep: 50C5092B8459BB41.\n4. Eldritch Rune (ID: 42B3AB5DF0DDF593): Cổ ngữ Cổ đại dùng để ép phép cao cấp",
    "notes": "Thưởng: 1x Coin, 5 XP Levels.\n5. Divine Mold (ID: 3BB13FEFEDD326F5): Khuôn Đúc Thần Thánh dùng tạo hình các bảo bối ma thuật"
  }
];
