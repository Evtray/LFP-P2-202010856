from models.Afd import Afd
from models.Gr import Gr
from models.GrProduction import GrProduction
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
# import time
import threading
import time
#import filedialog
from tkinter import filedialog

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # init lists
        self.automatas = []
        self.grs = []
        
        # add gr to list
        self.grs.append(Gr("GR 1", ["S", "A", "B", "C"], ["a", "b", "z"], "S", [], [
            GrProduction("S", ["A"]),
            GrProduction("A", ["a", "A", "a"]),
            GrProduction("A", ["B"]),
            GrProduction("B", ["b", "B", "b"]),
            GrProduction("B", ["C"]),
            GrProduction("C", ["z", "C"]),
            GrProduction("C", ["z"]),
        ]))

        self.type_afd = None
        self.validation_type = None

        self.title("Proyecto 1 - 202010856")
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
        self.initFrame()
        # threading.Thread(target=self.load_init).start()

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
            self.sidebar_frame, text="Automatas", command=self.frameGr)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Salir", fg_color="gray", command=self.exit)
        self.sidebar_button_3.grid(row=8, column=0, padx=20, pady=10)
        self.content_frame = customtkinter.CTkFrame(self)

        self.label_alert = None

        self.frameGramatic()

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
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

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

    def frameGr(self):
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
            self.sidebar_options, text="Cargar archivos", command=self.frameGrCreate)
        self.sidebar_button_0.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_options, text="Mostrar información", command=self.frameGrEvaluate)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_options, text="Validar una cadena", command=self.frameGrGenerate)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_options, text="Ruta de validación", command=self.frameGrHelp)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(
            self.sidebar_options, text="Recorrido paso a paso", command=self.frameGrHelp)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)

        self.sidebar_button_5 = customtkinter.CTkButton(
            self.sidebar_options, text="Validar cadena en una pasada", command=self.frameGrHelp)
        self.sidebar_button_5.grid(row=6, column=0, padx=20, pady=10)

        self.content_frame_sub = customtkinter.CTkFrame(self.content_frame)

    def replaceSpacing(self, text):
        text = text.replace(" ", "")
        text = text.replace("\n", "")
        text = text.replace("\t", "")
        return text

    def exit(self):
        self.destroy()

    def alert(self, title):
        print("alert", title)
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
