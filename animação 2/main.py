import pygame
import sys
import random
from pygame.locals import *
from game.sprites import Player, Asteroid
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE, BLUE
from game.sounds import load_sounds, play_sound

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Navigator')
    
    # Clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Load game sounds
    sounds = load_sounds()
    
    # Create player sprite
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Score counter
    score = 0
    font = pygame.font.SysFont('Arial', 24)
    
    # Game state
    game_over = False
    
    # Main game loop
    running = True
    asteroid_spawn_timer = 0
    
    while running:
        # Limit frame rate
        delta_time = clock.tick(FPS) / 1000.0
        
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if game_over and event.key == K_r:
                    # Reset game
                    game_over = False
                    score = 0
                    player.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
                    for asteroid in asteroids:
                        asteroid.kill()
        
        if not game_over:
            # Get keyboard input
            keys = pygame.key.get_pressed()
            player.handle_input(keys, delta_time)
            
            # Update player position
            player.update(delta_time)
            
            # Keep player on screen
            player.constrain(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
            
            # Spawn new asteroids
            asteroid_spawn_timer += delta_time
            if asteroid_spawn_timer >= 1.0:  # Spawn every second
                asteroid_spawn_timer = 0
                new_asteroid = Asteroid(random.randint(0, SCREEN_WIDTH), -50)
                asteroids.add(new_asteroid)
                all_sprites.add(new_asteroid)
            
            # Update all asteroids
            for asteroid in asteroids:
                asteroid.update(delta_time)
                # Remove asteroids that are off-screen
                if asteroid.rect.top > SCREEN_HEIGHT:
                    asteroid.kill()
                    score += 1
            
            # Check for collisions
            if pygame.sprite.spritecollide(player, asteroids, False):
                play_sound(sounds['explosion'])
                game_over = True
        
        # Draw background
        screen.fill(BLACK)
        
        # Draw stars (simple background effect)
        for i in range(100):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            pygame.draw.circle(screen, WHITE, (x, y), 1)
        
        # Draw all sprites
        all_sprites.draw(screen)
        
        # Draw score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if game_over:
            game_over_text = font.render('Game Over! Press R to restart', True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
        
        # Update the display
        pygame.display.flip()
    
    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
