from core.controller import Game
from core.factory import ObjectsFactory


def main():
    game = Game(50, 50)
    factory = ObjectsFactory(game)

    factory.set_glider(1, 1)
    factory.set_glider(10, 10)
    factory.set_glider(20, 20)
    factory.set_glider(30, 30)
    factory.set_blinker(19, 19)
    factory.set_blinker(22, 22)
    factory.set_blinker(3, 15)

    game.show_board()
    while not game.is_still:
        game.next_generation()
        game.show_board()


if __name__ == '__main__':
    main()
