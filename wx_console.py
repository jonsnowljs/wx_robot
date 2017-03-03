from wxpy import *

robot = Robot(save_path='./test.pkl')
tuling = Tuling('ced2e43e3aa8471aae2a0dc6f888027d')


@robot.register()
def print_other(msg):
    pp(dict((k, getattr(msg, k)) for k in dir(msg)))


robot.start(block = False)

from IPython import embed
embed(header="console")
robot.logout
robot.start(block = False)
