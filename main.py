import easygui
import os
os.system("chcp 65001")
path = os.getcwd()
#土木工程制图（第四版） 多媒体辅助教学系统
MainWindow =easygui.buttonbox("欢迎使用土木工程制图（第四版） 多媒体辅助教学系统 精简启动器。\n请选择接下来的操作：",
                              title="土木工程制图（第四版） 多媒体辅助教学系统 精简启动器",choices=["讲课和复习铺助系统","解题指导辅助系统","退出"])
print(MainWindow)
if MainWindow == "讲课和复习铺助系统":
    os.system("cd "+os.getcwd())
    print("cd"+path)
    os.system("start \"\" \"cai\\bb1.swf\" \"flashplayer_sa.exe\"")
elif MainWindow == "解题指导辅助系统":
    os.system("cd " + os.getcwd())
    print("cd" + path)
    os.system("start \"\" \"cai\\BB2.swf\" \"flashplayer_sa.exe\"")
