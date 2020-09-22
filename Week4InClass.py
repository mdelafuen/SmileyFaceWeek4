import arcade

def main():
    arcade.open_window(700, 700, "Smile Demo")
    arcade.set_background_color(arcade.color.PIGGY_PINK)
    # create objects here
    face = arcade.create_ellipse_outline(350, 350, 200, 200, arcade.color.BLACK)
    eye1 = arcade.create_ellipse(270, 400, 30, 30, arcade.color.BLACK)
    eye2 = arcade.create_ellipse(420, 400, 30, 30, arcade.color.BLACK)
    nose_points = [(320,350), (370, 350), (345, 370)]
    nose = arcade.create_polygon(nose_points, arcade.color.DARK_PINK)



    arcade.start_render()
    # draw stuff here
    face.draw()
    eye1.draw()
    eye2.draw()
    nose.draw()
    arcade.draw_arc_outline(350, 350, 200, 125,
                            arcade.color.RADICAL_RED, 180, 360, 3)


    arcade.finish_render()



    arcade.run()




main()