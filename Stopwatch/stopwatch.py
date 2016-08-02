import Tkinter as tk

#Counting Function
counter = 0
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

mainDisp = tk.Tk()
mainDisp.minsize(width = 400, height = 400)
mainDisp.maxsize(width = 400, height = 400)
mainDisp.title("Stopwatch")

w = tk.Canvas(mainDisp)
w.pack()
w.create_oval(100,50,300,250, width = 4, fill = "black")
w.create_text(200,150,fill="darkgreen",font="Times 20 italic bold",text="Stopwatch")

label = tk.Label(mainDisp, fg="dark green")
label.pack()
counter_label(label)

button = tk.Button(mainDisp, text='Stop', width=200, command=label.destroy)
button.pack()

mainDisp.mainloop()
