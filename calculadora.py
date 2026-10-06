import tkinter as tk
import math

# --- DICCIONARIO DE TEMAS ---
TEMAS = {
    "oscuro": {
        "bg_ventana": "#1e1e1e",
        "bg_pantalla": "#2d2d2d",
        "fg_pantalla": "white",
        "bg_numero": "#333333",
        "fg_numero": "white",
        "bg_op": "#ff9800",
        "fg_op": "white",
        "bg_igual": "#4CAF50",
        "fg_igual": "white",
        "bg_limpiar": "#f44336",
        "fg_limpiar": "white",
        "bg_cientifico": "#00bcd4",
        "fg_cientifico": "white",
        "menu_bg": "#2d2d2d",
        "menu_fg": "white"
    },
    "claro": {
        "bg_ventana": "#f0f0f0",
        "bg_pantalla": "#ffffff",
        "fg_pantalla": "#333333",
        "bg_numero": "#e0e0e0",
        "fg_numero": "#000000",
        "bg_op": "#ffb74d",
        "fg_op": "#000000",
        "bg_igual": "#81c784",
        "fg_igual": "#000000",
        "bg_limpiar": "#e57373",
        "fg_limpiar": "#000000",
        "bg_cientifico": "#4dd0e1",
        "fg_cientifico": "#000000",
        "menu_bg": "#ffffff",
        "menu_fg": "#333333"
    },
    "hacker": {
        "bg_ventana": "#0d0208",
        "bg_pantalla": "#1a0005",
        "fg_pantalla": "#00ff66",
        "bg_numero": "#161b22",
        "fg_numero": "#00ff66",
        "bg_op": "#ff0055",
        "fg_op": "#ffffff",
        "bg_igual": "#00ff66",
        "fg_igual": "#0d0208",
        "bg_limpiar": "#ff3300",
        "fg_limpiar": "#ffffff",
        "bg_cientifico": "#9900ff",
        "fg_cientifico": "#ffffff",
        "menu_bg": "#161b22",
        "menu_fg": "#00ff66"
    }
}

# Tema actual por defecto
tema_actual = "oscuro"

def pulsar(valor):
    actual = texto_pantalla.get()
    if actual in ("Error", "Modo Científico"):
        texto_pantalla.set(str(valor))
    else:
        texto_pantalla.set(actual + str(valor))

def limpiar():
    texto_pantalla.set("")

def calcular():
    try:
        expresion = texto_pantalla.get()
        expresion = expresion.replace('^', '**').replace('×', '*').replace('÷', '/')
        resultado = str(eval(expresion))
        texto_pantalla.set(resultado)
    except Exception:
        texto_pantalla.set("Error")

def calcular_cientifica(func):
    try:
        val_str = texto_pantalla.get()
        if not val_str or val_str == "Error":
            return
        val = float(val_str)
        if func == 'raiz': res = math.sqrt(val)
        elif func == 'cuadrado': res = val ** 2
        elif func == 'cubo': res = val ** 3
        elif func == 'sin': res = math.sin(math.radians(val))
        elif func == 'cos': res = math.cos(math.radians(val))
        elif func == 'tan': res = math.tan(math.radians(val))
        elif func == 'log': res = math.log10(val)
        elif func == 'ln': res = math.log(val)
        texto_pantalla.set(str(res))
    except Exception:
        texto_pantalla.set("Error")

def insertar_constante(const):
    actual = texto_pantalla.get()
    val = str(math.pi) if const == 'pi' else str(math.e)
    if actual in ("Error", "Modo Científico", ""):
        texto_pantalla.set(val)
    else:
        texto_pantalla.set(actual + "*" + val)

def cambiar_modo(modo):
    if modo == "basica":
        ventana.geometry("290x410")
        frame_cientifico.grid_remove()
        frame_basico.grid()
    elif modo == "cientifica":
        ventana.geometry("290x560")
        frame_basico.grid()
        frame_cientifico.grid()

def aplicar_tema(nombre_tema):
    global tema_actual
    tema_actual = nombre_tema
    t = TEMAS[tema_actual]

    # Ventana y menús
    ventana.config(bg=t["bg_ventana"])
    menu_modos.config(bg=t["menu_bg"], fg=t["menu_fg"])
    menu_temas.config(bg=t["menu_bg"], fg=t["menu_fg"])
    barra_menu.config(bg=t["menu_bg"], fg=t["menu_fg"])

    # Pantalla
    pantalla.config(bg=t["bg_pantalla"], fg=t["fg_pantalla"], insertbackground=t["fg_pantalla"])

    # Frames
    frame_basico.config(bg=t["bg_ventana"])
    frame_cientifico.config(bg=t["bg_ventana"])

    # Actualizar botones básicos y limpiar
    for btn in botones_widgets:
        texto = btn.cget("text")
        if texto in ('/', '*', '-', '+'):
            btn.config(bg=t["bg_op"], fg=t["fg_op"])
        elif texto == '=':
            btn.config(bg=t["bg_igual"], fg=t["fg_igual"])
        elif texto == 'C':
            btn.config(bg=t["bg_limpiar"], fg=t["fg_limpiar"])
        else:
            btn.config(bg=t["bg_numero"], fg=t["fg_numero"])

    # Actualizar botones científicos
    for btn in botones_cientificos_widgets:
        btn.config(bg=t["bg_cientifico"], fg=t["fg_cientifico"])

# --- VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Calculadora Pro")
ventana.geometry("290x410")
ventana.config(bg=TEMAS[tema_actual]["bg_ventana"])
ventana.resizable(False, False)

# --- BARRA DE MENÚ ---
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Modos
menu_modos = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Modos", menu=menu_modos)
menu_modos.add_command(label="Calculadora Básica", command=lambda: cambiar_modo("basica"))
menu_modos.add_command(label="Calculadora Científica", command=lambda: cambiar_modo("cientifica"))

# Menú Temas (¡Nuevo!)
menu_temas = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Temas", menu=menu_temas)
menu_temas.add_command(label="Oscuro (Default)", command=lambda: aplicar_tema("oscuro"))
menu_temas.add_command(label="Claro", command=lambda: aplicar_tema("claro"))
menu_temas.add_command(label="Hacker (Neon)", command=lambda: aplicar_tema("hacker"))

menu_modos.add_separator()
menu_modos.add_command(label="Salir", command=ventana.quit)

texto_pantalla = tk.StringVar()

# Pantalla de resultados
t = TEMAS[tema_actual]
pantalla = tk.Entry(
    ventana, 
    textvariable=texto_pantalla, 
    font=("Arial", 20), 
    bd=5, 
    bg=t["bg_pantalla"], 
    fg=t["fg_pantalla"], 
    insertbackground=t["fg_pantalla"], 
    width=18, 
    justify="right"
)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Listas para guardar las referencias de los botones y actualizarlos al cambiar de tema
botones_widgets = []
botones_cientificos_widgets = []

# --- CONTENEDOR BÁSICO ---
frame_basico = tk.Frame(ventana, bg=t["bg_ventana"])
frame_basico.grid(row=1, column=0, columnspan=4)

botones_basicos_info = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3)
]

for (texto, fila, col) in botones_basicos_info:
    if texto in ('/', '*', '-', '+'):
        bg_c, fg_c = t["bg_op"], t["fg_op"]
    elif texto == '=':
        bg_c, fg_c = t["bg_igual"], t["fg_igual"]
    else:
        bg_c, fg_c = t["bg_numero"], t["fg_numero"]

    cmd = calcular if texto == '=' else lambda t_txt=texto: pulsar(t_txt)
    btn = tk.Button(frame_basico, text=texto, width=4, height=2, font=("Arial", 14, "bold"), bg=bg_c, fg=fg_c, bd=0, command=cmd)
    btn.grid(row=fila, column=col, padx=4, pady=4)
    botones_widgets.append(btn)

# Botón limpiar
btn_limpiar = tk.Button(frame_basico, text="C", width=20, height=1, font=("Arial", 12, "bold"), bg=t["bg_limpiar"], fg=t["fg_limpiar"], bd=0, command=limpiar)
btn_limpiar.grid(row=4, column=0, columnspan=4, padx=4, pady=4)
botones_widgets.append(btn_limpiar)

# --- CONTENEDOR CIENTÍFICO ---
frame_cientifico = tk.Frame(ventana, bg=t["bg_ventana"])
frame_cientifico.grid(row=2, column=0, columnspan=4, pady=5)

botones_cientificos_info = [
    ('√', 0, 0, 'raiz', 'func'), ('x²', 0, 1, 'cuadrado', 'func'), ('x³', 0, 2, 'cubo', 'func'), ('^', 0, 3, '**', 'pulsar'),
    ('sin', 1, 0, 'sin', 'func'), ('cos', 1, 1, 'cos', 'func'), ('tan', 1, 2, 'tan', 'func'), ('(', 1, 3, '(', 'pulsar'),
    ('log', 2, 0, 'log', 'func'), ('ln', 2, 1, 'ln', 'func'), ('π', 2, 2, 'pi', 'const'), (')', 2, 3, ')', 'pulsar')
]

for (texto, fila, col, accion, tipo) in botones_cientificos_info:
    if tipo == 'func': cmd = lambda f=accion: calcular_cientifica(f)
    elif tipo == 'const': cmd = lambda c=accion: insertar_constante(c)
    elif tipo == 'pulsar': cmd = lambda p=accion: pulsar(p)

    btn = tk.Button(frame_cientifico, text=texto, width=4, height=1, font=("Arial", 11, "bold"), bg=t["bg_cientifico"], fg=t["fg_cientifico"], bd=0, command=cmd)
    btn.grid(row=fila, column=col, padx=4, pady=2)
    botones_cientificos_widgets.append(btn)

frame_cientifico.grid_remove()

ventana.mainloop()
