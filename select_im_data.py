import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.image import imread

# Select some pixels from this image
im = imread('FRAME_initial demag_3.4 ps_500 Hz_2_29_AVR.png')

class SelectArea:
    '''
    Select area of image data by dragging mouse to create one or more
    rectangular regions of interest
    '''
    def __init__(self, ax):
        self.ax = ax
        self.rects = []
        self.pixels = [] 
        self.done = False
        self.press = None
        self.title = ax.get_title()
        ax.set_title('Drag to select areas.  Right click when done')
        connect = self.ax.figure.canvas.mpl_connect
        self.cidpress = connect('button_press_event', self.on_press)
        self.cidmotion = connect('motion_notify_event', self.on_motion)
        self.cidrelease = connect('button_release_event', self.on_release)

    def on_press(self, event):
        if event.button == 1:
            # Left click
            self.press = event.xdata, event.ydata
            rect = Rectangle(self.press, 1, 1, alpha=.1, color='blue')
            self.ax.add_patch(rect)
            self.rects.append(rect)
        elif event.button == 3:
            # Right click
            self.disconnect()

    def on_motion(self, event):
        if self.press is None: return
        x0, y0 = self.press
        x1, y1 = event.xdata, event.ydata
        self.rects[-1].set_width(x1 - x0)
        self.rects[-1].set_height(y1 - y0)
        self.ax.figure.canvas.draw()

    def on_release(self, event):
        self.ax.figure.canvas.draw()
        x1, y1 = event.xdata, event.ydata

        self.press = None

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.done = True
        self.ax.set_title(self.title)
        self.ax.figure.canvas.draw()
        self.ax.figure.canvas.mpl_disconnect(self.cidpress)
        self.ax.figure.canvas.mpl_disconnect(self.cidrelease)
        self.ax.figure.canvas.mpl_disconnect(self.cidmotion)

fig, ax = plt.subplots()
ax.imshow(im)
a = SelectArea(ax)
plt.show()
