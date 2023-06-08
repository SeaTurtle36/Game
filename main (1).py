import pygame
import random

WIDTH = 602
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

class ColouredBlock:
  def __init__(self, colour, x_pos, y_pos, width, height):
    self.rect = pygame.Rect(x_pos, y_pos, width, height)
    self.colour = colour
    self.visible = True
    

  def drawRect(self):
    if self.visible:
      pygame.draw.rect(WINDOW, self.colour, self.rect)
      
      
def draw_more_blocks(more_blocks):
  for block in more_blocks:
    block.drawRect()
    

def draw_window(board, ball):
  WINDOW.fill((0, 0, 25))
  pygame.display.set_caption("Breakout")
  pygame.draw.rect(WINDOW, (255, 255, 255), board)
  pygame.draw.rect(WINDOW, (255, 255, 255), ball)
  

def pygame_update():
  pygame.display.update()


def move_ball(ball, ball_x_speed, ball_y_speed):
  ball.x += ball_x_speed
  ball.y += ball_y_speed


def move_board(board, keys_pressed):
  if keys_pressed[pygame.K_d]:
    board.x += 6

  if keys_pressed[pygame.K_a]:
    board.x -= 6


def main():
  ball_x_speed = 4
  ball_y_speed = -3
  RED = (255, 0, 0)
  ORANGE = (255, 127, 0)
  YELLOW = (255, 255, 0)
  GREEN = (90, 255, 0)
  BLUE = (90, 0, 255)
  PURPLE = (127, 0, 127)
  board = pygame.Rect(260, 364, 90, 10)
  ball = pygame.Rect(320, 300, 7, 7)

  more_blocks = []
  x = 0
  for i in range(14):
    more_blocks.append(ColouredBlock(PURPLE, x, 65, 40, 10))
    more_blocks.append(ColouredBlock(BLUE, x, 52, 40, 10))
    more_blocks.append(ColouredBlock(GREEN, x, 39, 40, 10))
    more_blocks.append(ColouredBlock(YELLOW, x, 26, 40, 10))
    more_blocks.append(ColouredBlock(ORANGE, x, 13, 40, 10))
    more_blocks.append(ColouredBlock(RED, x, 0, 40, 10))
    x += 43
  
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
      if pygame.event == pygame.QUIT:
        run = False
    # ball collision
    if ball.x >= WIDTH - 7 or ball.x <= 0:
      ball_x_speed *= -1

    elif ball.y <= 0:
      ball_y_speed *= -1

    elif ball.y >= HEIGHT:
      pygame.quit()

    if ball.colliderect(board):
      ball_y_speed *= -1
      if ball_x_speed > 0 and ball_x_speed < 5:
        ball_x_speed = random.choice([1, 2, 3, 4])
      else:
        ball_x_speed = random.choice([-1, -2, -3, -4])
      
    for block in more_blocks:
      if ball.colliderect(block.rect) and block.visible == True:
        ball_y_speed *= -1
        block.visible = False
    
    draw_window(board, ball)
    draw_more_blocks(more_blocks)
    pygame_update()
    move_ball(ball, ball_x_speed, ball_y_speed)
    move_board(board, keys_pressed)
    
  pygame.quit()


main()