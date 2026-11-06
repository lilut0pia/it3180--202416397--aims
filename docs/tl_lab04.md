# Báo cáo Thực hành Lab 04: Release flow & phiên bản phát hành

---

### Câu hỏi: Vì sao chuẩn bị trên `master` (hoặc `main`) trước, không sửa trên nhánh `release/*`?

* **Tuân thủ luồng công việc chuẩn (Git Workflow Standards):** 
  Nhánh `main` đóng vai trò là dòng phát triển chính (Mainline Development). Việc nâng version trong mã nguồn (`__version__ = "1.0.0"`), cập nhật `main.py` và hoàn thiện file `CHANGELOG.md` ngay trên `main` đảm bảo mọi lịch sử chuẩn bị phát hành đều được lưu trữ lại đầy đủ tại mốc gốc phát triển.
* **Dễ dàng rẽ nhánh phát hành (Clean Release Branching):** 
  Sau khi `main` đã có đầy đủ mã nguồn chính thức, số phiên bản `1.0.0` và `CHANGELOG.md` hoàn chỉnh, việc cắt nhánh phát hành `release/lab04` từ `main` sẽ tạo ra một nhánh phát hành sạch sẽ, sẵn sàng đóng gói mà không cần thêm các commit sửa đổi lặt vặt.
* **Tránh xung đột và lệch lịch sử (Prevent Drift & Conflicts):** 
  Nếu sửa phiên bản và `CHANGELOG.md` trực tiếp trên nhánh `release/*`, sau khi đóng gói xong bạn lại phải tốn thêm bước gộp (merge/rebase) ngược về lại `main`. Điều này dễ dẫn đến nguy cơ quên đồng bộ khiến `main` bị trễ lịch sử hoặc phát sinh xung đột không đáng có.

---

### Câu hỏi 1: Vì sao nhánh `release/*` trong quy trình bài lab không merge ngược lại vào `main`? So sánh với GitFlow chuẩn.

#### 1. Nguyên nhân không merge ngược lại `main` trong bài lab
* **Khởi tạo trực tiếp từ `main`:** Trong quy trình bài lab, nhánh `release/lab04` được cắt ra từ `main` **sau khi** `main` đã hoàn tất toàn bộ công tác chuẩn bị phát hành.
* **Không có sửa lỗi phát sinh trên `release` (No Drift):** Vì không thực hiện thêm commit sửa lỗi (hotfix/bugfix) nào trực tiếp trên nhánh `release/lab04`, mã nguồn trên `release/lab04` và `main` tại mốc cắt nhánh là hoàn toàn đồng nhất.
* **Quy trình đơn giản hóa:** Nhánh `release/lab04` đóng vai trò như một mốc "đóng băng" (code freeze) để đóng gói và gắn tag `v1.0.0`. Việc không gộp ngược giúp tránh các merge commit thừa trên `main`.

#### 2. So sánh với quy trình GitFlow chuẩn

| Tiêu chí | Quy trình thực hành trong Lab | Quy trình GitFlow chuẩn |
| :--- | :--- | :--- |
| **Nhánh chính** | Sử dụng 1 nhánh chính duy nhất là `main`. | Sử dụng song song 2 nhánh chính lâu dài: `main` (sản phẩm) và `develop` (phát triển). |
| **Điểm xuất phát `release/*`** | Cắt nhánh `release/*` từ `main` sau khi đã chuẩn bị xong. | Cắt nhánh `release/*` từ `develop` khi đã đủ tính năng. |
| **Đồng bộ sau Release** | Gắn tag trên `release/*` và giữ nhánh release làm mốc đóng băng. | Sau khi hoàn thiện, gộp `release/*` **vào cả `main` lẫn `develop`**, sau đó mới xóa nhánh release. |
| **Mức độ phức tạp** | Nhẹ nhàng, phù hợp với nhóm vừa và nhỏ hoặc mô hình GitHub Flow. | Phức tạp hơn, phù hợp dự án enterprise lớn có chu kỳ phát hành dài. |

---

### Câu hỏi 2: Vì sao phiên bản này được nâng lên `1.0.0` mà không phải là `0.4.0`?

* **Quy tắc Đánh số phiên bản ngữ nghĩa (Semantic Versioning - SemVer):**
  * Định dạng phiên bản theo chuẩn SemVer có dạng **`MAJOR.MINOR.PATCH`** (ví dụ: `1.0.0`).
  * Các phiên bản `0.x.x` (như `v0.1.0`, `v0.2.0`, `v0.3.0` ở các bài lab trước) đại diện cho giai đoạn **thử nghiệm / phát triển ban đầu (Initial Development)**, nơi API và cấu trúc mã nguồn chưa ổn định.
* **Cột mốc sản phẩm chính thức (Production Ready / General Availability):**
  * Việc chuyển từ `0.3.0` lên **`1.0.0`** đánh dấu mốc dự án AIMS-mini đã đạt mức **hoàn thiện tính năng cốt lõi**, mã nguồn ổn định, đáp ứng đầy đủ yêu cầu nghiệp vụ và sẵn sàng phát hành chính thức.
* **Khác biệt với `0.4.0`:**
  * Tăng lên `0.4.0` chỉ thể hiện một bản cập nhật tính năng nhỏ bổ sung trong giai đoạn thử nghiệm (`0.x`).
  * Nâng thẳng lên `1.0.0` thể hiện cam kết về tính ổn định và tương thích lâu dài của bộ mã nguồn.

---

### Câu hỏi 3: Báo cáo Kiểm toán Cấu hình (Configuration Audit) & Ghi nhận trạng thái (Status Accounting)

#### 1. Phân biệt `git switch --detach` và `git worktree`

| Tiêu chí | `git switch --detach` | `git worktree` |
| :--- | :--- | :--- |
| **Cơ chế** | Đổi trạng thái làm việc của thư mục hiện tại về một commit/tag cũ (detached HEAD). | Tạo một thư mục làm việc mới độc lập chứa commit/tag chỉ định. |
| **Ưu điểm** | Nhanh chóng, không tốn thêm dung lượng đĩa. | Mở song song nhiều phiên bản cùng lúc mà không làm gián đoạn nhánh đang làm việc. |
| **Phù hợp cho** | Xem lại nhanh code/chạy thử giao diện bản cũ. | Thực hiện test tự động, debug song song giữa 2 bản phát hành. |

#### 2. Kết quả đối soát trạng thái & Checklist kiểm toán `v1.0.0`
* **Đối soát nhánh:** Lệnh `git log --oneline main..release/lab04` trả về kết quả rỗng, xác nhận nhánh `main` đã chứa đầy đủ code của nhánh release.
* **Kiểm tra phiên bản & Tệp rác:** Lệnh `git show v1.0.0:aims/__init__.py` xác nhận `__version__ = "1.0.0"`, và `git ls-tree -r --name-only v1.0.0` xác nhận mã nguồn sạch không đính kèm tệp rác biên dịch (`.pyc`, `__pycache__`).
* **Kết quả Test & Đóng gói:** Đã thực thi toàn bộ Unit Test thành công (báo `OK`) trên bản `v1.0.0` thông qua `worktree`, và đóng gói mã nguồn sạch dạng tệp `aims-1.0.0.zip` bằng câu lệnh `git archive`.