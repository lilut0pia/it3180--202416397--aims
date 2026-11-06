# Báo cáo Thực hành Lab 02: Feature/Topic flow & Pull Request

---

#### 1. Vì sao phải đồng bộ (sync/pull) nhánh `master` trước khi tạo Pull Request?
* **Phát hiện và giải quyết xung đột sớm (Conflict Resolution):** Trong quá trình bạn làm việc trên nhánh phụ, nhánh `master` có thể đã có thêm các commit mới từ các thành viên khác. Việc pull `master` về và gộp vào nhánh phụ trước giúp bạn tự xử lý các xung đột (if any) ngay tại máy local thay vì để xảy ra xung đột trên PR.
* **Đảm bảo tính tương thích của mã nguồn:** Giúp bạn kiểm thử lại toàn bộ chương trình (`python main.py`) trên máy local với phiên bản `master` mới nhất, đảm bảo tính năng mới không làm hỏng các phần code người khác vừa cập nhật.
* **Tạo điều kiện cho Merge thuận lợi (Clean Merge):** Giúp Pull Request trên GitHub ở trạng thái sẵn sàng merge (Able to merge) mà không bị chặn bởi các xung đột tự động.

---

#### 2. Khi nào KHÔNG ĐƯỢC dùng lệnh `git rebase`?
* **KHÔNG rebase trên các nhánh công khai (Public / Shared Branches):** Như nhánh `master`, `main` hoặc các nhánh tính năng đang có nhiều người cùng tham gia làm việc chung.
* **Lý do (Quy tắc vàng của Rebase):** 
  * `git rebase` hoạt động bằng cách **viết lại lịch sử commit** (thay đổi SHA-1 hash của các commit).
  * Nếu bạn rebase một nhánh đã được push lên remote và người khác đã pull nhánh đó về, việc viết lại lịch sử sẽ làm lệch nhánh local của đồng nghiệp, gây ra xung đột nghiêm trọng và làm rối loạn toàn bộ `git log` của nhóm.
* **Lời khuyên:** Chỉ dùng `rebase` trên các nhánh cá nhân (Private Feature Branch) local chưa push, hoặc nhánh riêng của bạn trước khi gộp vào `master`.

---

#### 3. Sự khác nhau giữa cách đặt tên `feature/*` và `topic/*` là gì?

| Tiêu chí | Nhánh `feature/*` (Feature Branch) | Nhánh `topic/*` (Topic Branch) |
| :--- | :--- | :--- |
| **Phạm vi & Quy mô** | Dùng cho các **tính năng nghiệp vụ lớn**, có kế hoạch rõ ràng (ví dụ: `feature/add-discount-card`, `feature/payment-vnpay`). | Dùng cho các **nhiệm vụ nhỏ, ngắn hạn** hoặc thử nghiệm một ý tưởng/chủ đề cụ thể (ví dụ: `topic/pr-template`, `topic/fix-css`). |
| **Vòng đời (Lifespan)** | Thường tồn tại lâu hơn, trải qua nhiều commit và qua nhiều giai đoạn kiểm thử. | Vòng đời rất ngắn, thường tạo ra để xử lý nhanh 1 task rồi merge và xóa nhánh ngay trong ngày. |
| **Quy trình áp dụng** | Phổ biến trong các mô hình như Git Flow, GitHub Flow chuẩn cho phát triển phần mềm. | Thường dùng trong các nhiệm vụ cấu hình, tài liệu (docs), hoặc thử nghiệm nhanh (experimental concept). |