import pyautogui
import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
import tkinter as tk

# pip freeze > requirements.txt
# print(pyautogui.pixel(1, 1))

class App(TKMT.ThemedTKinterFrame):

    def handleButtonClick(self):
        if self.optionmenuvar.get() == "Verificar posição do mouse":
            pyautogui.displayMousePosition()
        elif self.optionmenuvar.get() == "Verificar pixel do meio":

            largura, altura = pyautogui.size()
            contador = 1

            pixel_central_x = largura // 2
            pixel_central_y = altura // 2
            
            while contador < 6:
                print(f"Pixel central: ({pixel_central_x}, {pixel_central_y})")
                print(pyautogui.pixel(pixel_central_x, pixel_central_y))
                contador += 1
        return

    def __init__(self):
        super().__init__("Funções", "park", "dark")

        self.input_frame = self.addLabelFrame("Menu:", rowspan=1)
        self.input_frame.Button("Confirmar", self.handleButtonClick)
        self.option_menu_list = ["Verificar posição do mouse", "Verificar pixel do meio"]
        self.optionmenuvar = tk.StringVar(value=self.option_menu_list[0])

        self.input_frame.OptionMenu(self.option_menu_list, self.optionmenuvar)

        self.run()

App()



