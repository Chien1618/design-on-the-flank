# Design on the Flank

**Mô tả bằng lời. Nhận một file code. Sao chép vào Framer.**

Bộ hướng dẫn giúp AI tạo Framer Code Components có các thiết lập chỉnh trực tiếp trong bảng Properties. Dành cho người không biết code, dùng với Codex, Claude Code, Claude và ChatGPT.

**[Bắt đầu tại đây →](docs/vi/bat-dau.md)**

## Chọn AI bạn đang dùng

| AI | Hướng dẫn | Tệp cần tải |
|---|---|---|
| Codex | [Cài bằng một tin nhắn](docs/vi/codex.md) | AI tải skill từ repository này |
| Claude Code | [Cài bằng một tin nhắn](docs/vi/claude-code.md) | AI tải skill từ repository này |
| Claude | [Upload skill](docs/vi/claude.md) | [Skill ZIP](downloads/design-on-the-flank-skill.zip) |
| ChatGPT | [Thiết lập Project](docs/vi/chatgpt.md) | [Instructions](downloads/chatgpt-instructions.txt) + [Knowledge](downloads/design-on-the-flank-knowledge.txt) |
| Chỉ muốn thử trong một cuộc trò chuyện | [Cách dùng nhanh](docs/vi/bat-dau.md#thu-nhanh) | [Bộ hướng dẫn một file](downloads/design-on-the-flank-knowledge.txt) |

Trên GitHub, khi mở tệp để tải, chọn **Download raw file** (biểu tượng tải xuống) nếu tệp chưa tự tải. Không cần tải toàn bộ repository.

## Sau khi thiết lập

Sao chép câu này vào AI:

> Dùng Design on the Flank. Tạo một thẻ giới thiệu cho Framer, có tiêu đề, mô tả, màu nền, màu chữ, khoảng cách bên trong và bo góc chỉnh được. Xuất một file TSX hoàn chỉnh và hướng dẫn mình dán vào Framer. Mình không biết code.

Tiếp theo: **[Đưa code vào Framer](docs/vi/dua-vao-framer.md)** · [Prompt mẫu](docs/vi/prompt-mau.md) · [Gặp lỗi](docs/vi/go-loi.md) · [Câu hỏi thường gặp](docs/vi/faq.md)

## Trạng thái bản 0.1.0

Đây là bản thử nghiệm đầu tiên. Gói được tạo từ một nguồn chung. [Báo cáo kiểm tra](docs/validation.md) ghi rõ phần đã kiểm tra và phần còn cần thử trong ứng dụng thật. Skill hướng dẫn AI; nó không tự kết nối hoặc xuất bản website Framer và không bảo đảm mọi kết quả AI đều chạy ngay.

## For maintainers

Canonical source: `skills/design-on-the-flank/`. User-facing documentation is Vietnamese; agent instructions are English and ask the AI to answer in the user's language.

- [Publishing and rebuild guide](docs/maintainer.md)
- [Website copy and download-button mapping](web/README.md)
- [Changelog](CHANGELOG.md)
- [Usage permission](LICENSE.md)

Downloads are intentionally committed for direct website links. Rebuild with `python3 scripts/build.py`, then validate with `python3 scripts/validate.py`. End users do not need Python or a terminal.
