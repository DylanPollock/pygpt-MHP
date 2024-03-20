#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.03.20 06:00:00                  #
# ================================================== #

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QCheckBox, QMenuBar

from pygpt_net.ui.widget.dialog.audio import AudioTranscribeDialog
from pygpt_net.ui.widget.element.labels import HelpLabel
from pygpt_net.ui.widget.textarea.editor import CodeEditor
from pygpt_net.utils import trans


class AudioTranscribe:
    def __init__(self, window=None):
        """
        Audio Transcribe dialog

        :param window: Window instance
        """
        self.window = window

    def setup_menu(self) -> QMenuBar:
        """Setup video dialog menu"""
        self.menu_bar = QMenuBar()
        self.file_menu = self.menu_bar.addMenu(trans("menu.file"))
        self.actions = {}

        # open
        self.actions["open"] = QAction(QIcon(":/icons/folder.svg"), trans("action.open"))
        self.actions["open"].triggered.connect(self.window.tools.transcriber.open_file)

        # save as
        self.actions["save_as"] = QAction(QIcon(":/icons/save.svg"), trans("action.save_as"))
        self.actions["save_as"].triggered.connect(self.window.tools.transcriber.save_as_file)

        # exit
        self.actions["exit"] = QAction(QIcon(":/icons/logout.svg"), trans("menu.file.exit"))
        self.actions["exit"].triggered.connect(self.window.tools.transcriber.close)

        # add actions
        self.file_menu.addAction(self.actions["open"])
        self.file_menu.addAction(self.actions["save_as"])
        self.file_menu.addAction(self.actions["exit"])
        return self.menu_bar

    def setup(self):
        """Setup transcribe dialog"""
        id = 'audio.transcribe'

        self.window.ui.editor[id] = CodeEditor(self.window)
        self.window.ui.editor[id].setReadOnly(False)
        self.window.ui.editor[id].setProperty('class', 'code-editor')

        self.window.ui.nodes['audio.transcribe.convert_video'] = QCheckBox(trans("audio.transcribe.auto_convert"))
        self.window.ui.nodes['audio.transcribe.convert_video'].setChecked(True)
        self.window.ui.nodes['audio.transcribe.convert_video'].clicked.connect(
            lambda: self.window.tools.transcriber.toggle_auto_convert()
        )

        self.window.ui.nodes['audio.transcribe.clear'] = QPushButton(trans("dialog.logger.btn.clear"))
        self.window.ui.nodes['audio.transcribe.clear'].clicked.connect(
            lambda: self.clear()
        )

        self.window.ui.nodes['audio.transcribe.open'] = QPushButton(trans("audio.transcribe.open"))
        self.window.ui.nodes['audio.transcribe.open'].clicked.connect(
            lambda: self.window.tools.transcriber.open_file())

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.window.ui.nodes['audio.transcribe.clear'])
        bottom_layout.addWidget(self.window.ui.nodes['audio.transcribe.open'])

        self.window.ui.nodes['audio.transcribe.title'] = HelpLabel(trans("audio.transcribe.tip"))
        self.window.ui.nodes['audio.transcribe.status'] = QLabel("...")
        self.window.ui.nodes['audio.transcribe.status'].setAlignment(Qt.AlignCenter)
        self.window.ui.nodes['audio.transcribe.status'].setWordWrap(True)

        layout = QVBoxLayout()
        layout.setMenuBar(self.setup_menu())
        layout.addWidget(self.window.ui.editor[id])
        layout.addWidget(self.window.ui.nodes['audio.transcribe.title'])
        layout.addLayout(bottom_layout)
        layout.addWidget(self.window.ui.nodes['audio.transcribe.convert_video'])
        layout.addWidget(self.window.ui.nodes['audio.transcribe.status'])

        self.window.ui.dialog['audio.transcribe'] = AudioTranscribeDialog(self.window)
        self.window.ui.dialog['audio.transcribe'].setLayout(layout)
        self.window.ui.dialog['audio.transcribe'].setWindowTitle(trans("audio.transcribe.title"))


    def clear(self):
        """Clear transcribe dialog"""
        self.window.tools.transcriber.clear()