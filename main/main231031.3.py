#version = 0.1.3

from easygui import buttonbox
from os import system

#土木工程制图（第四版） 多媒体辅助教学系统
mainChoice =buttonbox("欢迎使用土木工程制图（第四版） 多媒体辅助教学系统 精简启动器。\n请选择接下来的操作：",
                              title="土木工程制图（第四版） 多媒体辅助教学系统 精简启动器 v0.1.3",choices=["讲课和复习铺助系统","解题指导辅助系统","退出"])

if mainChoice == "讲课和复习铺助系统":
    system("start \"\" \"cai\\bb1.swf\" \"flashplayer_sa.exe\"")
elif mainChoice == "解题指导辅助系统":
    system("start \"\" \"cai\\BB2.swf\" \"flashplayer_sa.exe\"")
