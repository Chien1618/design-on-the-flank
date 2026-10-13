---
slug: design-on-the-flank
title: Tạo component Framer với Codex hoặc ChatGPT
description: Chọn ứng dụng bạn đang dùng, gửi yêu cầu và sao chép code vào Framer. Có hướng dẫn từng bước từ lúc cài đến lúc chỉnh component trên trang.
---

# Bạn muốn thêm gì vào website Framer?

Một nút bấm, thẻ giới thiệu hay phần câu hỏi mở ra khi bấm? Bạn có thể nhờ Codex hoặc ChatGPT viết code, sau đó sao chép vào Framer để dùng.

Design on the Flank là tài liệu hướng dẫn AI làm việc đó. Chọn ứng dụng bạn đang dùng để bắt đầu.

## Tôi dùng Codex

Mở Codex và gửi tin nhắn này:

```text
Cài giúp tôi skill Design on the Flank từ link này:
https://github.com/Chien1618/design-on-the-flank/tree/main/skills/design-on-the-flank

Cài xong hãy báo cho tôi. Nếu không cài được, nói rõ tôi cần làm gì tiếp theo.
```

Khi Codex báo đã cài xong, gửi tiếp:

```text
Dùng Design on the Flank tạo một thẻ giới thiệu cho Framer.
Thẻ có tiêu đề, mô tả và nền màu kem. Tôi muốn chỉnh chữ, màu và bo góc trong Framer.
Trả toàn bộ code để tôi sao chép một lần, rồi chỉ tôi cách dán vào Framer.
```

[Bấm đây nếu Codex không cài được](../docs/vi/codex.md).

## Tôi dùng ChatGPT

1. [Tải tài liệu](../downloads/design-on-the-flank-knowledge.txt).
2. Mở một cuộc trò chuyện mới trong ChatGPT và đính kèm file vừa tải.
3. Gửi tin nhắn này:

```text
Đọc tài liệu tôi đính kèm và dùng nó để tạo component Framer trong cuộc trò chuyện này.

Tạo cho tôi một thẻ giới thiệu có tiêu đề, mô tả và nền màu kem. Tôi muốn chỉnh chữ, màu và bo góc trong Framer.
Trả toàn bộ code để tôi sao chép một lần, rồi chỉ tôi cách dán vào Framer.
```

Tiếp tục nhờ sửa hoặc tạo thêm trong cùng chat. Nếu mở chat mới, gửi lại tài liệu. [Xem hướng dẫn có hình thức lưu tài liệu trong Project](../docs/vi/chatgpt.md).

## Có code rồi thì làm gì?

1. Bấm **Copy** ở khung code AI trả về.
2. Mở Framer → **Assets** → **Code** → **Create Code File**.
3. Đặt tên file. Chọn toàn bộ code mẫu và thay bằng code vừa sao chép.
4. Kéo component vừa tạo từ Assets vào trang.
5. Chọn component để chỉnh chữ, màu và các thiết lập ở bảng bên phải. Mở **Preview** để thử.

[Nếu cần hướng dẫn chi tiết, xem tại đây](../docs/vi/dua-vao-framer.md).

Bạn có thể thay “thẻ giới thiệu” bằng thứ mình cần, hoặc gửi thêm một ảnh tham khảo cho AI.

## Nếu Framer báo lỗi

Chụp lại lỗi và gửi vào cuộc trò chuyện đang làm:

```text
Tôi dán code vào Framer và gặp lỗi này. Hãy sửa rồi gửi lại toàn bộ code để tôi thay một lần. Giữ nguyên những phần khác.
```

Mở lại file code cũ trong Framer để thay nội dung. Giữ một bản sao trước khi thay để có thể quay lại.

---

Dùng [Claude](../docs/vi/claude.md) hoặc [Claude Code](../docs/vi/claude-code.md)? Có hướng dẫn riêng cho bạn.

[Thêm câu yêu cầu mẫu](../docs/vi/prompt-mau.md) · [Câu hỏi thường gặp](../docs/vi/faq.md)

Bản 0.1.0 đang thử nghiệm. Code AI tạo ra vẫn cần được kiểm tra trong Framer.
