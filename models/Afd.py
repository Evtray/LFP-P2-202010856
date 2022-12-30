# import os
import os

# create class Afd
class Afd:
    # static variable to autoincrement id
    id = 0
    # constructor

    def __init__(self, name, states, alphabet, initial_state, accepting_states, transitions):
        # autoincrement id
        Afd.id += 1
        self.name = name
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def __str__(self):
        return "States: " + str(self.states) + " Alphabet: " + str(self.alphabet) + " Transitions: " + str(self.transitions) + " Initial State: " + str(self.initial_state) + " Final States: " + str(self.final_states)

    def validateString(self, type, chars):

        currentState = self.initial_state
        transitions_used = []

        for char in chars:
            if char not in self.alphabet:
                return {"result": False, "msg": "El caracter " + char + " no esta en el alfabeto"}

            is_valid = False
            search_transition = self.searchTransition(currentState)
            for transition in search_transition:
                if transition[1] == char:
                    transitions_used.append(transition)
                    currentState = transition[2]
                    is_valid = True
                    break
            
            if not is_valid:
                return {"result": False, "msg": "No existe una transicion para el caracter " + char + " en el estado " + currentState}

        if currentState in self.accepting_states:
            if type == "route":
                self.generatePdf(transitions_used)
                return {"result": True, "msg": "Reporte generado"}
                
            return {"result": True, "msg": f'La cadena es valida'}
        else:
            return {"result": False, "msg": "La cadena no es valida"}


    def searchTransition(self, currentState):
        transitions = []
        for transition in self.transitions:
            if transition[0] == currentState:
                transitions.append(transition)

        return transitions

    def generatePdf(self, transitions_used):
        dot = ''
        dot += f'digraph prueba {"{"} \n'
        dot += f'node [style=filled, color=lightblue2, fontcolor=black, shape=box]; \n'
        dot += f'layout=dot; rankdir=LR; shape=circle \n'
        for transtion in transitions_used:
            dot += f'{transtion[0]} -> {transtion[2]} [label = "{transtion[1]}"]; \n'
        dot += f'"Nombre: {self.name} \n'
        dot += f'" [shape=box] \n {"}"}  \n'

        document = open(f'dots/{self.name}-route.dot', 'w')
        document.write(dot)
        document.close()
        os.system(f'dot.exe -Tpdf dots/{self.name}-route.dot -o pdfs/{self.name}-route.pdf')
        
        return True

    def generateDot(self):
        dot = f'digraph {self.name} {"{"} \n'
        # add padding to graph
        dot += f'node [style=filled, color=lightblue2, fontcolor=black, shape=box]; \n'
        dot += f'layout=dot; rankdir=LR; shape=circle \n'
        dot += f'{self.initial_state} [shape = doublecircle]; \n'
        for state in self.states:
            if state in self.accepting_states:
                dot += f'{state} [shape = doublecircle]; \n'
            else:
                dot += f'{state} [shape = circle]; \n'
        dot += f'Inicio [shape = plaintext]; \n'	
        dot += f'Inicio -> {self.initial_state}; \n'

        for transition in self.transitions:
            dot += f'{transition[0]} -> {transition[2]} [label = "{transition[1]}"]; \n'
        
        dot += f'"Nombre: {self.name} \n'
        dot += f'Estados: '
        # recorrer states
        for state in self.states:
            dot += f'{state},'

        dot += f'\n Alfabeto: '
        # recorrer alphabet
        for letter in self.alphabet:
            dot += f'{letter},'

        dot += f'\n Estados de aceptacion: '
        # recorrer accepting_states
        for state in self.accepting_states:
            dot += f'{state},'

        dot += f'\n Estado inicial: {self.initial_state} \n'

        dot += f'Transiciones: \n'
        for transition in self.transitions:
            dot += f'{transition[0]} -> {transition[1]};{transition[2]} \n'
        dot += f'" [shape=box] {"}"}'

        document = open(f'dots/{self.name}.dot', 'w')
        document.write(dot)
        document.close()

        os.system(f'dot.exe -Tpng dots/{self.name}.dot -o pngs/{self.name}.png')

        return True
        

