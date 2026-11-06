# Báo cáo Thực hành Lab 05: Hotfix flow & bảo trì nhiều phiên bản

---

### 1. So sánh chiến lược Upstream First và Release First

| Chi tiết | Chiến lược Upstream First | Chiến lược Release First (Dùng trong Lab 05) |
| :--- | :--- | :--- |
| **Luồng thực hiện** | Sửa lỗi trực tiếp trên nhánh chính (`main`/`master`) trước, sau đó `cherry-pick` hoặc gộp ngược về các nhánh `release/*` đang hỗ trợ. | Sửa lỗi trên nền bản release cũ (`release/lab04`), sau đó `cherry-pick` lan truyền về `main` và các nhánh release mới hơn (`release/lab05`). |
| **Ưu điểm** | - Nhánh `main` luôn được ưu tiên có bản sửa lỗi sớm nhất.<br>- Tránh tình trạng quên lan truyền lỗi về nhánh chính.<br>- Quy trình nhất quán với hầu hết các dự án mã nguồn mở (như Linux Kernel, Kubernetes). | - Tạo bản hotfix nhanh chóng trên đúng môi trường mã nguồn của phiên bản đang bị lỗi (không lẫn code mới).<br>- Giảm nguy cơ phát sinh xung đột phức tạp do `main` đã thay đổi quá nhiều so với bản release cũ. |
| **Nhược điểm** | - Khi `cherry-pick` ngược về nhánh release cũ dễ gặp xung đột lớn nếu mã nguồn `main` đã tái cấu trúc (refactor) nhiều.<br>- Phải cẩn thận tách biệt commit sửa lỗi để không kéo theo code tính năng chưa phát hành. | - Dễ dẫn đến nguy cơ **quên lan truyền** bản sửa lỗi lên `main` hoặc các nhánh release khác.<br>- Phải quản lý nhiều nhánh hotfix tạm thời và thao tác `cherry-pick` nhiều lần. |

---

### 2. Phát hiện quên lan truyền bản sửa lỗi sang `release/lab05` bằng lệnh ở Phần F

Nếu quên lan truyền bản sửa lỗi hotfix sang nhánh `release/lab05`, các câu lệnh kiểm toán ở **Phần F** sẽ phát hiện như sau:

1. **Lệnh `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`:**
   * **Hiện tượng:** Chỉ in ra **1 commit** (commit lan truyền lên `main`), thay vì **2 commit** như kỳ vọng.
2. **Lệnh chạy vòng lặp kiểm tra tự động (Automated Behavioral Test):**
   * Nếu bổ sung mốc `release/lab05` vào vòng lặp kiểm thử:
     ```bash
     for ref in v1.0.1 v1.1.0 release/lab05 main; do ... done
     ```
   * **Kết quả phát hiện:** Mốc `release/lab05` sẽ in ra số **`0`** (tìm không ra đĩa do chưa sửa lỗi case-sensitive), trong khi `v1.0.1` và `main` in ra **`1`**.

---

### Câu hỏi: Vì sao ở Phần A chưa gắn tag `v1.1.0`?

* **Trạng thái đóng băng kiểm thử (Code Freeze / Release Candidate):** 
  Nhánh `release/lab05` được tạo ở Phần A mới chỉ đại diện cho giai đoạn chuẩn bị phát hành. Nhánh này cần được "đóng băng" để chạy kiểm thử cuối cùng và sẵn sàng tích hợp các bản sửa lỗi quan trọng phát sinh từ bản cũ (như hotfix `#20`).
* **Tính bất biến của Tag (Tag Immutability):** 
  Tag đại diện cho mốc phát hành chính thức đến tay người dùng. Nếu gắn tag `v1.1.0` ngay ở Phần A, bản phát hành đó sẽ thiếu mất bản sửa lỗi `#20`.
* **Tránh hạ cấp / tạo phiên bản thừa (`v1.1.1`):** 
  Hoãn gắn tag cho đến Phần E (sau khi đã tích hợp xong hotfix) giúp phiên bản `v1.1.0` chính thức ra mắt chứa đầy đủ cả tính năng mới lẫn bản sửa lỗi, mà không bắt buộc phải tăng số phiên bản lên `v1.1.1`.