# import os
import os

# create class Afd


class Gr:
    # static variable to autoincrement id
    id = 0
    # constructor

    def __init__(self, name, no_terminals, terminals, initial_no_terminal, accepting_no_terminals, productions):
        # autoincrement id
        Gr.id += 1
        self.name = name
        self.no_terminals = no_terminals
        self.terminals = terminals
        self.initial_no_terminal = initial_no_terminal
        self.productions = productions
        self.accepting_no_terminals = accepting_no_terminals
        self.dot = ''
        self.last_node = 0

    def __str__(self):
        no_terminals = ""
        for no_terminal in self.no_terminals:
            no_terminals += no_terminal + ","
        no_terminals = no_terminals[:-1]

        terminals = ""
        for terminal in self.terminals:
            terminals += terminal + ","
        terminals = terminals[:-1]

        productions = ""
        for production in self.productions:
            productions += str(production) + "\n"

        return f'Nombre: {self.name} \nNo Terminals: {no_terminals} \nTerminals: {terminals} \nNo terminal inicial: {self.initial_no_terminal} \nProductions: \n{productions}'

    def generateTree(self):
        # quitar espacios
        name = self.name.replace(' ', '')
        name = name + 'tree'
        productions = self.productions.copy()

        self.dot = ''
        self.last_node = 0
        self.dot += f'graph {name} {"{"} \n'
        self.dot += f'node [color=lightblue2, fontcolor=black, shape=box]; \n'
        self.dot += f'layout=dot; rankdir=TB; shape=circle \n'    
        self.dot += f'nodo0 [label=init shape=plain]\r'    
        self.recursiveExpression(productions, 0, self.initial_no_terminal)
        self.dot += '}'

        document = open(f'dots/{name}.dot', 'w')
        document.write(self.dot)
        document.close()

        os.system(
            f'dot -Tpng dots/{name}.dot -o pngs/{name}.png')

        return f'pngs/{name}.png'

    def recursiveExpression(self, productions, node, expression):
        make_node = node
        response = self.searchProduction(expression, productions)
        production = response['production']
        productions.pop(response['index'])
        self.writeDot(expression, self.last_node, make_node)
        for terminal in production.terminals:
            if self.typeExpression(terminal) == 'terminal':
                make_node += 1
                self.writeDot(terminal, node, make_node)
            if self.typeExpression(terminal) == 'no_terminal':
                make_node += 1
                make_node = self.recursiveExpression(productions, make_node, terminal)
        return make_node
        
        
    def writeDot(self, expression, node, node_make):
        type = self.typeExpression(expression)
        if type == 'no_terminal':
            self.last_node = node_make
        shape = type == 'terminal' and 'plain' or 'circle'
        self.dot += f'nodo{node_make} [label={expression} shape={shape}]\r'
        if node_make > 0:
            self.dot += f'nodo{node} -- nodo{node_make}\r'

    def typeExpression(self, expression):
        for terminal in self.terminals:
            if terminal == expression:
                return 'terminal'

        for no_terminal in self.no_terminals:
            if no_terminal == expression:
                return 'no_terminal'

    def searchProduction(self, no_terminal, productions):
        for production in productions:
            if production.no_terminal == no_terminal:
                return {'production' : production, 'index': productions.index(production)}
