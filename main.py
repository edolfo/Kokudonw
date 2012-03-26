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
        self.pos.x = 100  #starting position
        self.vel=coords()
        self.vel.x=200
        self.vel.y=200
        self.sprite=pyglet.image.load('blueflower.png')

    def timeStep(self,dt):
        self.pos.x = self.pos.x + self.vel.x*dt
        self.pos.y = self.pos.y + self.vel.y*dt

        # check bounds
        bounds = coords()
        bounds.x, bounds.y = window.get_size()
        if bounds.x < self.pos.x or self.pos.x < 0:
            self.vel.x = self.vel.x * -1
        if bounds.y < self.pos.y or self.pos.y < 0:
            self.vel.y = self.vel.y * -1

        baddie.sprite.blit(baddie.pos.x,baddie.pos.y)


baddie= mob()
deltaT = 1./60.
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
    window.clear()
    #positionLabel.draw()
    #label.draw()
    #pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
    #[0, 1, 2],
    #('v2i', (pos.x, pos.y,
    #         pos.x+50, pos.y,
    #         pos.x+25, pos.y+25))
    #                             )
    #protagonist.blit(pos.x,pos.y)
    baddie.sprite.blit(baddie.pos.x,baddie.pos.y)
    pass



#Prints to stdout every event that is handled
window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.clock.schedule_interval(baddie.timeStep, deltaT)
pyglet.app.run()
