from wxpy import *


# 搜索公众号
def searchinmps(name):
    return robot.mps().search(name)[0]


# 搜索朋友
def searchinfriend(name):
    return robot.friends().search(name)[0]


# 搜索讨论组
def searchingroup(name):
    return robot.groups().search(name)[0]


robot = Robot()
my_friend = searchinfriend('Dave')
print(my_friend)
boring_group = robot.groups().search('')


@robot.register()
def just_print(msg):
    print(msg)

@robot.register([my_friend,Group], TEXT)
def auto_reply(msg):
    if not (isinstance(msg.chat, Group) and not msg.is_at):
        return '收到消息:{} {}'.format(msg.text, msg.type)

robot.start()
