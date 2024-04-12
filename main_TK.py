import tkinter


"""
вопрос: Label
ответы: Button
Счет: кол-во правильных ответов
"""


class App:
    """приложение"""
    def __init__(self, width: int, height: int) -> None:
        self.window = tkinter.Tk()
        self.width = width
        self.height = height
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.mainloop()


App(1024, 1600)
