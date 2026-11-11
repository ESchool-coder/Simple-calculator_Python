#This is better 
import tkinter as tk
from tkinter import font
import math
import re

class AcademicScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Academic Sci-Calc | Math, Physics & Chemistry")
        self.root.geometry("560x680")
        self.root.resizable(False, False)
        self.root.configure(bg="#11111b")

        self.expression = ""
        self.last_ans = 0
        self.angle_mode = "RAD"

        self.constants = {
            "NA": 6.02214076e23,
            "R_gas": 8.314462618,
            "c_light": 299792458,
            "h_planck": 6.62607015e-34,
            "k_B": 1.380649e-23,
            "e_charge": 1.602176634e-19,
            "G_grav": 6.67430e-11,
            "g_acc": 9.80665,
            "π": math.pi,
            "e": math.e
        }

        self.display_font = font.Font(family="Consolas", size=26, weight="bold")
        self.history_font = font.Font(family="Consolas", size=12)
        self.btn_font = font.Font(family="Segoe UI", size=11, weight="bold")
        self.mode_font = font.Font(family="Segoe UI", size=10, weight="bold")

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        top_frame = tk.Frame(self.root, bg="#181825", pady=15, padx=15)
        top_frame.pack(fill="both")

        status_frame = tk.Frame(top_frame, bg="#181825")
        status_frame.pack(fill="x")

        self.mode_btn = tk.Button(
            status_frame, text="MODE: RAD", font=self.mode_font,
            bg="#313244", fg="#a6e3a1", bd=0, padx=10, pady=2, cursor="hand2",
            command=self.toggle_angle_mode
        )
        self.mode_btn.pack(side="left")

        self.info_label = tk.Label(
            status_frame, text="Ready | University Edition", font=self.mode_font,
            bg="#181825", fg="#89b4fa", anchor="e"
        )
        self.info_label.pack(side="right")

        self.history_label = tk.Label(
            top_frame, text="", font=self.history_font,
            bg="#181825", fg="#a6adc8", anchor="e"
        )
        self.history_label.pack(fill="both", pady=(10, 0))

        self.display_var = tk.StringVar(value="0")
        self.display_label = tk.Label(
            top_frame, textvariable=self.display_var, font=self.display_font,
            bg="#181825", fg="#cdd6f4", anchor="e"
        )
        self.display_label.pack(fill="both", pady=(5, 0))

        btn_frame = tk.Frame(self.root, bg="#11111b", padx=10, pady=10)
        btn_frame.pack(fill="both", expand=True)

        buttons = [
            ['NA', 'R_gas', 'c', 'h', 'kB', 'G'],
            ['q_e', 'g', 'π', 'e', 'EE', 'ANS'],
            ['sin', 'cos', 'tan', 'asin', 'acos', 'atan'],
            ['ln', 'log10', 'x²', 'xʸ', '√', '∛'],
            ['(', ')', 'n!', '%', 'DEL', 'AC'],
            ['7', '8', '9', '÷', '1/x', '|x|'],
            ['4', '5', '6', '×', '10ˣ', 'eˣ'],
            ['1', '2', '3', '-', '0', '.'],
            ['+', '=']
        ]

        colors = {
            "const": ("#1e1e2e", "#f5c2e7"),
            "sci": ("#181825", "#94e2d5"),
            "num": ("#313244", "#cdd6f4"),
            "op": ("#45475a", "#f9e2af"),
            "clear": ("#f38ba8", "#11111b"),
            "eq": ("#89b4fa", "#11111b")
        }

        const_list = ['NA', 'R_gas', 'c', 'h', 'kB', 'G', 'q_e', 'g', 'π', 'e', 'EE', 'ANS']
        sci_list = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log10', 'x²', 'xʸ', '√', '∛', '(', ')', 'n!', '%', '1/x', '|x|', '10ˣ', 'eˣ']
        op_list = ['÷', '×', '-', '+']

        for r_idx, row in enumerate(buttons):
            btn_frame.rowconfigure(r_idx, weight=1)
            for c_idx, text in enumerate(row):
                btn_frame.columnconfigure(c_idx, weight=1)

                if text in const_list:
                    bg, fg = colors["const"]
                elif text in sci_list:
                    bg, fg = colors["sci"]
                elif text in op_list:
                    bg, fg = colors["op"]
                elif text in ['DEL', 'AC']:
                    bg, fg = colors["clear"]
                elif text == '=':
                    bg, fg = colors["eq"]
                else:
                    bg, fg = colors["num"]

                col_span = 1
                if r_idx == 8 and text == '+':
                    col_span = 2
                elif r_idx == 8 and text == '=':
                    c_idx = 2
                    col_span = 4

                btn = tk.Button(
                    btn_frame, text=text, font=self.btn_font,
                    bg=bg, fg=fg, bd=0, activebackground="#585b70",
                    activeforeground="#ffffff", cursor="hand2",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=r_idx, column=c_idx, columnspan=col_span, sticky="nsew", padx=2, pady=2)

    def toggle_angle_mode(self):
        self.angle_mode = "DEG" if self.angle_mode == "RAD" else "RAD"
        self.mode_btn.config(
            text=f"MODE: {self.angle_mode}",
            fg="#a6e3a1" if self.angle_mode == "RAD" else "#fab387"
        )

    def bind_keys(self):
        for key in '0123456789.+-*/()%':
            self.root.bind(key, lambda e, k=key: self.handle_keypress(k))
        self.root.bind('<Return>', lambda e: self.on_button_click('='))
        self.root.bind('<BackSpace>', lambda e: self.on_button_click('DEL'))
        self.root.bind('<Escape>', lambda e: self.on_button_click('AC'))

    def handle_keypress(self, key):
        mapping = {'*': '×', '/': '÷'}
        self.on_button_click(mapping.get(key, key))

    def show_constant_info(self, symbol):
        descriptions = {
            'NA': "Avogadro: 6.02214e23 mol⁻¹ (Moles/Atoms)",
            'R_gas': "Gas Const (R): 8.31446 J/(mol·K)",
            'c': "Speed of Light (c): 2.9979e8 m/s",
            'h': "Planck Const (h): 6.62607e-34 J·s",
            'kB': "Boltzmann (kB): 1.38065e-23 J/K",
            'G': "Gravitation (G): 6.6743e-11 N·m²/kg²",
            'q_e': "Elem. Charge (e⁻): 1.60218e-19 C",
            'g': "Std Gravity (g): 9.80665 m/s²"
        }
        if symbol in descriptions:
            self.info_label.config(text=descriptions[symbol])

    def on_button_click(self, char):
        self.show_constant_info(char)

        if char == 'AC':
            self.expression = ""
            self.history_label.config(text="")
            self.display_var.set("0")
            self.info_label.config(text="Ready | University Edition")

        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")

        elif char == '=':
            self.calculate()

        elif char in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log10', '√', '∛']:
            func_map = {
                'sin': 'sin(', 'cos': 'cos(', 'tan': 'tan(',
                'asin': 'asin(', 'acos': 'acos(', 'atan': 'atan(',
                'ln': 'ln(', 'log10': 'log10(', '√': 'sqrt(', '∛': 'cbrt('
            }
            self.expression += func_map[char]
            self.display_var.set(self.expression)

        elif char == 'x²':
            self.expression += '^2'
            self.display_var.set(self.expression)

        elif char == 'xʸ':
            self.expression += '^'
            self.display_var.set(self.expression)

        elif char == '10ˣ':
            self.expression += '10^'
            self.display_var.set(self.expression)

        elif char == 'eˣ':
            self.expression += 'e^'
            self.display_var.set(self.expression)

        elif char == '1/x':
            self.expression += '^(-1)'
            self.display_var.set(self.expression)

        elif char == '|x|':
            self.expression += 'abs('
            self.display_var.set(self.expression)

        elif char == 'n!':
            self.expression += '!'
            self.display_var.set(self.expression)

        elif char == 'EE':
            self.expression += 'E'
            self.display_var.set(self.expression)

        else:
            if self.expression == "0" and char not in ['.', '÷', '×', '-', '+', '%', 'E']:
                self.expression = ""
            self.expression += char
            self.display_var.set(self.expression)

    def _sin(self, x): return math.sin(math.radians(x)) if self.angle_mode == "DEG" else math.sin(x)
    def _cos(self, x): return math.cos(math.radians(x)) if self.angle_mode == "DEG" else math.cos(x)
    def _tan(self, x): return math.tan(math.radians(x)) if self.angle_mode == "DEG" else math.tan(x)
    def _asin(self, x): return math.degrees(math.asin(x)) if self.angle_mode == "DEG" else math.asin(x)
    def _acos(self, x): return math.degrees(math.acos(x)) if self.angle_mode == "DEG" else math.acos(x)
    def _atan(self, x): return math.degrees(math.atan(x)) if self.angle_mode == "DEG" else math.atan(x)
    def _cbrt(self, x): return math.copysign(abs(x) ** (1/3), x)

    def calculate(self):
        try:
            raw_expr = self.expression.strip()
            if not raw_expr:
                self.display_var.set("0")
                return

            eval_expr = raw_expr
            eval_expr = eval_expr.replace('×', '*').replace('÷', '/').replace('^', '**')
            eval_expr = eval_expr.replace('%', '/100')

            replacements = {
                'NA': f"({self.constants['NA']})",
                'R_gas': f"({self.constants['R_gas']})",
                'q_e': f"({self.constants['e_charge']})",
                'kB': f"({self.constants['k_B']})",
                'ANS': f"({self.last_ans})",
                'π': f"({math.pi})",
                'c': f"({self.constants['c_light']})",
                'h': f"({self.constants['h_planck']})",
                'G': f"({self.constants['G_grav']})",
                'g': f"({self.constants['g_acc']})",
                'e': f"({math.e})"
            }
            for k, v in replacements.items():
                eval_expr = eval_expr.replace(k, v)

            def factorial_replacement(match):
                value = match.group(1)
                return f"factorial({value})"

            eval_expr = re.sub(r'([A-Za-z0-9_\)\]]+)\!', factorial_replacement, eval_expr)
            eval_expr = re.sub(r'([0-9]+(?:\.[0-9]+)?)\!', factorial_replacement, eval_expr)

            namespace = {
                '__builtins__': {},
                'sin': self._sin,
                'cos': self._cos,
                'tan': self._tan,
                'asin': self._asin,
                'acos': self._acos,
                'atan': self._atan,
                'log': math.log,
                'log10': math.log10,
                'ln': math.log,
                'sqrt': math.sqrt,
                'cbrt': self._cbrt,
                'abs': abs,
                'factorial': math.factorial,
                'pi': math.pi,
                'e': math.e,
                'math': math
            }

            result = eval(eval_expr, namespace, {})
            if not math.isfinite(result):
                raise ValueError("Result is not finite")

            self.last_ans = float(result)
            result_text = str(int(result)) if float(result).is_integer() else format(result, '.12g')
            self.history_label.config(text=raw_expr)
            self.display_var.set(result_text)
            self.expression = result_text
        except Exception:
            self.history_label.config(text=f"Error: {raw_expr}")
            self.display_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = AcademicScientificCalculator(root)
    root.mainloop()

# Hi my name is Eyad and i love gamedev

# This is a the main code if i destroy the copy code

#def add_numbers(x, y):
  #  """Function to add two numbers"""
   # return x + y

#def subtract_numbers(x, y):
    #"""Function to subtract two numbers"""
#    return x - y

#if __name__ == "__main__":
 #   print("--- Welcome to the Simple Calculator ---")
  #  print("The result of adding 10 + 5 is:", add_numbers(10, 5))
 #   print("The result of subtracting 10 - 5 is:", subtract_numbers(10, 5))

