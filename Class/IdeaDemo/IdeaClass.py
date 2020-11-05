"""
create by 2020-10-28    author hf
"""
from common.common import CommonBehavior
from config.env_config import GetConfig
from data.idea.element import IdeaElement
from common.log import Logger

logger = Logger("ideaclass")


class IdeaClass:
    def __init__(self, browser='chrome', env="test"):
        self.behvior = CommonBehavior(browser)
        self.loginurl = GetConfig.get_project_config(env=env, project="idea", data="idea").get("loginurl")
        self.data = GetConfig.get_project_config(env=env, project="idea", data="data")
        logger.debug(self.data)

    def login(self, user=None, pwd=None):
        """打开登录页面，填写账号密码，最后进行登录,正常登陆逻辑"""
        loginswitch = 'loginswitch'
        username = 'username'
        password = 'password'
        loginbt = 'loginbt'
        check = "check"
        result = True
        try:
            self.behvior.open(self.loginurl)
            self.behvior.max_window()
            self.behvior.wait_getelement("id", IdeaElement.Login.get(loginswitch))  # 智能等待 切换按钮出现
            self.behvior.click("id", IdeaElement.Login.get(loginswitch))
            self.behvior.input_text("id", IdeaElement.Login.get(username),
                                    self.data.get("Login").get("username") if user == None else user)
            self.behvior.input_text("id", IdeaElement.Login.get(password),
                                    self.data.get("Login").get("password") if pwd == None else pwd)
            self.behvior.click("css", IdeaElement.Login.get(loginbt))
            self.behvior.wait_getelement("css", IdeaElement.Login.get(check))  # 智能等待 切换按钮出现
        except Exception as e:
            logger.error(e)
            result = False
        return result

    def __del__(self):
        self.behvior.close()


if __name__ == '__main__':
    i = IdeaClass()
    i.login()
