class ObjectsFactory:
    def __init__(self, controller):
        self.controller = controller

    def set_glider(self, r_i, c_i):
        self.controller.set_alive(r_i + 2, c_i)
        self.controller.set_alive(r_i + 2, c_i + 1)
        self.controller.set_alive(r_i + 2, c_i + 2)
        self.controller.set_alive(r_i + 1, c_i + 2)
        self.controller.set_alive(r_i, c_i + 1)

    def set_blinker(self, r_i, c_i):
        self.controller.set_alive(r_i, c_i)
        self.controller.set_alive(r_i, c_i + 1)
        self.controller.set_alive(r_i, c_i + 2)
