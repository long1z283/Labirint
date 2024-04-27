#створи гру "Лабіринт"!
from pygame import * 
# Клас героя 
class Enemy(GameSprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__(player_image, player_x, player_y, player_speed) 
    
    # Оновлений метод руху ворога
    def update(self, target_x, target_y): 
        if self.rect.x < target_x: 
            self.rect.x += self.speed 
        elif self.rect.x > target_x: 
            self.rect.x -= self.speed 
        if self.rect.y < target_y: 
            self.rect.y += self.speed 
        elif self.rect.y > target_y: 
            self.rect.y -= self.speed 
    
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    
    keys = key.get_pressed() 
    if keys[K_LEFT] and player.rect.x > 0: 
        player.rect.x -= player.speed 
    if keys[K_RIGHT] and player.rect.x < main_width - player.rect.width: 
        player.rect.x += player.speed 
    if keys[K_UP] and player.rect.y > 0: 
        player.rect.y -= player.speed 
    if keys[K_DOWN] and player.rect.y < main_height - player.rect.height: 
        player.rect.y += player.speed 

    # Оновлення позиції ворога з урахуванням позиції героя
    cyborg.update(player.rect.x, player.rect.y)
    
    if player.rect.colliderect(final.rect):    
        print("YOU WIN!")  
        win_text = font_win.render("YOU WIN!", True, (255, 255, 255))    
        main_win.blit(win_text, (main_width // 2 - 80, main_height // 2))  
        mixer.Sound("money.ogg").play()   
        game = False
  
    elif player.rect.colliderect(wall1.rect) or player.rect.colliderect(wall2.rect) or player.rect.colliderect(wall3.rect) or player.rect.colliderect(cyborg.rect):  
        print("YOU LOSE!")  
        player.rect.x -= -9 
        player.rect.y -= -9 
        lose_text = font_lose.render("YOU LOSE!", True, (255, 0, 0))    
        main_win.blit(lose_text, (main_width // 2 - 80, main_height // 2))  
        mixer.Sound("kick.ogg").play() 
        game = False
     
    main_win.blit(background, (0, 0))     
    player.reset() 
    cyborg.reset() 
    final.reset()  
    wall1.draw_wall() 
    wall2.draw_wall() 
    wall3.draw_wall() 
    display.update() 
    clock.tick(FPS)