class Window:
    __height = 50 #(altura)
    __width = 50 #(ancho)
    __title = "test"
    __resize = False

   #setters
    def setdimensions (self,height,width):
        self.__height = height
        self.__width = width

        # Establecer el tamaño de la ventana (n x m píxeles)
        #ventana.geometry(f"{height}x{width}")

    def setresize(self,resize):
        self.__resize = resize

    def settitle(self,titulo):
        self.__title = titulo

   #getters

    def gettitle(self):
        return self.__title

    def getdimensions(self):
        return [self.__height,self.__width]

    def getresize(self):
        return self.__resize

    def createwindow(self):
        import tkinter as tk
        ventana = tk.Tk()
        ventana.title(self.__title)
        ventana.geometry(f"{self.__width}x{self.__height}")
        ventana.resizable(self.__resize,self.__resize)
        ventana.mainloop()




