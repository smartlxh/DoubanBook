# -*- coding:utf-8 -*-
import scrapy
import re
from douban.items import DoubanItem
from scrapy.selector import Selector

from bs4 import BeautifulSoup
from douban.items import DoubanItem

class doubanSpider(scrapy.Spider):
    name = "douban"
    header = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"}
    def start_requests(self):
        urls = [
            'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseIndex,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36','Referer' : 'https://book.douban.com/'})

    def parseIndex(self, response):

        soup = BeautifulSoup(response.body,'lxml')
        tbody = soup.findAll('tbody')

        for t in tbody:
            for tr in t.findAll('tr'):
                for m in tr.findAll('td'):
                    #print m.a.attrs['href']
                    for i in range (0,1000,20):

                        url =response.urljoin(m.a.attrs['href']+"?"+"start="+str(i)+"&type=T")
                    #    print url
                        yield scrapy.Request(url,callback = self.parseTag,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36','Referer' : 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'})
                    #yield scrapy.Request(response.urljoin(m.a.attrs['href']),callback = self.parseTag,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36','Referer' : 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'})
                    pass
            #yield scrapy.Request('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',callback=self.parseTag ,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'})


    def parseTag(self,response):

        soup = BeautifulSoup(response.body,'lxml')

        for li in soup.find_all('li',class_='subject-item'):
           item = DoubanItem()

           item['imgUrl'] = li.img['src']
           a = li.findAll('a')[1]
           item['bookName'] =  a['title']
           item['detailUrl'] = a['href']
           #item['author'] = li.findAll('div')[2].string
           country_author_price = li.findAll('div')[2].string.strip().strip('\n')

           country1 = re.findall('\[\S+\]',country_author_price)
           country2 = re.findall('\((\S+)\)',country_author_price)
           dat = re.findall('(\d+-\d*)',country_author_price)#日期
           price = re.findall('\d+\.\d+',country_author_price)
           #print country_author_price
           #pub = re.findall(r'\S+版\S+',country_author_price)
           author = country_author_price.split('/')[0].strip()

           if len(dat) !=0:
               item['dat'] = dat[0].strip()
           if len(country1) != 0:
               item['country'] = country1[0].strip()
               item['author']= author.replace(country1[0],'').strip();
           elif len(country1) != 0:
               item['country'] = country2[0].strip()
               item['author']=author.replace(country2[0],'').strip();
           else :
               item['country'] = "中国"
               item['author'] =country_author_price.split('/')[0].strip()

           #if len(pub) !=0:
            #    item['pub'] = pub[0].strip()
            #    pass
                #print item['pub']

           if len(price) !=0:
               item['price'] = price[0].strip()
           else :
                item['price'] =''
           if li.p !=None:
                item['description'] = li.p.string.strip()
           else:
                item['description'] =''
           span = li.find_all('span', class_='rating-stars')
           if len(span)!=0:

                item['score'] =li.find_all('span',class_='rating-stars')[0]['data-rating'].strip()
           else:
               item['score'] = ''
           #items.append(item)
           yield item
           #yield scrapy.Request(url,callback = self.parseDetail,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'})
        #return items
    def parseDetail(self,response):
        pass
