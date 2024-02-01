from tkinter import Tk, BOTH, Canvas

class Window():
  def __init__(self, width, height):
    self.__root = Tk()
    self.__root.title("My Window")
    self.__canvas = Canvas(self.__root, width=width, height=height)
    self.__canvas.pack(fill=BOTH, expand=True)
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
    self.running = False


  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()

  def wait_for_close(self):
    self.running = True
    if self.running == True:
      self.redraw()

  def close(self):
    self.running = False

def main():
  win = Window(800, 600)
  win.wait_for_close()

main()