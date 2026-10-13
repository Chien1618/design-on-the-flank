# Design on the Flank

Bạn muốn làm một nút, thẻ giới thiệu hay phần hỏi đáp cho website Framer? Bộ hướng dẫn này giúp Codex hoặc ChatGPT viết code để bạn sao chép vào Framer. Chữ, màu và các thiết lập bạn yêu cầu sẽ được đưa vào bảng chỉnh bên phải.

Chọn ứng dụng bạn đang dùng và làm theo bên dưới.

## Tôi dùng Codex

**1. Mở Codex, sao chép tin nhắn này và gửi:**

```text
Cài giúp tôi skill Design on the Flank từ link này:
https://github.com/Chien1618/design-on-the-flank/tree/main/skills/design-on-the-flank

Cài xong hãy báo cho tôi. Nếu không cài được, nói rõ tôi cần làm gì tiếp theo.
```

**2. Khi Codex báo đã cài xong, gửi yêu cầu của bạn.** Ví dụ:

```text
Dùng Design on the Flank tạo một thẻ giới thiệu cho Framer.
Thẻ có tiêu đề, mô tả và nền màu kem. Tôi muốn chỉnh chữ, màu và bo góc trong Framer.
Trả toàn bộ code để tôi sao chép một lần, rồi chỉ tôi cách dán vào Framer.
```

**3. Lấy code Codex trả về và làm theo [cách dán vào Framer ở dưới](#dua-vao-framer).**

[Nếu Codex không cài được →](docs/vi/codex.md)

## Tôi dùng ChatGPT

**1. [Tải tài liệu này](https://github.com/Chien1618/design-on-the-flank/raw/refs/heads/main/downloads/design-on-the-flank-knowledge.txt).**

**2. Mở một cuộc trò chuyện mới trong ChatGPT.** Bấm nút đính kèm file cạnh ô nhắn tin, chọn file vừa tải, rồi gửi tin nhắn này:

```text
Đọc tài liệu tôi đính kèm và dùng nó để tạo component Framer trong cuộc trò chuyện này.

Tạo cho tôi một thẻ giới thiệu có tiêu đề, mô tả và nền màu kem. Tôi muốn chỉnh chữ, màu và bo góc trong Framer.
Trả toàn bộ code để tôi sao chép một lần, rồi chỉ tôi cách dán vào Framer.
```

**3. Lấy code ChatGPT trả về và làm theo [cách dán vào Framer ở dưới](#dua-vao-framer).**

Tiếp tục nhờ sửa hoặc tạo thêm trong cùng cuộc trò chuyện. Nếu mở cuộc trò chuyện mới, đính kèm lại tài liệu.

<details>
<summary>Bấm tải nhưng trình duyệt chỉ hiện chữ?</summary>

Nhấn **Ctrl+A** rồi **Ctrl+C** để sao chép toàn bộ trang. Trên Mac, dùng **Cmd+A** rồi **Cmd+C**. Dán vào ChatGPT và gửi trước, sau đó gửi yêu cầu tạo component ở trên.

</details>

<details>
<summary>Muốn lưu tài liệu để dùng cho nhiều cuộc trò chuyện?</summary>

[Làm theo cách tạo Project trong ChatGPT](docs/vi/chatgpt.md#luu-lai).

</details>

<a id="dua-vao-framer"></a>
## Có code rồi, dán vào Framer ở đâu?

1. Bấm **Copy** ở khung code AI trả về. Nếu AI trả file, nhờ nó hiện toàn bộ code trong chat để bạn sao chép.
2. Mở dự án Framer → **Assets** → **Code** → **Create Code File**. Chọn **Component** nếu được hỏi.
3. Đặt tên, ví dụ **MyCard**. Bấm vào phần code mẫu, chọn tất cả rồi dán code vừa sao chép để thay thế.
4. Chờ Framer xử lý. Kéo **MyCard** từ Assets vào trang.
5. Chọn thẻ trên trang để chỉnh chữ, màu và bo góc ở bảng bên phải. Mở **Preview** để xem thử.

Bạn có thể thay yêu cầu “thẻ giới thiệu” bằng thứ mình muốn tạo, hoặc gửi thêm ảnh tham khảo cho AI.

## Nếu có lỗi

Chụp lại lỗi, gửi cho AI trong cuộc trò chuyện đang làm và nhắn:

```text
Tôi dán code vào Framer và gặp lỗi này. Hãy sửa rồi gửi lại toàn bộ code để tôi thay một lần. Giữ nguyên những phần khác.
```

Khi sửa, mở lại **file code cũ** trong Framer và thay nội dung. Giữ một bản sao code cũ để quay lại nếu cần.

---

Dùng Claude? [Xem cách cài](docs/vi/claude.md). Dùng Claude Code? [Xem tại đây](docs/vi/claude-code.md).

[Thêm câu yêu cầu mẫu](docs/vi/prompt-mau.md) · [Hướng dẫn Framer chi tiết](docs/vi/dua-vao-framer.md) · [Câu hỏi thường gặp](docs/vi/faq.md)

Bản 0.1.0 đang thử nghiệm. Code AI tạo ra vẫn cần được kiểm tra trong Framer. [Xem phần đã kiểm tra](docs/validation.md).

<details>
<summary>Tài liệu cho người quản lý bộ skill và website</summary>

[Nội dung đưa lên web](web/README.md) · [Cách cập nhật bộ skill](docs/maintainer.md) · [Lịch sử thay đổi](CHANGELOG.md) · [Quyền sử dụng](LICENSE.md)

</details>
