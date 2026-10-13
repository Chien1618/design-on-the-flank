# Nội dung để đưa lên website

Đây là bộ nội dung và tệp tải xuống, chưa phải một website đã triển khai. Người đọc cuối không cần xem GitHub hay hướng dẫn kỹ thuật của repository.

## Các trang

| Đường dẫn web đề xuất | File nội dung |
|---|---|
| `/` | `web/landing.vi.md` |
| `/start` | `docs/vi/bat-dau.md` |
| `/setup/chatgpt` | `docs/vi/chatgpt.md` |
| `/setup/claude` | `docs/vi/claude.md` |
| `/setup/codex` | `docs/vi/codex.md` |
| `/setup/claude-code` | `docs/vi/claude-code.md` |
| `/framer` | `docs/vi/dua-vao-framer.md` |
| `/prompts` | `docs/vi/prompt-mau.md` |
| `/help` | `docs/vi/go-loi.md` |
| `/faq` | `docs/vi/faq.md` |

Chuyển liên kết Markdown tương đối sang các đường dẫn web ở bảng này. Trên website, thay các link tải GitHub trong tài liệu bằng URL file đã upload để người dùng bấm tải trực tiếp. Các liên kết đến `docs/validation.md`, `LICENSE.md`, `CHANGELOG.md` có thể trỏ về GitHub hoặc các trang phụ tương ứng trên web. Giữ nguyên liên kết tài liệu chính thức.

## Nút tải xuống

Upload các file trong `downloads/` vào kho file của website rồi gắn nút tới URL thực. Cách này giúp người dùng không cần hiểu giao diện GitHub.

| Nút | File |
|---|---|
| Tải skill cho Claude | `design-on-the-flank-skill.zip` |
| Hướng dẫn lưu trong ChatGPT Project (tùy chọn) | Nội dung `chatgpt-instructions.txt` |
| Tải tài liệu ChatGPT | `design-on-the-flank-knowledge.txt` |
| Thử nhanh bằng tài liệu | `design-on-the-flank-knowledge.txt` |
| Tải component ví dụ | `FlankCard.tsx` |

Nếu muốn liên kết tải trực tiếp từ GitHub, dùng URL raw thực của file, ví dụ `https://raw.githubusercontent.com/Chien1618/design-on-the-flank/main/downloads/design-on-the-flank-skill.zip`. Chỉ dùng sau khi xác minh repository đã public và URL tải thành công. Liên kết nhánh `main` lấy bản mới nhất; dùng tag phiên bản khi cần cố định bản tải.

## Gợi ý trình bày

- Cho chọn Codex hoặc ChatGPT trước khi hiển thị các bước; để đường dẫn Claude/Claude Code bên dưới.
- Đặt nút Copy cạnh từng prompt; hiện thông báo “Đã sao chép” khi thành công.
- Với ChatGPT, mặc định chỉ hiện tải một tài liệu và đính kèm vào chat. Để cách tạo Project trong phần tùy chọn “Muốn dùng thường xuyên?”.
- Với Claude, ghi “Giữ nguyên file ZIP, không giải nén”.
- Có đường lui “Không thấy mục này?” dẫn đến cách dùng một file trong chat.
- Hiện phiên bản và trạng thái thử nghiệm; không ghi “đã kiểm thử trên mọi AI”.
- Dùng ảnh chụp giao diện thật khi bổ sung ảnh; không tạo ảnh giả nút hoặc menu.

Không đưa script build, lệnh Git, cấu trúc repository hay hướng dẫn cho người bảo trì vào luồng cài đặt của người dùng.
