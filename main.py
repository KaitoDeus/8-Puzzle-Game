import pygame
import sys
import os
import tkinter as tk
from tkinter import filedialog
from image_processor import load_and_split_image
from ui_system import Tile, Modal, BG_COLOR
from ui_statistics import GameDashboard
from game_logic import PuzzleGame

# Core state variables
game = PuzzleGame()
is_finished = False
victory_modal = None
image_tiles = {}
current_image_name = ""

def exit_game():
    pygame.quit()
    sys.exit()

def reset_game():
    global is_finished, victory_modal
    game.reset()
    is_finished = False
    victory_modal = None

def close_modal():
    global victory_modal
    victory_modal = None

def undo():
    if not is_finished and game.undo():
        pass

def redo():
    if not is_finished and game.redo():
        pass

def solve_bfs():
    if not is_finished:
        print("Solving BFS...")

def solve_astar():
    if not is_finished:
        print("Solving A*...")

def insert_image():
    if is_finished: return
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh cho Puzzle",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp *.svg"), ("All files", "*.*")]
    )
    if file_path:
        new_tiles, name = load_and_split_image(file_path, 190)
        if new_tiles:
            global image_tiles, current_image_name
            image_tiles = new_tiles
            current_image_name = name

def handle_tile_click(index):
    global is_finished, victory_modal
    if not is_finished and game.move(index):
        if game.is_goal():
            is_finished = True
            victory_modal = Modal(
                "Bạn đã giải thành công!",
                "Chơi lại", reset_game,
                "Không", close_modal
            )

def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("8-Puzzle Game")
    
    # Tkinter root for dialogs
    root = tk.Tk()
    root.withdraw()
    
    clock = pygame.time.Clock()

    # Define callbacks for the UI
    callbacks = {
        'insert_image': insert_image,
        'reset_game': reset_game,
        'solve_bfs': solve_bfs,
        'solve_astar': solve_astar,
        'undo': undo,
        'redo': redo
    }
    
    # Initialize UI Dashboard (Header, Panels, Buttons)
    dashboard = GameDashboard(SCREEN_WIDTH, SCREEN_HEIGHT, callbacks)
    
    # Initialize Tiles (Logic handled in main loop)
    tile_size = 190
    board_rect = dashboard.board_rect
    start_x = board_rect.x + (board_rect.width - (3 * tile_size)) // 2
    start_y = board_rect.y + (board_rect.height - (3 * tile_size)) // 2
    
    tiles_ui = []
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            tile_rect = (start_x + j * tile_size, start_y + i * tile_size, tile_size, tile_size)
            tile = Tile(tile_rect, 0, idx, callback=handle_tile_click)
            tiles_ui.append(tile)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if is_finished and victory_modal:
                victory_modal.handle_event(event)
            else:
                dashboard.handle_event(event)
                for tile in tiles_ui:
                    tile.handle_event(event)
        
        # --- Update ---
        dashboard.update_image_name(current_image_name)
        # Future: update dashboard.update_stats() with real data
        
        for i, tile in enumerate(tiles_ui):
            val = game.current_state[i]
            tile.value = val
            tile.image = image_tiles.get(val)
        
        # --- Render ---
        screen.fill(BG_COLOR)
        
        dashboard.draw(screen)
        for tile in tiles_ui:
            tile.draw(screen)
            
        if is_finished and victory_modal:
            victory_modal.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
