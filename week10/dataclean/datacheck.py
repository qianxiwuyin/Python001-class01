import pymysql
import pandas as pd
from snownlp import SnowNLP
from snownlp import seg


sql = 'select * from szdata.old_szdata where title limit 10 '
conn = pymysql.connect(
            port=3306,
            user='root',
            password='zt123666',
            database='szdata',
            charset='utf8mb4'
        )
df = pd.read_sql(sql,conn)
a= df[['title','description']]
print(a)






