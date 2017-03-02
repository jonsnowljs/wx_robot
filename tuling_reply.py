from wxpy import *

robot = Robot()

tuling = Tuling('ced2e43e3aa8471aae2a0dc6f888027d')

my_mp = ensure_one(robot.mps().search('小冰'))


@robot.register(my_mp, TEXT)
def tuling_reply(msg):
    tuling.do_reply(msg)
    print(tuling.do_reply(msg))
    print(msg)


robot.start()