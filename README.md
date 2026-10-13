# Design on the Flank

Tạo component Framer bằng cách mô tả thứ bạn muốn: một cảnh 3D xoay theo chuột, nền hạt chuyển động, hiệu ứng shader trên ảnh, hay một đoạn kể chuyện chạy theo cuộn trang.

AI trả lại một file code hoàn chỉnh. Bạn sao chép vào Framer rồi chỉnh màu, tốc độ, hình ảnh và các thiết lập đã yêu cầu trong bảng Properties.

## Bạn dùng AI nào?

- **Codex:** gửi tin nhắn cài đặt bên dưới.
- **ChatGPT:** [tải file bắt đầu](https://github.com/Chien1618/design-on-the-flank/raw/refs/heads/main/downloads/design-on-the-flank-knowledge.txt), đính kèm vào chat rồi mô tả component. [Xem từng bước](docs/vi/chatgpt.md).
- **Claude:** [tải gói ZIP](https://github.com/Chien1618/design-on-the-flank/raw/refs/heads/main/downloads/design-on-the-flank-skill.zip) và thêm trong mục Skills. [Xem từng bước](docs/vi/claude.md).
- **Claude Code:** [cài bằng một tin nhắn](docs/vi/claude-code.md).

Gửi cho Codex:

```text
Cài giúp tôi skill Design on the Flank từ:
https://github.com/Chien1618/design-on-the-flank/tree/main/skills/design-on-the-flank
Giữ đủ các file tài liệu đi kèm. Nếu có bản cũ, giữ lại chỉnh sửa của tôi trước khi cập nhật. Cài xong hãy báo cho tôi.
```

Sau khi cài, thử yêu cầu:

```text
Dùng Design on the Flank tạo một component Framer: đám hạt 3D chuyển động theo chuột, khi cuộn thì gom thành một quả cầu. Cho tôi chỉnh màu, số hạt, tốc độ và mức phản ứng với chuột trong Framer. Trả toàn bộ code trong một khung để tôi sao chép một lần. Tôi không biết code.
```

[Cách dán code vào Framer](docs/vi/dua-vao-framer.md) · [Các ý tưởng khác](docs/vi/prompt-mau.md) · [Khi gặp lỗi](docs/vi/go-loi.md)

## Có những gì?

| Phần | Nội dung |
|---|---|
| Framer | Component, Property Controls, responsive, overrides, CMS và WebGL |
| Three.js | Scene, geometry, material, ánh sáng, texture, model, animation, interaction, shader và postprocessing |
| GSAP | Đủ 8 skill chính thức của GreenSock: core, timeline, ScrollTrigger, plugins, utils, React, performance và frameworks |
| Framer plugins | Tài liệu riêng khi bạn muốn làm plugin |

Một skill chính dẫn đến từng chủ đề nhỏ. AI đọc phần cần cho yêu cầu đang làm. Với ChatGPT, file bắt đầu chứa mục lục có link; nếu không mở được link, AI sẽ đưa đúng file cần bạn tải và đính kèm.

Bản **0.2.0** có nội dung từ **20 skill và 6 tài liệu tham khảo**, chia thành **384 phần**. UI/UX Pro Max đã được loại khỏi gói. [Mục lục kỹ thuật](skills/design-on-the-flank/references/catalog.md) · [Nguồn và giấy phép](skills/design-on-the-flank/ATTRIBUTION.md).

Một file code vẫn có thể cần thư viện hoặc model/ảnh bên ngoài. AI phải nói rõ những gì cần thêm và đã kiểm tra tới đâu. Gói tài liệu đã được kiểm tra cấu trúc; chưa thử toàn bộ quy trình tạo component trên từng nền tảng AI và Framer. [Chi tiết kiểm tra](docs/validation.md).
