import pygame
from racer import RacerGame
from ui import Button
from persistence import load_settings, save_settings, load_scores, save_score

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

state = "menu"
game = None
username = "Player"

settings = load_settings()

# кнопки меню
play_btn = Button("Play", 200, 200, 200, 50)
leader_btn = Button("Leaderboard", 200, 300, 200, 50)
settings_btn = Button("Settings", 200, 400, 200, 50)
quit_btn = Button("Quit", 200, 500, 200, 50)

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "menu":
                if play_btn.is_clicked(event.pos):
                    username = input("Enter name: ")
                    game = RacerGame(settings)
                    state = "game"
                elif leader_btn.is_clicked(event.pos):
                    state = "leaderboard"
                elif settings_btn.is_clicked(event.pos):
                    state = "settings"
                elif quit_btn.is_clicked(event.pos):
                    running = False

            elif state == "game_over":
                state = "menu"

            elif state == "leaderboard":
                state = "menu"

            elif state == "settings":
                settings["sound"] = not settings["sound"]
                save_settings(settings)
                state = "menu"

    # -------- STATES --------

    if state == "menu":
        play_btn.draw(screen)
        leader_btn.draw(screen)
        settings_btn.draw(screen)
        quit_btn.draw(screen)

    elif state == "game":
        result = game.update(screen)
        if result == "game_over":
            save_score({
                "name": username,
                "score": game.score,
                "distance": game.distance
            })
            state = "game_over"

    elif state == "game_over":
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (180, 300))

    elif state == "leaderboard":
        scores = load_scores()
        font = pygame.font.SysFont(None, 30)
        y = 100
        for i, s in enumerate(scores):
            txt = f"{i+1}. {s['name']} - {s['score']}"
            screen.blit(font.render(txt, True, (255,255,255)), (100, y))
            y += 40

    elif state == "settings":
        font = pygame.font.SysFont(None, 30)
        txt = f"Sound: {settings['sound']} (click to toggle)"
        screen.blit(font.render(txt, True, (255,255,255)), (100, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()