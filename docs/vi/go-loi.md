# Nếu component chưa hoạt động

Không cần tự sửa những dòng code bạn không hiểu. Gửi lại thông tin để AI sửa toàn bộ file.

| Bạn nhìn thấy gì? | Việc nên làm |
|---|---|
| Framer báo lỗi màu đỏ | Sao chép nguyên thông báo lỗi hoặc chụp ảnh; gửi cùng code hiện tại cho AI |
| Component trống | Kiểm tra đã kéo vào trang, có kích thước nhìn thấy được và đã chọn ảnh/dữ liệu bắt buộc chưa |
| Không thấy các mục chỉnh | Chọn trực tiếp component thay vì khung bao ngoài; kiểm tra file code có báo lỗi không |
| Chỉnh một mục nhưng không có tác dụng | Gửi tên mục, giá trị đã chọn và ảnh kết quả; yêu cầu AI kiểm tra control có nối vào component không |
| Code mới nhưng nội dung vẫn cũ | Kiểm tra giá trị đã lưu trên instance; Framer có thể giữ thiết lập trước đó |
| Animation không chạy trên Canvas | Mở Preview; nếu vẫn lỗi, nói rõ lỗi xuất hiện ở Canvas hay Preview |
| Mất ảnh hoặc dữ liệu sau khi sửa | Giữ lại code cũ và yêu cầu AI kiểm tra việc đổi tên props; không xóa instance đang có vội |
| Chạy tốt một cái, lỗi khi thêm cái thứ hai | Gửi tình huống hai instance; yêu cầu AI kiểm tra ID, CSS và trạng thái có bị dùng chung không |

## Tin nhắn sửa lỗi có thể sao chép

> Component này chưa hoạt động đúng. Mình không biết code. Đây là code hiện tại và ảnh/thông báo lỗi. Mình đang thử ở [Canvas hoặc Preview]. Kết quả mong muốn là [mô tả]. Kết quả hiện tại là [mô tả]. Hãy sửa đúng nguyên nhân, giữ các props và chức năng khác, rồi trả toàn bộ file TSX để mình thay thế một lần. Nói rõ bạn đã kiểm tra gì.

Nếu code đã bị thay nhiều lần, gửi phiên bản hiện tại và phiên bản gần nhất hoạt động đúng. Tránh yêu cầu AI đoán nội dung file mà nó chưa được xem.
