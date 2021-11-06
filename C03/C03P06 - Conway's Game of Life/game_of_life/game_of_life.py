from core.controller import Controller


def main():
    ctrl = Controller(50, 50)
    ctrl.set_glider(1, 1)
    ctrl.set_glider(10, 10)
    ctrl.set_glider(20, 20)
    ctrl.set_glider(30, 30)
    ctrl.set_blinker(19, 19)
    ctrl.set_blinker(22, 22)
    ctrl.set_blinker(3, 15)
    ctrl.show_board()
    while not ctrl.is_still:
        ctrl.next_generation()
        ctrl.show_board()


if __name__ == '__main__':
    main()
