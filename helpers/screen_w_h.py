from AppKit import NSScreen

def get_screen_w_h():
    screen_width = NSScreen.mainScreen().frame().size.width
    screen_height = NSScreen.mainScreen().frame().size.height

    return (screen_width, screen_height)

def get_screen_center():
    screen_width, screen_height = get_screen_w_h()
    return (screen_width/2, screen_height/2)