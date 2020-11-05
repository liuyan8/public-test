"""
create by 2020-10-28    author hf
"""
import pytest
from Class.IdeaDemo.IdeaClass import IdeaClass


class TestDemo:

    def setup(self):
        """首次执行进行实例化"""
        self.idea = IdeaClass(browser='chrome', env="test")

    def teardown(self):
        del self.idea

    def test_login(self):
        """正常登陆用例"""
        assert self.idea.login()

    @pytest.mark.parametrize('user', [2242])
    def test_login_usererr(self, user):
        assert not self.idea.login(user)

    # 登录接口返回token
    @pytest.fixture()
    def test_login_gettoken(self):
        return "token"

    def test_check_order(self, test_login_gettoken):
        token = test_login_gettoken
        assert token == "token"

    @pytest.mark.skipif(True, reason="跳过演示")
    def tset_skip(self):
        pass


if __name__ == "__main__":
    pytest.main(['test_case_demo.py',"--html=../reports/report.html"])
