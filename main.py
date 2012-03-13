#
#!/usr/bin/env python
#
#  Jeff Kaplan 3/2012
#

import pyglet


window = pyglet.window.Window()

label = pyglet.text.Label('Hello, Jewel Theif',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
positionLabel = pyglet.text.Label()

@window.event
def on_mouse_motion(x, y, dx, dy):
    window.clear()
    positionLabel = pyglet.text.Label('x = ' + str(x) + '  y = ' + str(y),
                          font_name='Times New Roman',
                          font_size=24,
                          x=window.width//4, y=window.height//4,
                          anchor_x='center', anchor_y='center')
    positionLabel.draw()

@window.event
def on_draw():
    #window.clear()
    #positionLabel.draw()
    #label.draw()
    pass

#Prints to stdout every event that is handled
window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()
