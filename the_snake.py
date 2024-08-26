"""Классическая игра Змейка, написанная с помощью классов, методов и пр."""
from random import randrange
import random
import pygame as pg

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SCREEN_CENTRE = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

for_random_direction = [UP, DOWN, LEFT, RIGHT]

DIRECTIONS = {
    (LEFT, pg.K_UP): UP,
    (RIGHT, pg.K_UP): UP,
    (UP, pg.K_LEFT): LEFT,
    (DOWN, pg.K_LEFT): LEFT,
    (UP, pg.K_RIGHT): RIGHT,
    (DOWN, pg.K_RIGHT): RIGHT,
    (LEFT, pg.K_DOWN): DOWN,
    (RIGHT, pg.K_DOWN): DOWN
}

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 12

# Настройка игрового окна:
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pg.display.set_caption('Змейка')

# Настройка времени:
clock = pg.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Объявляем родительский класс"""

    def __init__(self, position=SCREEN_CENTRE, body_color=None, length=1):
        self.body_color = body_color
        self.position = position
        self.length = length

    def draw(self):
        """Родительский метод для рисования объектов"""
        raise NotImplementedError(
            'Предполагаем реализацию этого метода только в дочерних классах')


class Apple(GameObject):
    """Объявляем дочерний класс, унаследованный от GameObject"""

    def __init__(self, occupied_positions):
        super().__init__(position=SCREEN_CENTRE, body_color=None)
        self.randomize_position(occupied_positions)
        self.body_color = APPLE_COLOR
        self.new_position = None

    def draw(self):
        """Отрисовка яблока"""
        rect = pg.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, self.body_color, rect)
        pg.draw.rect(screen, BORDER_COLOR, rect, 1)

    def randomize_position(self, occupied_positions):
        """Метод для создания яблока в случайном месте"""
        while True:
            self.position = (
                randrange(0, SCREEN_WIDTH, GRID_SIZE),
                randrange(0, SCREEN_HEIGHT, GRID_SIZE)
            )

            if self.position not in occupied_positions:
                break


class Snake(GameObject):
    """Объявляем дочерний класс для змеи, унаследованный от GameObject"""

    def __init__(self):
        super().__init__(position=SCREEN_CENTRE, body_color=None, length=1)
        self.reset()
        self.direction = RIGHT
        self.body_color = SNAKE_COLOR
        self.last = None
        self.next_direction = None

    def draw(self):
        """Отрисовка змеи"""
        for position in self.positions:
            rect = (pg.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pg.draw.rect(screen, self.body_color, rect)
            pg.draw.rect(screen, BORDER_COLOR, rect, 1)
        self.a = self.positions[0]
        self.x, self.y = self.a

    def move(self):
        """
        Тут реализована анимация добавления головы в сторону направления
        а также удаление хвоста в конце метода
        """
        head_horizontal_point, head_vertical_point = self.get_head_position()
        horizontal_shift, vertical_shift = self.direction
        self.positions.insert(
            0,
            (
                ((head_horizontal_point + horizontal_shift * GRID_SIZE)
                 % SCREEN_WIDTH),
                ((head_vertical_point + vertical_shift * GRID_SIZE)
                 % SCREEN_HEIGHT),
            ),
        )
        self.last = self.positions[-1]
        if self.last:
            self.positions.pop()
            last_rect = pg.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pg.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def update_direction(self, direction):
        """
        Метод обновляет направление
        движения змейки
        """
        self.direction = direction

    def reset(self):
        """Метод перезагрузки игры"""
        self.positions = [(320, 240)]
        self.direction = random.choice(for_random_direction)

    def get_head_position(self):
        """Метод для вычисления головы змеи"""
        head = self.positions[0]
        return head


# Функция обработки действий пользователя

def handle_keys(game_object):
    """Функция, которая обрабатывает нажатия на стрелки клавиш"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        elif event.type == pg.KEYDOWN:
            if event.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
                game_object.update_direction(
                    DIRECTIONS.get((game_object.direction, event.key),
                                   game_object.direction))
            elif event.key == pg.K_ESCAPE:
                pg.quit()
                raise SystemExit


def main():
    """Функция main"""
    # Инициализация PyGame:
    pg.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple(snake.positions)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)
        elif snake.positions[0] == apple.position:
            snake.positions.append(apple.position)
            snake.length += 1
            apple.randomize_position(snake.positions)
        snake.draw()
        apple.draw()
        pg.display.update()
        handle_keys(snake)
        snake.update_direction(snake.direction)


if __name__ == '__main__':
    main()
