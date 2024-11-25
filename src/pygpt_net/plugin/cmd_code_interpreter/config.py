#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.11.18 19:00:00                  #
# ================================================== #

from pygpt_net.plugin.base.config import BaseConfig, BasePlugin


class Config(BaseConfig):
    def __init__(self, plugin: BasePlugin = None, *args, **kwargs):
        super(Config, self).__init__(plugin)
        self.plugin = plugin

    def from_defaults(self, plugin: BasePlugin = None):
        """
        Set default options for plugin

        :param plugin: plugin instance
        """
        dockerfile = '# Tip: After making changes to this Dockerfile, you must rebuild the image to apply the changes'
        dockerfile += '(Menu -> Tools -> Rebuild IPython Docker Image)'
        dockerfile += '\n\n'
        dockerfile += 'FROM python:3.9'
        dockerfile += '\n\n'
        dockerfile += '# You can customize the packages installed by default here:'
        dockerfile += '\n# ========================================================'
        dockerfile += '\nRUN pip install jupyter ipykernel'
        dockerfile += '\n# ========================================================'
        dockerfile += '\n\n'
        dockerfile += 'RUN mkdir /data'
        dockerfile += '\n\n'
        dockerfile += '# Expose the necessary ports for Jupyter kernel communication'
        dockerfile += '\nEXPOSE 5555 5556 5557 5558 5559'
        dockerfile += '\n\n'
        dockerfile += '# Data directory, bound as a volume to the local \'data/ipython\' directory'
        dockerfile += '\nWORKDIR /data'
        dockerfile += '\n\n'
        dockerfile += '# Start the IPython kernel with specified ports and settings'
        dockerfile += '\nCMD ["ipython", "kernel", \\'
        dockerfile += '\n--ip=0.0.0.0, \\'
        dockerfile += '\n--transport=tcp, \\'
        dockerfile += '\n--shell=5555, \\'
        dockerfile += '\n--iopub=5556, \\'
        dockerfile += '\n--stdin=5557, \\'
        dockerfile += '\n--control=5558, \\'
        dockerfile += '\n--hb=5559, \\'
        dockerfile += '\n--Session.key=19749810-8febfa748186a01da2f7b28c, \\'
        dockerfile += '\n--Session.signature_scheme=hmac-sha256]'

        # cmd enable/disable
        plugin.add_option(
            "ipython_dockerfile",
            type="textarea",
            value=dockerfile,
            label="Dockerfile for IPython kernel",
            description="Dockerfile used to build IPython kernel container image",
            tooltip="Dockerfile",
            tab="ipython",
        )
        plugin.add_option(
            "ipython_image_name",
            type="text",
            value='pygpt_ipython_kernel',
            label="Docker image name",
            tab="ipython",
        )
        plugin.add_option(
            "ipython_container_name",
            type="text",
            value='pygpt_ipython_kernel_container',
            label="Docker container name",
            tab="ipython",
        )
        plugin.add_option(
            "ipython_session_key",
            type="text",
            value='19749810-8febfa748186a01da2f7b28c',
            label="Session Key",
            tab="ipython",
        )
        plugin.add_option(
            "ipython_conn_addr",
            type="text",
            value='127.0.0.1',
            label="Connection Address",
            tab="ipython",
        )
        plugin.add_cmd(
            "ipython_execute",
            instruction="execute Python code in IPython interpreter (in current kernel) and get output.",
            params=[
                {
                    "name": "code",
                    "type": "str",
                    "description": "code to execute in IPython interpreter, usage of !magic commands is allowed",
                    "required": True,
                },
            ],
            enabled=True,
            description="Allows Python code execution in IPython interpreter (in current kernel)",
            tab="ipython",
        )
        plugin.add_cmd(
            "ipython_execute_new",
            instruction="execute Python code in the IPython interpreter in a new kernel and get the output. Use this option only if a kernel restart is required; otherwise, use `ipython_execute` to run the code in the current session",
            params=[
                {
                    "name": "code",
                    "type": "str",
                    "description": "code to execute in IPython interpreter, usage of !magic commands is allowed",
                    "required": True,
                },
            ],
            enabled=True,
            description="Allows Python code execution in IPython interpreter (in new kernel)",
            tab="ipython",
        )
        plugin.add_cmd(
            "ipython_kernel_restart",
            instruction="restart IPython kernel",
            params=[],
            enabled=True,
            description="Allows to restart IPython kernel",
            tab="ipython",
        )
        plugin.add_option(
            "ipython_port_shell",
            type="int",
            value=5555,
            label="Port: shell",
            tab="ipython",
            advanced=True,
        )
        plugin.add_option(
            "ipython_port_iopub",
            type="int",
            value=5556,
            label="Port: iopub",
            tab="ipython",
            advanced=True,
        )
        plugin.add_option(
            "ipython_port_stdin",
            type="int",
            value=5557,
            label="Port: stdin",
            tab="ipython",
            advanced=True,
        )
        plugin.add_option(
            "ipython_port_control",
            type="int",
            value=5558,
            label="Port: control",
            tab="ipython",
            advanced=True,
        )
        plugin.add_option(
            "ipython_port_hb",
            type="int",
            value=5559,
            label="Port: hb",
            tab="ipython",
            advanced=True,
        )

        plugin.add_option(
            "python_cmd_tpl",
            type="text",
            value="python3 {filename}",
            label="Python command template",
            description="Python command template to execute, use {filename} for filename placeholder",
            tab="python_legacy",
        )
        plugin.add_option(
            "sandbox_docker",
            type="bool",
            value=False,
            label="Sandbox (docker container)",
            description="Executes commands in sandbox (docker container). "
                        "Docker must be installed and running.",
            tab="python_legacy",
        )
        plugin.add_option(
            "sandbox_docker_image",
            type="text",
            value='python:3.8-alpine',
            label="Docker image",
            description="Docker image to use for sandbox",
            tab="python_legacy",
        )
        plugin.add_option(
            "auto_cwd",
            type="bool",
            value=True,
            label="Auto-append CWD to sys_exec",
            description="Automatically append current working directory to sys_exec command",
            tab="general",
        )
        plugin.add_option(
            "attach_output",
            type="bool",
            value=True,
            label="Connect to the Python code interpreter window",
            description="Attach code input/output to the Python code interpreter window.",
            tab="general",
        )

        # commands
        plugin.add_cmd(
            "code_execute",
            instruction="save generated Python code and execute it",
            params=[
                {
                    "name": "path",
                    "type": "str",
                    "description": "path to save",
                    "default": ".interpreter.current.py",
                    "required": True,
                },
                {
                    "name": "code",
                    "type": "str",
                    "description": "code",
                    "required": True,
                },
            ],
            enabled=False,
            description="Allows Python code execution (generate and execute from file)",
            tab="python_legacy",
        )
        plugin.add_cmd(
            "code_execute_file",
            instruction="execute Python code from existing file",
            params=[
                {
                    "name": "path",
                    "type": "str",
                    "description": "file path",
                    "required": True,
                },
            ],
            enabled=False,
            description="Allows Python code execution from existing file",
            tab="python_legacy",
        )
        plugin.add_cmd(
            "code_execute_all",
            instruction="run all Python code from my interpreter",
            params=[
                {
                    "name": "code",
                    "type": "str",
                    "description": "code to append and execute",
                    "required": True,
                },
            ],
            enabled=False,
            description="Allows Python code execution (generate and execute from file)",
            tab="python_legacy",
        )
        plugin.add_cmd(
            "sys_exec",
            instruction="execute ANY system command, script or app in user's environment. Do not use this command to install Python libraries, use IPython environment and IPython commands instead.",
            params=[
                {
                    "name": "command",
                    "type": "str",
                    "description": "system command",
                    "required": True,
                },
            ],
            enabled=True,
            description="Allows system commands execution",
            tab="general",
        )
        plugin.add_cmd(
            "get_python_output",
            instruction="get output from my Python interpreter",
            params=[],
            enabled=True,
            description="Allows to get output from last executed code",
            tab="general",
        )
        plugin.add_cmd(
            "get_python_input",
            instruction="get all input code from my Python interpreter",
            params=[],
            enabled=True,
            description="Allows to get input from Python interpreter",
            tab="general",
        )
        plugin.add_cmd(
            "clear_python_output",
            instruction="clear output from my Python interpreter",
            params=[],
            enabled=True,
            description="Allows to clear output from last executed code",
            tab="general",
        )
        plugin.add_cmd(
            "render_html_output",
            instruction="send HTML/JS code to HTML built-in browser (HTML Canvas) and render it",
            params=[
                {
                    "name": "html",
                    "type": "str",
                    "description": "HTML/JS code",
                    "required": True,
                },
            ],
            enabled=True,
            description="Allows to render HTML/JS code in HTML Canvas",
            tab="html_canvas",
        )
        plugin.add_cmd(
            "get_html_output",
            instruction="get current output from HTML Canvas",
            params=[],
            enabled=True,
            description="Allows to get current output from HTML Canvas",
            tab="html_canvas",
        )