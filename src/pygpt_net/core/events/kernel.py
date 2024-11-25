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

from .base import BaseEvent


class KernelEvent(BaseEvent):
    """Events for controlling core flow"""
    # input
    INPUT_SYSTEM = "kernel.input.system"
    INPUT_USER = "kernel.input.user"

    # queue
    AGENT_CALL = "kernel.agent.call"
    AGENT_CONTINUE = "kernel.agent.continue"
    APPEND_BEGIN = "kernel.append.begin"
    APPEND_DATA = "kernel.append.data"
    APPEND_END = "kernel.append.end"
    CALL = "kernel.call"
    REQUEST = "kernel.request"
    REQUEST_NEXT = "kernel.request.next"
    RESPONSE_ERROR = "kernel.response.error"
    RESPONSE_FAILED = "kernel.response.failed"
    RESPONSE_OK = "kernel.response.OK"
    SET_STATUS = "kernel.status"
    TOOL_CALL = "kernel.tool.call"

    # reply
    REPLY_ADD = "kernel.reply.add"
    REPLY_RETURN = "kernel.reply.return"


    def __init__(
            self,
            name: str = None,
            data: dict = None,
    ):
        """
        Event object class

        :param name: event name
        :param data: event data
        """
        super(KernelEvent, self).__init__(name, data)
        self.id = "KernelEvent"
