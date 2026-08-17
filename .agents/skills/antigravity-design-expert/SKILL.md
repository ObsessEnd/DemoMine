---
name: antigravity-design-expert
description: >-
  Chuyên gia thiết kế giao diện UI/UX cao cấp cho Web. Hướng dẫn tạo phong cách Spatial Depth,
  Glassmorphism, Weightless Floating Cards, Typography phân tầng sắc nét, Dark Fantasy/Deepslate
  Color Tokens và chuyển động Micro-interactions mượt mà.
---

# Antigravity Design Expert Skill

Skill này cung cấp tiêu chuẩn và quy trình thiết kế giao diện Web hiện đại, thẩm mỹ cao, tránh các lỗi giao diện cơ bản và rập khuôn.

---

## 1. NGUYÊN TẮC THIẾT KẾ CỐT LÕI (CORE PRINCIPLES)

### 1.1. Spatial Depth & Weightlessness (Không gian & Độ nổi)
- **Floating Cards**: Sử dụng đổ bóng đa tầng mềm mại thay vì viền thô cứng:
  ```css
  --shadow-float: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 10px 24px -2px rgba(0, 0, 0, 0.4);
  --shadow-hover: 0 10px 30px -4px rgba(0, 0, 0, 0.6), 0 0 16px rgba(0, 229, 163, 0.2);
  ```
- **Glassmorphism Chuẩn Mực**: Nền mờ bán trong suốt kết hợp viền ánh sáng:
  ```css
  background: rgba(18, 24, 36, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  ```

### 1.2. Bảng Màu Hài Hòa (Harmonious Color Palette)
- **Deep Slate / Dark Mode**:
  - Background chính: `#0a0d14` (Deep Void)
  - Container / Card: `#121824` / `#182030`
  - Border viền: `#26334d`
- **Màu Nhấn (Accent Glows)**:
  - Cyan / Emerald (Sinh lực / Năng lượng): `#00e5a3` (Glow: `rgba(0, 229, 163, 0.25)`)
  - Gold (Hoàng kim / Huyền thoại): `#fbbf24` (Glow: `rgba(251, 191, 36, 0.25)`)
  - Crimson (Sát thương / Boss): `#f43f5e` (Glow: `rgba(244, 63, 94, 0.25)`)
  - Purple (Hư không / Ma thuật): `#a855f7` (Glow: `rgba(168, 85, 247, 0.25)`)

### 1.3. Typography Phân Cấp Sắc Nét
- Heading Font: `Silkscreen` hoặc `Cinzel` (Pixel RPG / Fantasy feel)
- Body Font: `Inter`, `-apple-system`, sans-serif (Độ đọc tối ưu ở mọi kích cỡ)
- Letter-spacing: Header `+0.5px` đến `+1px`, Badge/Tag `+0.4px` (All Caps).

---

## 2. CHUYỂN ĐỘNG & MICRO-INTERACTIONS
- Tuyệt đối không dùng chuyển động tức thời (`0s`).
- Tiêu chuẩn: `transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);`
- Hover State: Nâng thẻ lên nhẹ (`transform: translateY(-4px);`) và kích hoạt viền phát sáng.

---

## 3. CÁC ĐIỀU CẤM KỴ (ANTI-PATTERNS)
- ❌ Không dùng font tím nhạt trên nền đen bệt thiếu chiều sâu.
- ❌ Không viền màu dạ quang quá dày hoặc chói mắt.
- ❌ Không nhồi nhét icon bừa bãi không có nhãn chú thích.
- ❌ Tránh card lồng nhau quá 3 lớp (Over-nested cards).
