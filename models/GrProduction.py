class GrProduction:

    def __init__(self, no_terminal, terminals):
        self.no_terminal = no_terminal
        self.terminals = terminals

    def __str__(self):
        terminals = ""
        for terminal in self.terminals:
            terminals += terminal + " ,"
        terminals = terminals[:-1]

        return f'{self.no_terminal} > {terminals}'
