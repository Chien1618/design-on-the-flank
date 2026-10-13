# Tạo component bằng ChatGPT

Lần đầu, bạn chỉ cần một file tài liệu và một cuộc trò chuyện.

## 1. Tải tài liệu

[Bấm vào đây để tải](https://github.com/Chien1618/design-on-the-flank/raw/refs/heads/main/downloads/design-on-the-flank-knowledge.txt). File có tên **design-on-the-flank-knowledge.txt**.

Nếu trình duyệt hiện nội dung thay vì tải file, chọn toàn bộ bằng **Ctrl+A**, sao chép bằng **Ctrl+C**, rồi dán vào ChatGPT. Trên Mac, dùng phím **Cmd** thay cho **Ctrl**.

## 2. Gửi tài liệu cho ChatGPT

Mở cuộc trò chuyện mới. Bấm nút đính kèm file cạnh ô nhắn tin, rồi chọn file vừa tải. Nếu đã dán nội dung ở bước 1, gửi nội dung đó trước và đi tiếp bước 3.

## 3. Gửi yêu cầu của bạn

Sao chép câu này để thử:

```text
Đọc tài liệu tôi vừa cung cấp và dùng nó để tạo component Framer trong cuộc trò chuyện này.

Tạo cho tôi một thẻ giới thiệu có tiêu đề, mô tả và nền màu kem. Tôi muốn chỉnh chữ, màu và bo góc trong Framer.
Trả toàn bộ code để tôi sao chép một lần, rồi chỉ tôi cách dán vào Framer.
```

Sau này, thay phần mô tả bằng thứ bạn muốn tạo. Bạn cũng có thể gửi ảnh tham khảo.

## 4. Đưa code vào Framer

Bấm **Copy** ở khung code ChatGPT trả về, rồi làm theo [cách dán vào Framer](dua-vao-framer.md).

Nếu ChatGPT chia code thành nhiều phần hoặc chỉ gửi file, nhắn:

```text
Hiện toàn bộ code trong một khung duy nhất để tôi bấm Copy và dán một lần vào Framer.
```

Tiếp tục yêu cầu sửa trong cùng cuộc trò chuyện. Khi bắt đầu cuộc trò chuyện mới, gửi lại tài liệu.

<a id="luu-lai"></a>
## Muốn dùng thường xuyên?

Bạn có thể lưu tài liệu trong một **Project** để dùng cho nhiều cuộc trò chuyện ở cùng một nơi:

1. Trong ChatGPT, chọn **New project / Dự án mới** và đặt tên **Làm website Framer**.
2. Trong Project vừa tạo, chọn thêm file/nguồn và upload file tài liệu ở bước 1.
3. Mở cài đặt Project qua menu dấu ba chấm, tìm **Project instructions / Hướng dẫn**.
4. Dán đoạn bên dưới và lưu lại:

```text
Khi tôi yêu cầu tạo hoặc sửa component Framer, hãy đọc và áp dụng tài liệu Design on the Flank đã đính kèm trong Project.

Tôi cần toàn bộ code trong một file hoặc một khung code để sao chép vào Framer. Đưa các mục tôi muốn chỉnh vào bảng thiết lập của component. Khi sửa, giữ các thiết lập cũ nếu tôi không yêu cầu đổi. Hướng dẫn từng bước bằng tiếng Việt và nói rõ nếu chưa chạy thử trong Framer.
```

Sau đó bắt đầu các cuộc trò chuyện làm Framer **bên trong Project này**. Nếu không thấy Project, cứ dùng cách gửi file vào chat ở trên.

[Các câu yêu cầu khác để thử](prompt-mau.md) · [Quay lại trang chính](../../README.md)
