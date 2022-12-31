from models.Ap import Ap
from models.Gr import Gr
from models.GrProduction import GrProduction
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
# import time
import threading
import time
# import filedialog
from tkinter import filedialog

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # init lists
        self.grs = []
        self.aps = []
        self.count = 0
        self.ap = None
        # add gr to list

        self.title("Proyecto 2 - 202010856")
        self.geometry(f"{1400}x{700}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, rowspan=10, padx=(
            20, 20), pady=(20, 20), sticky="nsew")

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame, text="Bienvenido", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=4, columnspan=10,
                              padx=10, pady=10, sticky="nsew")

        self.label_student = customtkinter.CTkLabel(
            master=self.content_frame, text="Edwin Sandoval López - 202010856", font=customtkinter.CTkFont(size=15, weight="bold"), justify=tkinter.LEFT)
        self.label_student.grid(row=1, column=4, columnspan=10,
                                padx=10, pady=0, sticky="nsew")

        self.label_curso = customtkinter.CTkLabel(
            master=self.content_frame, text="Laboratorio de Lenguajes Formales de Programación, Sección N", font=customtkinter.CTkFont(size=15, weight="bold"), justify=tkinter.LEFT)
        self.label_curso.grid(row=2, column=4, columnspan=10,
                              padx=10, pady=0, sticky="nsew")

        self.progressbar_1 = customtkinter.CTkProgressBar(self.content_frame)
        self.progressbar_1.grid(row=5, column=4, columnspan=10, padx=(
            20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.set(0)
        threading.Thread(target=self.load_init).start()

    def load_init(self):
        actual = 0
        while actual < 1:
            actual += 0.20
            self.progressbar_1.set(actual)
            time.sleep(1)
            if actual == 1:
                self.initFrame()

    def initFrame(self):
        self.content_frame.grid_remove()

        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Proyecto 2", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame, text="Gramáticas", command=self.frameGramatic)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame, text="Automatas", command=self.frameAutomatas)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Salir", fg_color="gray", command=self.exit)
        self.sidebar_button_3.grid(row=8, column=0, padx=20, pady=10)
        self.content_frame = customtkinter.CTkFrame(self)

        self.label_alert = None

        self.frameMain()

    def frameMain(self):
        self.content_frame.grid_remove()
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.grid(row=0, column=1,  rowspan=4, padx=(
            20, 20), pady=(20, 20), sticky="nsew")

        # configure grid layout (4x4)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure((2, 3), weight=0)
        self.content_frame.grid_rowconfigure(10, weight=1)

    def frameGramatic(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame.grid_remove()
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.grid(row=0, column=1,  rowspan=4, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame.grid_rowconfigure(4, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0, columnspan=4,
                              padx=10, pady=10, sticky="nsew")

        # create sidebar frame with widgets
        self.sidebar_options = customtkinter.CTkFrame(
            self.content_frame, width=140, corner_radius=0)
        self.sidebar_options.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_options.grid_rowconfigure(10, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_options, text="Gramáticas", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_0 = customtkinter.CTkButton(
            self.sidebar_options, text="Cargar archivo", command=self.frameGramaticFile)
        self.sidebar_button_0.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_options, text="Información general", command=self.frameGramaticShow)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_options, text="Árbol de derivación", command=self.frameGramaticThree)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)

        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)

    def frameGramaticShow(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Mostrar información general", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0,
                              padx=10, pady=10, sticky="nsew", )

        self.automatas_label = customtkinter.CTkLabel(
            self.content_frame_sub, text="Gramáticas", anchor="w")
        self.automatas_label.grid(row=1, column=0, padx=10, pady=10,)

        # recorrer los automatas y agregarlos al menu
        values_menu = []
        for gr in self.grs:
            values_menu.append(gr.name)

        self.automatas_optionemenu = customtkinter.CTkOptionMenu(
            self.content_frame_sub, values=values_menu)
        self.automatas_optionemenu.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button_evaluate = customtkinter.CTkButton(
            master=self.content_frame_sub, text="Mostrar", command=self.gramaticShow)
        self.button_evaluate.grid(
            row=2, column=4, padx=10, pady=10, sticky="nsew")

    def gramaticShow(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self.content_frame_sub, width=620, height=300)
        self.textbox.grid(row=3, column=0, rowspan=7,
                          padx=(20, 0), pady=(20, 0), sticky="nsew")

        gr = None
        for gr_item in self.grs:
            if gr_item.name == self.automatas_optionemenu.get():
                gr = gr_item
                break

        # insert text
        self.textbox.insert(tkinter.END, gr)

    def frameGramaticThree(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Árbol de derivación", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0,
                              padx=10, pady=10, sticky="nsew", )

        self.automatas_label = customtkinter.CTkLabel(
            self.content_frame_sub, text="Gramáticas", anchor="w")
        self.automatas_label.grid(row=1, column=0, padx=10, pady=10,)

        # recorrer los automatas y agregarlos al menu
        values_menu = []
        for gr in self.grs:
            values_menu.append(gr.name)

        self.automatas_optionemenu = customtkinter.CTkOptionMenu(
            self.content_frame_sub, values=values_menu)
        self.automatas_optionemenu.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button_evaluate = customtkinter.CTkButton(
            master=self.content_frame_sub, text="Generar", command=self.treeShow)
        self.button_evaluate.grid(
            row=2, column=4, padx=10, pady=10, sticky="nsew")

    def treeShow(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        gr = None
        for gr_item in self.grs:
            if gr_item.name == self.automatas_optionemenu.get():
                gr = gr_item
                break

        file_name = gr.generateTree()

        # insert image ./imgs/afd_example.png
        self.image = Image.open(file_name)
        # resize image height 500
        width, height = self.image.size
        new_height = 450
        new_width = int((new_height * width) / height)
        self.image = self.image.resize(
            (new_width, new_height), Image.ANTIALIAS)

        self.image = ImageTk.PhotoImage(self.image)
        self.label_image = customtkinter.CTkLabel(
            self.content_frame_sub, image=self.image)
        self.label_image.grid(row=4, column=0, columnspan=4, padx=(
            20, 0), pady=(20, 0), sticky="nsew")

    def frameGramaticFile(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)

        init = "./"

        file = filedialog.askopenfilename(
            initialdir=init, title="Select file", filetypes=(("Text files", "*.glc"), ("all files", "*.*")))

        if file == "":
            return

        # validar que sea un archivo txt
        if file.split(".")[-1] != "glc":
            self.alert("Error: El archivo debe ser un archivo gr")
            return

        f = open(file, "r")
        lines = f.readlines()
        f.close()

        state = 0
        name = ""
        no_terminals = ""
        terminals = ""
        initial_no_terminal = ""
        accepting_no_terminals = []
        productions = []
        flag = True
        for line in lines:
            if state == 0:
                name = self.replaceSpacing(line)
                state = 1
            elif state == 1:
                no_terminals = self.replaceSpacing(line)
                no_terminals = no_terminals.split(",")
                state = 2
            elif state == 2:
                terminals = self.replaceSpacing(line)
                terminals = terminals.split(",")
                # ver que terminals no existan en no_terminals
                for terminal in terminals:
                    if terminal in no_terminals:
                        self.alert(
                            "Error: El terminal " + terminal + " ya existe en los no terminales")
                        flag = False
                state = 3
            elif state == 3:
                initial_no_terminal = self.replaceSpacing(line)
                if initial_no_terminal not in no_terminals:
                    self.alert(
                        "Error: El no terminal inicial no existe en los no terminales")
                    flag = False
                state = 5
            elif state == 5:
                transition = line
                if self.replaceSpacing(line) == "%" or self.replaceSpacing(line) == "":
                    # crear afd
                    for gr in self.grs:
                        if gr.name == name:
                            self.alert(
                                "Error: Ya existe un gr con el mismo nombre")
                            flag = False

                    if flag:
                        self.grs.append(
                            Gr(name, no_terminals, terminals, initial_no_terminal, accepting_no_terminals, productions))
                    state = 0
                    name = ""
                    no_terminals = ""
                    terminals = ""
                    initial_no_terminal = ""
                    accepting_no_terminals = []
                    productions = []
                    flag = True
                else:
                    transitions0 = transition.split(">")
                    transitions1 = transitions0[1].split(" ")
                    # eliminar epsilon los que sean espacios o vacios
                    transitions1 = list(filter(None, transitions1))
                    t_terminals = []
                    for transition in transitions1:
                        transition = self.replaceSpacing(transition)
                        if transition in no_terminals:
                            t_terminals.append(transition)
                        elif transition in terminals:
                            t_terminals.append(transition)
                        else:
                            self.alert(
                                "Error: El e/no terminal " + transition + " no existe en los terminales")
                            flag = False
                    productions.append(GrProduction(
                        transitions0[0], t_terminals))

        self.success("Grs creados con exito")

    def frameAutomatas(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame.grid_remove()
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.grid(row=0, column=1,  rowspan=4, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame.grid_rowconfigure(4, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0, columnspan=4,
                              padx=10, pady=10, sticky="nsew")

        # create sidebar frame with widgets
        self.sidebar_options = customtkinter.CTkFrame(
            self.content_frame, width=140, corner_radius=0)
        self.sidebar_options.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_options.grid_rowconfigure(10, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_options, text="Automatas", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_0 = customtkinter.CTkButton(
            self.sidebar_options, text="Cargar archivos", command=self.frameAutomatasFile)
        self.sidebar_button_0.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_options, text="Mostrar información", command=self.frameAutomatasShow)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_options, text="Validar una cadena", command=self.frameAutomataValidate)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(
            self.sidebar_options, text="Recorrido paso a paso", command=self.frameAutomatasStepByStep)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)

        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)

    def frameAutomatasFile(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)

        init = "./"

        file = filedialog.askopenfilename(
            initialdir=init, title="Select file", filetypes=(("Text files", "*.ap"), ("all files", "*.*")))

        if file == "":
            return

        # validar que sea un archivo txt
        if file.split(".")[-1] != "ap":
            self.alert("Error: El archivo debe ser un archivo ap")
            return

        f = open(file, "r")
        lines = f.readlines()
        f.close()

        state = 0
        name = ""
        alphabet = []
        simbols = []
        states = []
        initial_state = ""
        acceptance_state = ""
        transitions = []
        flag = True
        for line in lines:
            if state == 0:
                name = self.replaceSpacing(line)
                state = 1
            elif state == 1:
                alphabet = self.replaceSpacing(line)
                alphabet = alphabet.split(",")
                state = 2
            elif state == 2:
                simbols = self.replaceSpacing(line)
                simbols = simbols.split(",")
                state = 3
            elif state == 3:
                states = self.replaceSpacing(line)
                states = states.split(",")
                state = 5
            elif state == 5:
                initial_state = self.replaceSpacing(line)
                state = 6
            elif state == 6:
                acceptance_state = self.replaceSpacing(line)
                state = 7
            elif state == 7:
                if self.replaceSpacing(line) == "%" or self.replaceSpacing(line) == "":
                    # crear afd
                    for ap in self.aps:
                        if ap.name == name:
                            self.alert(
                                "Error: Ya existe un ap con el mismo nombre")
                            flag = False

                    if flag:
                        self.aps.append(
                            Ap(name, alphabet, simbols, states, initial_state, acceptance_state, transitions))
                    transitions = []
                    state = 0
                    flag = True

                else:
                    line = self.replaceSpacing(line)
                    # separar por comas o puntos y comas
                    line = line.split(",")
                    sep = line[2].split(";")
                    line = [line[0], line[1], sep[0], sep[1], line[3]]
                    transitions.append(line)

        self.success("Grs creados con exito")

    def frameAutomatasShow(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Mostrar información de autómata", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0,
                              padx=10, pady=10, sticky="nsew", )

        self.automatas_label = customtkinter.CTkLabel(
            self.content_frame_sub, text="Automatas", anchor="w")
        self.automatas_label.grid(row=1, column=0, padx=10, pady=10,)

        # recorrer los automatas y agregarlos al menu
        values_menu = []
        for ap in self.aps:
            values_menu.append(ap.name)

        self.automatas_optionemenu = customtkinter.CTkOptionMenu(
            self.content_frame_sub, values=values_menu)
        self.automatas_optionemenu.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button_evaluate = customtkinter.CTkButton(
            master=self.content_frame_sub, text="Generar", command=self.automataShow)
        self.button_evaluate.grid(
            row=2, column=4, padx=10, pady=10, sticky="nsew")

    def automataShow(self):
        ap = None
        for ap_item in self.aps:
            if ap_item.name == self.automatas_optionemenu.get():
                ap = ap_item
                break

        ap.generatePdf()
        self.success("Archivo generado con exito")

    def frameAutomataValidate(self):
        # esconder alerta
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Evaluar Cadena", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0,
                              padx=10, pady=10, sticky="nsew", )

        self.afds_label = customtkinter.CTkLabel(
            self.content_frame_sub, text="Autómatas", anchor="w")
        self.afds_label.grid(row=1, column=0, padx=10, pady=10,)

        # recorrer los afds y agregarlos al menu
        values_menu = []
        for ap in self.aps:
            values_menu.append(ap.name)

        self.automatas_optionemenu = customtkinter.CTkOptionMenu(
            self.content_frame_sub, values=values_menu)
        self.automatas_optionemenu.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew")

        self.label_evaluate = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Cadena", justify=tkinter.LEFT)
        self.label_evaluate.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.text_evaluate = customtkinter.CTkEntry(
            master=self.content_frame_sub, width=30)
        self.text_evaluate.grid(
            row=2, column=1, padx=10, pady=10, columnspan=9, sticky="nsew")

        self.button_evaluate = customtkinter.CTkButton(
            master=self.content_frame_sub, text="Solo Valida", command=self.validateString)
        self.button_evaluate.grid(
            row=3, column=4, padx=10, pady=10, sticky="nsew")

        self.button_route = customtkinter.CTkButton(
            master=self.content_frame_sub, text="Ruta", command=self.validateStringRoute)
        self.button_route.grid(
            row=3, column=3, padx=10, pady=10, sticky="nsew")

        self.button_route = customtkinter.CTkButton(
            master=self.content_frame_sub, text="En una pasada", command=self.validateStringOnePass)
        self.button_route.grid(
            row=3, column=2, padx=10, pady=10, sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self.content_frame_sub, width=620, height=280)
        self.textbox.grid(row=4, column=0, columnspan=8,
                          padx=(20, 20), pady=(20, 0), sticky="nsew")

    def validateString(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.textbox.delete("1.0", "end")

        ap = None
        for ap_item in self.aps:
            if ap_item.name == self.automatas_optionemenu.get():
                ap = ap_item
                break

        if ap is not None:
            text = self.text_evaluate.get()
            text = self.replaceSpacing(text)
            if text != "":
                if ap.validateString(text):
                    self.success("Cadena válida")
                else:
                    self.alert("Cadena no válida")
            else:
                self.alert("Ingrese una cadena")
        else:
            self.alert("Seleccione un autómata")

    def validateStringRoute(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.textbox.delete("1.0", "end")
        ap = None
        for ap_item in self.aps:
            if ap_item.name == self.automatas_optionemenu.get():
                ap = ap_item
                break

        if ap is not None:
            text = self.text_evaluate.get()
            text = self.replaceSpacing(text)
            if text != "":
                if ap.validateString(text):
                    self.textbox.insert("1.0", str(
                        ap.validateStringRoute()) + "\n")
                    self.success("Cadena válida")
                else:
                    self.alert("Cadena no válida")
            else:
                self.alert("Ingrese una cadena")
        else:
            self.alert("Seleccione un autómata")

    def validateStringOnePass(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.textbox.delete("1.0", "end")

        ap = None
        for ap_item in self.aps:
            if ap_item.name == self.automatas_optionemenu.get():
                ap = ap_item
                break

        if ap is not None:
            text = self.text_evaluate.get()
            text = self.replaceSpacing(text)
            if text != "":
                if ap.validateStringOnePass(text):
                    self.success("Cadena válida")
                else:
                    self.alert("Cadena no válida")
            else:
                self.alert("Ingrese una cadena")
        else:
            self.alert("Seleccione un autómata")

    def frameAutomatasStepByStep(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        self.content_frame_sub.grid_remove()
        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)
        self.content_frame_sub.grid(row=0, column=1,  rowspan=7, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.content_frame_sub.grid_rowconfigure(10, weight=1)
        self.content_frame_sub.grid_columnconfigure(1, weight=1)
        # border radius content frame

        self.label_title = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Evaluar Cadena", font=customtkinter.CTkFont(size=20, weight="bold"), justify=tkinter.LEFT)
        self.label_title.grid(row=0, column=0,
                              padx=10, pady=10, sticky="nsew", )

        self.afds_label = customtkinter.CTkLabel(
            self.content_frame_sub, text="Autómatas", anchor="w")
        self.afds_label.grid(row=1, column=0, padx=10, pady=10,)

        # recorrer los afds y agregarlos al menu
        values_menu = []
        for ap in self.aps:
            values_menu.append(ap.name)

        self.automatas_optionemenu = customtkinter.CTkOptionMenu(
            self.content_frame_sub, values=values_menu)
        self.automatas_optionemenu.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew")

        self.label_evaluate = customtkinter.CTkLabel(
            master=self.content_frame_sub, text="Cadena", justify=tkinter.LEFT)
        self.label_evaluate.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.text_evaluate = customtkinter.CTkEntry(
            master=self.content_frame_sub, width=30)
        self.text_evaluate.grid(
            row=2, column=1, padx=10, pady=10, columnspan=9, sticky="nsew")

        self.button_evaluate = customtkinter.CTkButton(
            master=self.content_frame_sub, text="Validar", command=self.validateStringStepByStep)
        self.button_evaluate.grid(
            row=3, column=4, padx=10, pady=10, sticky="nsew")

    def validateStringStepByStep(self):
        if self.label_alert is not None:
            self.label_alert.grid_forget()

        for ap_item in self.aps:
            if ap_item.name == self.automatas_optionemenu.get():
                self.ap = ap_item
                break

        if self.ap is not None:
            text = self.text_evaluate.get()
            text = self.replaceSpacing(text)
            if text != "":
                if self.ap.validateStringOnePass(text):
                    self.count = 0
                    response = self.ap.generateDotPass(self.count)
                    
                    self.button_route = customtkinter.CTkButton(
                        master=self.content_frame_sub, text="Siguiente", command=self.nextRoute)
                    self.button_route.grid(
                        row=4, column=2, padx=10, pady=10, sticky="nsew")

                    self.button_route = customtkinter.CTkButton(
                        master=self.content_frame_sub, text="Anterior", command=self.previousRoute)
                    self.button_route.grid(
                        row=4, column=3, padx=10, pady=10, sticky="nsew")


                    self.image = Image.open(response)
                    # set width 600
                    width_percent = (600 / float(self.image.size[0]))
                    hsize = int(
                        (float(self.image.size[1]) * float(width_percent)))
                    self.image = self.image.resize(
                        (600, hsize), Image.ANTIALIAS)

                    self.image = ImageTk.PhotoImage(self.image)
                    self.label_image = customtkinter.CTkLabel(
                        self.content_frame_sub, image=self.image)
                    self.label_image.grid(row=5, column=0, columnspan=4, padx=(
                        20, 0), pady=(20, 0), sticky="nsew")

                else:
                    self.alert("Cadena no válida")
            else:
                self.alert("Ingrese una cadena")
        else:
            self.alert("Seleccione un autómata")

    def previousRoute(self):
        if self.count > 0:
            self.count -= 1
            response = self.ap.generateDotPass(self.count)
            self.image = Image.open(response)
            # set width 600
            width_percent = (600 / float(self.image.size[0]))
            hsize = int((float(self.image.size[1]) * float(width_percent)))
            self.image = self.image.resize((600, hsize), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.label_image.configure(image=self.image)
            self.label_image.image = self.image

    def nextRoute(self):
        if self.count < len(self.ap.states) - 1:
            self.count += 1
            response = self.ap.generateDotPass(self.count)
            self.image = Image.open(response)
            # set width 600
            width_percent = (600 / float(self.image.size[0]))
            hsize = int((float(self.image.size[1]) * float(width_percent)))
            self.image = self.image.resize((600, hsize), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.label_image.configure(image=self.image)
            self.label_image.image = self.image

    def replaceSpacing(self, text):
        text = text.replace(" ", "")
        text = text.replace("\n", "")
        text = text.replace("\t", "")
        return text

    def exit(self):
        self.destroy()

    def alert(self, title):
        self.label_alert = customtkinter.CTkLabel(
            master=self.content_frame_sub, text=title, fg_color=("red", "#f5c2c7"), corner_radius=5,  text_color="#842029", font=customtkinter.CTkFont(size=15, weight="bold"), justify=tkinter.LEFT)
        self.label_alert.grid(
            row=8, rowspan=1, column=0, padx=10, pady=10, columnspan=6, sticky="nsew")

    def success(self, title):
        self.label_alert = customtkinter.CTkLabel(
            master=self.content_frame_sub, text=title, fg_color=("green", "#d1e7dd"), corner_radius=5,  text_color="#0f5132", font=customtkinter.CTkFont(size=15, weight="bold"), justify=tkinter.LEFT)
        self.label_alert.grid(
            row=8, rowspan=1, column=0, padx=10, pady=10, columnspan=6, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
