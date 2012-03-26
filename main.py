#
#!/usr/bin/env python
#
#  Jeff Kaplan 3/2012
#

import pyglet

class coords:
    def __init__(self):
        self.x=0
        self.y=0


class mob:
    def __init__(self):
        self.pos=coords()
        self.vel=coords()
        self.vel.x=1
        self.vel.y=1

    def timeStep(self,dt):
        self.pos.x = self.pos.x + self.vel.x*dt
        self.pos.x = self.pos.x + self.vel.x*dt


protagonist = pyglet.image.load('blueflower.png')

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, Jewel Theif',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
positionLabel = pyglet.text.Label()

pos = coords()
cursor = pyglet.window.ImageMouseCursor(protagonist, 1, 1)
window.set_mouse_cursor(cursor)

@window.event
def on_mouse_motion(x, y, dx, dy):
    window.clear()
    #positionLabel = pyglet.text.Label('x = ' + str(x) + '  y = ' + str(y),
    #                      font_name='Times New Roman',
    #                      font_size=24,
    #                      x=window.width//4, y=window.height//4,
    #                      anchor_x='center', anchor_y='center')
    positionLabel.draw()
    pos.x=x
    pos.y=y

@window.event
def on_draw():
    #window.clear()
    #positionLabel.draw()
    #label.draw()
    #pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
    #[0, 1, 2],
    #('v2i', (pos.x, pos.y,
    #         pos.x+50, pos.y,
    #         pos.x+25, pos.y+25))
    #                             )
   
    pass



#Prints to stdout every event that is handled
window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()
