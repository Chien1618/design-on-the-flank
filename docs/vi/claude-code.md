# Dùng với Claude Code

Nếu bạn dùng Claude để trò chuyện thông thường, hãy mở [hướng dẫn Claude](claude.md).

## Cài bằng một tin nhắn

1. Mở Claude Code trong một thư mục làm việc.
2. Gửi toàn bộ lời nhắn sau:

> Hãy tải skill Design on the Flank từ https://github.com/Chien1618/design-on-the-flank/tree/main/skills/design-on-the-flank và cài làm personal skill trong ~/.claude/skills/design-on-the-flank/. Giữ nguyên cấu trúc SKILL.md, references và assets. Nếu đã có skill cùng tên, cho tôi biết trước khi thay thế. Chỉ tải các file của skill, không chạy script lạ. Kiểm tra cài đặt xong rồi hướng dẫn tôi dùng. Tôi không biết code; hãy tự làm những thao tác công cụ của bạn cho phép.

3. Thực hiện bước cho phép truy cập nếu Claude Code yêu cầu đúng các thao tác cài đặt trên.
4. Khi đã cài thành công, gửi: **“Dùng /design-on-the-flank tạo một thẻ giới thiệu Framer có chữ và màu chỉnh được.”** Nếu chưa nhận diện, bắt đầu phiên mới.

## Nếu không cài được

Dùng [tài liệu một file trong cuộc trò chuyện](bat-dau.md#thu-nhanh), hoặc gửi thông báo lỗi để AI giải thích bước cần làm. Bạn không cần tự học lệnh terminal.

## Khi cập nhật

Nhờ Claude Code so sánh phiên bản, giữ lại bản cũ và các chỉnh sửa cá nhân trước khi cập nhật. Skill không tự cập nhật.

Tiếp theo: [Đưa code vào Framer](dua-vao-framer.md).

Tham khảo: [Claude Code Skills](https://code.claude.com/docs/en/skills). Gói này chưa được thử cài trong một phiên Claude Code sạch; xem [trạng thái kiểm tra](../validation.md).
