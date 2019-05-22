import os
import unittest

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as CH_Options
from function import Excel

url = 'https://www.baidu.com/'

mobileEmulation = {'deviceName': 'iPhone X'}
options = CH_Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920x1080")
options.add_argument('--no-sandbox')# 在Ubuntu上执行要加上这句
options.add_experimental_option('mobileEmulation', mobileEmulation)
chrome_driver_path = os.path.split(os.path.realpath(__file__))[0] + '/chromedriver'
search_key = ['英荔', '英荔教育', '英荔商学院']
search_ele = [r'#results > div:nth-child(1) > div.c-result-content > article > header > div > a > h3 > span',
              r'#results > div:nth-child(2) > div.c-result-content > article > header > div > a > h3 > span',
              r'#results > div:nth-child(3) > div > article > header > div > a > h3 > span',
              r'#results > div:nth-child(5) > div.c-result-content > article > header > div > a > h3 > span',
              r'#results > div:nth-child(6) > div > article > header > div > a > h3 > span',]
search_eles = [r'#results > div:nth-child(1) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(2) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(3) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(4) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(6) > div.c-result-content > article > header > div > a > h3 > span',]
search_eless = [r'#results > div:nth-child(1) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(2) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(3) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(4) > div.c-result-content > article > header > div > a > h3 > span',
               r'#results > div:nth-child(5) > div.c-result-content > article > header > div > a > h3 > span',]
class baiDuMoblie(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_driver_path, options=options)
        self.driver.get(url)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

    """获取EXCEL表数据"""

    def get_excel_data(self, dataname, row=2):
        data = Excel(dataname)
        return data.read_excel(row)

    """给EXCEL表插入数据"""

    def set_excel_data(self, dataname,col, row, datas):
        excel_data = Excel(dataname)
        excel_data.write_excel_rol(col, row, datas)
    def test_search_baidu_moblie(self):
        n = 0
        search_input = self.driver.find_element_by_id('index-kw')
        search_input.clear()
        search_input.send_keys(search_key[0])
        sleep(2)
        search_input.send_keys(Keys.ENTER)
        sleep(2)
        for i in range(0, len(search_key)):
            search_input = self.driver.find_element_by_id('kw')
            search_input.clear()
            search_input.send_keys(search_key[i])
            sleep(2)
            search_input.send_keys(Keys.ENTER)
            sleep(2)
            if i == 0:
                for c in range(0, len(search_eles)):
                    try:
                        btn_c = self.driver.find_element_by_css_selector(search_eles[c])
                        self.driver.execute_script("arguments[0].scrollIntoView();", btn_c)
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+38, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        title = self.driver.title
                        self.driver.back()
                        self.set_excel_data('search_result', c+38, n+1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c+38, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c+38, n + 2, '否')
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c+38, n, '没有定位到元素')
                        self.set_excel_data('search_result', c+38, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c+38, n + 2, '没有结果')




            if i==1:
                for c in range(0, len(search_ele)):
                    try:
                        n = 4
                        btn_c = self.driver.find_element_by_css_selector(search_ele[c])
                        self.driver.execute_script("arguments[0].scrollIntoView();", btn_c)
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+38, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        title = self.driver.title
                        self.driver.back()
                        self.set_excel_data('search_result', c+38, n + 1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c+38, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c+38, n + 2, '否')
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c+38, n, '没有定位到元素')
                        self.set_excel_data('search_result', c+38, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c+38, n + 2, '没有结果')

                n += 4
            if i == 2:
                for c in range(0, len(search_eless)):
                    try:
                        btn_c = self.driver.find_element_by_css_selector(search_eless[c])
                        self.driver.execute_script("arguments[0].scrollIntoView();", btn_c)
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+38, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        title = self.driver.title
                        self.driver.back()
                        self.set_excel_data('search_result', c+38, n+1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c+38, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c+38, n + 2, '否')
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c+38, n, '没有定位到元素')
                        self.set_excel_data('search_result', c+38, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c+38, n + 2, '没有结果')

        print('完成{}测试'.format('test_search_baidu_mobile'))
if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(baiDuMoblie)
    unittest.TextTestRunner(verbosity=2).run(suite)