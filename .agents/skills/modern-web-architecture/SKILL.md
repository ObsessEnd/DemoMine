---
name: modern-web-architecture
description: >-
  Kiến trúc web hiện đại chuẩn SEO, hiệu năng cao, tối ưu hóa cấu trúc tệp tĩnh,
  hệ thống Song ngữ (Bilingual i18n), Global Search (Fuzzy Matching), và lưu trữ trạng thái LocalStorage.
---

# Modern Web Architecture Skill

Skill này định nghĩa các khuôn mẫu kiến trúc web chuẩn mực, giúp ứng dụng web tải nhanh, dễ bảo trì và tối ưu trải nghiệm người dùng.

---

## 1. CẤU TRÚC MULTI-PAGE & MODULAR TỐI ƯU
- **Tách bạch rõ ràng**:
  ```
  project-root/
  ├── css/            # Style tokens, theme variables, layout, components
  ├── js/             # data.js (Dữ liệu tĩnh), app.js (Controller)
  ├── images/         # SVG Icons, assets, diagrams
  ├── index.html      # Trang chủ Hub
  └── [topic].html    # Các trang chuyên đề độc lập
  ```
- **Lợi ích**: Tương thích 100% với GitHub Pages, Netlify, Vercel hoặc chạy trực tiếp offline qua giao thức `file://` mà không cần server phức tạp.

---

## 2. HỆ THỐNG SONG NGỮ (LIGHTWEIGHT I18N)
- Sử dụng CSS selector kết hợp `body.lang-vi` / `body.lang-en`:
  ```css
  body.lang-vi .en-text { display: none !important; }
  body.lang-en .vi-text { display: none !important; }
  ```
- Chuyển đổi ngôn ngữ bằng 1 click mà không cần tải lại trang hay gọi API nặng nề.
- Lưu trạng thái vào `localStorage.getItem('wiki_lang')`.

---

## 3. TÌM KIẾM TOÀN CỤC (FAST IN-MEMORY SEARCH)
- Sử dụng cơ chế tìm kiếm trong bộ nhớ với phím tắt nhanh (`/` hoặc `Ctrl+K`).
- Đóng mở modal mượt mà với `backdrop-filter: blur(6px)`.
- Hiển thị kết quả tức thì kèm danh mục, chỉ số và liên kết trực tiếp.
