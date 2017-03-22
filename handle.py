# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import player

PHASE = 0

class Handle(object):

    def __init__(self):
        # Record all the players
        self.player_dict = {}

    def GET(self):
        return "success"

    def POST(self):
        try:
            # Read in the input data
            webData = web.data()
            print "Handle Post webdata is ", webData  # 后台打日志
            recMsg = receive.parse_xml(webData)
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = recMsg.Content

            if (content == "帮助"):
                # Set help instruction
                replyCotent = ""
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()

            elif (content == "开始"):
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()

            elif (content == "注册"):
                # Record the openID and check whether it exist
                # If the player has added
                if self.player_dict.has_key(fromUser):
                    reply_content = "你已经注册，你的身份牌是" + self.player_dict[fromUser].number
                # Otherwise, add the player into the list
                else :
                    new_player = player.Player(toUser)
                    self.player_dict[fromUser] = new_player
                    reply_content = "你成功注册，你的身份牌是" + self.player_dict[fromUser].number

            elif (content == "显示所有玩家"):
                for (openid, player) in self.player_dict.items():


            # Phase for register and configuration
            if PHASE == 0:
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "请设置游戏人数以及游戏板，默认是12人局"

                if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content = recMsg.Content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    print "暂且不处理"
                    return "success"
        except Exception, Argment:
            return Argment