import os
import unittest

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from function import Excel

url = 'https://www.sogou.com/'
chrome_driver_path = os.path.split(os.path.realpath(__file__))[0] + '/chromedriver'
search_key = ['英荔', '英荔教育', '英荔商学院']
search_ele = [r'#sogou_cpc_0', r'#sogou_vr_30000909_0', r'#uigs__1', r'#sogou_vr_30000909_2', r'#sogou_vr_30000909_4']
search_eles = [r'#sogou_cpc_0', r'#uigs__0', r'#sogou_vr_30000909_1', r'#sogou_vr_30000909_2', r'#sogou_vr_30000909_4']
search_eless = [r'#ad_leftresult_0 > h3 > a', r'#uigs__0', r'#uigs__1', r'#sogou_vr_10000201_2', r'#sogou_vr_30000909_4']
options = CH_Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920x1080")
options.add_argument('--no-sandbox')# 在Ubuntu上执行要加上这句
class soGou(unittest.TestCase):
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

    def set_excel_data(self, dataname, col, row, datas):
        excel_data = Excel(dataname)
        excel_data.write_excel_rol(col, row, datas)
    def test_search_baidu(self):
        n = 0
        for i in range(0, len(search_key)):
            if i == 0:
                search_input = self.driver.find_element_by_id('query')
                search_input.clear()
                print(search_key[i])
                search_input.send_keys(search_key[i])
                search_btn = self.driver.find_element_by_id('stb')
                search_btn.click()
                sleep(2)
                for c in range(0, len(search_eles)):
                    try:
                        btn_c = self.driver.find_element_by_css_selector(search_ele[c])
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+20, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        handles = self.driver.window_handles
                        self.driver.switch_to.window(handles[-1])
                        title = self.driver.title
                        self.set_excel_data('search_result', c+20, n+1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c + 20, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c + 20, n + 2, '否')
                        self.driver.close()
                        self.driver.switch_to.window(handles[0])
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c + 20, n, '没有定位到元素')
                        self.set_excel_data('search_result', c + 20, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c + 20, n + 2, '没有结果')
            if i == 1:
                self.driver.get(url)
                search_input = self.driver.find_element_by_id('query')
                search_input.clear()
                search_input.send_keys(search_key[i])
                search_btn = self.driver.find_element_by_id('stb')
                search_btn.click()
                sleep(2)
                for c in range(0, len(search_ele)):
                    try:
                        n = 4
                        btn_c = self.driver.find_element_by_css_selector(search_eles[c])
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c + 20, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        handles = self.driver.window_handles
                        self.driver.switch_to.window(handles[-1])
                        title = self.driver.title
                        self.set_excel_data('search_result', c + 20, n + 1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c + 20, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c + 20, n + 2, '否')
                        self.driver.close()
                        self.driver.switch_to.window(handles[0])
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c + 20, n, '没有定位到元素')
                        self.set_excel_data('search_result', c + 20, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c + 20, n + 2, '没有结果')
                n += 4
            if i == 2:
                self.driver.get(url)
                search_input = self.driver.find_element_by_id('query')
                search_input.clear()
                search_input.send_keys(search_key[i])
                search_btn = self.driver.find_element_by_id('stb')
                search_btn.click()
                sleep(2)
                for c in range(0, len(search_ele)):
                    try:
                        btn_c = self.driver.find_element_by_css_selector(search_eless[c])
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c + 20, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        handles = self.driver.window_handles
                        self.driver.switch_to.window(handles[-1])
                        title = self.driver.title
                        self.set_excel_data('search_result', c + 20, n + 1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c + 20, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c + 20, n + 2, '否')
                        self.driver.close()
                        self.driver.switch_to.window(handles[0])
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c + 20, n, '没有定位到元素')
                        self.set_excel_data('search_result', c + 20, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c + 20, n + 2, '没有结果')
        print('完成{}测试'.format('sougou_test'))

if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(soGou)
    unittest.TextTestRunner(verbosity=2).run(suite)