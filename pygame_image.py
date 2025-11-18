import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flipped = pg.transform.flip(bg_img, True, False)
    bg_progress = 0
    bg_progress_f = 1600
    koukaton_img = pg.image.load("fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    koukaton_rect = koukaton_img.get_rect()
    koukaton_rect.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_1st = pg.key.get_pressed()
        if key_1st[pg.K_UP]:
            koukaton_rect.move_ip((0, -1))
        if key_1st[pg.K_DOWN]:
            koukaton_rect.move_ip((0, 1))
        if key_1st[pg.K_LEFT]:
            koukaton_rect.move_ip((-1, 0))
        if key_1st[pg.K_RIGHT]:
            koukaton_rect.move_ip((2, 0))

        koukaton_rect.move_ip((-1, 0))
        
        screen.blit(bg_img, [bg_progress, 0])
        screen.blit(bg_img_flipped, [bg_progress_f, 0])
        screen.blit(koukaton_img, koukaton_rect)
        pg.display.update()
        tmr += 1        
        bg_progress -= 1
        bg_progress_f -= 1
        if(bg_progress < -1600):
            bg_progress = 1600
        if(bg_progress_f < -1600):
            bg_progress_f = 1600
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()