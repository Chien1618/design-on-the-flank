# Bắt đầu với Design on the Flank

Bạn mô tả thứ mình muốn tạo. AI viết code. Bạn sao chép code vào Framer rồi chỉnh chữ, màu sắc và các thiết lập như chỉnh một component thông thường.

**Bạn không cần học lập trình hoặc gõ lệnh.** Bạn cần một tài khoản AI và một dự án Framer có thể chỉnh sửa code. Một số tính năng AI phụ thuộc tài khoản hoặc cài đặt của tổ chức.

## 1. Chọn ứng dụng của bạn

- Dùng **ChatGPT**: [làm theo hướng dẫn ChatGPT](chatgpt.md).
- Dùng **Claude** để trò chuyện: [làm theo hướng dẫn Claude](claude.md).
- Dùng ứng dụng **Codex**: [làm theo hướng dẫn Codex](codex.md).
- Dùng **Claude Code** để làm việc với file: [làm theo hướng dẫn Claude Code](claude-code.md).

Nếu chưa phân biệt được Claude và Claude Code: nếu bạn thường mở Claude rồi trò chuyện, hãy chọn hướng dẫn **Claude**.

## 2. Nói cho AI biết bạn muốn gì

Sao chép câu này để thử:

> Dùng Design on the Flank. Tạo một thẻ giới thiệu trong Framer với tiêu đề, mô tả, màu nền kem và bo góc. Cho mình chỉnh chữ, màu nền, màu chữ, khoảng cách bên trong và bo góc trong Properties. Xuất một file TSX hoàn chỉnh. Mình không biết code.

Bạn có thể đính kèm ảnh tham khảo và nói thêm điều gì cần giống ảnh. Không cần biết tên kỹ thuật của hiệu ứng.

## 3. Đưa kết quả vào Framer

AI sẽ trả một file có đuôi `.tsx` hoặc một khung chứa code. Đây là phần bạn cần sao chép nguyên vẹn. [Xem hướng dẫn từng bước](dua-vao-framer.md).

## 4. Chỉnh bằng bảng thiết lập

Chọn component trên trang Framer. Các mục như chữ, màu và bo góc xuất hiện trong bảng bên phải. “Props” là các thiết lập của component; “Property Controls” là những ô chỉnh thiết lập đó.

<a id="thu-nhanh"></a>
## Thử nhanh trong một cuộc trò chuyện

Chưa muốn cài? Tải [tài liệu một file](../../downloads/design-on-the-flank-knowledge.txt), đính kèm vào cuộc trò chuyện và gửi:

> Đọc tài liệu Design on the Flank mình đính kèm và áp dụng khi tạo component Framer trong cuộc trò chuyện này. Mình không biết code. Hãy xuất toàn bộ code trong một file TSX hoặc một khung code để mình sao chép.

Sau đó gửi yêu cầu tạo component. Cách này chỉ cung cấp hướng dẫn cho cuộc trò chuyện đó; không cài skill lâu dài. Nếu AI không đọc được file, mở file, sao chép nội dung và dán vào cuộc trò chuyện.

## Nếu kết quả chưa đúng

Gửi lại code hiện tại cùng ảnh hoặc thông báo lỗi cho AI. Nói rõ phần nào cần sửa và phần nào cần giữ. [Dùng prompt sửa lỗi có sẵn](go-loi.md).
