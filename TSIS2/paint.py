import pygame
from datetime import datetime

from tools import flood_fill

pygame.init()

# ---------------- WINDOW ----------------
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint")

# ---------------- CANVAS ----------------
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

preview = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# ---------------- STATE ----------------
running = True
clock = pygame.time.Clock()

current_tool = "pencil"  # pencil, line, rect, circle, fill, text
color = (0, 0, 0)

brush_size = 5

drawing = False
start_pos = None
last_pos = None

# text
text_input = ""
text_pos = None
typing = False

# ---------------- FLOOD FILL ----------------
def flood_fill(surface, x, y, target_color, new_color):
    if target_color == new_color:
        return

    width, height = surface.get_size()
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()

        if cx < 0 or cy < 0 or cx >= width or cy >= height:
            continue

        if surface.get_at((cx, cy))[:3] != target_color:
            continue

        surface.set_at((cx, cy), new_color)

        stack.append((cx+1, cy))
        stack.append((cx-1, cy))
        stack.append((cx, cy+1))
        stack.append((cx, cy-1))

# ---------------- MAIN LOOP ----------------
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # -------- KEYBOARD --------
        if event.type == pygame.KEYDOWN:

            # brush size
            if event.key == pygame.K_1:
                brush_size = 2
            elif event.key == pygame.K_2:
                brush_size = 5
            elif event.key == pygame.K_3:
                brush_size = 10

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("drawing_%Y-%m-%d_%H-%M-%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # text input
            if typing:
                if event.key == pygame.K_RETURN:
                    font = pygame.font.SysFont(None, 32)
                    text_surface = font.render(text_input, True, color)
                    canvas.blit(text_surface, text_pos)
                    typing = False

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        # -------- MOUSE DOWN --------
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # TEXT TOOL
            if current_tool == "text":
                text_pos = pos
                text_input = ""
                typing = True
                continue

            # FILL TOOL
            if current_tool == "fill":
                target = canvas.get_at(pos)[:3]
                flood_fill(canvas, pos[0], pos[1], target, color)
                continue

            drawing = True
            start_pos = pos
            last_pos = pos

        # -------- MOUSE UP --------
        if event.type == pygame.MOUSEBUTTONUP:

            if current_tool == "line":
                pygame.draw.line(canvas, color, start_pos, event.pos, brush_size)

            elif current_tool == "rect":
                x1, y1 = start_pos
                x2, y2 = event.pos
                rect = pygame.Rect(min(x1, x2), min(y1, y2),
                                   abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(canvas, color, rect, brush_size)

            elif current_tool == "circle":
                radius = int(((event.pos[0]-start_pos[0])**2 + (event.pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, radius, brush_size)

            drawing = False
            start_pos = None
            last_pos = None

        # -------- MOUSE MOVE --------
        if event.type == pygame.MOUSEMOTION and drawing:

            pos = event.pos

            # pencil
            if current_tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, pos, brush_size)
                last_pos = pos

            # preview tools
            if current_tool in ["line", "rect", "circle"]:
                preview.fill((0, 0, 0, 0))

                if current_tool == "line":
                    pygame.draw.line(preview, color, start_pos, pos, brush_size)

                elif current_tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                                       abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(preview, color, rect, brush_size)

                elif current_tool == "circle":
                    radius = int(((pos[0]-start_pos[0])**2 + (pos[1]-start_pos[1])**2) ** 0.5)
                    pygame.draw.circle(preview, color, start_pos, radius, brush_size)

    # ---------------- DRAW ----------------
    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))
    
    screen.blit(preview, (0, 0))

    # text preview
    if typing:
        font = pygame.font.SysFont(None, 32)
        txt = font.render(text_input, True, color)
        screen.blit(txt, text_pos)

    pygame.display.flip()

pygame.quit()