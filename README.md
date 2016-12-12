# DoubanBook

本项目首先从豆瓣爬取数据信息，然后将信息持久化存储到mysql数据库中。最后用springboot 提供rest服务。也提供docker支持。

### 使用方法

#### 获取代理ip
	git clone git@github.com:smartlxh/DoubanBook.git
	cd IPProxys
	python IPProxys.py

#### 运行spring-boot服务
	
	cd DoubanRestful
	cd target
	java -jar gs-rest-service-0.1.0.jar
	
	

注：获取代理ip为引用另一个开源项目[IPProxy](https://github.com/qiyeboy/IPProxys)：
	通过爬取免费代理ip网站并验证是否能用后将数据存到sqlite中去
	最后通过本机80端口访问


