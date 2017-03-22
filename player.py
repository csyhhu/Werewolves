# -*- coding: utf-8 -*-
# filename: player.py

import global_parameter

class Player(object):

    def __init__(self, openID):
        # Assign a number to this current player
        self.number = global_parameter.g_curr_number
        # When a new player is added, this global parameter will add one
        global_parameter.g_curr_number += 1
        # OpenID
        self.openID = openID
        # The character of this player
        self.character = -1

    def PrintInfo(self):
        print self.openID