# Báo cáo Thực hành Lab 01: Git cơ bản, Refactor & Baseline
---

### Câu hỏi phụ: Cấu hình `--global` lưu ở đâu và khác gì với `--local`?

#### 1. Vị trí lưu file cấu hình `--global`
File cấu hình `--global` được lưu tại thư mục cá nhân (User Home) trên máy tính:
* **Windows:** `C:\Users\<Tên_User>\.gitconfig`
* **Linux / macOS:** `~/.gitconfig`

#### 2. So sánh `--global` và `--local`

| Tiêu chí | Git `--global` | Git `--local` |
| :--- | :--- | :--- |
| **Phạm vi áp dụng** | Áp dụng cho **tất cả các repository** trên toàn bộ máy tính cá nhân. | Chỉ áp dụng duy nhất cho **repository hiện tại** đang đứng. |
| **Vị trí lưu trữ** | Thư mục Home của User (`~/.gitconfig`). | Thư mục cấu hình ẩn của dự án ([`.git/config`](../.git/config)). |
| **Thứ tự ưu tiên** | Mức ưu tiên thấp hơn (bị `--local` ghi đè nếu cài đặt trùng tên). | **Ưu tiên cao nhất** (Git luôn dùng cấu hình local trước). |
| **Mục đích sử dụng** | Đặt thông tin mặc định chung (`user.name`, `user.email`, editor). | Cài đặt thông tin riêng cho từng dự án (ví dụ: dùng email trường học cho repo này, email cá nhân cho repo khác). |

---

### Câu 1: Vì sao lại sử dụng lệnh `git mv` thay vì di chuyển file thủ công?

* **Bảo toàn lịch sử thay đổi (Git History):** Lệnh `git mv` báo cho Git biết đây là hành động **di chuyển/đổi tên file (renamed)** thay vì coi đó là 2 hành động riêng biệt (xóa file cũ ở thư mục gốc và tạo file mới trong thư mục [`aims/`](../aims/))[cite: 3, 4].
* **Truy vết lịch sử commit liên tục:** Nhờ dùng `git mv`, khi kiểm tra bằng lệnh `git log --follow -- aims/cart.py` hoặc xem tab *Files changed* trên Pull Request, toàn bộ lịch sử commit từ trước khi di chuyển file vẫn được liên kết và theo dõi đầy đủ[cite: 3, 4].
* **Review code rõ ràng:** Tránh làm rác commit và giúp thành viên khác khi xem PR thấy ngay bản chất của sự thay đổi là cấu trúc lại thư mục chứ không phải viết mới hoàn toàn[cite: 4].

---

### Câu 2: Nhánh/Tag `release/lab01` có phải là một Baseline không? Vì sao?

* **Đúng, đây là một Baseline (điểm mốc cơ sở):** Nhánh hoặc tag [`release/lab01`](../) đóng vai trò là mốc kiểm soát phiên bản chuẩn cho bài thực hành Lab 01.
* **Ý nghĩa của Baseline:**
  * **Đóng băng mã nguồn (Code Freeze):** Đánh dấu mốc mã nguồn đã hoàn thiện, ổn định và sẵn sàng bàn giao/chấm điểm cho phẩn Lab 01.
  * **Căn cứ đối chiếu:** Tạo điểm chuẩn cố định để khi tiếp tục phát triển các tính năng ở bài sau (Lab 02, Lab 03...), bạn luôn có thể quay lại điểm mốc này để kiểm tra hoặc so sánh mà không lo bị ảnh hưởng bởi code mới.

---

### Câu 3: Vì sao không nên commit trực tiếp vào nhánh `master` dù chỉ làm việc một mình?

* **Tuân thủ quy trình chuẩn (Workflow Best Practices):** Việc tạo nhánh phụ (`refactor/apply-release-flow`) và gộp qua Pull Request giúp rèn luyện thói quen làm việc chuẩn mực như trong các dự án thực tế hoặc dự án nhóm[cite: 3, 4].
* **Giữ nhánh `master` luôn luôn ổn định:** Nhánh `master` chỉ đại diện cho mã nguồn chính thức đã qua kiểm thử (chạy thành công [`main.py`](../main.py))[cite: 3]. Mọi thao tác thử nghiệm hay refactor được cô lập hoàn toàn trên nhánh riêng[cite: 3].
* **Dễ dàng kiểm tra và khắc phục sự cố:** Làm việc trên nhánh riêng giúp bạn kiểm tra toàn bộ điểm khác biệt (diff) trước khi merge[cite: 4]. Nếu gặp lỗi nghiêm trọng trong quá trình refactor, bạn có thể dễ dàng xóa nhánh phụ đó đi mà không làm hỏng hay làm bẩn lịch sử của nhánh `master`[cite: 4].