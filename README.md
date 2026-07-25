# 🎯 PixelCatcher

**PixelCatcher** és un selector de color ràpid, lleuger i portable per a Windows 11. Inspirat en el clàssic *ColorPix*, aquesta eina està dissenyada per a desenvolupadors, dissenyadors gràfics i artistes digitals que necessiten capturar colors de la pantalla de manera instantània.

A diferència d'altres eines complexes, PixelCatcher va directe al gra: obre'l, apunta amb el ratolí i captura el color.

## ✨ Característiques Principals

- 🔍 **Lupa de Píxels Integrada:** Visualitza el teu cursor amb un zoom d'11x11 píxels en temps real per aconseguir una precisió mil·limètrica.

- 📌 **Sempre Visible (Always on Top):** La finestra es manté per sobre de les teves aplicacions de disseny perquè no la perdis mai de vista.

- ❄️ **Congelació de Color:** Prem la tecla `ESPAI` per bloquejar el mostreig i mantenir el color a la pantalla.

- 📋 **Còpia Ràpida al Portapapers:** Prem la tecla `C` per copiar automàticament el codi HEX i utilitzar-lo als teus projectes.

- 🌙 **Interfície Moderna:** Disseny net en mode fosc (Dark Mode) que encaixa perfectament amb l'estètica de Windows 11.

- 🚀 **100% Portable:** Sense instal·lacions complicades. Un sol fitxer `.exe` llest per funcionar.

## 🚀 Com utilitzar-ho (Usuaris)

1. Ves a la pestanya de Releases i descarrega l'última versió de PixelCatcher.exe.

2. Executa el programa (no requereix instal·lació).

3. Mou el ratolí per la pantalla. Veuràs com el color i els valors HEX/RGB s'actualitzen en temps real.

4. Prem **`ESPAI`** per fixar un color que t'agradi.

5. Prem **`C`** per copiar el valor HEX al teu portapapers.

## 💻 Compilació des del codi font (Desenvolupadors)

Si vols modificar el codi o compilar el teu propi executable, PixelCatcher està construït amb **Python** (Tkinter, Pillow, PyAutoGUI).

**Requisits previs:** Assegura't de tenir Python instal·lat i afegit al teu `PATH`.

**1. Clonar el repositori i preparar l'entorn:** 

git clone https://github.com/anpopofir/PixelCatcher.git 

cd PixelCatcher python -m pip 

install pillow pyautogui pyinstaller

**2. Generar l'executable per a Windows (.exe):** 
Per compilar el programa en un sol fitxer portable i sense la finestra de la consola, executa: 

python -m PyInstaller --noconsole --onefile --clean --icon=icona.ico pixelcatcher.py

## 🤝 Contribucions

Les contribucions són molt benvingudes! Si tens alguna idea per millorar l'eina, obre una Issue o envia un Pull Request.

## 📄 Llicència

Aquest projecte està sota la llicència MIT - mira el fitxer LICENSE per a més detalls.

