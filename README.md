# ĐỀ TÀI: Nghiên cứu Heuristic và Blind Search, ứng dụng và so sánh trong giải quyết trò chơi 8-Puzzle

## Mục lục

1. [Phân tích bài toán](#phân-tích-bài-toán)
2. [Các thuật toán sử dụng](#các-thuật-toán-sử-dụng)
3. [Giao diện chương trình](#giao-diện-chương-trình)
4. [Cài đặt và chạy dự án](#cài-đặt-và-chạy-dự-án)

---

## Phân tích bài toán

### Mục đích bài toán

Bài toán 8-Puzzle là một dạng bài toán tìm kiếm cổ điển trong Trí tuệ nhân tạo. Mục tiêu là sắp xếp lại các mảnh ghép trên một ma trận 3x3 (gồm 8 ô số và 1 ô trống) từ một trạng thái xáo trộn bất kỳ đưa về trạng thái đích có thứ tự tiếp nối nhau bằng cách trượt các ô kề cận vào ô trống. Đề tài tập trung vào việc nghiên cứu, triển khai và đánh giá so sánh hiệu năng giữa hai triết lý tìm kiếm tiêu biểu: **Tìm kiếm mù (Breadth-First Search - BFS)** và **Tìm kiếm có kiến thức kinh nghiệm (A\* Search)**.

### Cách làm

Dự án được xây dựng mô phỏng trực quan bằng ngôn ngữ **Python** kết hợp với thư viện đồ họa **Pygame**:

- **Cấu trúc dữ liệu**: Sử dụng mảng 1 chiều để biểu diễn trạng thái bàn cờ, giúp tối ưu hóa quá trình tính toán, duyệt node và lưu trữ trong bộ nhớ thay vì mảng 2 chiều cơ bản.
- **Quản lý trạng thái (State Management)**: Khai báo lớp `PuzzleGame`, ứng dụng cấu trúc _Stack_ để theo dõi hệ thống lịch sử nước đi, hỗ trợ tính năng quay lui (Undo/Redo).
- **Hệ thống đánh giá khởi tạo**: Áp dụng kiểm tra **Số nghịch thế (Inversions)** nhằm đảm bảo mọi trạng thái bàn cờ được sinh ra ngẫu nhiên đều chắn chắn có lời giải (Solvable).

### Kiến trúc dự án (Architecture Model)

Cấu trúc của dự án được tổ chức theo thiết kế lấy cảm hứng từ MVC (Model - View - Controller), giúp tách biệt rõ ràng việc hiển thị, điều khiển sự kiện và xử lý thuật toán:

```text
+-----------------------+       +-----------------------+       +-----------------------+
|         VIEW          |       |      CONTROLLER       |       |     MODEL / LOGIC     |
|  (Pygame Components)  | <---> |   (Main Game Loop)    | <---> | (Game Rules & Solvers)|
| - ui_system.py        |       | - main.py             |       | - game_logic.py       |
| - ui_statistics.py    |       |   - State Management  |       | - bfs_solver.py       |
|                       |       |   - Event Handling    |       | - astar_solver.py     |
+-----------------------+       +-----------------------+       +-----------------------+
```

Luồng tương tác chi tiết giữa các thành phần cốt lõi:

```text
+-----------------------+       +-----------------------+
|       Pygame UI       | <---> |     Main Control      |
|  (Tiles, Modal, Dash) |       |  (Event Dispatcher)   |
+-----------------------+       +-----------------------+
            |                               |
            | Update View                   | Manage Data/Flow
            v                               v
+-----------------------+       +-----------------------+
|    Image Processor    |       |      Game Engine      |
| (Pillow Image Cropper)|       |     (PuzzleGame)      |
+-----------------------+       |  - Undo/Redo System   |
                                +-----------------------+
                                            |
                                            | Request Path
                                            v
                                +-----------------------+
                                |       AI Solvers      |
                                |       (BFS / A*)      |
                                +-----------------------+
```

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
function BFS(start_state, goal_state):
    khởi tạo hàng đợi: Q = [] (FIFO)
    đưa start_state vào Q

    khởi tạo tập visited = {}
    visited.add(start_state)

    while Q KHÔNG rỗng:
        state = lấy ra từ Q

        if state == goal_state:
            return đường đi // Trả về kết quả

        // Duyệt các trạng thái kế tiếp
        for mỗi next_state trong get_neighbors(state):
            if next_state KHÔNG nằm trong visited:
                đánh dấu đã thăm
                next_state.parent = state // Lưu vết
                visited.add(next_state)
                đưa next_state vào Q

    return FAILURE // Không có lời giải
```

### 2. Thuật toán A\* Search (Heuristic Search)

Thuật toán A\* tìm kiếm đường đi bằng cách giảm không gian duyệt thông qua hàm đánh giá hướng đích $f(n) = g(n) + h(n)$. Trong trò chơi này, nhóm dùng **khoảng cách Manhattan** (tổng khoảng cách dịch chuyển chiều dọc & ngang so với đích) làm $h(n)$.

- $g(n)$: Số bước đã đi từ ban đầu đến hiện tại.
- $h(n)$: Giá trị đánh giá hàm Heuristic (Manhattan Distance).

**Pseudocode:**

```text
function A_Star(start_state, goal_state):
    khởi tạo hàng đợi ưu tiên: PQ = [] (ưu tiên theo f nhỏ nhất)
    đưa start_state vào PQ với độ ưu tiên f = 0

    khởi tạo tập visited để lưu chi phí tốt nhất
    g(start_state) = 0

    while PQ KHÔNG rỗng:
        state = lấy ra từ PQ (phần tử có f nhỏ nhất)

        if state == goal_state:
            return đường đi // Trả về kết quả

        // Duyệt các trạng thái kế tiếp
        for mỗi next_state trong get_neighbors(state):
            chi_phí_mới (new_g) = g(state) + 1

            if next_state chưa thăm HOẶC new_g < g(next_state):
                g(next_state) = new_g
                h = khoảng_cách_Manhattan(next_state, goal_state)
                f = g + h

                next_state.parent = state // Lưu vết
                đưa next_state vào PQ với độ ưu tiên f

    return FAILURE // Không có lời giải
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

Yêu cầu hệ thống
- **Python**: Phiên bản 3.10 trở lên (Hỗ trợ tốt nhất 3.12, 3.13 và cả bản preview 3.14).
- **Thư viện**: 
  - `pygame-ce`: Phiên bản cộng đồng của Pygame, hỗ trợ tốt các đời Python mới.
  - `Pillow`: Xử lý cắt ghép ảnh.

---

Dự án sử dụng Python cơ bản và thư viện Pygame, có thể chạy thẳng trên mọi hệ điều hành (Windows/macOS/Linux).

**Bước 1:** Đảm bảo máy tính đã cài đặt **Python 3.10** hoặc mới hơn.

**Bước 2:** Di chuyển vào thư mục dự án và thiết lập môi trường:

```bash
# Tạo môi trường ảo (Khuyên dùng để tránh xung đột)
python -m venv .venv

# Kích hoạt môi trường ảo:
# - Windows: .venv\Scripts\activate
# - macOS/Linux: source .venv/bin/activate

# Cập nhật pip và cài đặt thư viện
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Bước 3:** Khởi chạy trò chơi:

```bash
python main.py
```

> **Lưu ý**: Dự án sử dụng `pygame-ce` để đảm bảo hoạt động ổn định trên các phiên bản Python mới nhất (3.12+). Nếu bạn đã cài đặt `pygame` bản cũ, hãy gỡ ra trước khi cài đặt requirements.
