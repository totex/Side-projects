from pyglet.gl import *


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(800, 600)
        self.set_maximum_size(1280, 900)
        img = pyglet.image.load('res/rect.png')
        self.spr = pyglet.sprite.Sprite(img, 300, 300)

        #            X            Y            X + width                      Y + height
        self.rect = [self.spr.x, self.spr.y, self.spr.x + self.spr.width, self.spr.y + self.spr.height]

        glOrtho(0, 800, 0, 600, -1, 1)

    def on_draw(self):
        self.clear()
        #self.spr1.draw()
        self.spr.draw()

    # TODO after window's resize, the rectangle should be still clickable
    # the new position of the rectangle on x will be at (300/800)*1280, (old pos.x/old window width) * new window width
    # the new position of the rectangle on y will be at (300/600)*900, (old pos.y/old window height) * new window height
    # 300 by 300 is the initial position of the sprite on x and y
    # 800 is the initial width of the window, 600 is the initial height of the window
    # 1280 is the new width of the window, 900 is the new height of the window
    def on_mouse_press(self, x, y, button, modifiers):
        w_width, w_height = self.get_size()
        # bottom left x = (spr.x/old window width) * new window width
        # bottom left y = (spr.y/old window height) * new window height
        self.rect[0] = (self.spr.x / 800) * w_width # bottom left x
        self.rect[1] = (self.spr.y / 600) * w_height # bottom left y
        # upper right x = bottom left x + (new window width/old window width) * sprite.width
        # upper right y = bottom left y + (new window height/old window height) * sprite.height
        self.rect[2] = self.rect[0] + (w_width / 800) * self.spr.width # upper right x
        self.rect[3] = self.rect[1] + (w_height / 600) * self.spr.height # upper right y
        # self.sprite_clicked(x, y, self.spr2)
        self.rect_clicked(x, y, self.rect)

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def update(self, dt):
        pass

    # this works only, when the window is not resized
    def sprite_clicked(self, x, y, sprite):
        if x > sprite.x and x < sprite.x + sprite.width and y > sprite.y and y < sprite.y + sprite.height:
            print('inside')

	# this works always, when the window is resized
    def rect_clicked(self, x, y, rect):
        if x > rect[0] and x < rect[2] and y > rect[1] and y < rect[3]:
            print('inside')


    def on_resize(self, width, height):
        glViewport(0, 0, width, height)

if __name__ == "__main__":
    window = GameWindow(800, 600, "My Window", resizable=True)
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    pyglet.app.run()