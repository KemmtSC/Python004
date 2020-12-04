# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MysqlPipeline:

    @classmethod
    
    def open_spider(self,spider):
         self.conn = pymysql.connect(
             host = 'localhost',
             port = 3306,
             user = 'root',
             password = '3230287yys',
             database = 'db',
             charset = 'utf8'
         )
         self.cursor = self.conn.cursor()
         self.cursor.execute('truncate table db')
         self.conn.commit()



    def process_item(self,item,spider):

        try:
            self.cursor.execute("insert into db (movie_name,movie_score,movie_actor,movie_type,movie_time) VALUES (%s,%s,%s,%s,%s)", (item['movie_name'],item['movie_score'],item['movie_actor'],item['movie_type'],item['movie_time']))
            self.conn.commit()
        except pymysql.Error:
            print("Error%s,%s,%s,%s,%s" % (item['movie_name'],item['movie_score'],item['movie_actor'],item['movie_type'],item['movie_time']))
        return item
      

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

        

        # keys = ','.join(data.keys())
        # values = ','.join(['%s']*len(data))
        # sql = 'INSET INTO %s (%s) VALUES (%s)' %(item.table,keys,values)
        # self.cursor.execute(sql,tuple(data.values()))
        # self.db.commit()
        # return item

# class ProxyspiderPipeline:
#     def process_item(self, item, spider):
#         return item
