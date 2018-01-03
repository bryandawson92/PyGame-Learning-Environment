from .pygamewrapper import PyGameWrapper
try:
    from .doomwrapper import DoomWrapper
except:
    pass
    #print("couldn't import doomish")
