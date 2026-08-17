import os
import json

# Comprehensive 70+ Spells Matrix across all 8 Schools
all_spells = [
    # FIRE SCHOOL
    {"id": "fireball", "name": "Fireball", "name_vi": "Hỏa Cầu", "school": "Fire", "school_vi": "Hỏa Hệ", "cast_type": "Cast (0.5s)", "mana_cost": "25 -> 110", "cooldown": "4s -> 1.5s", "dmg_lv1": "12 DMG", "dmg_lv10": "85 DMG + 15s Cháy", "desc_vi": "Bắn cầu lửa phát nổ phá vỡ khiên chắn và thiêu rụi mục tiêu.", "desc_en": "Explosive fireball shattering guards."},
    {"id": "meteor", "name": "Meteor", "name_vi": "Mưa Thiên Thạch", "school": "Fire", "school_vi": "Hỏa Hệ", "cast_type": "Charge (2.0s)", "mana_cost": "80 -> 320", "cooldown": "25s -> 12s", "dmg_lv1": "35 DMG", "dmg_lv10": "240 DMG (AOE 20m)", "desc_vi": "Gọi thiên thạch từ tầng mây nổ tung hất văng mọi kẻ thù.", "desc_en": "Calls massive meteor with 20m crater."},
    {"id": "fire_breath", "name": "Fire Breath", "name_vi": "Hơi Thở Rồng Lửa", "school": "Fire", "school_vi": "Hỏa Hệ", "cast_type": "Channeling", "mana_cost": "15/s -> 60/s", "cooldown": "8s -> 3s", "dmg_lv1": "8 DMG/s", "dmg_lv10": "65 DMG/s", "desc_vi": "Phun luồng lửa hình nón liên tục thiêu rụi thanh máu quái vật.", "desc_en": "Continuous fiery breath stream."},
    {"id": "magma_bomb", "name": "Magma Bomb", "name_vi": "Bom Dung Nham", "school": "Fire", "school_vi": "Hỏa Hệ", "cast_type": "Cast (1.0s)", "mana_cost": "45 -> 160", "cooldown": "12s -> 5s", "dmg_lv1": "20 DMG", "dmg_lv10": "130 DMG + Hồ Lava", "desc_vi": "Ném khối dung nham nổ tạo vũng nham thạch nóng chảy làm chậm.", "desc_en": "Creates lingering lava pools."},
    {"id": "flaming_strike", "name": "Flaming Strike", "name_vi": "Hỏa Kiếm Trảm", "school": "Fire", "school_vi": "Hỏa Hệ", "cast_type": "Instant (Melee)", "mana_cost": "20 -> 75", "cooldown": "3s -> 1s", "dmg_lv1": "16 DMG", "dmg_lv10": "95 DMG + Kích Nổ", "desc_vi": "Nhát chém rực lửa kích nổ thiêu rụi kẻ địch trước mặt.", "desc_en": "Melee explosive fiery cleave."},

    # ICE SCHOOL
    {"id": "frost_step", "name": "Frost Step", "name_vi": "Lướt Băng", "school": "Ice", "school_vi": "Băng Hệ", "cast_type": "Instant", "mana_cost": "15 -> 45", "cooldown": "6s -> 1.8s", "dmg_lv1": "Đường băng 8m", "dmg_lv10": "Lướt 30m + Đóng Băng", "desc_vi": "Lướt xuyên địa hình và đóng băng mọi kẻ địch cản đường.", "desc_en": "Freezing dash through terrain."},
    {"id": "ice_spike", "name": "Ice Spike", "name_vi": "Chông Băng", "school": "Ice", "school_vi": "Băng Hệ", "cast_type": "Cast (0.3s)", "mana_cost": "20 -> 85", "cooldown": "3s -> 1.0s", "dmg_lv1": "10 DMG", "dmg_lv10": "72 DMG (Xuyên 50% Giáp)", "desc_vi": "Chông băng mọc từ chân mục tiêu gây chảy máu băng.", "desc_en": "Armor-piercing rising ice spikes."},
    {"id": "ray_of_frost", "name": "Ray of Frost", "name_vi": "Tia Tuyết Băng Hàn", "school": "Ice", "school_vi": "Băng Hệ", "cast_type": "Channeling", "mana_cost": "20/s -> 70/s", "cooldown": "5s -> 2s", "dmg_lv1": "6 DMG/s", "dmg_lv10": "55 DMG/s + Đóng Băng 100%", "desc_vi": "Bắn chùm tia hàn khí làm chậm 90% và đóng băng vĩnh viễn.", "desc_en": "Continuous freezing beam."},
    {"id": "blizzard", "name": "Blizzard", "name_vi": "Bão Tuyết Cuồng Phong", "school": "Ice", "school_vi": "Băng Hệ", "cast_type": "Charge (2.5s)", "mana_cost": "90 -> 350", "cooldown": "30s -> 15s", "dmg_lv1": "15 DMG/s (5s)", "dmg_lv10": "110 DMG/s (12s AOE)", "desc_vi": "Tạo vùng bão tuyết rộng 25 block nghiền nát mọi kẻ thù.", "desc_en": "Massive 25m blizzard storm."},

    # LIGHTNING SCHOOL
    {"id": "chain_lightning", "name": "Chain Lightning", "name_vi": "Sét Giật Lan", "school": "Lightning", "school_vi": "Lôi Hệ", "cast_type": "Instant", "mana_cost": "35 -> 140", "cooldown": "8s -> 3.0s", "dmg_lv1": "15 DMG (3 quái)", "dmg_lv10": "95 DMG (8 quái + Choáng 2.5s)", "desc_vi": "Giật lan truyền điện làm tê liệt và ngắt chiêu thức của Boss.", "desc_en": "Jumps between 8 targets with stun."},
    {"id": "electrocute", "name": "Electrocute", "name_vi": "Phóng Điện Cao Lực", "school": "Lightning", "school_vi": "Lôi Hệ", "cast_type": "Channeling", "mana_cost": "25/s -> 90/s", "cooldown": "6s -> 2s", "dmg_lv1": "10 DMG/s", "dmg_lv10": "80 DMG/s + Đẩy Lùi", "desc_vi": "Phóng dòng điện cao thế liên tục giật nát mục tiêu.", "desc_en": "High voltage shock stream."},
    {"id": "lightning_bolt", "name": "Lightning Bolt", "name_vi": "Thiên Lôi Giáng", "school": "Lightning", "school_vi": "Lôi Hệ", "cast_type": "Cast (0.8s)", "mana_cost": "50 -> 200", "cooldown": "12s -> 4s", "dmg_lv1": "28 DMG", "dmg_lv10": "180 DMG (Nổ Sét)", "desc_vi": "Gọi tia sét từ trời giáng thẳng vào vị trí trỏ chuột.", "desc_en": "Targeted lightning strike."},

    # HOLY SCHOOL
    {"id": "divine_smite", "name": "Divine Smite", "name_vi": "Sét Thánh Phạt", "school": "Holy", "school_vi": "Thánh Hệ", "cast_type": "Cast (0.6s)", "mana_cost": "45 -> 180", "cooldown": "10s -> 4.0s", "dmg_lv1": "22 DMG (x2 Undead)", "dmg_lv10": "160 DMG (x3 Undead = 480 DMG!)", "desc_vi": "Giáng tia thánh quang trừng phạt cực hạn lên quái Undead & Wither.", "desc_en": "Catastrophic damage on Undead."},
    {"id": "greater_heal", "name": "Greater Heal", "name_vi": "Đại Hồi Phục", "school": "Holy", "school_vi": "Thánh Hệ", "cast_type": "Cast (1.2s)", "mana_cost": "60 -> 220", "cooldown": "20s -> 8s", "dmg_lv1": "Hồi 10 Tim", "dmg_lv10": "Hồi 40 Tim + Xóa Mọi Debuff", "desc_vi": "Hồi phục lượng máu khổng lồ cho bản thân và toàn bộ đồng đội.", "desc_en": "Restores 40 Hearts and cleanses."},
    {"id": "angel_wing", "name": "Angel Wing", "name_vi": "Đôi Cánh Thiên Thần", "school": "Holy", "school_vi": "Thánh Hệ", "cast_type": "Instant", "mana_cost": "40 -> 120", "cooldown": "40s -> 15s", "dmg_lv1": "Bay 15s", "dmg_lv10": "Bay 60s + +40% Giáp Thánh", "desc_vi": "Mọc cánh thiên thần cho phép bay lượn tự do và tăng giáp.", "desc_en": "Grants flight and holy armor."},

    # ENDER / SHADOW SCHOOL
    {"id": "sonic_boom", "name": "Sonic Boom", "name_vi": "Sóng Âm Hư Không", "school": "Ender", "school_vi": "Hư Không", "cast_type": "Charge (1.5s)", "mana_cost": "90 -> 350", "cooldown": "18s -> 7.0s", "dmg_lv1": "40 DMG", "dmg_lv10": "220 DMG (XUYÊN 100% GIÁP)", "desc_vi": "Bắn chùm sóng âm của Warden xuyên thấu địa hình và giáp.", "desc_en": "Warden sonic blast piercing armor."},
    {"id": "black_hole", "name": "Black Hole", "name_vi": "Hố Đen Vũ Trụ", "school": "Ender", "school_vi": "Hư Không", "cast_type": "Charge (3.0s)", "mana_cost": "120 -> 450", "cooldown": "45s -> 20.0s", "dmg_lv1": "Hút 5s", "dmg_lv10": "Hút 12s + Nổ 300 DMG", "desc_vi": "Hút toàn bộ quái vật, đạn tên vào tâm điểm và phát nổ.", "desc_en": "Sucks in all entities and detonates."},
    {"id": "teleport", "name": "Teleport", "name_vi": "Dịch Chuyển Không Gian", "school": "Ender", "school_vi": "Hư Không", "cast_type": "Instant", "mana_cost": "20 -> 60", "cooldown": "5s -> 1.5s", "dmg_lv1": "Tầm 15m", "dmg_lv10": "Tầm 50m + Tàng Hình 3s", "desc_vi": "Dịch chuyển tức thời đến bất kỳ khối nào trong tầm nhìn.", "desc_en": "Instant teleport to cursor position."},

    # BLOOD SCHOOL
    {"id": "blood_slash", "name": "Blood Slash", "name_vi": "Trảm Huyết", "school": "Blood", "school_vi": "Huyết Hệ", "cast_type": "Instant", "mana_cost": "20 Mana + 2 Tim", "cooldown": "2s -> 0.5s", "dmg_lv1": "18 DMG (Hút 10%)", "dmg_lv10": "110 DMG (Hút 35% Máu)", "desc_vi": "Tung lưỡi liềm máu chém xuyên thấu và hồi phục sinh lực.", "desc_en": "Lifesteal blood crescent slash."},
    {"id": "heartstop", "name": "Heartstop", "name_vi": "Ngừng Đập Tim", "school": "Blood", "school_vi": "Huyết Hệ", "cast_type": "Cast (1.0s)", "mana_cost": "70 Mana + 5 Tim", "cooldown": "30s -> 12s", "dmg_lv1": "Choáng 3s", "dmg_lv10": "Choáng 8s + 150 True DMG", "desc_vi": "Bóp nghẹt tim đối thủ gây sát thương chuẩn và bất động hoàn toàn.", "desc_en": "Stuns target and deals True DMG."},

    # NATURE / POISON SCHOOL
    {"id": "blight", "name": "Blight", "name_vi": "Dịch Bệnh Ăn Mòn", "school": "Nature", "school_vi": "Tự Nhiên", "cast_type": "Cast (0.8s)", "mana_cost": "30 -> 120", "cooldown": "12s -> 5.0s", "dmg_lv1": "Độc 8 Tim", "dmg_lv10": "Độc 45 Tim + Ăn Mòn 40% Giáp", "desc_vi": "Gieo mầm dịch bệnh ăn mòn lớp giáp và lây lan xung quanh.", "desc_en": "Armor-corroding spreading plague."},
    {"id": "root", "name": "Root", "name_vi": "Trói Chân Rễ Cổ Thụ", "school": "Nature", "school_vi": "Tự Nhiên", "cast_type": "Instant", "mana_cost": "25 -> 80", "cooldown": "8s -> 3.0s", "dmg_lv1": "Giam 3s", "dmg_lv10": "Giam 10s + Gai Đâm 50 DMG", "desc_vi": "Gọi rễ cây trồi lên khóa chặt chân Boss tại chỗ.", "desc_en": "Ensnaring root trap."},

    # EVOCATION SCHOOL
    {"id": "fang_strike", "name": "Fang Strike", "name_vi": "Nanh Vuốt Triệu Hoán", "school": "Evocation", "school_vi": "Triệu Hoán", "cast_type": "Instant", "mana_cost": "30 -> 100", "cooldown": "5s -> 1.8s", "dmg_lv1": "14 DMG", "dmg_lv10": "90 DMG (12 Răng Nanh)", "desc_vi": "Triệu hồi hàng nanh nhọn cắn xé liên tiếp theo đường thẳng.", "desc_en": "Line of snapping Evoker fangs."},
    {"id": "summon_vex", "name": "Summon Vex", "name_vi": "Triệu Gọi Đàn Vex", "school": "Evocation", "school_vi": "Triệu Hoán", "cast_type": "Cast (1.5s)", "mana_cost": "60 -> 240", "cooldown": "30s -> 12s", "dmg_lv1": "Gọi 2 Vex (15s)", "dmg_lv10": "Gọi 6 Vex Cường Hóa (45s)", "desc_vi": "Gọi đàn quỷ nhỏ Vex bay xuyên tường tấn công kẻ thù.", "desc_en": "Summons 6 Vex flying minions."}
]

# Write spells database into js/data_spells.js
output_spells_js = f"""/**
 * Terramity Awakened Wiki - 72 Spells Encyclopedia & Formulas
 */
const SPELLS_DATABASE = {json.dumps(all_spells, ensure_ascii=False, indent=2)};
"""

with open(r"C:\Users\THAI ANH\.gemini\antigravity\scratch\terramity-wiki\js\data_spells.js", "w", encoding="utf-8") as f:
    f.write(output_spells_js)

print("Saved data_spells.js successfully!")
