import os
import unittest

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from function import Excel

url = 'https://cn.bing.com/'
mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
chrome_driver_path = os.path.split(os.path.realpath(__file__))[0] + '/chromedriver'
search_key = ['英荔', '英荔教育', '英荔商学院']

search_ele = [r'#b_results > li:nth-child(1) > div.b_algoheader > h2 > a:nth-child(2)',
              r'#b_results > li:nth-child(2) > div.b_algoheader > h2 > a:nth-child(2)',
              r'#b_results > li:nth-child(3) > div.b_algoheader > h2 > a:nth-child(2)',
              r'#b_results > li:nth-child(4) > div.b_algoheader > h2 > a:nth-child(2)',
              r'#b_results > li:nth-child(5) > div.b_algoheader > h2 > a:nth-child(2)',]

search_eles = [r'#b_results > li:nth-child(1) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(2) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(3) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(4) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(5) > div.b_algoheader > h2 > a:nth-child(2)',]


search_eless = [r'#b_results > li:nth-child(1) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(2) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(3) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(4) > div.b_algoheader > h2 > a:nth-child(2)',
               r'#b_results > li:nth-child(5) > div.b_algoheader > h2 > a:nth-child(2)',]
class bingMoblie(unittest.TestCase):
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
        excel_data.write_excel_rol(col,row, datas)

    def test_search_bing_moblie(self):
        n = 0
        search_input = self.driver.find_element_by_id('sb_form_q')
        search_input.clear()
        search_input.send_keys(search_key[0])
        search_btn = self.driver.find_element_by_id('sbBtn')
        search_btn.click()
        sleep(1)
        for i in range(0, len(search_key)):
            search_input = self.driver.find_element_by_id('sb_form_q')
            search_input.clear()
            search_input.send_keys(search_key[i])
            search_btn = self.driver.find_element_by_id('sb_form_go')
            search_btn.click()
            sleep(1)
            if i == 0:
                for c in range(0, len(search_eles)):
                    try:
                        btn_c = self.driver.find_element_by_css_selector(search_eles[c])
                        self.driver.execute_script("arguments[0].scrollIntoView();", btn_c)
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+47, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        title = self.driver.title
                        self.driver.back()
                        self.set_excel_data('search_result', c+47, n+1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c+47, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c+47, n + 2, '否')
                        sleep(2)
                    except:
                        print(search_eles[c])
                        self.set_excel_data('search_result', c+47, n, '没有定位到元素')
                        self.set_excel_data('search_result', c+47, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c+47, n + 2, '没有结果')




            if i==1:
                for c in range(0, len(search_ele)):
                    try:
                        n = 4
                        btn_c = self.driver.find_element_by_css_selector(search_ele[c])
                        self.driver.execute_script("arguments[0].scrollIntoView();", btn_c)
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+47, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        title = self.driver.title
                        self.driver.back()
                        self.set_excel_data('search_result', c+47, n + 1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c+47, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c+47, n + 2, '否')
                        sleep(2)
                    except:
                        print(search_ele[c])
                        print(btn_c_t)
                        self.set_excel_data('search_result', c+47, n, '没有定位到元素')
                        self.set_excel_data('search_result', c+47, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c+47, n + 2, '没有结果')

                n += 4
            if i == 2:
                for c in range(0, len(search_eless)):
                    try:
                        btn_c = self.driver.find_element_by_css_selector(search_eless[c])
                        self.driver.execute_script("arguments[0].scrollIntoView();", btn_c)
                        btn_c_t = btn_c.text
                        self.set_excel_data('search_result', c+47, n, btn_c_t)
                        btn_c.click()
                        sleep(2)
                        title = self.driver.title
                        self.driver.back()
                        self.set_excel_data('search_result', c+47, n+1, title)
                        if title == '首页 | 英荔商学院':
                            self.set_excel_data('search_result', c+47, n + 2, '是')
                        else:
                            self.set_excel_data('search_result', c+47, n + 2, '否')
                        sleep(2)
                    except:
                        self.set_excel_data('search_result', c+47, n, '没有定位到元素')
                        self.set_excel_data('search_result', c+47, n + 1, '没有定位到元素')
                        self.set_excel_data('search_result', c+47, n + 2, '没有结果')


if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(bingMoblie)
    unittest.TextTestRunner(verbosity=2).run(suite)