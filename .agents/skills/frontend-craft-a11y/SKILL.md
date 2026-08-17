---
name: frontend-craft-a11y
description: >-
  Tiêu chuẩn kỹ nghệ Frontend: Tối ưu Accessibility (A11y), Contrast Ratio WCAG AAA,
  Semantic HTML5, SVG Vector Rendering, và tối ưu hóa trải nghiệm trên mọi thiết bị (Responsive Mobile-First).
---

# Frontend Craft & Accessibility (A11y) Skill

Skill này đảm bảo mọi sản phẩm web luôn đạt độ hoàn thiện cao nhất về mặt kỹ thuật, khả năng tiếp cận và độ tương thích đa nền tảng.

---

## 1. TIÊU CHUẨN TƯƠNG PHẢN & ACCESSIBILITY (WCAG 2.1)
- **Độ tương phản màu chữ**: Đảm bảo tỉ lệ tương phản tối thiểu `4.5:1` cho văn bản thường và `3:1` cho tiêu đề lớn trên nền tối.
- **Trợ năng bàn phím**: Mọi nút bấm, liên kết và modal đều hỗ trợ điều hướng qua phím `Tab`, `Enter`, `Escape`.
- **Thẻ Semantic HTML5**: Luôn sử dụng `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` thay vì lạm dụng `<div>`.

---

## 2. VECTOR SVG CHUẨN ĐỘ PHÂN GIẢI CAO
- Sử dụng SVG nội suy trực tiếp với `viewBox` cho logo, icon hệ phái, cổng không gian.
- Không lo vỡ nét (pixelation) khi phóng to trên màn hình Retina / 4K.
- Dung lượng siêu nhẹ (< 1KB mỗi icon) giúp đạt điểm Google Lighthouse 100/100 về hiệu năng tải trang.

---

## 3. RESPONSIVE BREAKPOINTS CHUẨN
```css
/* Mobile */
@media (max-width: 640px) { ... }

/* Tablet */
@media (max-width: 1024px) { ... }

/* Desktop Large */
@media (min-width: 1280px) { ... }
```
