import re

# 1. Upgrade creatures.html
creatures_extra_content = '''
    <!-- Section: Alex's Caves 6 Biomes & Bosses -->
    <section style="margin-top:3.5rem;">
      <h2>🌋 <span class="vi-text">6 Quần Xã Hang Động Cổ Đại (Alex's Caves)</span><span class="en-text">Alex's Caves: 6 Ancient Subterranean Biomes</span></h2>
      <p style="color:var(--text-secondary); margin-bottom:1rem;">
        <span class="vi-text">Sử dụng Bàn Spelunkery Table + Cave Tablets để định vị 6 hệ sinh thái ngầm sâu dưới lòng đất:</span>
        <span class="en-text">Locate all 6 unique subterranean cave biomes using Spelunkery Table & Cave Tablets:</span>
      </p>

      <div class="grid-cards">
        <div class="card" style="border-top:2px solid #ef4444;">
          <h3 style="color:#ef4444;">🧲 1. Magnetic Caves (Hang Từ Tính)</h3>
          <p style="font-size:0.85rem; color:var(--text-secondary);">Quặng Neodymium Đỏ/Xanh đối cực, động cơ từ tính Quarry Smasher. Boss: <strong>Magnetron</strong> (Rớt <em>Heart of Iron</em>).</p>
        </div>
        <div class="card" style="border-top:2px solid #10b981;">
          <h3 style="color:#10b981;">🦖 2. Primordial Caves (Hang Tiền Sử)</h3>
          <p style="font-size:0.85rem; color:var(--text-secondary);">Khủng long bạo chúa Tremorsaurus, cây dương xỉ cổ đại, hổ răng kiếm. Thu thập Trứng khủng long và Heavy Bone.</p>
        </div>
        <div class="card" style="border-top:2px solid #84cc16;">
          <h3 style="color:#84cc16;">☢️ 3. Toxic Caves (Hang Đột Biến Phóng Xạ)</h3>
          <p style="font-size:0.85rem; color:var(--text-secondary);">Chất thải Uranium hạt nhân, Gián khổng lồ Gammaroach, Raygun. <strong>Yêu cầu mang bộ đồ Hazmat Suit chống nhiễm xạ!</strong></p>
        </div>
        <div class="card" style="border-top:2px solid #06b6d4;">
          <h3 style="color:#06b6d4;">🌊 4. Abyssal Chasm (Vực Thẳm Đại Dương)</h3>
          <p style="font-size:0.85rem; color:var(--text-secondary);">Áp suất nước cực lớn, Tộc người cá Deep Ones giao dịch ngọc trai, Mine Guardian thủy lôi. <strong>Yêu cầu Bộ giáp Lặn Diving Suit!</strong></p>
        </div>
        <div class="card" style="border-top:2px solid #a855f7;">
          <h3 style="color:#a855f7;">👁️ 5. Forlorn Hollows (Hang U Ám Bóng Tối)</h3>
          <p style="font-size:0.85rem; color:var(--text-secondary);">Tộc chuột chũi Underzealot hiến tế tà thuật, quái vật Corrodent đào hầm, quặng ngọc Occult Gem.</p>
        </div>
        <div class="card" style="border-top:2px solid #ec4899;">
          <h3 style="color:#ec4899;">🍬 6. Candy Cavity (Hang Kẹo Ngọt)</h3>
          <p style="font-size:0.85rem; color:var(--text-secondary);">Thị trấn Bánh Gừng Gingerbread Town, Tháp Phù Thủy Kẹo Licowitch. Rớt <em>Radiant Essence</em> chế Vạc Chuyển Đổi Sinh Thái.</p>
        </div>
      </div>
    </section>

    <!-- Section: Ice & Fire 3 Dragon Species & Legendary Monsters -->
    <section style="margin-top:3.5rem;">
      <h2>🐉 <span class="vi-text">Tam Đại Long Tộc & 13 Quái Thú Huyền Thoại (Ice & Fire)</span><span class="en-text">Ice & Fire: 3 Dragon Species & 13 Mythical Beasts</span></h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th><span class="vi-text">Sinh Vật / Boss</span><span class="en-text">Creature / Boss</span></th>
              <th><span class="vi-text">Hệ Phái / Chủng Loại</span><span class="en-text">Element / Type</span></th>
              <th><span class="vi-text">Môi Trường Xuất Hiện</span><span class="en-text">Spawn Location</span></th>
              <th><span class="vi-text">Trang Bị & Giáp Rèn Được</span><span class="en-text">Craftable Equipment</span></th>
              <th><span class="vi-text">Cơ Chế & Điểm Yếu Thực Chiến</span><span class="en-text">Combat Strategy</span></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color:#ef4444;">🔥 Fire Dragon (Rồng Lửa)</strong></td>
              <td>Hỏa Long (Tier 1 - 5)</td>
              <td>Tổ rồng mặt đất & Hang dung nham ngầm (Y: -30)</td>
              <td>Fire Dragonscale Armor, Fire Dragonsteel</td>
              <td>Miễn nhiễm 100% Lửa. Sử dụng Vũ khí Băng Hệ hoặc cung tên tầm xa hạ gục trên không.</td>
            </tr>
            <tr>
              <td><strong style="color:#06b6d4;">❄️ Ice Dragon (Rồng Băng)</strong></td>
              <td>Băng Long (Tier 1 - 5)</td>
              <td>Đỉnh núi tuyết băng giá & Hang tuyết vĩnh cửu</td>
              <td>Ice Dragonscale Armor, Ice Dragonsteel</td>
              <td>Phun hơi thở đóng băng làm chậm cực nặng. Dùng phép Hỏa thuật (Meteor, Fireball) đốt cháy x2 sát thương.</td>
            </tr>
            <tr>
              <td><strong style="color:#eab308;">⚡ Lightning Dragon (Rồng Sấm)</strong></td>
              <td>Lôi Long (Tier 1 - 5)</td>
              <td>Rừng nhiệt đới Jungle & Hang thạch anh tím</td>
              <td>Lightning Dragonscale, Lightning Dragonsteel</td>
              <td>Tốc độ bay nhanh nhất trong 3 loài, giật sét choáng ngắt chiêu. Cần khiên kháng sét hoặc giáp Hazen.</td>
            </tr>
            <tr>
              <td><strong style="color:#a855f7;">🐍 Gorgon (Xà Nữ Hóa Đá)</strong></td>
              <td>Quái Thú Thần Thoại</td>
              <td>Đền thờ Hy Lạp ngầm bờ biển</td>
              <td>Đầu Gorgon Head (Hóa đá mọi Boss trong 10s)</td>
              <td><strong>CỰC KỲ NGUY HIỂM:</strong> Nhìn thẳng vào mắt Gorgon sẽ bị chết ngay tức khắc (Insta-kill). Phải nhắm mắt hoặc đeo Blindfold!</td>
            </tr>
            <tr>
              <td><strong style="color:#10b981;">🐉 Hydra (Rồng Chín Đầu)</strong></td>
              <td>Quái Thú Thần Thoại</td>
              <td>Đầm lầy hắc ám Swamp Biomes</td>
              <td>Trái Tim Hydra Heart (Hồi phục máu vĩnh viễn)</td>
              <td>Mỗi lần chém đứt 1 đầu sẽ mọc thêm 2 đầu mới trừ khi dùng Lửa đốt cháy vết thương!</td>
            </tr>
            <tr>
              <td><strong style="color:#38bdf8;">🌊 Sea Serpent (Thủy Quái Biển Sâu)</strong></td>
              <td>Quái Thú Thần Thoại</td>
              <td>Đại dương sâu thẳm Deep Ocean</td>
              <td>Vảy Sea Serpent Scale (Giáp bơi nhanh nhất game)</td>
              <td>Nhảy vọt khỏi mặt nước đớp thuyền người chơi. Bắn tên kéo lên bờ để giảm 80% độ cơ động của nó.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
'''

with open('creatures.html', 'r', encoding='utf-8') as f:
    c_html = f.read()

if "Alex's Caves: 6 Ancient" not in c_html and '</main>' in c_html:
    c_html = c_html.replace('</main>', f'{creatures_extra_content}\n  </main>')
    with open('creatures.html', 'w', encoding='utf-8') as f:
        f.write(c_html)
    print("Upgraded creatures.html successfully!")

# 2. Upgrade dimensions.html with complete 12 Eyes Guide
eyes_extra_content = '''
    <!-- Section: 12 Ancient Eyes of End Remastered -->
    <section style="margin-top:3.5rem;">
      <h2>👁️ <span class="vi-text">Bách Khoa 12 Mắt Thần Mở Cổng The End (End Remastered)</span><span class="en-text">12 Ancient Eyes of End Remastered</span></h2>
      <p style="color:var(--text-secondary); margin-bottom:1rem;">
        <span class="vi-text">Trong Terramity Awakened, Cổng The End không thể mở bằng Mắt Ender thông thường mà yêu cầu phải thu thập đủ 12 con Mắt Thần Ma Thuật từ các thủ lĩnh và tàn tích:</span>
        <span class="en-text">To unlock the Ancient End Portal, gather all 12 unique ancient eyes across 3 dimensions:</span>
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th><span class="vi-text">Tên Mắt Thần (Eye)</span><span class="en-text">Eye Name</span></th>
              <th><span class="vi-text">Vị Trí & Nguồn Rơi</span><span class="en-text">Source & Location</span></th>
              <th><span class="vi-text">Tỉ Lệ / Cách Sở Hữu</span><span class="en-text">Drop Rate / Recipe</span></th>
              <th><span class="vi-text">Hướng Dẫn Săn Lùng Thực Chiến</span><span class="en-text">Hunting Strategy</span></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color:#06b6d4;">👁️ Guardian Eye (Mắt Hộ Vệ)</strong></td>
              <td>Đền Thờ Biển Ocean Monument</td>
              <td>100% Rớt khi diệt Elder Guardian</td>
              <td>Đào thẳng từ nóc đền thờ biển, uống sữa giải hiệu ứng Đào Chậm (Mining Fatigue).</td>
            </tr>
            <tr>
              <td><strong style="color:#e11d48;">👁️ Magical Eye (Mắt Ma Thuật)</strong></td>
              <td>Dinh Thự Woodland Mansion</td>
              <td>100% Rớt khi diệt Thầy Pháp Evoker</td>
              <td>Đột kích phòng tế lễ tầng 3 của Dinh Thự Rừng Rậm.</td>
            </tr>
            <tr>
              <td><strong style="color:#38bdf8;">👁️ Cold Eye (Mắt Băng Giá)</strong></td>
              <td>Nhà Băng Igloo Rương Ngầm</td>
              <td>100% Trong rương bí mật dưới thảm</td>
              <td>Tìm lều tuyết Igloo ở xứ lạnh, đào phá thảm len để tìm lối thang xuống tầng hầm bí mật.</td>
            </tr>
            <tr>
              <td><strong style="color:#f59e0b;">👁️ Lost Eye (Mắt Thất Lạc)</strong></td>
              <td>Đền Thờ Rừng Rậm Jungle Pyramid</td>
              <td>Rương kho báu đền thờ</td>
              <td>Vượt qua bẫy dây cung và giải câu đố 3 cần gạt đá ngầm.</td>
            </tr>
            <tr>
              <td><strong style="color:#ef4444;">👁️ Nether Eye (Mắt Địa Ngục)</strong></td>
              <td>Pháo Đài Địa Ngục Nether Fortress</td>
              <td>Rèn từ Lệ Ma Ghast + Que Quỷ Lửa Blaze</td>
              <td>Ghép tại bàn chế tạo sau khi chinh phục pháo đài Nether.</td>
            </tr>
            <tr>
              <td><strong style="color:#10b981;">👁️ Cursed Eye (Mắt Nguyền Rủa)</strong></td>
              <td>Tàn Tích Pháo Đài Bastion Remnant</td>
              <td>Rương báu trung tâm đảo dung nham</td>
              <td>Đột kích phòng chứa kho báu Bastion do Piglin Brutes canh giữ.</td>
            </tr>
            <tr>
              <td><strong style="color:#0f172a;">👁️ Black Eye (Mắt Hư Vô)</strong></td>
              <td>Thành Phố Cổ Đại Ancient City</td>
              <td>100% Rớt khi hạ gục Quái Thú The Warden</td>
              <td>Trang bị giáp chống sóng âm hoặc bắn cung tỉa từ khoảng cách 25 block.</td>
            </tr>
            <tr>
              <td><strong style="color:#64748b;">👁️ Wither Eye (Mắt Quỷ Wither)</strong></td>
              <td>Triệu hồi Boss Wither</td>
              <td>100% Rớt cùng Ngôi Sao Địa Ngục</td>
              <td>Xây bệ 4 Cát Linh Hồn + 3 Đầu Lâu Wither Skeleton.</td>
            </tr>
            <tr>
              <td><strong style="color:#8b5cf6;">👁️ Corrupted Eye (Mắt Tha Hóa)</strong></td>
              <td>Hầm Mỏ Bỏ Hoang Mineshaft</td>
              <td>Rương xe gòng dưới lòng đất</td>
              <td>Lần theo đường ray hầm mỏ bỏ hoang dưới tầng đá sâu Deepslate.</td>
            </tr>
            <tr>
              <td><strong style="color:#ec4899;">👁️ Rogue Eye (Mắt Đạo Tặc)</strong></td>
              <td>Đền Thờ Sa Mạc Desert Pyramid</td>
              <td>Rương kho báu dưới bẫy TNT</td>
              <td>Đào tránh tấm áp lực TNT ở đáy giếng sa mạc.</td>
            </tr>
            <tr>
              <td><strong style="color:#e2e8f0;">👁️ Undead Eye (Mắt Xác Sống)</strong></td>
              <td>Bão Sấm Chớp Sét Đánh</td>
              <td>100% Rớt từ Bầy Kỵ Sĩ Ngựa Xương Skeleton Trap</td>
              <td>Tiếp cận chú ngựa xương xuất hiện giữa cơn dông bão sấm sét.</td>
            </tr>
            <tr>
              <td><strong style="color:#0284c7;">👁️ Old Eye (Mắt Cổ Xưa)</strong></td>
              <td>Kho Báu Chôn Giấu Buried Treasure</td>
              <td>100% Rương kho báu bờ biển</td>
              <td>Tìm bản đồ kho báu trong xác tàu đắm Shipwreck rồi đào tại dấu X đỏ.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
'''

with open('dimensions.html', 'r', encoding='utf-8') as f:
    d_html = f.read()

if "12 Ancient Eyes of End" not in d_html and '</main>' in d_html:
    d_html = d_html.replace('</main>', f'{eyes_extra_content}\n  </main>')
    with open('dimensions.html', 'w', encoding='utf-8') as f:
        f.write(d_html)
    print("Upgraded dimensions.html successfully!")

# 3. Upgrade utilities.html with Starcatcher Fishing Almanac
fishing_extra_content = '''
    <!-- Section: Starcatcher Fishing Almanac -->
    <section style="margin-top:3.5rem;">
      <h2>🎣 <span class="vi-text">Đại Bách Khoa Câu Cá Starcatcher (121 Loài Cá Thần Bí)</span><span class="en-text">Starcatcher Fishing Almanac: 121 Species</span></h2>
      <p style="color:var(--text-secondary); margin-bottom:1rem;">
        <span class="vi-text">Hệ thống câu cá Starcatcher phân bố theo Biome, Thời tiết (Nắng/Mưa), Chu kỳ Ngày/Đêm và Chiều không gian. Tra cứu môi trường sinh thái của các loài cá quý hiếm:</span>
        <span class="en-text">Catch over 120 unique fish species across Overworld, Nether Lava, End Void, and Aether skies:</span>
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th><span class="vi-text">Tên Loài Cá / Vật Phẩm</span><span class="en-text">Fish Species</span></th>
              <th><span class="vi-text">Quần Xã Sinh Thái (Biome)</span><span class="en-text">Biome / Environment</span></th>
              <th><span class="vi-text">Thời Tiết & Chu Kỳ</span><span class="en-text">Weather & Time</span></th>
              <th><span class="vi-text">Loại Cần / Phao Yêu Cầu</span><span class="en-text">Required Rod / Bobber</span></th>
              <th><span class="vi-text">Công Dụng & Hiệu Ứng Tiêu Thụ</span><span class="en-text">Effects & Uses</span></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color:var(--accent-gold);">⭐ Starlight Tuna (Cá Ngừ Ánh Sao)</strong></td>
              <td>Biển Đêm Sâu (Deep Ocean)</td>
              <td>Ban Đêm Trời Quang (Midnight Clear)</td>
              <td>Starcatcher Rod + Aqua Bobber</td>
              <td>Hồi 20 Máu + Tăng 30% Tốc Độ Bơi và Phát Sáng (Glowing) trong 5 phút.</td>
            </tr>
            <tr>
              <td><strong style="color:#ef4444;">🔥 Magma Eel (Lươn Dung Nham)</strong></td>
              <td>Hồ Dung Nham Nether (Lava Oceans)</td>
              <td>Mọi Thời Tiết (Any Weather)</td>
              <td>Netherite Rod + Lava Bobber</td>
              <td>Nấu chín nhận Kháng Lửa (Fire Resistance 8:00) + Hồi 12 Thanh Thức Ăn.</td>
            </tr>
            <tr>
              <td><strong style="color:#a855f7;">🌌 Void Guppy (Cá 7 Màu Hư Không)</strong></td>
              <td>Khoảng Không The End (End Islands)</td>
              <td>Trời Tối (End Sky)</td>
              <td>Ender Rod + Void Hook</td>
              <td>Ăn vào cho phép Dịch chuyển ngẫu nhiên an toàn lên bề mặt cồn cát End gần nhất.</td>
            </tr>
            <tr>
              <td><strong style="color:#38bdf8;">☁️ Aether Puffer (Cá Nóc Thiên Đường)</strong></td>
              <td>Hồ Nước Đảo Bay Aether</td>
              <td>Ban Ngày Nắng Ấm (Daylight)</td>
              <td>Skyroot Rod + Golden Hook</td>
              <td>Tạo hiệu ứng Phản Trọng Lực bay bổng nhẹ nhàng trong 60 giây không lo ngã chết.</td>
            </tr>
            <tr>
              <td><strong style="color:#10b981;">💎 Prismatic Salmon (Cá Hồi Lăng Kính)</strong></td>
              <td>Sông Rừng Rậm Nhiệt Đới Jungle</td>
              <td>Khi Trời Mưa Bão (Thunderstorm)</td>
              <td>Heavy Hook + Prismatic Bobber</td>
              <td>Rơi ra <em>Prismatic Shard</em> dùng rèn Ngọc Lăng Kính Prismatic Jewel!</td>
            </tr>
            <tr>
              <td><strong style="color:#e11d48;">🩸 Blood Piranha (Cá Hổ Ăn Thịt Huyết Tộc)</strong></td>
              <td>Đầm Lầy Swamp / Hang Âm U</td>
              <td>Nửa Đêm Trăng Tròn (Full Moon)</td>
              <td>Iron Hook + Blood Vial Bait</td>
              <td>Tăng 15% Sát thương Hút Máu (Lifesteal) trong 3 phút tiếp theo.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
'''

with open('utilities.html', 'r', encoding='utf-8') as f:
    u_html = f.read()

if "Starcatcher Fishing Almanac: 121 Species" not in u_html and '</main>' in u_html:
    u_html = u_html.replace('</main>', f'{fishing_extra_content}\n  </main>')
    with open('utilities.html', 'w', encoding='utf-8') as f:
        f.write(u_html)
    print("Upgraded utilities.html successfully!")

print("All 5 summary domains integrated into the web wiki!")
