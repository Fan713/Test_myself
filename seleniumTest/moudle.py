# -*-encoding:utf-8 -*- 
import time
from selenium import webdriver


browser=webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# browser=webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser.maximize_window()                 #窗口最大化
#访问百度首页
first_url='https://www.baidu.com/'
print('now access %s'%(first_url))
browser.get(first_url)     #进入百度首页
#获取输入框尺寸
size=browser.find_element_by_id('kw').size
print('baidu_size=',size)
#返回百度页面底部备案信息
text=browser.find_element_by_id('ftConw').text
print('baidu_text=',text)
#返回元素的属性值，可以是id、name、type或元素拥有的其他任意属性
attribute_type=browser.find_element_by_id('kw').get_attribute('type')
attribute_id=browser.find_element_by_id('kw').get_attribute('id')
attribute_name=browser.find_element_by_id('kw').get_attribute('name')
print('baidu_attribute_type=',attribute_type)
print('baidu_attribute_id=',attribute_id)
print('baidu_attribute_name=',attribute_name)
#返回元素的结果是否可见，返回结果为True或False
result=browser.find_element_by_id('kw').is_displayed()
print(result)

#访问新闻页面
second_url='https://news.baidu.com/'
print('now access %s'%(second_url))
browser.get(second_url)
time.sleep(2)
#返回（后退）到百度首页
print('back to %s'%(first_url))
browser.back()
time.sleep(2)
#前进到新闻页
print('forward to %s'%(second_url))
browser.forward()



################################################################################
# #登录百度账号界面
# str_login='''
# <div id="wrapper" style="display: block;">
# .....
# <div id="u"><a class="toindex" 
# href="/">百度首页</a><a href="javascript:;" 
# name="tj_settingicon" class="pf">设置<i class="c-icon c-icon-triangle-down"></i></a>
# <a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;sms=5" name="tj_login" class="lb" onclick="return false;">登录</a></div>
# '''
# els=browser.find_elements_by_tag_name('a')
# print('els=',els)
# for i in els:
#     if i.text==u'登录':
#         i.click()
#         break
# browser.implicitly_wait(10)
# strlogin_2='''
# <div class="buttons" id="TANGRAM__PSP_4__titleButtons"><a id="TANGRAM__PSP_4__closeBtn" class="close-btn" href="###" onmousedown="event.stopPropagation &amp;&amp; event.stopPropagation(); event.cancelBubble = true; return false;" onclick="return false;"></a></div>
# '''
# browser.find_element_by_class_name('buttons').click()     #关闭登录界面对话框
# time.sleep(1)
# 
# 
# ##################################################################################
# # 在百度页面输入搜索内容
# str_baidu='''
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# '''
# input_element=browser.find_element_by_id('kw')
# # input_element=browser.find_element_by_name('wd')
# # input_element=browser.find_element_by_class_name('s_ipt')
# input_element.send_keys('python菜鸟教程')
# input_element.submit()
##################################################################################

time.sleep(10)
browser.close()
browser.quit()


