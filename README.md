# Design on the Flank

Bộ AI skill dành cho việc xây dựng **Framer Code Components với Three.js, WebGL và GSAP**. Sử dụng cùng Codex, Claude hoặc ChatGPT để tạo hiệu ứng 3D, chuyển động theo cuộn trang và các tương tác tùy chỉnh từ mô tả hoặc thiết kế tham khảo.

Mỗi component được tạo dưới dạng **một file TSX hoàn chỉnh** để sao chép vào Framer, kèm các thiết lập trong bảng **Properties**. Bạn có thể thay đổi nội dung, màu sắc, hình ảnh và thông số chuyển động mà không cần chỉnh sửa code.

## Khả năng

- **Đồ họa 3D:** cảnh sản phẩm, hệ thống hạt, vật liệu, ánh sáng và tương tác theo chuột hoặc cảm ứng.
- **Hiệu ứng WebGL:** biến dạng hình ảnh, gợn sóng, chuyển cảnh và shader tùy chỉnh.
- **Chuyển động GSAP:** timeline, hiệu ứng chữ, chuỗi chuyển cảnh và animation theo vị trí cuộn.
- **Tích hợp Framer:** bố cục responsive, Property Controls và chuyển đổi code có sẵn thành component sử dụng trong Framer.
- **Chỉnh sửa component:** bổ sung tính năng hoặc sửa lỗi trên code hiện tại, giữ các thiết lập không thuộc phạm vi thay đổi.

## Bắt đầu

Chọn nền tảng bạn đang sử dụng:

| Nền tảng | Cách sử dụng | Hướng dẫn |
|---|---|---|
| **Codex** | Gửi yêu cầu cài skill bên dưới | [Cài đặt với Codex](docs/vi/codex.md) |
| **Claude** | [Tải gói skill](https://github.com/Chien1618/design-on-the-flank/raw/refs/heads/main/downloads/design-on-the-flank-skill.zip) và thêm vào mục Skills | [Cài đặt với Claude](docs/vi/claude.md) |
| **Claude Code** | Yêu cầu AI cài skill vào môi trường làm việc | [Cài đặt với Claude Code](docs/vi/claude-code.md) |
| **ChatGPT** | [Tải tài liệu bắt đầu](https://github.com/Chien1618/design-on-the-flank/raw/refs/heads/main/downloads/design-on-the-flank-knowledge.txt) và đính kèm vào cuộc trò chuyện | [Sử dụng với ChatGPT](docs/vi/chatgpt.md) |

### Cài đặt nhanh với Codex

Sao chép yêu cầu sau vào Codex:

```text
Cài skill Design on the Flank từ repository này:
https://github.com/Chien1618/design-on-the-flank/tree/main/skills/design-on-the-flank

Cài đầy đủ tài liệu đi kèm. Nếu đã có phiên bản cũ, giữ lại các chỉnh sửa cá nhân trước khi cập nhật.
```

Sau khi cài đặt, bắt đầu cuộc trò chuyện mới và mô tả component bạn muốn tạo.

### Sử dụng với ChatGPT

Đính kèm tài liệu bắt đầu rồi gửi mô tả component. Nếu ChatGPT cần thêm tài liệu và không mở được đường dẫn, tải file được yêu cầu và gửi vào cùng cuộc trò chuyện. [Xem hướng dẫn chi tiết](docs/vi/chatgpt.md).

## Tạo component

1. **Mô tả kết quả mong muốn.** Nêu hiệu ứng, cách tương tác và những thông số cần chỉnh trong Framer. Có thể gửi thêm hình ảnh, video tham khảo hoặc code hiện tại.
2. **Nhận code hoàn chỉnh.** AI cung cấp một file TSX hoặc một khung code để sao chép toàn bộ.
3. **Đưa vào Framer.** Tạo Code Component, thay nội dung mẫu bằng code đã nhận rồi kéo component vào trang. [Hướng dẫn từng bước](docs/vi/dua-vao-framer.md).
4. **Tùy chỉnh và kiểm tra.** Điều chỉnh các thiết lập trong Properties, mở Preview để thử chuyển động và tương tác.

Với component sử dụng model 3D, ảnh hoặc dữ liệu riêng, cung cấp tài nguyên tương ứng và làm theo hướng dẫn thiết lập đi kèm code.

### Ví dụ yêu cầu

```text
Dùng Design on the Flank tạo một component Framer với hệ thống hạt 3D.

Các hạt phản ứng theo vị trí chuột và tập hợp thành hình cầu khi cuộn trang.
Cho phép chỉnh màu, số lượng hạt, tốc độ và mức phản ứng trong bảng Properties.
Trên điện thoại, hiệu ứng phản ứng với thao tác chạm.

Trả một file TSX hoàn chỉnh để sao chép vào Framer, kèm hướng dẫn sử dụng.
```

[Xem thêm yêu cầu mẫu](docs/vi/prompt-mau.md)

## Tài liệu

- [Đưa code vào Framer](docs/vi/dua-vao-framer.md)
- [Xử lý lỗi thường gặp](docs/vi/go-loi.md)
- [Câu hỏi thường gặp](docs/vi/faq.md)

## Nguồn và giấy phép

Bộ tài liệu tích hợp kiến thức Framer và Three.js từ [Framer Labs](https://github.com/fredm00n/framerlabs), cùng [GSAP Skills chính thức của GreenSock](https://github.com/greensock/gsap-skills).

[Điều khoản sử dụng](LICENSE.md) · [Nguồn tài liệu và giấy phép bên thứ ba](skills/design-on-the-flank/ATTRIBUTION.md)
