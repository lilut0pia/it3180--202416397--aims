# Báo cáo Thực hành Lab 03: Bugfix flow, xung đột & hoàn tác


---


#### 1. Merge Base là gì?
* **Khái niệm:** **Merge base** (gốc gộp) là **commit chung gần nhất (most recent common ancestor)** giữa hai hoặc nhiều nhánh trong Git.
* **Vai trò trong quá trình Merge / Rebase:**
  * Khi thực hiện gộp nhánh (ví dụ: gộp `feature/discount` vào `master`), Git sẽ tự động tìm điểm **Merge base** của hai nhánh này.
  * Git so sánh sự thay đổi của nhánh `master` kể từ Merge base với sự thay đổi của nhánh `feature/discount` kể từ Merge base để thực hiện thuật toán **3-way merge** (gộp 3 chiều).
* **Ứng dụng thực tế:** Merge base giúp Git xác định chính xác những đoạn code nào mới được thêm/sửa ở mỗi nhánh, từ đó tự động hợp nhất code hoặc cảnh báo các đoạn code bị xung đột (conflict).

---

#### 2. Vì sao các nhánh chính/công khai (`master`, `release/*`) bắt buộc phải dùng `revert` thay vì `reset`?
* **Bảo vệ lịch sử chung (Shared History):** Các nhánh như `master` hoặc `release/*` đã được push lên remote và có nhiều thành viên trong team cùng pull về máy local. Sử dụng `git reset` sẽ **xóa bỏ commit và viết lại lịch sử**, làm cho nhánh local của các thành viên khác bị lệch mốc (diverged history), gây lỗi và xung đột nghiêm trọng cho toàn bộ đội phát triển.
* **Tính minh bạch và kiểm toán (Auditability):** `git revert` không xóa vết cũ mà tạo một **commit mới** có nội dung đảo ngược lại thay đổi của commit bị lỗi. Điều này giữ cho lịch sử dự án hoàn toàn minh bạch: ghi nhận rõ ràng tính năng đó đã được thêm vào khi nào và bị hủy bỏ ở thời điểm nào.
* **Tuân thủ quy trình kiểm duyệt (PR Workflow):** Nhánh `master` thường được áp dụng quy tắc bảo vệ nhánh (Branch Protection Rules) ngăn chặn commit/force-push trực tiếp. Việc dùng `revert` cho phép tạo một nhánh sửa lỗi riêng (ví dụ `bugfix/revert-...`), đẩy lên GitHub và mở Pull Request để cả team review trước khi chính thức hoàn tác trên nhánh chính.