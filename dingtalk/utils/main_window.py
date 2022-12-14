# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import win32gui

from dingtalk.utils.window import hwnd_title, get_all_hwnd


# 获取钉钉主窗口句柄
def get_handle():
    # 查找所有窗口标题和句柄 StandardFrame_DingTalk
    win32gui.EnumWindows(get_all_hwnd, 0)
    for handle, title in hwnd_title.items():
        if title != "钉钉":
            continue
        if win32gui.GetClassName(handle) != "StandardFrame_DingTalk":  # 跳过其他窗口捕获主窗口
            continue
        print("获取到钉钉窗口句柄：" + str(handle))
        return handle
    try:
        if handle is None:
            exit(0)
    except:
        print("请先打开钉钉窗口")
        exit(0)
