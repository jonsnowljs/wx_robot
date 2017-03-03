from wxpy import *

robot = Robot(save_path='./test.pkl')

tuling = Tuling('ced2e43e3aa8471aae2a0dc6f888027d')

#全部好友机器人回复
my_frs = robot.friends()


@robot.register(my_frs, TEXT)
def tuling_reply(msg):
    tuling.do_reply(msg)
    print(tuling.do_reply(msg))
    print(msg)


robot.start()