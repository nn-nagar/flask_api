# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector

class QuetetutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            database = 'dbname'
            #auth_plugin='root'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS dbname""")
        self.curr.execute("""create table dbname(
            id text,
            name text,
            market_cap text,
            price text,
            volume text,
            circulating_supply text
            
            
        )""")
        



    def process_item(self, item, spider):
        #self.store_db(item)
        print("pipeline :" + item['name'])
        return item

    def store_db(self,item):
        self.curr.execute("""insert into dbname values (%s,%s,%s,%s,%s,%s)""",(
            item['id'],
            item['name'],
            item['market_cap'],
            item['price'],
            item['value'],
            item['circulating_supply']
            # item['change']
        ))
        self.conn.commit()
