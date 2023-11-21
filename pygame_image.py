import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2=pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True,False)
    kk_imges = [kk_img, pg.transform.rotozoom(kk_img, 4, 1.0),pg.transform.rotozoom(kk_img, 7, 1.0),pg.transform.rotozoom(kk_img, 10, 1.0)]
    
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x=tmr%3200 
        
        screen.blit(bg_img, [-x,0 ])
        screen.blit(bg_img2,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        
        if tmr % 8 == 0 or tmr % 8 == 7:
            screen.blit(kk_imges[0],[300,200])
        elif tmr % 8 == 1 or tmr % 8 == 6:
            screen.blit(kk_imges[1],[300,200])
        elif tmr % 8 == 2 or tmr % 8 == 5:
            screen.blit(kk_imges[2],[300,200])
        else:
            screen.blit(kk_imges[3],[300,200])
        
        pg.display.update()
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()