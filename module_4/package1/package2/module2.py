from .package3 import module3


class except_verification(module3.verification):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.check()
