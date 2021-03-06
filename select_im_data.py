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
            self.ax.figure.canvas.draw()
            plt.pause(.1)
        elif event.button == 3:
            # Right click
            self.disconnect()

    def on_motion(self, event):
        if self.press is None: return
        x0, y0 = self.press
        x1, y1 = event.xdata, event.ydata
        if not any([p is None for p in (x0, x1, y0, y1)]):
            self.rects[-1].set_width(x1 - x0)
            self.rects[-1].set_height(y1 - y0)
        self.ax.figure.canvas.draw()
        plt.pause(.1)

    def on_release(self, event):
        self.ax.figure.canvas.draw()
        x0, y0 = self.press
        x1, y1 = event.xdata, event.ydata
        xl, xr = int(min(x0, x1)), int(max(x0, x1))
        yt, yb = int(min(y0, y1)), int(max(y0, y1))
        # Add the new pixels to self.pixels
        # Switching definition of x and y because indexing is stupid
        rect_pixels = [(y, x) for x in range(xl, xr + 1) for y in range(yt, yb + 1)]
        self.pixels.extend([p for p in rect_pixels if p not in self.pixels])
        self.press = None
        plt.pause(.1)

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
