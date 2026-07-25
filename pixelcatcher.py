import tkinter as tk
from PIL import ImageGrab, Image, ImageTk
import pyautogui
import sys
import os

# Evitar errors de PyInstaller en mode noconsole
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

class ColorPixWin11:
    def __init__(self, root):
        self.root = root
        self.root.title("ColorPix Lupa")
        self.root.geometry("280x350")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.configure(bg="#1e1e2e")
        
        self.frozen = False
        self.current_hex = "#FFFFFF"
        self.photo_img = None # Referència per evitar que l'escombraria de memòria esborri la imatge
        
        # --- INTERFÍCIE ---
        tk.Label(root, text="COLORPIX AMB LUPA", font=("Segoe UI", 11, "bold"), fg="#cdd6f4", bg="#1e1e2e").pack(pady=(10, 5))
        
        # Contenidor superior (Lupa + Color sòlid)
        top_frame = tk.Frame(root, bg="#1e1e2e")
        top_frame.pack(pady=5)
        
        # 1. Lupa (Canvas on dibuixarem la imatge ampliada)
        self.zoom_size = 99 # 11 píxels x 9 d'escala
        self.canvas_lupa = tk.Canvas(top_frame, width=self.zoom_size, height=self.zoom_size, bg="black", highlightthickness=1, highlightbackground="#89b4fa")
        self.canvas_lupa.grid(row=0, column=0, padx=10)
        
        # 2. Color Sòlid
        self.color_box = tk.Frame(top_frame, width=70, height=self.zoom_size, bg="#ffffff", highlightthickness=1, highlightbackground="#89b4fa")
        self.color_box.grid(row=0, column=1, padx=10)
        
        # Estat
        self.status_label = tk.Label(root, text="MOVENT (Espai: Congelar)", font=("Segoe UI", 8, "bold"), fg="#a6e3a1", bg="#1e1e2e")
        self.status_label.pack(pady=2)

        # Valors
        vals_frame = tk.Frame(root, bg="#1e1e2e")
        vals_frame.pack(pady=5, fill="x", padx=20)
        self.hex_label = tk.Label(vals_frame, text="HEX: #FFFFFF", font=("Consolas", 14, "bold"), fg="#f9e2af", bg="#1e1e2e")
        self.hex_label.pack(anchor="center", pady=2)
        self.rgb_label = tk.Label(vals_frame, text="RGB: (255, 255, 255)", font=("Consolas", 11), fg="#89dceb", bg="#1e1e2e")
        self.rgb_label.pack(anchor="center", pady=2)
        
        # Botons
        self.copy_btn = tk.Button(root, text="Copiar HEX (C)", command=self.copy_to_clipboard, font=("Segoe UI", 9, "bold"), bg="#89b4fa", fg="#11111b", relief="flat", cursor="hand2")
        self.copy_btn.pack(fill="x", padx=40, ipady=3, pady=(5,0))

        # Controls de teclat
        self.root.bind("<space>", self.toggle_freeze)
        self.root.bind("c", lambda e: self.copy_to_clipboard())
        self.root.bind("C", lambda e: self.copy_to_clipboard())
        
        self.update_color()

    def toggle_freeze(self, event=None):
        self.frozen = not self.frozen
        if self.frozen:
            self.status_label.config(text="CONGELAT (Espai: Desbloquejar)", fg="#f38ba8")
        else:
            self.status_label.config(text="MOVENT (Espai: Congelar)", fg="#a6e3a1")

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.current_hex)
        self.copy_btn.config(text="✓ Copiat!")
        self.root.after(1000, lambda: self.copy_btn.config(text="Copiar HEX (C)"))

    def update_color(self):
        if not self.frozen:
            try:
                x, y = pyautogui.position()
                
                # --- NOU: Capturar 11x11 píxels al voltant del ratolí ---
                radi = 5 # 5 a l'esquerra, 5 a la dreta + 1 centre = 11 píxels
                caixa = (x - radi, y - radi, x + radi + 1, y + radi + 1)
                img = ImageGrab.grab(bbox=caixa, all_screens=True)
                
                # Ampliar la imatge a 99x99 mantenint els píxels durs (NEAREST)
                img_zoom = img.resize((self.zoom_size, self.zoom_size), Image.NEAREST)
                self.photo_img = ImageTk.PhotoImage(img_zoom)
                
                # Actualitzar el Canvas de la lupa
                self.canvas_lupa.delete("all")
                self.canvas_lupa.create_image(0, 0, anchor="nw", image=self.photo_img)
                
                # Dibuixar una creu vermella al centre per indicar el píxel exacte
                centre = self.zoom_size // 2
                self.canvas_lupa.create_rectangle(centre - 4, centre - 4, centre + 5, centre + 5, outline="red", width=1)
                
                # Obtenir el color exacte del píxel central (el píxel 5,5 de la imatge original d'11x11)
                r, g, b = img.getpixel((radi, radi))[:3]
                color_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()
                
                # Actualitzar els textos i el color sòlid
                self.current_hex = color_hex
                self.color_box.config(bg=color_hex)
                self.hex_label.config(text=f"HEX: {color_hex}")
                self.rgb_label.config(text=f"RGB: ({r}, {g}, {b})")
            except Exception:
                pass
                
        self.root.after(50, self.update_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPixWin11(root)
    root.mainloop()
