# import os
import os
from PIL import Image
from webbrowser import open_new_tab
import shutil
# create class Afd


class Ap:
    # static variable to autoincrement id
    id = 0
    # constructor

    def __init__(self, name,  alphabet, simbols, states, initial_state, acceptance_state, transitions):
        # autoincrement id
        Ap.id += 1
        self.name = name
        self.alphabet = alphabet
        self.simbols = simbols
        self.states = states
        self.initial_state = initial_state
        self.transitions = transitions
        self.acceptance_state = acceptance_state
        self.last_route = []
        self.last_transtions = []

    def __str__(self):
        alphabet = ""
        for alphabet in self.alphabet:
            alphabet += alphabet + ","
        alphabet = alphabet[:-1]

        simbols = ""
        for simbols in self.simbols:
            simbols += simbols + ","
        simbols = simbols[:-1]

        states = ""
        for states in self.states:
            states += states + ","
        states = states[:-1]

        transitions = ""
        for transitions in self.transitions:
            transitions += str(transitions) + "\n"

        return f'Nombre: {self.name} \nAlfabeto: {alphabet} \nSimbolos: {simbols} \nEstados: {states} \nEstado inicial: {self.initial_state} \nEstado de aceptacion: {self.acceptance_state} \nTransiciones: \n{transitions}'

    def generatePdf(self):
        name = self.name.replace(' ', '')
        name = name + "ap"

        dot = f'digraph {name} {"{"} \n'
        # add padding to graph
        dot += f'node [style=filled, color=lightblue2, fontcolor=black, shape=box]; \n'
        dot += f'layout=dot; rankdir=LR; shape=circle \n'
        dot += f'{self.initial_state} [shape = circle]; \n'
        for state in self.states:
            if not state == self.initial_state:
                if state == self.acceptance_state:
                    dot += f'{state} [shape = doublecircle]; \n'
                else:
                    dot += f'{state} [shape = circle]; \n'
        #      I -> A [label = "λ,λ;#"];
        for transition in self.transitions:
            dot += f'{transition[0]} -> {transition[3]} [label = "{transition[1]},{transition[2]};{transition[4]}"]; \n'

        dot += f'"Nombre: {self.name} \n'
        dot += f'Alfabeto: '
        # recorrer states
        for letter in self.alphabet:
            dot += f'{letter},'
        dot = dot[:-1]

        dot += f' \n'
        dot += f'Simbolos: '
        # recorrer states
        for simbol in self.simbols:
            dot += f'{simbol},'
        dot = dot[:-1]

        dot += f' \n'
        dot += f'Estados: '
        # recorrer states
        for state in self.states:
            dot += f'{state},'
        dot = dot[:-1]

        dot += f' \n'
        dot += f'Estado inicial: {self.initial_state} \n'
        dot += f'Estado de aceptacion: {self.acceptance_state} \n'
        dot += f'Transiciones: \n'
        for transition in self.transitions:
            for transition2 in transition:
                dot += f'{transition2},'
            dot = dot[:-1]
            dot += f' \n'

        dot += f'" [shape=box] {"}"}'

        document = open(f'dots/{name}.dot', 'w', encoding='utf-8')
        document.write(dot)
        document.close()

        os.system(
            f'dot.exe -Tpdf dots/{name}.dot -o pdfs/{name}.pdf')

        return True

    def validateString(self, rstring):
        # validate string
        count = 0
        self.last_route = []
        self.last_transtions = []
        stack = ['#']
        state = self.initial_state
        transition = search = self.searchTransition(state, '$')
        if transition:
            state = transition[3]
            self.last_route.insert(0, transition)
            self.last_transtions.insert(0, [count, [], "", transition])
        rstring = rstring
        rletter = ""
        for letter in rstring:
            count += 1
            rletter += letter
            if letter in self.alphabet or letter in self.simbols:
                search = self.searchTransition(state, letter)
                if search:
                    if not search[2] == '$':
                        if len(stack) > 0:
                            stack.pop()
                        else:
                            return False
                    if not search[4] == '$':
                        stack.append(search[4])

                    print(stack)
                    state = search[3]
                    self.last_route.insert(0, search)
                    self.last_transtions.insert(
                        0, [count, [] + stack, rletter, transition])
                else:
                    return False
            else:
                return False

        if len(stack) == 1:
            if stack[0]:
                transition = search = self.searchTransition(state, '$')
                if transition:
                    if transition[3] == self.acceptance_state:
                        self.last_route.insert(0, transition)
                        self.last_transtions.insert(
                            0, [count + 1, [], "#", transition])
                        return True

        return False

    def searchTransition(self, state, letter):
        for transition in self.transitions:
            if transition[0] == state and transition[1] == letter:
                return transition
        return False

    def validateStringRoute(self):
        response = "Ruta: \n"
        self.last_route.reverse()
        for transition in self.last_route:
            for transition2 in transition:
                response += f'{transition2},'
            response += f' \n'

        return response

    def validateStringOnePass(self, text):
        self.validateString(text)
        name = self.name.replace(' ', '')
        name = name + "table"

        dot = f'digraph {name} {"{"} \n'
        dot += f'AP1 [fillcolor = "#ff880022";label = <<table border="0" cellborder="1" cellspacing="0" cellpadding="20"> \n'
        dot += f'<tr> <td> <b>Iteración</b> </td> <td> Pila</td> <td> Entrada</td> <td> Transición</td> </tr> \n'
        self.last_transtions.reverse()
        for transition in self.last_transtions:
            temp1 = ""
            transition[1].reverse()
            for transition2 in transition[1]:
                temp1 += f'{transition2}'

            temp2 = ""
            for transition2 in transition[3]:
                temp2 += f'{transition2},'
            temp2 = temp2[:-1]

            dot += f'<tr> <td> {transition[0]} </td> <td> {temp1} </td> <td> {transition[2]} </td> <td> {temp2} </td> </tr> \n'
        dot += f'</table>>;shape = plain;]; \n'
        dot += '}'

        document = open(f'dots/{name}.dot', 'w', encoding='utf-8')
        document.write(dot)
        document.close()

        os.system(
            f'dot.exe -Tpdf dots/{name}.dot -o pdfs/{name}.pdf')

        return True
