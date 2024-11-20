#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.11.20 03:00:00                  #
# ================================================== #
import json

from pygpt_net.item.ctx import CtxItem

class BaseEvent:
    def __init__(
            self,
            name: str = None,
            data: dict = None,
            ctx: CtxItem = None
    ):
        """
        Base Event object class

        :param name: event name
        :param data: event data
        :param ctx: context instance
        """
        self.id = None
        self.name = name
        self.data = data
        self.ctx = ctx  # CtxItem
        self.stop = False  # True to stop propagation
        self.internal = False
        self.call_id = 0


    @property
    def full_name(self) -> str:
        """Get full event name"""
        return self.id + ": " + self.name

    def to_dict(self) -> dict:
        """Dump event to dict"""
        return {
            'name': self.name,
            'data': self.data,
            'stop': self.stop,
            'internal': self.internal,
        }

    def dump(self) -> str:
        """
        Dump event to json string

        :return: JSON string
        """
        try:
            return json.dumps(self.to_dict())
        except Exception as e:
            pass
        return ""

    def __str__(self):
        return self.dump()