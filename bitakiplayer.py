# Αρχικά καλούμε τις βιβλιοθήκες που θα χρησιμοποιήσουμε
# Οπως βιβλιοθήκες για το παράθυρο
import time
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk
from pygame import mixer


# Σε αυτό το σημείο θα δημιουργήσουμε αρχίκα το παράθυρο της εφαρμογής μας
class MusicPlayer:

    def __init__(self, window, master=None):
        window.geometry('1920x1080')
        window.title('Bitaki Player')
        window.resizable(0, 0)


        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            my_label.config(text=hour + ":" + minute + ":" + second)
            my_label.after(1000, clock)

        def update():
            my_label.config(text="New Text")


        my_label = Label(root, text="", font=("Helvetica", 50), fg="grey",)
        my_label.pack(pady=10)
        clock()

        # Στο σημείο αυτό εισάγουμε τα κουμπιά ονομάζοντας το καθένα , δινοντάς του το σωστό μεγεθός και την
        # κατάλληλη λειτοργία
        Load = Button(window, text='Load', width=10, font=('Times', 20), bg='#FF3333' , command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 20), bg='#FF3333' , command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 20), bg='#FF3333' , command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 20), bg='#FF3333' , command=self.stop)

        # Στο σημείο αυτο θα δώσουμε θέση στα κουμπιά μέσα στο παράθυρο
        Load.place(x=300, y=30)
        Play.place(x=1120, y=30)
        Pause.place(x=1420, y=30)
        Stop.place(x=1720, y=30)
        self.music_file = False
        self.playing_state = False



    # Εδώ θα δίνεται στο χρήστη η δυνατότητα να φορτώσει τα δικά του αρχεία μουσικής
    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        # Η if θα διαβάζει τα αρχεία και θα ξεκινάει την αναπαραγωγή
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        # Η if αυτή θα έχει την ευθήνη για το να κάνει παύση(pause) η αναπαραγωγή
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            # Και εδώ θα γίνεται το unpause
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        # Τέλος προσθέτουμε την δυνατότητα διακοπής της αναπαραγωγής
        mixer.music.stop()


root = Tk()
app = MusicPlayer(root)
root.title("Bitaki Player")
# Εδώ προσθέτουμε ένα backround
image = Image.open("01.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack()
# Εδω προσθέτουμε το icon του παραθύρου
root.iconbitmap('C:\\Users\\User\\PycharmProjects\\Bitaki Player\\eye.ico')
root.mainloop()