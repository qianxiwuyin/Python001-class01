import pandas as pd
import numpy as np


#生成一组数据
group =['x','y']
data=pd.DataFrame({'group':np.random.randint(0,50,15),
                   'id':np.random.randint(0,15,15),
                   'age': np.random.randint(0,60,15),
                   'high': np.random.randint(0,2,15),
                   })
print('1. SELECT * FROM data;')
print(data)

print('2. SELECT * FROM data LIMIT 10;')
a=data.loc[0:9]
print(a)
print('3.SELECT id FROM data;id 是 data 表的特定一列')
#将id 设置为索引
data.set_index('id')
print(data['id'])

print('4. SELECT COUNT(id) FROM data;')
c=data.groupby('id').aggregate( {'id':'count' })
print(c)

print('5. SELECT * FROM data WHERE id<1000 AND age>30;')

d=data[(data['id']<1000) & (data['age']>30)]
print(d)

print('------------------------------')
table1 = pd.DataFrame({"id": np.random.randint(0,15,10),
                       "order_id":np.random.randint(0,8,10),
                       'column_name':np.random.randint(0,3,10)
                       })
print('6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;')
#print(table1)
table3=table1.drop_duplicates(subset='order_id',keep='first')
table3= table3.groupby('id').aggregate({'order_id':'count',})
print(table3)

print('-----------table2---------------')
table2 = pd.DataFrame({
    "id":np.random.randint(0,15,10),
    "order":np.random.randint(0.8,10),
    "pai":np.random.randint(0.3,10)
})
print('7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;')
co=pd.merge(table1, table2, on= 'id', how='inner')
print(co)
print('8. SELECT * FROM table1 UNION SELECT * FROM table2;')
pd.merge(table1, table2)

print('9.DELETE FROM table1 WHERE id=10;')

f=table1[table1['id']==10]

print(f)

print('10. ALTER TABLE table1 DROP COLUMN column_name;')


del1=table1.drop('column_name',axis=1)
print(del1)