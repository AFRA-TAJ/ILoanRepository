#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[5]:


import mysql.connector as sql
conn=sql.connect(host='localhost',database='loan_managt',user='root',password='Af#ra_02!')#connecting with database
if conn.is_connected:
    print("Database is connected:")
    
stmt=conn.cursor()
create_str='''
create table if not exists customer
(
c_id int,
name varchar(50),
email varchar(50),
ph varchar(50),
address varchar(100),
credit_score int
)
'''
stmt.execute(create_str)

statmt=conn.cursor()
creat_str='''
create table if not exists loan
(
loan_id int,
cust_name varchar(50),
principal_amt int,
interest_rate int,
loan_term int,
loan_type varchar(50),
loan_status varchar(50)
)
'''
statmt.execute(creat_str)

create_insert='''
insert into customer values(1,"diya","diya@example.com",1234567876,"123 street",670),(2,"priya","priya@example.com",8299967876,"456 street",870),(3,"joe","diya@example.com",9934567876,"789 street",750)
'''
stmt=conn.cursor()
stmt.execute(create_insert)
conn.commit()
print('Inserted Successfully:')

creat_insert='''
insert into loan values(1,"diya",30000,0.5,12,"CarLoan","Approved"),(2,"priya",40000,0.5,24,"HomeLoan","Pending"),(3,"joe",50000,0.5,6,"CarLoan","Pending")
'''
statmt=conn.cursor()
statmt.execute(creat_insert)
conn.commit()
print('Inserted Successfully')


# In[ ]:




