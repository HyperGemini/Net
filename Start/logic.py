class Formula:
    def __init__(self):
        pass

    def interpret(self, valuation):
        pass


class Var(Formula):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def interpret(self, valuation):
        return valuation[self.name]





class Const(Formula):
    pass

class And(Formula):
    pass

class Or(Formula):
    pass

class Impl(Formula):
    pass

class Eq(Formula):
    pass

class Not(Formula):
    pass


if __name__ == '__main__':
    pass