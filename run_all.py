import smtplib
import unittest

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime as dt
ProjectPath = os.path.split(os.path.realpath(__file__))[0]
def get_case_list():
    """获取case_list.txt文件中要执行的用例文件的名称"""
    print(ProjectPath, '我是caselist')
    list = open(os.path.join(ProjectPath, "case_list.txt"))
    cases = []
    for value in list.readlines():
        data = str(value)
        if data != "" and not data.startswith("#"):
            cases.append(data.replace("\n", ""))
    print(cases, "cases")
    return cases
def send_mail():

    msg = MIMEMultipart('mixed')
    # 添加邮件内容
    #msg_html = MIMEText(content, 'html', 'utf-8')
    # msg.attach(msg_html)
    content_msg = 'To all：附件附上企业版lms自动化测试报告。此邮件为自动发送，请勿回复。该测试报告适用为{0}发布版本'
    print(content_msg)
    msg_content = MIMEText(content_msg.format(dt.now().strftime('%Y%m%d'), 'plain', 'utf-8'))
    msg.attach(msg_content)

    # 添加附件
    msg_attachment = MIMEText(filename)
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = mail_user
    msg['To'] = ';'.join(mail_to)
    try:
        # 连接邮件服务器
        s = smtplib.SMTP_SSL(mail_host, 465)
        # 登陆
        s.login(mail_user, mail_pwd)
        # 发送邮件
        s.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        s.quit()
    except Exception as e:
        print("Exceptioin ", e)


def get_list():
    """获取case_list.txt文件中要执行的用例文件，返回以文件为单位的list集合"""
    suite_module = []
    list = get_case_list()
    for value in list:
        case_path = os.path.join(ProjectPath, "case")
        discover = unittest.defaultTestLoader.discover(case_path,   pattern=value.split("/")[-1]+'.py', top_level_dir=None)
        suite_module.append(discover)
    #print(suite_module, "suite_module")
    return suite_module

if __name__ == '__main__':
    title = "搜索测试报告"
    browser = 'chrome'
    description = "浏览器：" + browser
    testunit = unittest.TestSuite()
    list = get_list()
    if len(list) > 0:
        for suite in get_list():
            testunit.addTest(suite)
    filename = ProjectPath + '/search_result.xls'
    runner = unittest.TextTestRunner()
    runner.run(testunit)
    # 邮件服务器
    mail_host = 'smtp.exmail.qq.com'
    # 发件人地址
    mail_user = 'qf.luo@eliteu.com.cn'
    # 发件人密码
    mail_pwd = 'Luoqingfu2019'
    # 邮件标题
    mail_subjet = '企业版LMSUI自动化测试报告_{0}'
    # 收件人地址list
    mail_tolist= ['746832476@qq.com', '755682146@qq.com']
    mail_to = []
    for n in range(len(mail_tolist)):
        mail_to.append(mail_tolist[n])
    report_file = filename
    # 发送测试报告邮件

    #send_mail()
    print('Send Test Report Mail Now...')

