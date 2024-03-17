from Chapter12.Chapter_12_6.page.locators import *


class BasePage(object):
    # 构造一个基础类
    def __init__(self, driver):
        # 在初始化的时候，会自动运行
        self.driver = driver


class HomePageOpn(BasePage):
    # 首页元素操作
    # 单击首页标签
    def click_home_label(self):
        # 单击搜索框
        ele = self.driver.find_element(*HomePageLocators.HomeLabel)
        ele.click()
        
    # 单击首页搜索框
    def click_search_box(self):
        # 单击搜索框
        ele = self.driver.find_element(*HomePageLocators.SearchBox)
        ele.click()
        # ele.tap()

    # 在弹出的搜索页面输入文字
    def search_goods(self, goods_name):
        # 输入书名
        ele = self.driver.find_element(*HomePageLocators.Search)
        ele.send_keys(goods_name)

    # 在弹出的搜索页面，单击搜索按钮
    def click_search_btn(self):
        # 单击登录按钮
        ele = self.driver.find_element(*HomePageLocators.SearchBtn)
        ele.click()


class BookPageOpn(BasePage):
    # 书籍列表和详情页操作
    # 点击"京东物流"筛选商品
    def click_jd(self):
        ele = self.driver.find_element(*BookPageLocators.JDLogistics)
        ele.click()

    # 通过点击作者元素，进入书籍详情页
    def click_list_author(self, author):
        # 获取作者列表
        # 因为该元素定位跟业务逻辑有关，所以搜索内容不同，定位器不同，因此不从locators.py读取定位器
        # ele = self.driver.find_element(*BookPageLocators.ListAuthor)
        ele = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '{}'.format(author))
        ele.click()

    # 单击加入购物车按钮
    def click_add2card_btn(self):
        ele = self.driver.find_element(*BookPageLocators.Add2CardBtn)
        ele.click()

    # 单击返回按钮
    def click_back_btn(self):
        ele = self.driver.find_element(*BookPageLocators.BackBtn)
        ele.click()

    # 单击确定按钮
    def click_ok_btn(self):
        ele = self.driver.find_element(*BookPageLocators.OkBtn)
        ele.click()

    # 单击close icon按钮
    def click_close_icon(self):
        ele = self.driver.find_element(*BookPageLocators.CloseIcon)
        ele.click()

    # 单击收藏按钮
    def click_collection_btn(self):
        ele = self.driver.find_element(*BookPageLocators.CollectionBtn)
        ele.click()

    # 获取详情页作者信息
    def get_detail_author(self, author):
        author_info = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "{}"'.format(author)).text
        return author_info

    def get_detail_publish(self, publisher):
        # 先定位"出版社"这个元素
        ele = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '{}'.format(publisher))
        return ele.get_attribute('name')


class ShopCartPageOpn(BasePage):
    # 购物车页面元素操作
    # 单击购物车标签
    def click_shopcart_label(self):
        ele = self.driver.find_element(*ShopCartPageLocators.ShopCartLabel)
        ele.click()

    # 获取购物车书籍名称列表
    def get_book_name_list(self):
        eles = self.driver.find_elements(*ShopCartPageLocators.ListBookName)
        return eles

    # 获取购物车第一本书籍名称
    def get_book_name_first(self):
        author_name = self.driver.find_element(*ShopCartPageLocators.ListBookName).get_attribute('name')
        return author_name

    # 单击结算按钮
    def click_settlement_btn(self):
        ele = self.driver.find_element(*ShopCartPageLocators.SettlementBtn)
        ele.click()

    # 获取提交订单按钮是否可单击的状态
    def get_submit_btn_status(self):
        ele = self.driver.find_element(*ShopCartPageLocators.SubmitBtn)
        return ele.get_attribute('enabled')


class PersonPageOpn(BasePage):
    # 个人页面元素操作
    # 单击我的标签
    def click_person_label(self):
        ele = self.driver.find_element(*PersonPageLocators.PersonLabel)
        ele.click()

    # 单击"收藏"图标
    def click_product_collection(self):
        ele = self.driver.find_element(*PersonPageLocators.ProductCollection)
        ele.click()


class CollectionPageOpn(BasePage):
    # 商品收藏页面的元素操作

    # 所有商品名，保存为列表
    def get_collect_bookname_list(self, book_name):
        eles = self.driver.find_elements(AppiumBy.IOS_PREDICATE, 'label CONTAINS "{}"'.format(book_name))
        return eles

    # 返回第一个收藏的商品
    def get_collect_goods_first(self, book_name):
        first_goods = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label CONTAINS "{}"'.format(book_name))
        return first_goods

    # 点击取消收藏按钮
    def click_uncollect(self):
        ele = self.driver.find_element(*CollectionPageLocators.UncollectBtn)
        ele.click()


