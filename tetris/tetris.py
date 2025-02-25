import curses
import random
import time

LARGURA, ALTURA = 10, 20
TETROMINOS = [
    [[1, 1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]

class Tetris:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.board = [[0] * LARGURA for _ in range(ALTURA)]
        self.piece = self.new_piece()
        self.x, self.y = LARGURA // 2 - 1, 0
        self.running = True

    def new_piece(self):
        return random.choice(TETROMINOS)

    def rotate_piece(self):
        self.piece = [list(row) for row in zip(*self.piece[::-1])]

    def move_piece(self, dx, dy):
        if self.valid_position(self.x + dx, self.y + dy, self.piece):
            self.x += dx
            self.y += dy

    def valid_position(self, x, y, piece):
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell and (x + j < 0 or x + j >= LARGURA or y + i >= ALTURA or self.board[y + i][x + j]):
                    return False
        return True

    def fix_piece(self):
        for i, row in enumerate(self.piece):
            for j, cell in enumerate(row):
                if cell:
                    self.board[self.y + i][self.x + j] = 1
        self.piece = self.new_piece()
        self.x, self.y = LARGURA // 2 - 1, 0
        if not self.valid_position(self.x, self.y, self.piece):
            self.running = False

    def clear_lines(self):
        self.board = [row for row in self.board if any(cell == 0 for cell in row)]
        while len(self.board) < ALTURA:
            self.board.insert(0, [0] * LARGURA)

    def draw(self):
        self.stdscr.clear()
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.stdscr.addstr(y, x * 2, "[]")
        for i, row in enumerate(self.piece):
            for j, cell in enumerate(row):
                if cell:
                    self.stdscr.addstr(self.y + i, (self.x + j) * 2, "[]")
        self.stdscr.refresh()

    def run(self):
        self.stdscr.nodelay(True)
        while self.running:
            key = self.stdscr.getch()
            if key == curses.KEY_LEFT:
                self.move_piece(-1, 0)
            elif key == curses.KEY_RIGHT:
                self.move_piece(1, 0)
            elif key == curses.KEY_DOWN:
                self.move_piece(0, 1)
            elif key == ord(' '):
                self.rotate_piece()
            if not self.valid_position(self.x, self.y + 1, self.piece):
                self.fix_piece()
                self.clear_lines()
            else:
                self.y += 1
            self.draw()
            time.sleep(0.1)

def main(stdscr):
    game = Tetris(stdscr)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
