# 爬取猫眼电影的前 10 个电影名称、电影类型和上映时间
import requests
import lxml.etree
import pandas as pd
from bs4 import BeautifulSoup as bs


# 爬取页面详细信息

# 电影详细页面
url = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
cookies = '__mta=146632971.1601191977263.1601199865464.1601206734098.6; uuid_n_v=v1; uuid=A880D4E0009311EB976821670BA38D646AA3DCFE01E348CA954F25F5AD004DB4; mojo-uuid=064a5f5ac30666fabc48082319bc8f75; _lxsdk_cuid=174ce7aa0edc8-0c14fa6c125b95-3a65460c-100200-174ce7aa0eec8; _lxsdk=A880D4E0009311EB976821670BA38D646AA3DCFE01E348CA954F25F5AD004DB4; mojo-session-id={"id":"6bcc6f107a7303f459ca3f9750de2824","time":1601204842989}; recentCis=364; _csrf=c58dcaf3965699f381817505111d880a62cde8debabda20b35868edbeda08fa9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601195915,1601204979,1601205304,1601206450; mojo-trace-id=69; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601207503; __mta=146632971.1601191977263.1601206734098.1601207502653.7; _lxsdk_s=174cf3eed07-246-5cf-b62%7C%7C115'

# 声明为字典使用字典的语法赋值
headers = {'user-agent': user_agent, 'cookie': cookies}

response = requests.get(url, headers=headers)

# xml化处理
selector = lxml.etree.HTML(response.text)
#print(response.text)
# 电影名称
film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[2]/a/text()')

print(f'电影名称: {film_name}')

#上映日期
plan_date = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/text()')
print(f'上映日期: {plan_date}')

#电影类型
film_tag = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/text()')
print(f'电影类型：{film_tag}')

mylist = [film_name, plan_date, film_tag]




movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='GBK', index=False, header=False)
