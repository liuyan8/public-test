"""
create by 2020-10-28    author hf     learn from 虫师
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time, os
from os import path


class CommonBehavior(object):
    '''
     封装公共参数
    '''

    def __init__(self, browser='chrome'):
        '''
        封装启动方法
        '''
        if browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":  # 没有界面浏览器，后台运行
            driver = webdriver.PhantomJS()
        elif browser == 'edge':  # win10浏览器
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError("请传入指定浏览器(chrome/firefox/opera/....)，传入值不符合可操作的浏览器：" % browser)

    def wait_getelement(self, key, value, show=True, secs=5):
        '''
        使用显示等待进行，查询元素
        EC.presence_of_element_located 判断某个元素是否被加到了dom树里，并不代表该元素一定可见，
        EC.visibility_of_element_located 判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0
        具体可参考https://blog.csdn.net/niedongri/article/details/79384586
        '''
        if key == "id":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.ID, value)) if show == False else EC.visibility_of_element_located(
                    (By.ID, value)))
        elif key == "name":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.NAME, value)) if show == False else EC.visibility_of_element_located(
                    (By.NAME, value)))
        elif key == "class_name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located(
                (By.CLASS_NAME, value)) if show == False else EC.visibility_of_element_located(
                (By.CLASS_NAME, value)))
        elif key == "text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located(
                (By.LINK_TEXT, value)) if show == False else EC.visibility_of_element_located(
                (By.LINK_TEXT, value)))
        elif key == "xpath":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located(
                    (By.XPATH, value)) if show == False else EC.visibility_of_element_located(
                    (By.XPATH, value)))
        elif key == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, value)) if show == False else EC.visibility_of_element_located(
                (By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "请输入需要查找的元素类型,'id','name','class','link_text','xpath','key,value'.")

    def get_element(self, key, value):
        '''
         不使用等待，查询元素
        '''

        if key == "id":
            element = self.driver.find_element_by_id(value)
        elif key == "name":
            element = self.driver.find_element_by_name(value)
        elif key == "class":
            element = self.driver.find_element_by_class_name(value)
        elif key == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif key == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif key == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "请输入需要查找的元素类型,'id','name','class','link_text','xpath','key,value'.")
        return element

    def open(self, url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def set_window(self, wide, high):
        self.driver.set_window_size(wide, high)

    def input_text(self, key, value, text):
        self.wait_getelement(key, value)  # 智能等待
        el = self.get_element(key, value)  # 按照指定的去匹配用什么方式去查找元素
        el.send_keys(text)

    def input_clear(self, key, value):
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        el.clear()

    def click(self, key, value):
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        el.click()

    def right_click(self, key, value):
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, key, value):
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, key, value):
        """
        双击
        """
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, key, value, t_key, t_value):
        """
        拖拽功能，将某元素拖拽到指定元素位置
        """
        self.wait_getelement(key, value)
        element = self.get_element(key, value)
        self.wait_getelement(t_key, t_value)
        target = self.get_element(t_key, t_value)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        文字点击功能
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()

    def submit(self, key, value):
        '''
        表单提交
        '''
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        el.submit()

    def F5(self):
        self.driver.refresh()

    def js(self, script):
        '''
        执行js操作
        driver.js("window.scrollTo(200,1000);") 滚动到指定位置
        '''
        self.driver.execute_script(script)

    def get_attribute(self, key, value, attribute):
        '''
        获取元素的属性的值
        '''
        el = self.get_element(key, value)
        return el.get_attribute(attribute)

    def get_text(self, key, value):
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        return el.text

    def get_display(self, key, value):
        '''
        确定元素是否显示
        '''
        self.wait_getelement(key, value)
        el = self.get_element(key, value)
        return el.is_displayed()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def save_windows_img(self, file_path):
        '''
        截图功能
        '''
        self.driver.get_screenshot_as_file(file_path)

    def get_image_path(self):
        image_path = os.path.dirname(path.dirname(__file__)) + '\\Report\\image\\'
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        image = image_path + "_" + now + ".png"
        time.sleep(1)
        print(image)  # 必须先打印，不然无法返回image
        return image

    def wait(self, secs):
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        确定确认框
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        关闭确认框
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, key, value):
        '''
        切换句柄
        '''
        self.wait_getelement(key, value)
        iframe_el = self.get_element(key, value)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        切回默认句柄
        '''
        self.driver.switch_to.default_content()

    def open_new_window(self, key, value):
        original_windows = self.driver.current_window_handle
        el = self.get_element(key, value)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)
