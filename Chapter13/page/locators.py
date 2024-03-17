from appium.webdriver.common.appiumby import AppiumBy


class HomePageLocators(object):
    # 首页
    HomeLabel = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "首页"`]')  # 底部的首页标签
    # 当首页搜索框定位器发生变化，只需修改下方代码
    SearchBox = (AppiumBy.IOS_PREDICATE, 'name CONTAINS "搜索栏"')  # 首页的搜索栏
    Search = (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"')  # 搜索页搜索框
    SearchBtn = (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" and name == "搜索"')  # 搜索按钮


class BookPageLocators(object):
    # 书籍列表和详情页,------这里的定位方式不能和业务数据有关系
    JDLogistics = (AppiumBy.IOS_PREDICATE, 'label == "京东物流" AND name == "京东物流"')  # 京东物流筛选
    Add2CardBtn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "加入购物车"`]')  # 加入购物车按钮
    OkBtn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "确定"`]')  # 新增确定按钮
    CloseIcon = (AppiumBy.IOS_PREDICATE, 'label == "closeIcon"') # 新增关闭窗口图标
    BackBtn = (AppiumBy.ACCESSIBILITY_ID, '返回')  # 返回按钮
    CollectionBtn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "收藏"`][2]')  # 收藏按钮
    # publisher = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="出版社"]/preceding-sibling::XCUIElementTypeStaticText[1]')
    # publisher = (AppiumBy.ACCESSIBILITY_ID, '人民邮电出版社')



class ShopCartPageLocators(object):
    # "购物车"页面
    ShopCartLabel = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "购物车"`]')  # 购物车标签
    ListBookName = (AppiumBy.IOS_PREDICATE, 'label CONTAINS "Python实现Web UI自动化测试实战"')  # 书籍名称
    SettlementBtn = (AppiumBy.IOS_PREDICATE, 'label CONTAINS "去结算"')  # 去结算按钮
    SubmitBtn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "提交订单"`]')  # 提交订单按钮


class PersonPageLocators(object):
    # “我的”页面
    PersonLabel = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "我的"`]')  # “我的”标签
    ProductCollection = (AppiumBy.IOS_PREDICATE, 'label == "商品收藏"') # 商品收藏按钮


class CollectionPageLocators(object):
    # "收藏"页面
    CollectBookName = (AppiumBy.IOS_PREDICATE, 'label CONTAINS "Python实现Web UI自动化测试实战"')  # 收藏书籍的名称
    UncollectBtn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "取消 收藏"`][1]') # 取消收藏按钮
