# ĐỀ TÀI: Nghiên cứu Heuristic và Blind Search, ứng dụng và so sánh trong giải quyết trò chơi 8-Puzzle

## Mục lục

1. [Tên đề tài](#tên-đề-tài-nghiên-cứu-heuristic-và-blind-search-ứng-dụng-và-so-sánh-trong-giải-quyết-trò-chơi-8-puzzle)
2. [Phân công công việc](#phân-công-công-việc)
3. [Phân tích bài toán](#phân-tích-bài-toán)
4. [Các thuật toán sử dụng](#các-thuật-toán-sử-dụng)
5. [Giao diện chương trình](#giao-diện-chương-trình)
6. [Cài đặt và chạy dự án](#cài-đặt-và-chạy-dự-án)

---

## Phân công công việc

Nhóm thực hiện: Nhóm 4 (Gồm 5 thành viên)

| STT | Thành viên       | Nhiệm vụ chính                               |
| :-- | :--------------- | :------------------------------------------- |
| 1   | **Thành viên 1** | Cài đặt thuật toán BFS (Blind Search)        |
| 2   | **Thành viên 2** | Quản lý chuyển động & logic Undo/Redo        |
| 3   | **Thành viên 3** | Module chèn ảnh, Hiệu ứng animation          |
| 4   | **Thành viên 4** | Thiết kế UI/UX, hiệu ứng chuyển động phụ     |
| 5   | **Thành viên 5** | Cài đặt thuật toán A\* và Dashboard thống kê |

---

## Phân tích bài toán

### Mục đích bài toán

Bài toán 8-Puzzle là một dạng bài toán tìm kiếm cổ điển trong Trí tuệ nhân tạo. Mục tiêu là sắp xếp lại các mảnh ghép trên một ma trận 3x3 (gồm 8 ô số và 1 ô trống) từ một trạng thái xáo trộn bất kỳ đưa về trạng thái đích có thứ tự tiếp nối nhau bằng cách trượt các ô kề cận vào ô trống. Đề tài tập trung vào việc nghiên cứu, triển khai và đánh giá so sánh hiệu năng giữa hai triết lý tìm kiếm tiêu biểu: **Tìm kiếm mù (Breadth-First Search - BFS)** và **Tìm kiếm có kiến thức kinh nghiệm (A\* Search)**.

### Cách làm

Dự án được xây dựng mô phỏng trực quan bằng ngôn ngữ **Python** kết hợp với thư viện đồ họa **Pygame**:

- **Cấu trúc dữ liệu**: Sử dụng mảng 1 chiều để biểu diễn trạng thái bàn cờ, giúp tối ưu hóa quá trình tính toán, duyệt node và lưu trữ trong bộ nhớ thay vì mảng 2 chiều cơ bản.
- **Quản lý trạng thái (State Management)**: Khai báo lớp `PuzzleGame`, ứng dụng cấu trúc _Stack_ để theo dõi hệ thống lịch sử nước đi, hỗ trợ tính năng quay lui (Undo/Redo).
- **Hệ thống đánh giá khởi tạo**: Áp dụng kiểm tra **Số nghịch thế (Inversions)** nhằm đảm bảo mọi trạng thái bàn cờ được sinh ra ngẫu nhiên đều chắn chắn có lời giải (Solvable).

### Đóng góp mới so với các ứng dụng đã có

So với các chương trình mô phỏng 8-Puzzle truyền thống hoặc terminal CLI đơn giản đã có sẵn trên mạng, dự án của nhóm mang tới những nâng cấp đáng giá:

1. **Quản lý lịch sử nước đi nâng cao**: Khôi phục lại trạng thái cũ thông qua Undo/Redo bằng hai Stack song song, đem lại cảm giác mượt mà và cho phép người chơi thử nghiệm thoải mái thay vì chỉ ngồi nhìn AI tự giải.
2. **Khả năng tùy chỉnh Hình Ảnh**: Vượt xa khỏi những con số khô khan, ứng dụng hỗ trợ người dùng chèn ảnh tuỳ thích, phân chia tự động thành các tiles, kết hợp giữa bài toán search và game giải trí (Jigsaw Puzzle).
3. **So sánh Live Dashboard**: Trực quan hóa các thông số (Số ms thực thi, Số state/node duyệt) trực tiếp ngay trên bảng điều khiển mà không cần tìm kết xuất trong terminal, giúp người dùng đại chúng dễ dàng hiểu cách thuật toán tiếp cận.
4. **Giao diện hiện đại**: Giao diện được thiết kế UI/UX theo thiên hướng ứng dụng Desktop.

---

## Các thuật toán sử dụng

Ứng dụng cài đặt hai thuật toán tìm kiếm phổ biến để benchmark. Dưới đây là mã giả (Pseudocode) cung cấp luồng đi cơ sở.

### 1. Thuật toán BFS (Breadth-First Search)

Thuật toán tìm kiếm theo chiều rộng thực hiện duyệt tất cả các node ở độ sâu $d$ trước rồi mới đi sâu tầng kế tiếp ($d+1$). Ưu điểm của BFS là **chắc chắn luôn tìm được lời giải tối ưu nhất (ngắn nhất)** trên đồ thị không trọng số, tuy nhiên nhược điểm là tốn quá nhiều tài nguyên do bùng nổ không gian bộ nhớ.

**Pseudocode:**

```text
function BFS(initial_state, goal_state):
    khởi tạo hàng đợi: queue = [] (ưu tiên phục vụ người vào trước - FIFO)
    queue.push(initial_state)

    khởi tạo tập hợp: visited = {} (để lưu trạng thái đã duyệt)
    visited.add(initial_state)

    while queue KHÔNG rỗng:
        current_state = queue.pop()

        if current_state == goal_state:
            return trace_path(current_state) // Tìm thấy đích -> Trả về danh sách thao tác đi

        // Sinh ra các trạng thái có thể đi tiếp theo
        for each neighbor in get_neighbors(current_state):
            if neighbor KHÔNG nằm trong visited:
                neighbor.parent = current_state // Ghi nhớ để gỡ vết
                visited.add(neighbor)
                queue.push(neighbor)

    return FAILURE // Do xáo trộn đã kiểm tra Inversion, nhánh này phụ phục vụ an toàn code.
```

### 2. Thuật toán A\* Search (Heuristic Search)

Thuật toán A\* tìm kiếm đường đi bằng cách giảm không gian duyệt thông qua hàm đánh giá hướng đích $f(n) = g(n) + h(n)$. Trong trò chơi này, nhóm dùng **khoảng cách Manhattan** (tổng khoảng cách dịch chuyển chiều dọc & ngang so với đích) làm $h(n)$.

- $g(n)$: Số bước đã đi từ ban đầu đến hiện tại.
- $h(n)$: Giá trị đánh giá hàm Heuristic (Manhattan Distance).

**Pseudocode:**

```text
function A_Star(initial_state, goal_state):
    khởi tạo hàng đợi ưu tiên: priority_queue = [] (ưu tiên trạng thái có f(n) rể nhất)
    priority_queue.push(initial_state, priority = 0)

    khởi tạo tập hợp visited = {}
    visited.add(initial_state)

    while priority_queue KHÔNG rỗng:
        current_state = priority_queue.pop() // Lấy trạng thái có f(n) bé nhất

        if current_state == goal_state:
            return trace_path(current_state)

        for each neighbor in get_neighbors(current_state):
            // Tính toán chi phí
            g(neighbor) = g(current_state) + 1
            h(neighbor) = ManhattanDistance(neighbor, goal_state)
            f(neighbor) = g(neighbor) + h(neighbor)

            if neighbor KHÔNG nằm trong visited HOẶC f(neighbor) tìm được tối ưu hơn:
                neighbor.parent = current_state
                visited.add(neighbor)
                priority_queue.push(neighbor, độ_ưu_tiên = f(neighbor))

    return FAILURE
```

---

## Giao diện chương trình

Dưới đây là thiết kế giao diện (UI) và kiến trúc quy hoạch hiển thị của ứng dụng 8-Puzzle. Tương tác có thể chạy trực tiếp bằng lệnh `python main.py`.

### Khung Bản Thiết Khế (Wireframe)

Quy hoạch giao diện theo khu vực. Các chức năng điều khiển trò chơi nằm ở sidebar, và bảng Puzzle kích thước lớn nằm giữa làm tâm điểm.

![Wireframe UI](assets/wireframe-ui.png)
_(Hình 1: Phân bổ khu vực chức năng trên màn hình)_

### Trạng Thái Mô Phỏng Giao Diện

Bản Mockup ứng dụng kết hợp màu sắc, hiển thị thông số và hệ thống UI Pygame.

- Hiện tại bảng trạng thái Undo/Redo và các thao tác chuột kéo thả ghép mảnh đã có thể tương tác thực thụ.
- Thông số **Dashboard Thời Gian Chạy Lời Giải** sẽ trực tiếp kết xuất số đo do các thuật toán BFS hoặc A\* cung cấp theo thời gian thực thi của code.

![Mockup Giao diện hoàn chỉnh](assets/mockup.png)
_(Hình 2: Ứng dụng tích hợp Sidebar phân tích chỉ số thời gian thực và Bảng Puzzle)_

## Cài đặt và chạy dự án

Dự án sử dụng Python cơ bản và thư viện Pygame, có thể chạy thẳng trên mọi hệ điều hành (Windows/macOS/Linux).

**Bước 1:** Đảm bảo máy tính đã cài đặt **Python 3.10** trở lên.

**Bước 2:** Di chuyển vào thư mục của dự án và cài đặt thư viện đồ họa cần thiết (khuyên dùng môi trường ảo `venv`):

```bash
# Tạo và kích hoạt môi trường ảo (Tuỳ chọn)
python -m venv .venv
# - Windows: .venv\Scripts\activate
# - macOS/Linux: source .venv/bin/activate

# Cài đặt file requirements
pip install -r requirements.txt
```

**Bước 3:** Khởi chạy tệp tin chính (Entry Point) của phần mềm:

```bash
python main.py
```
