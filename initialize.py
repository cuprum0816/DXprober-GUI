"""
Start.py
Last Change 2023/11/09
"""
import os
import tkinter
from sys import exit
from tkinter import messagebox
import main


def install() -> None:
    pass


if os.path.isfile(os.path.join("./config", "user.ini")):
    # noinspection PyArgumentList
    main.Main.user_interface()  # Start main program
else:
    prompt = "看起来您是第一次使用 DXProber GUI\n按确定以开始初始化设置\n按取消以退出程序"
    response = tkinter.messagebox.askokcancel(title="DXProber GUI", message=prompt)
    if response:
        install()
    else:
        exit()
