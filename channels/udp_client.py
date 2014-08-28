#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
UDP-Client通道类
通过调用管理类对象的process_data函数实现信息的发送。
"""
import logging

from libs.base_channel import BaseChannel


logger = logging.getLogger('yykj_serial')


class UdpClientChannel(BaseChannel):
    def __init__(self, network, channel_name, channel_protocol, channel_params, manager):
        self.status = None
        BaseChannel.__init__(network, channel_name, channel_protocol, channel_params, manager)

    def run(self):
        logger.debug("UdpClientChannel has runned.")
        return

    def isAlive(self):
        return True

    def send_cmd(self, device_info, device_cmd):
        pass