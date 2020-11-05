"""
create by 2020-10-28    author hf
这里为什么数据不用yaml呢？因为Yaml具有一些特性和元素定位冲突比较多不方便保存，因此用代码保存比较好，也可以使用其他文件来保存
"""


class IdeaElement:
    Login = dict(
        loginswitch='rc-tabs-0-tab-login',  # 登录切换按钮元素
        username='account',  # 登录账号元素
        password='password',  # 登录密码元素
        loginbt='.ant-btn',  # 登录按钮元素
        check='.userInfo___3hw0_'
    )
