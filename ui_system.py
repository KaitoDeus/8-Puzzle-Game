import pygame

BG_COLOR = (240, 240, 240)        # Lighter Gray 
PANEL_BG = (255, 255, 255)        # Pure White for panels
TEXT_COLOR = (0, 0, 0)            # Black text
SUBTEXT_COLOR = (80, 80, 80)      # Gray for secondary info
BORDER_COLOR = (160, 160, 160)    # Concrete gray for borders

# Button Colors
BTN_DEFAULT = (225, 225, 225)     # Classic gray button
BTN_HOVER = (200, 220, 240)       # Light blue highlight 
PRIMARY_ACCENT = (0, 120, 215)    # Windows Blue
SECONDARY_ACCENT = (112, 48, 160) # Purple 
DANGER_ACCENT = (200, 0, 0)       # Standard Red
SUCCESS_ACCENT = (0, 150, 0)      # Standard Green

def get_font(size, bold=False):
    font_priority = ['segoe ui', 'tahoma', 'arial', 'sans-serif']
    return pygame.font.SysFont(font_priority, size, bold=bold)

class UIUtils:
    @staticmethod
    def draw_rect_border(surface, rect, color, width=1):
        pygame.draw.rect(surface, color, rect, width)

class Panel:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        
    def handle_event(self, event):
        pass
        
    def update(self):
        pass
        
    def draw(self, screen):
        pygame.draw.rect(screen, PANEL_BG, self.rect)
        pygame.draw.rect(screen, BORDER_COLOR, self.rect, 1)

class Label:
    def __init__(self, pos, text, font_size=18, color=TEXT_COLOR, bold=False, center=False):
        self.pos = pos
        self.text = str(text)
        self.font = get_font(font_size, bold)
        self.color = color
        self.center = center # True: Căn giữa, False: Căn góc trên trái
        
    def handle_event(self, event): pass
    def update(self): pass
        
    def draw(self, screen):
        text_surf = self.font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect()
        if self.center:
            text_rect.center = self.pos
        else:
            text_rect.topleft = self.pos
        screen.blit(text_surf, text_rect)

class Button:
    def __init__(self, rect, text, font_size=18, callback=None, color=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = get_font(font_size)
        self.callback = callback
        self.is_hovered = False
        self.base_color = color if color else BTN_DEFAULT
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                    
    def update(self):
        pass
        
    def draw(self, screen):
        color = BTN_HOVER if self.is_hovered else self.base_color
        
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BORDER_COLOR, self.rect, 1)
        
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

class Tile:
    def __init__(self, rect, value, index, color=None, callback=None):
        self.rect = pygame.Rect(rect)
        self.value = value
        self.index = index
        self.font = get_font(36, bold=True)
        self.color = color if color else (255, 255, 255)
        self.callback = callback
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback(self.index)
                    
    def update(self): pass
        
    def draw(self, screen):
        if self.value == 0:
            pygame.draw.rect(screen, (230, 230, 230), self.rect)
            pygame.draw.rect(screen, BORDER_COLOR, self.rect, 1)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
            pygame.draw.rect(screen, BORDER_COLOR, self.rect, 1)
            
            text_surf = self.font.render(str(self.value), True, PRIMARY_ACCENT)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)