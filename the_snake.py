from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 7

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    def __init__(self):
        self.body_color = None
        self.position = (340, 240)
    def draw(self):
        pass



class Apple(GameObject):
    def __init__(self):
        super().__init__()
        self.position = (340, 240)
        self.body_color = APPLE_COLOR
        self.position = (340, 240)
        self.new_position = None

    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


    # def update_position(self):
    #     if self.new_position:
    #         self.position = self.new_position
    #         self.new_position = None

class Snake(GameObject):

    def __init__(self):
        super().__init__()
        self.length = 1
        self.positions = [(100, 240)]
        self.direction = RIGHT
        self.body_color = SNAKE_COLOR
        self.last = None
        self.next_direction = None


    # # Метод draw класса Snake
    def draw(self, surface):
        for position in self.positions:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        self.a = self.positions[0]
        self.x, self.y = self.a

    #     # Отрисовка головы змейки
    #     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
    #     pygame.draw.rect(screen, self.body_color, head_rect)
    #     pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

    #     if self.last:
    #         last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
    #         pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
    #         self.positions.pop(-1)
    
    

    def move(self):
        if self.direction == RIGHT:
            if self.x <= SCREEN_WIDTH:
                self.positions.insert(0, (self.x+20, self.y))
            else:
                self.x = 0
                self.positions.insert(0, (self.x+20, self.y))
        if self.direction == LEFT:
            if self.x >= 0:
                self.positions.insert(0, (self.x-20, self.y))
            else:
                self.x = 640
                self.positions.insert(0, (self.x-20, self.y))
        if self.direction == UP:
            if self.y >= 0:
                self.positions.insert(0, (self.x, self.y-20))
            else:
                self.y = 480
                self.positions.insert(0, (self.x, self.y-20))        
        if self.direction == DOWN:
            if self.y <= 480:
                self.positions.insert(0, (self.x, self.y+20))
            else:
                self.y = 0
                self.positions.insert(0, (self.x, self.y+20))
            
            

    def pop(self):
        if self.position == self.a:
            self.positions.append(self.position)
            self.length += self.length
        self.last = self.positions[-1]
        if self.last:
            self.positions.pop(-1)
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
        
    
    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None



    

        # def delete(new_direction):
        #     self.positions.pop(-1)

        # deleting = delete(new_direction)

            # Отрисовка головы змейки
        # head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        # pygame.draw.rect(screen, self.body_color, head_rect)
        # pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        # if self.last:
        #     last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
        #     pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
        #     self.positions.pop(-1)


# def change_position(apple, snake):
#     if apple.position == snake.position:
#         apple.position = (100, 100)






# Функция обработки действий пользователя
def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(SPEED)
        apple.draw()
        snake.draw(pygame.Surface) 
        pygame.display.update()
        snake.pop()
        handle_keys(snake)
        snake.update_direction()
        
        snake.move()  
        # change_position(apple, snake)
        # apple.update_position()

        

if __name__ == '__main__':
    main()



