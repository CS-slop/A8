# GitHub Repo name: A8
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        self.current_frame = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        layout = QHBoxLayout()

        top_layout = QHBoxLayout()

        self.image_label = QLabel()
        self.image_label.setPixmap(self.frames[0])

        top_layout.addWidget(self.image_label)

        layout.addLayout(top_layout)

        frame.setLayout(layout)

        self.setCentralWidget(frame)

    def next_frame(self):
        #set frame to next frame - uses modulus for when self.current_frame exceeds salf.num_frames
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image_label.setPixmap(self.frames[self.current_frame])


    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
