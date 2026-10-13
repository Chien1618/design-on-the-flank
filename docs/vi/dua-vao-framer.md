# Đưa code vào Framer

Bạn chỉ cần sao chép và dán. Không cần đọc hiểu code.

## Thêm một component mới

1. Trong câu trả lời của AI, mở file `.tsx` hoặc tìm khung code và bấm **Copy**. Sao chép toàn bộ code; không lấy phần giải thích hay dấu bao khung code.
2. Mở dự án trong Framer.
3. Mở **Assets** ở bên trái, tìm **Code** và chọn **Create Code File**. Nếu Framer hỏi loại file, chọn component. Tên menu có thể thay đổi theo phiên bản.
4. Đặt tên dễ nhớ, ví dụ `ParticleScene`.
5. Bấm vào vùng soạn thảo code, chọn toàn bộ nội dung mẫu bằng **Cmd+A** trên Mac hoặc **Ctrl+A** trên Windows. Dán code AI đã tạo để thay thế toàn bộ.
6. Chờ Framer lưu và xử lý code. Nếu có thông báo lỗi màu đỏ, xem [hướng dẫn sửa lỗi](go-loi.md).
7. Tìm component vừa tạo trong Assets và kéo vào trang.
8. Chọn đúng component trên trang. Chỉnh các thiết lập trong bảng bên phải.
9. Mở **Preview** để thử hành vi khi xem trang.

“Canvas” là vùng bạn thiết kế trang. “Preview” là chế độ xem thử. Một số hiệu ứng chỉ chạy đầy đủ trong Preview.

## Thử các thiết lập

- Đổi tiêu đề và kiểm tra chữ trên component thay đổi.
- Đổi màu và tốc độ chuyển động nếu có.
- Bật/tắt một thiết lập nếu có.
- Thu hẹp chiều rộng để xem nội dung trên màn hình nhỏ.
- Thử rê chuột, chạm hoặc cuộn trong Preview tùy hiệu ứng.

## Cập nhật component đang dùng

1. Giữ một bản sao code cũ trước khi thay đổi.
2. Gửi code hiện tại cho AI và nói phần cần sửa.
3. Mở **đúng file code cũ** trong Framer.
4. Thay toàn bộ nội dung bằng bản hoàn chỉnh mới.
5. Kiểm tra lại nội dung và thiết lập trên các instance đã dùng.

Không cần tạo file mới nếu chỉ cập nhật component cũ. Các giá trị bạn từng chỉnh có thể được Framer giữ lại; thay đổi giá trị mặc định trong code không nhất thiết thay đổi các instance đã có.

Tham khảo: [Framer Code Components](https://www.framer.com/developers/components-introduction).
