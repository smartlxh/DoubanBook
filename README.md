# DoubanBook

本项目首先从豆瓣爬取数据信息，然后将信息持久化存储到mysql数据库中。最后用springboot 提供rest服务。也提供docker支持。

### 使用方法

#### 获取代理ip
	git clone git@github.com:smartlxh/DoubanBook.git
	cd IPProxys
	python IPProxys.py


#### 运行豆瓣爬虫爬取信息(注意在db.properties中配置数据库信息)
	
	cd doubanSpider
	scrapy crawl douban
	
#### 运行spring-boot服务(注意在db.properties中配置数据库信息)

	
	cd DoubanRestful
	cd target
	java -jar gs-rest-service-0.1.0.jar

#### 接口API
 http://127.0.0.1/author?name=value
 http://127.0.0.1/book?name=value
 http://127.0.0.1/country?name=value
 分别为按照作者、书名和国家查询。返回json格式
 例如
 		
 		http://127.0.0.1:8080/greeting?name=%E5%B0%8F%E7%8E%8B%E5%AD%90
 ![](http://i1.piimg.com/567571/7b181d03a023d5d4.png)
	
	

注：获取代理ip为引用另一个开源项目[IPProxy](https://github.com/qiyeboy/IPProxys)：
	通过爬取免费代理ip网站并验证是否能用后将数据存到sqlite中去
	最后通过本机80端口访问


