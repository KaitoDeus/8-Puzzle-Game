# BẢN ĐẶC TẢ YÊU CẦU DỰ ÁN CUỐI KÌ - MÔN TRÍ TUỆ NHÂN TẠO

## 1. Thông tin chung

- **Tên đề tài**: Nghiên cứu Heuristic, ứng dụng và so sánh 5 thuật toán tìm kiếm (BFS, DFS, IDDFS, Greedy Best-First Search, A\* Search) trong việc giải quyết trò chơi ghép hình N ô (N-Puzzle Game). Hiển thị thông số cho mỗi thuật toán tìm kiếm được, xây dựng thêm các tính năng phụ cho phép user chèn ảnh, sử dụng stack để quản lý các bước đi redo/undo.
- **Nhóm thực hiện**: Nhóm 4 (5 Thành viên)
- **Hạn chót (Deadline)**: 24/04/2026
- **Công nghệ sử dụng**:
  - **Ngôn ngữ**: Python 3.13
  - **Thư viện đồ họa**: Pygame
  - **Tiêu chuẩn lập trình**: OOP, SOLID, Design Patterns.
  - **Phương pháp**: Phát triển nhanh với sự hỗ trợ của AI Agent.

---

## 2. Mục tiêu đề tài

Nghiên cứu và triển khai các thuật toán tìm kiếm từ cơ bản đến nâng cao để giải quyết bài toán N-Puzzle. So sánh hiệu năng giữa các thuật toán dựa trên các tiêu chí: thời gian thực thi (ms) và số lượng nút (states) đã duyệt. Đồng thời, xây dựng một ứng dụng có giao diện người dùng (UI/UX) mượt mà, hỗ trợ tùy biến hình ảnh.

---

## 3. Danh sách các thuật toán triển khai

Dự án tập trung vào 5 thuật toán chính để giải quyết bài toán N-Puzzle (ví dụ: 8-Puzzle):

1.  **Breadth-First Search (BFS)**: Tìm kiếm theo chiều rộng, đảm bảo tìm ra lời giải ngắn nhất nhưng tiêu tốn bộ nhớ.
2.  **Depth-First Search (DFS)**: Tìm kiếm theo chiều sâu, không đảm bảo tối ưu và dễ rơi vào vòng lặp vô tận nếu không xử lý tốt.
3.  **Iterative Deepening DFS (IDDFS)**: Kết hợp ưu điểm của BFS và DFS, giới hạn độ sâu để tìm lời giải.
4.  **Greedy Best-First Search**: Tìm kiếm tham lam dựa trên hàm Heuristic (ước lượng khoảng cách đến đích).
5.  **A\* Search**: Thuật toán tìm kiếm tối ưu nhất trong bài toán này, sử dụng hàm $f(n) = g(n) + h(n)$.
    - _Các hàm Heuristic dự kiến_: Manhattan Distance, Hamming Distance (Misplaced Tiles).

---

## 4. Đặc tả chức năng (Functional Requirements)

### 4.1. Quản lý Trò chơi

- **Khởi tạo**: Tạo trạng thái ngẫu nhiên (có thể giải được) của bàn cờ 3x3.
- **Giải bài toán**: Người dùng chọn thuật toán và nhấn "Solve", hệ thống sẽ hiển thị các bước di chuyển tự động để về trạng thái đích.
- **Trạng thái đích (Goal State)**:
  ```
  1 2 3
  4 5 6
  7 8 0 (ô trống)
  ```

### 4.2. Xử lý hình ảnh nâng cao

- **Hình ảnh mặc định**: Khi mở ứng dụng, hệ thống tải sẵn một hình ảnh mặc định và chia thành 8 mảnh ghép.
- **Tùy biến hình ảnh**:
  - Cho phép người dùng tải lên ảnh bất kỳ (.jpg, .png).
  - Hệ thống tự động tính toán kích thước, cắt và gán hình ảnh vào các ô (tiles) tương ứng.

### 4.3. Đo lường và So sánh

- **Hiển thị thời gian**: Tính toán thời gian thực thi của thuật toán bằng miliseconds (ms).
- **Số bước giải**: Hiển thị tổng số bước cần di chuyển để đạt đích.
- **Bảng so sánh**: Một Dashboard nhỏ thống kê kết quả của các thuật toán khác nhau trên cùng một trạng thái đầu vào.

---

## 5. Yêu cầu phi chức năng (Non-functional Requirements)

- **Giao diện (UI/UX)**:
  - Sử dụng **Pygame** để tạo hiệu ứng di chuyển mảnh ghép mượt mà.
  - Màu sắc hài hòa, bố cục dễ nhìn, trực quan.
- **Kiến trúc phần mềm**:
  - **SOLID**: Đảm bảo code dễ bảo trì và mở rộng.
  - **Design Patterns**: Áp dụng các mẫu thiết kế phổ biến (Strategy, Factory) để cấu trúc code rõ ràng, giúp AI Agent dễ dàng bảo trì và mở rộng.
- **Hiệu năng**: Hệ thống không được treo khi thực hiện các thuật toán phức tạp (sử dụng Multi-threading).

---

## 6. Giao diện dự kiến (Mockup)

Bản thiết kế giao diện (Pygame) đề xuất cho dự án:
![Mockup giao diện](assets/mockup.png)
_Hình ảnh minh họa: Bàn cờ 3x3 bên trái, bảng điều khiển và thống kê hiệu năng bên phải._

---

## 7. Phân công công việc (Task Assignment)

Dự án được chia đều cho 5 thành viên với các trách nhiệm cụ thể:

| STT | Thành viên       | Thuật toán phụ trách           | Nhiệm vụ bổ trợ (Làm chung UI)                                                             |
| :-- | :--------------- | :----------------------------- | :----------------------------------------------------------------------------------------- |
| 1   | **Thành viên A** | **Breadth-First Search (BFS)** | - Khởi tạo khung project (Boilerplate).<br>- Quản lý trạng thái bàn cờ.                    |
| 2   | **Thành viên B** | **Depth-First Search (DFS)**   | - Xử lý logic di chuyển của các tiles.<br>- Tối ưu bộ nhớ cho tìm kiếm.                    |
| 3   | **Thành viên C** | **Iterative Deepening DFS**    | - Xử lý hình ảnh (Cắt ảnh, Upload ảnh).<br>- Tích hợp hiệu ứng animation.                  |
| 4   | **Thành viên D** | **Greedy Best-First Search**   | - Nghiên cứu và cài đặt Heuristic (Hamming).<br>- Thiết kế Dashboard kết quả.              |
| 5   | **Thành viên E** | **A\* Search**                 | - Nghiên cứu và cài đặt Heuristic (Manhattan).<br>- Module đo lường Benchmark (ms, nodes). |

---

**Lưu ý**: Giao diện (Pygame UX/UI) là nhiệm vụ **chung**, tất cả các thành viên cùng tham gia xây dựng và kết nối module thuật toán của mình vào giao diện chính.

---

## 7. Quy trình thực hiện dự án (Rút gọn)

1.  **Giai đoạn 1 (10/04 - 17/04)**: Hoàn thành logic AI, thuật toán tìm kiếm và xử lý hình ảnh.
2.  **Giai đoạn 2 (18/04 - 24/04)**: Tích hợp giao diện Pygame, tối ưu hóa hiệu năng, kiểm thử và đóng gói.
    **Hạn chót nộp dự án: 24/04/2026.**
