import pygame
import sys
from ui_system import Panel, Button, Label, Tile, UIUtils, BG_COLOR, PRIMARY_ACCENT, SECONDARY_ACCENT, SUCCESS_ACCENT, DANGER_ACCENT, SUBTEXT_COLOR, BORDER_COLOR
from game_logic import PuzzleGame

game = PuzzleGame()

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("8-Puzzle Game")

def reset_game():
    game.reset()
    print("Game Reset")

def handle_tile_click(index):
    if game.move(index):
        print(f"Moved tile at index {index}")
        if game.is_goal():
            print("Goal Reached!")

def solve_bfs():
    print("Solving with BFS...")

def solve_astar():
    print("Solving with A*...")

def undo():
    if game.undo():
        print("Undo successful")

def redo():
    if game.redo():
        print("Redo successful")

def insert_image():
    print("Inserting Image...")

def main():
    clock = pygame.time.Clock()
    
    # --- UI Setup ---
    ui_elements = []
    
    # 1. Header & Title Bar Removed
    # Content starts higher up
    CONTENT_Y = 20
    
    # [namePicture.png] label
    ui_elements.append(Label((50, CONTENT_Y + 10), "[no_image_loaded.png]", font_size=16, color=SUBTEXT_COLOR))
    
    # 2. Main Board Panel
    board_rect = pygame.Rect(50, CONTENT_Y + 50, 580, 500)
    ui_elements.append(Panel(board_rect))
    
    # "Chèn ảnh" button (Aligned to the top-right of the board)
    ui_elements.append(Button((board_rect.right - 140, CONTENT_Y, 140, 40), "Chèn ảnh", font_size=18, callback=insert_image))
    
    # Tiles (3x3 Grid) - Centered in panel
    tile_size = 140
    gap = 15
    start_x = board_rect.x + (board_rect.width - (3 * tile_size + 2 * gap)) // 2
    start_y = board_rect.y + (board_rect.height - (3 * tile_size + 2 * gap)) // 2
    
    tiles_ui = []
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            val = game.current_state[idx]
            tile_rect = (start_x + j * (tile_size + gap), start_y + i * (tile_size + gap), tile_size, tile_size)
            tile = Tile(tile_rect, val, idx, callback=handle_tile_click)
            tiles_ui.append(tile)
            ui_elements.append(tile)

    # 3. Action Buttons (Bottom Bar - Spaced evenly under board)
    btn_w, btn_h = 160, 50
    btn_y = board_rect.bottom + 30
    ui_elements.append(Button((board_rect.x, btn_y, btn_w, btn_h), "<< Đi lui", color=PRIMARY_ACCENT, callback=undo))
    ui_elements.append(Button((board_rect.centerx - btn_w//2, btn_y, btn_w, btn_h), "Đi tới >>", color=PRIMARY_ACCENT, callback=redo))
    ui_elements.append(Button((board_rect.right - btn_w, btn_y, btn_w, btn_h), "Chơi lại", color=DANGER_ACCENT, callback=reset_game))

    # 4. Right Side Panels
    side_x = 660
    # Algorithm Panel
    algo_panel = Panel((side_x, CONTENT_Y + 50, 320, 320))
    ui_elements.append(algo_panel)
    ui_elements.append(Label((algo_panel.rect.centerx, algo_panel.rect.y + 30), "Giải thuật tối ưu", font_size=24, center=True))
    
    ui_elements.append(Button((side_x + 30, algo_panel.rect.y + 80, 260, 90), "Breadth First Search", font_size=20, callback=solve_bfs))
    ui_elements.append(Button((side_x + 30, algo_panel.rect.y + 190, 260, 90), "A* Search", font_size=20, callback=solve_astar))

    # Stats Panel
    stats_panel = Panel((side_x, CONTENT_Y + 390, 320, 250))
    ui_elements.append(stats_panel)
    ui_elements.append(Label((stats_panel.rect.centerx, stats_panel.rect.y + 30), "Thông số trò chơi", font_size=22, center=True))
    
    stats_y = stats_panel.rect.y + 80
    ui_elements.append(Label((side_x + 30, stats_y), "Thời gian chơi:", font_size=18, color=SUBTEXT_COLOR))
    ui_elements.append(Label((side_x + 220, stats_y), "00:00", font_size=18))
    
    ui_elements.append(Label((side_x + 30, stats_y + 40), "Thời gian giải:", font_size=18, color=SUBTEXT_COLOR))
    ui_elements.append(Label((side_x + 220, stats_y + 40), "0.0 ms", font_size=18))
    
    ui_elements.append(Label((side_x + 30, stats_y + 80), "Số bước duyệt:", font_size=18, color=SUBTEXT_COLOR))
    ui_elements.append(Label((side_x + 220, stats_y + 80), "0", font_size=18))

    # --- Main Loop ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            for element in ui_elements:
                element.handle_event(event)
        
        # --- Cập nhật (Update) ---
        for i, tile in enumerate(tiles_ui):
            tile.value = game.current_state[i]
            tile.update()

        for element in ui_elements:
            if not isinstance(element, Tile):
                element.update()
            
        # --- Vẽ (Render) ---
        screen.fill(BG_COLOR)
        
        for element in ui_elements:
            element.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
