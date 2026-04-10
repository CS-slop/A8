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

        # Image
        self.image_label = QLabel()
        self.image_label.setPixmap(self.frames[0])
        top_layout.addWidget(self.image_label)

        # Slider
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(30)

        # Tick marks
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(20)

        top_layout.addWidget(self.slider)

        # Spot for text and displaying slider value
        middle_layout = QHBoxLayout()

        self.fps_label = QLabel("Frames per second:")
        self.fps_value = QLabel(str(self.slider.value()))

        middle_layout.addWidget(self.fps_label)
        middle_layout.addWidget(self.fps_value)

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.toggle_animation)

        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        frame.setLayout(layout)

        self.slider.valueChanged.connect(self.update_slider_display)
        layout.addWidget(self.button)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        pause_action = QAction("Pause", self)
        exit_action = QAction("Exit", self)

        file_menu.addAction(pause_action)
        file_menu.addAction(exit_action)

        pause_action.triggered.connect(self.pause_animation)
        exit_action.triggered.connect(self.close)

        self.setCentralWidget(frame)

    def next_frame(self):
        #set frame to next frame - uses modulus for when self.current_frame exceeds salf.num_frames
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image_label.setPixmap(self.frames[self.current_frame])

    def update_slider_display(self):
        self.fps_value.setText(str(self.slider.value()))

    def toggle_animation(self):
        if self.button.text() == "Start":
            fps = self.slider.value()
            interval = int(1000 / fps)

            self.timer.start(interval)
            self.button.setText("Stop")
        else:
            self.timer.stop()
            self.button.setText("Start")

    def pause_animation(self):
        self.timer.stop()
        self.button.setText("Start")

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
