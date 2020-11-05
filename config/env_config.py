"""
create by 2020-10-28    author hf
"""
import yaml, os
from common.log import Logger

logger = Logger(name="envconfig")


class GetConfig:

    @classmethod
    def get_project_config(cls, project="idea", data="idea", env="test"):
        """根据请求的参环境返回不同环境数据"""
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\data\\{}\\{}.yaml".format(
            project, data)
        logger.debug(path)
        result = yaml.safe_load(open(path, encoding='utf-8'))
        logger.debug(result)
        return result.get("test") if env == "test" else result.get("env") if env == "env" else result.get("prodect")


if __name__ == '__main__':
    GetConfig.get_project_config(env="test", project="idea", data="data")
