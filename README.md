# IT3180 - AIMS-mini

Ứng dụng cửa hàng DVD tối giản được viết bằng Python, phục vụ thực hành
quy trình phát triển phần mềm, kiểm thử và làm việc với Git.

## Chức năng

- Quản lý giỏ hàng:
  - Thêm tối đa 20 DVD.
  - Xóa DVD.
  - Tính tổng tiền và tổng tiền sau giảm giá.
  - In nội dung giỏ hàng.
- Sắp xếp DVD theo tiêu đề hoặc giá.
- Tìm kiếm DVD theo tiêu đề:
  - Tìm chuỗi con.
  - Không phân biệt chữ hoa/chữ thường.
- Tìm kiếm DVD theo thể loại:
  - Tìm chuỗi con.
  - Không phân biệt chữ hoa/chữ thường.
- Kiểm tra dữ liệu bằng unit test với `unittest`.

## Yêu cầu

- Python 3.10 trở lên.
- Git (khuyến nghị khi thực hành các workflow trong tài liệu lab).
- Không yêu cầu thư viện bên ngoài.

## Hướng dẫn chạy

Mở PowerShell hoặc Git Bash tại thư mục gốc của repository, sau đó chạy:

```bash
# Chạy chương trình mẫu
python main.py

# Chạy toàn bộ unit test
python -m unittest discover -s tests -v
```

## Kết quả mẫu

Kết quả khi chạy `python main.py`:

```text
AIMS-mini v1.0.0
The disc has been added
The disc has been added
The disc has been added
***********************CART***********************
Ordered Items:
1. DVD - The Lion King - Animation - Roger Allers - 87: 19.95 $
2. DVD - Star Wars - Science Fiction - George Lucas - 87: 24.95 $
3. DVD - Aladdin - Animation -  - 0: 18.99 $
Total cost: 63.89 $
***************************************************
Total cost: 63.89 $
```

Kết quả kiểm thử thành công hiện tại:

```text
Ran 7 tests
OK
```

## Các mốc làm việc

| Mốc | Nội dung | Tài liệu |
| :---: | :--- | :--- |
| Lab 01 | Thiết lập môi trường và Refactor flow | [tl_lab01.md](docs/tl_lab01.md) |
| Lab 02 | Feature/Topic flow và Pull Request | [tl_lab02.md](docs/tl_lab02.md) |
| Lab 03 | Bugfix flow, xử lý xung đột và hoàn tác | [tl_lab03.md](docs/tl_lab03.md) |
| Lab 04 | Release flow và phiên bản phát hành | [tl_lab04.md](docs/tl_lab04.md) |
| Lab 05 | Hotfix flow và bảo trì nhiều phiên bản | [tl_lab05.md](docs/tl_lab05.md) |

Các thay đổi chức năng và bản sửa lỗi được ghi nhận trong
[CHANGELOG.md](CHANGELOG.md).

## Cấu trúc repository

```text
.
├── aims/
│   ├── __init__.py
│   ├── cart.py              # Giỏ hàng và các thao tác trên giỏ
│   ├── dvd.py               # Mô hình DigitalVideoDisc
│   └── search_by_title.py   # Tìm kiếm theo title và category
├── docs/
│   ├── tl_lab01.md          # Báo cáo Lab 01
│   ├── tl_lab02.md          # Báo cáo Lab 02
│   ├── tl_lab03.md          # Báo cáo Lab 03
│   ├── tl_lab04.md          # Báo cáo Lab 04
│   ├── tl_lab05.md          # Báo cáo Lab 05
│   └── use-cases.md         # Use case của hệ thống
├── tests/
│   ├── test_cart.py         # Test chức năng giỏ hàng
│   └── test_search.py       # Test chức năng tìm kiếm
├── main.py                  # Điểm bắt đầu chạy chương trình
├── CHANGELOG.md             # Lịch sử thay đổi
└── README.md                # Tài liệu hướng dẫn
```
