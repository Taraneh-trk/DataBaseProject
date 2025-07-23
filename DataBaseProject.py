import sqlite3 as db
import datetime
connect = db.connect('database.db')
cursor = connect.cursor()


exists = input('run before ? ')
# creating tables
# 1
t1 = """
    CREATE TABLE if not exists tpl (
        tpl_id int PRIMARY KEY,
        tpl_name varchar(255) not null,
        foreign key(tpl_id) references user(user_id)
    );
"""
t2 = """
    CREATE TABLE if not exists user (
        user_id int PRIMARY KEY,
        user_name varchar(255) not null,
        user_email varchar(255) not null unique,
        user_password varchar(255) not null unique,
        user_age int,
        user_type text,
        tpl_id int references tpl(tpl_id),
        check(user_type in ('normal','admin'))
    );
"""
t3 = """
    CREATE TABLE if not exists orders (
        order_id int PRIMARY KEY,
        order_date date,
        total_cost float,
        register_user_id int references user(user_id),
        tpl_id int references tpl(tpl_id),
        wh_id int references warehouse(wh_id),
        order_status varchar(255),
        order_type varchar(255),
        order_details text,
        isgift text,
        check(isgift in ('yes','no'))
    );
"""
t4 = """
    CREATE TABLE if not exists catelog (
        product_id int PRIMARY KEY,
        product_type varchar(255),
        product_image blob,
        built_cost float,
        sell_price float,
        country varchar(255),
        weight float,
        length float,
        details text,
        product_keeping_id text,
        product_name varchar(255) not null,
        tpl_id int references tpl(tpl_id),
        register_user_id int references user(user_id),
        order_user_id int references user(user_id)
    );
"""
t5 = """
    CREATE TABLE if not exists warehouse (
        wh_id int PRIMARY KEY,
        wh_name varchar(255) not null,
        isopen text,
        wh_built_date date,
        wh_country varachar(255),
        tpl_id int references tpl(tpl_id), 
        check(isopen in ('yes','no'))
    );
"""
t6 = """
    CREATE TABLE if not exists location (
        location_id int PRIMARY KEY,
        hasconteiner text,
        tpl_id int references tpl(tpl_id), 
        wh_id int references warehouse(wh_id) not null,
        location_details text,
        longitude text,
        latitude text,
        register_user_id int references user(user_id),
        check(hasconteiner in ('yes','no'))
    );
"""

cursor.execute(t1)
connect.commit()
cursor.execute(t2)
connect.commit()
cursor.execute(t3)
connect.commit()
cursor.execute(t4)
connect.commit()
cursor.execute(t5)
connect.commit()
cursor.execute(t6)
connect.commit()

# inserting data
# 2
if exists=='no':
    tpl1 = """
        insert into tpl values (1,"taraneh");
    """
    tpl2 = """
        insert into tpl values (2,"zohre");
    """
    tpl3 = """
        insert into tpl values(3,"yousef");
    """
    tpl4 = """
        insert into tpl values(4,"mina");
    """
    tpl5 = """
        insert into tpl values(5,"kiana");
    """

    cursor.execute(tpl1)
    connect.commit()
    cursor.execute(tpl2)
    connect.commit()
    cursor.execute(tpl3)
    connect.commit()
    cursor.execute(tpl4)
    connect.commit()
    cursor.execute(tpl5)
    connect.commit()

# do not fill with data that does not match to domain

# tpl6 = """
#     insert into tpl values(1,taraneh);
# """
# cursor.execute(tpl6)
# connect.commit()

if exists=='no':
    user1 = """
        insert into user values (1,"taraneh","sztu1381@gamil.com",1234,20,"admin",1);
    """
    user2 = """
        insert into user values (2,"zohre","sztu1382@gamil.com",4567,50,"normal",2);
    """
    user3 = """
        insert into user values(3,"yousef","sztu1383@gamil.com",8965,18,"admin",3);
    """
    user4 = """
        insert into user values(4,"mina","sztu1384@gamil.com",2356,22,"normal",4);
    """
    user5 = """
        insert into user values(5,"kiana","sztu1385@gamil.com",7632,27,"admin",5);
    """

    cursor.execute(user1)
    connect.commit()
    cursor.execute(user2)
    connect.commit()
    cursor.execute(user3)
    connect.commit()
    cursor.execute(user4)
    connect.commit()
    cursor.execute(user5)
    connect.commit()

if exists=='no':
    user1 = """
        insert into orders values (1,"2022-11-09",1000,2,2,3,"done","pen",'1 3',"yes");
    """
    user2 = """
        insert into orders values (2,"2022-10-25",500,4,4,2,"not_done","pencile",'2 15',"no");
    """
    user3 = """
        insert into orders values(3,"2023-04-09",700,4,4,3,"done","car",'2 12',"no");
    """
    user4 = """
        insert into orders values(4,"2023-04-05",1000,4,4,1,"done","pen",'14 16',"yes");
    """
    user5 = """
        insert into orders values(5,"2022-10-09",1200,3,3,5,"not_done","book",'1 7}',"no");
    """
    user6 = """
        insert into orders values(6,"2022-06-09",1500,2,2,2,"not_done","book",'8 15',"no");
    """
    user7 = """
        insert into orders values(7,"2022-07-10",2000,1,3,5,"done","car",'2 4',"yes");
    """
    user8 = """
        insert into orders values(8,"2022-10-23",3000,2,1,1,"not_done","pen",'1 3',"no");
    """
    user9 = """
        insert into orders values(9,"2023-08-15",700,3,3,4,"done","pen",'11 13',"no");
    """
    user10 = """
        insert into orders values(10,"2022-11-07",?,1,5,5,"done","pencile",'14 11',"no");
    """

    cursor.execute(user1)
    connect.commit()
    cursor.execute(user2)
    connect.commit()
    cursor.execute(user3)
    connect.commit()
    cursor.execute(user4)
    connect.commit()
    cursor.execute(user5)
    connect.commit()
    cursor.execute(user6)
    connect.commit()
    cursor.execute(user7)
    connect.commit()
    cursor.execute(user8)
    connect.commit()
    cursor.execute(user9)
    connect.commit()
    cursor.execute(user10,(pow(10,18),))
    connect.commit()

if exists=='no':
    user1 = """
        insert into catelog values (1,"pen",0,1000,1200,"iran",2,1,"",1,"pen_khoob",2,3,2);
    """
    user2 = """
        insert into catelog values (2,"pen",0,800,900,"iran",2,1,"",2,"pen_bad",4,3,4);
    """
    user3 = """
        insert into catelog values(3,"car",0,900,2000,"iran",2,1,"",3,"car_baklas",4,5,4);
    """
    user4 = """
        insert into catelog values(4,"book",0,300,350,"iran",2,1,"",4,"boook",3,2,3);
    """
    user5 = """
        insert into catelog values(5,"pencile",0,600,780,"iran",2,1,"",5,"penciiil",4,3,4);
    """

    cursor.execute(user1)
    connect.commit()
    cursor.execute(user2)
    connect.commit()
    cursor.execute(user3)
    connect.commit()
    cursor.execute(user4)
    connect.commit()
    cursor.execute(user5)
    connect.commit()

if exists=='no':
    user1 = """
        insert into warehouse values (1,"abi","yes",2020-11-09,"iran",2);
    """
    user2 = """
        insert into warehouse values (2,"ghermez","no",2020-10-09,"iran",3);
    """
    user3 = """
        insert into warehouse values(3,"zard","yes",2021-11-25,"iran",2);
    """
    user4 = """
        insert into warehouse values(4,"banafsh","yes",2020-11-09,"iran",4);
    """
    user5 = """
        insert into warehouse values(5,"meshki","yes",2021-11-09,"iran",5);
    """

    cursor.execute(user1)
    connect.commit()
    cursor.execute(user2)
    connect.commit()
    cursor.execute(user3)
    connect.commit()
    cursor.execute(user4)
    connect.commit()
    cursor.execute(user5)
    connect.commit()

if exists=='no':
    user1 = """
        insert into location values (1,"yes",2,1,"",11,16,2);
    """
    user2 = """
        insert into location values (2,"yes",2,3,"",12,17,3);
    """
    user3 = """
        insert into location values(3,"no",3,2,"",13,18,1);
    """
    user4 = """
        insert into location values(4,"yes",4,4,"",14,19,2);
    """
    user5 = """
        insert into location values(5,"yes",5,5,"",15,20,3);
    """
    user6 = """
        insert into location values(6,"yes",3,5,"",45,67,1);
    """

    cursor.execute(user1)
    connect.commit()
    cursor.execute(user2)
    connect.commit()
    cursor.execute(user3)
    connect.commit()
    cursor.execute(user4)
    connect.commit()
    cursor.execute(user5)
    connect.commit()
    cursor.execute(user6)
    connect.commit()


# Insert data
if exists=='no':
    tpl_data = [
        (i, f"tpl_name_{i}") for i in range(6, 21)
    ]

    user_data = [
        (i, f"user_{i}", f"user_{i}@example.com", f"password_{i}", 20 + i, "admin" if i % 2 == 0 else "normal", i) 
        for i in range(6, 21)
    ]

    orders_data = [
        (i, (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y-%m-%d'), 1000 + i * 100, (i % 20) + 1, (i % 20) + 1, (i % 5) + 1, "done" if i % 2 == 0 else "not_done", f"type_{i}", (i % 20) + 1, "yes" if i % 2 == 0 else "no") 
        for i in range(11, 22)
    ]

    catelog_data = [
        (i, f"type_{i}", None, 100 + i * 10, 200 + i * 10, f"country_{i}", 1.0 + i, 10.0 + i, f"details_{i}", f"pk_{i}", f"product_{i}", (i % 20) + 1, (i % 20) + 1, (i % 20)) 
        for i in range(6, 21)
    ]

    warehouse_data = [
        (i, f"warehouse_{i}", "yes" if i % 2 == 0 else "no", (datetime.datetime.now() - datetime.timedelta(days=i * 30)).strftime('%Y-%m-%d'), f"country_{i}", (i % 20) + 1) 
        for i in range(6, 21)
    ]

    location_data = [
        (i, "yes" if i % 2 == 0 else "no", (i % 20) + 1, (i % 5) + 1, f"details_{i}", f"long_{i}", f"lat_{i}", (i % 20) + 1) 
        for i in range(7, 21)
    ]

    # Insert data into tables
    def insert_data(table_name, data):
        placeholders = ', '.join(['?' for _ in range(len(data[0]))])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.executemany(query, data)
        connect.commit()

    insert_data('tpl', tpl_data)
    insert_data('user', user_data)
    insert_data('orders', orders_data)
    insert_data('catelog', catelog_data)
    insert_data('warehouse', warehouse_data)
    insert_data('location', location_data)



# 3
w = """
        insert into user values(21,"tata","sztu13@gamilcom",0000,1200,"admin",8);
    """
cursor.execute(w)
connect.commit()
w = """
        update user 
        set (user_email,user_password,user_age)=("sztu1380@gamil.com",2543,28)
        where user_id=8;
    """
cursor.execute(w)
connect.commit()
w = """
        delete from user 
        where user_id=21;
    """
cursor.execute(w)
connect.commit()
w = """
        insert into tpl values(21,"");
    """
cursor.execute(w)
connect.commit()
w = """
        update tpl 
        set (tpl_name)=("tata")
        where tpl_id=21;
    """
cursor.execute(w)
connect.commit()
w = """
        delete from tpl 
        where tpl_id=21;
    """
cursor.execute(w)
connect.commit()

# 4
print("1 =============================")
w = """
        select distinct user_name,user_email
        from user , orders
        where user_id = register_user_id;
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('2 =============================')
# 5
w = """
       select product_id,sum(sell_price-built_cost)
       from catelog 
       group by product_id
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('3 =============================')
# 6

# w = """
#        select product_id,count(order_user_id)
#        from catelog
#        where order_user_id is not null
#        group by product_id
#     """
w = """
        select product_id,count(order_user_id)
        from catelog , orders
        where catelog.order_user_id = orders.register_user_id
        and order_details LIKE  '%'||product_id||'%'
        group by product_id
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('4 =============================')
# 7
w = """
        select warehouse.wh_id,count(location_id)
        from location , warehouse
        where location.wh_id = warehouse.wh_id
        group by warehouse.wh_id
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('5 =============================')
# 8
# w = """
#        select tpl_id , total_cost
#        from orders
#     """
# w1 = """
#        select catelog.tpl_id , order_id , built_cost
#        from orders , catelog
#        where catelog.order_user_id = orders.register_user_id
#        and order_details = product_id 
#        group by catelog.tpl_id , order_id
#     """
# w2 = """
#         select tpl_id , built_cost
#         from  catelog
#         where order_user_id is not null
# """
w2 = """
        with orders_built_cost as
            (
                select order_id , built_cost
                from orders , catelog
                where catelog.order_user_id = orders.register_user_id
                and order_details = product_id
            )
        select tpl_id ,order_id , built_cost
        from tpl , orders_built_cost
"""
data = cursor.execute(w2)
for i in data:
    print(i)
print()
# data = cursor.execute(w2)
# for i in data:
#     print(i)
print('6 =============================')
# 9
w = """
    select 
        catelog.tpl_id, 
        strftime('-%m-', orders.order_date) AS month, 
        avg(sell_price - built_cost) AS avg_profit
    from 
        orders
    join 
        catelog ON catelog.order_user_id = orders.register_user_id
    where 
        order_details = product_id 
        AND strftime('-%m-', orders.order_date) = '-10-'
    group by
        catelog.tpl_id

    union

    select 
        catelog.tpl_id, 
        '-10-' AS month, 
        0 AS avg_profit
    from 
        catelog
    left join 
        orders ON catelog.order_user_id = orders.register_user_id
        AND order_details = product_id
    where 
        orders.order_id is null;

    """
data = cursor.execute(w)
for i in data:
    print(i)
print('7 =============================')
# 10
w = """
       select product_id,product_name,product_keeping_id
       from catelog 
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('8 =============================')
# 11
w = """
       select user_id , count(order_id) , sum(total_cost)
       from user , orders
       where user_id = register_user_id
        and orders.order_date between '2019-20-08' and '2022-10-25'
       group by user_id
    """

data = cursor.execute(w)
for i in data:
    print(i)
print('9 =============================')
# 12
w = """
        select warehouse.wh_id,count(location_id)
        from location , warehouse
        where location.wh_id = warehouse.wh_id and hasconteiner = 'yes'
        group by warehouse.wh_id
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('1 =============================')

# phase 3
# 13
w = """
       with order_weekday as
            (SELECT
                order_id , register_user_id , order_details , 
                CASE strftime('%w', order_date)
                    WHEN '0' THEN 'Sunday'
                    WHEN '1' THEN 'Monday'
                    WHEN '2' THEN 'Tuesday'
                    WHEN '3' THEN 'Wednesday'
                    WHEN '4' THEN 'Thursday'
                    WHEN '5' THEN 'Friday'
                    WHEN '6' THEN 'Saturday'
                END AS weekday_name
            FROM
                orders),
        profit_weekday as
            (select tpl_id , (sell_price - built_cost) as profit , weekday_name
            from order_weekday o, catelog c
            where o.register_user_id = c.order_user_id
                and product_id = order_details)
        select tpl_id , weekday_name , avg(profit)
        from profit_weekday
        group by tpl_id , weekday_name
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('2 =============================')
# 14

# and date = date ??? 
w = """
    select *
    from catelog
    where product_id in (
            select order_details
            from (select o1.order_details , count(o2.order_details)/3 as frequency
            from orders o1, orders o2 , orders o3
            where o1.register_user_id = o2.register_user_id
                and o3.register_user_id = o2.register_user_id
                and o1.order_details <> o2.order_details
                and o3.order_details <> o2.order_details
                and o3.order_details <> o1.order_details
            group by o1.order_details 
            order by frequency desc
            limit 3)
    )
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('3 =============================')
# 15
w = """
        select country, sum(sell_price-built_cost) as amount
        from catelog
        group by country
        order by amount desc
        limit 3
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('4 =============================')
# 16
w = """
       select *
       from user
       where user_id in (
            select user_id
            from (  select user_id , tpl_id  , profit
                    from (  select o.register_user_id as user_id, c.tpl_id as tpl_id, sum(sell_price - built_cost) as profit
                            from catelog c, orders o
                            where o.register_user_id = c.order_user_id
                            and order_details = product_id
                            group by o.register_user_id , c.tpl_id)
                    order by profit desc)
       ) 
    """
# w = """
# drop table alaki
# """
# cursor.execute(w)
# connect.commit()
data = cursor.execute(w)
for i in data:
    print(i)
print('5 =============================')
# 17
w = """
        select country , count(product_id) as count
        from catelog
        group by country
        order by count desc;
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('6 =============================')
# 18
w = """
        select tpl_id , amount/total
        from (  (select tpl_id , (100*amount) as amount
                from (  select o.tpl_id , count(*) as amount
                        from tpl t, orders o
                        where t.tpl_id = o.tpl_id
                        group by o.tpl_id)  )

                ,

                (select count(*) as total
                from tpl t, orders o
                where t.tpl_id = o.tpl_id)
             )
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('7 =============================')
# 19
w = """
        with order_month as
            (SELECT
                order_id , register_user_id , order_details , order_date , 
                CASE strftime('%m', order_date)
                    WHEN '01' THEN 'January'
                    WHEN '02' THEN 'February'
                    WHEN '03' THEN 'March'
                    WHEN '04' THEN 'April'
                    WHEN '05' THEN 'May'
                    WHEN '06' THEN 'June'
                    WHEN '07' THEN 'July'
                    WHEN '08' THEN 'August'
                    WHEN '09' THEN 'September'
                    WHEN '10' THEN 'October'
                    WHEN '11' THEN 'November'
                    WHEN '12' THEN 'December'
                END AS month_name
            FROM
                orders),
        monthly_profit as
            (select tpl_id , (sell_price - built_cost) as profit , month_name , order_date
            from order_month o, catelog c
            where o.register_user_id = c.order_user_id
                and product_id = order_details),
        monthly_profit_avg as
            (select tpl_id , month_name , avg(profit) as monthly_avg
            from monthly_profit
            where order_date >= date('now', '-2 year') and order_date <= date('now', '-1 year')
            group by tpl_id , month_name)
        
        select tpl_id , avg(monthly_avg)
        from monthly_profit_avg
        group by tpl_id
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('8 =============================')
# 20
w = """
        with order_weekday as
            (SELECT
                order_id , register_user_id , order_details , 
                CASE strftime('%w', order_date)
                    WHEN '0' THEN 'weekday'
                    WHEN '1' THEN 'weekday'
                    WHEN '2' THEN 'weekday'
                    WHEN '3' THEN 'weekday'
                    WHEN '4' THEN 'weekday'
                    WHEN '5' THEN 'weekend'
                    WHEN '6' THEN 'weekday'
                END AS day_type
            FROM
                orders),
        profit_day_type as
            (select (sell_price - built_cost) as profit , day_type
            from order_weekday o, catelog c
            where o.register_user_id = c.order_user_id
                and product_id = order_details)
        select day_type , avg(profit)
        from profit_day_type
        group by day_type
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('9 =============================')
# 21
w = """
        select *
        from user
        where user_id in (select user_id
            from (  select user_id , count(order_id) as buy_number
                    from user , orders
                    where user_id = register_user_id
                    group by user_id    )
            where buy_number in (select max(buy_number)
                                    from (  select user_id , count(order_id) as buy_number
                                            from user , orders
                                            where user_id = register_user_id
                                            group by user_id    )))
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('10=============================')
# 22
w1 = """
        select country , count(order_id) as order_number
        from catelog c, orders o
        where c.order_user_id = o.register_user_id
            and order_details = product_id  
        group by country            
"""
w2 = """
            select country
            from (  select country , count(order_id) as order_number
                    from catelog c, orders o
                    where c.order_user_id = o.register_user_id
                        and order_details = product_id  
                    group by country    )
            where order_number in (select max(order_number)
                                    from (  select country , count(order_id) as order_number
                                            from catelog c, orders o
                                            where c.order_user_id = o.register_user_id
                                                and order_details = product_id  
                                            group by country   ))
    """
data = cursor.execute(w1)
for i in data:
    print(i)
data = cursor.execute(w2)
for i in data:
    print(i)
print('11 =============================')
# 23
w = """
        select age_group , avg(profit)
        from (select user_id , 
                case 
                when user_age BETWEEN 18 AND 25 THEN '18-25'
                when user_age BETWEEN 26 AND 35 THEN '26-35'
                when user_age BETWEEN 36 AND 45 THEN '36-45'
                when user_age BETWEEN 46 AND 55 THEN '46-55'
                else '56+'
                end as age_group ,
                (sell_price - built_cost) as profit
        from user u, orders o, catelog c
        where u.user_id = o.register_user_id
            and c.order_user_id = o.register_user_id
            and order_details = product_id ) 
        group by age_group
        order by profit desc
        
    """
data = cursor.execute(w)
for i in data:
    print(i)
print('12 =============================')
# 24
w = """
        WITH unique_customers AS (
            SELECT 
                tpl_id, 
                COUNT(DISTINCT register_user_id) AS total_customers
            FROM orders
            WHERE order_date >= DATE('now', '-2 year') AND order_date <= DATE('now', '-1 year')
            GROUP BY tpl_id
        ),
        repeat_customers AS (
            SELECT 
                tpl_id, 
                COUNT(DISTINCT register_user_id) AS repeat_customers
            FROM (
                SELECT 
                    tpl_id, 
                    register_user_id, 
                    COUNT(order_id) AS order_count
                FROM orders
                WHERE order_date >= DATE('now', '-2 year')
                GROUP BY tpl_id, register_user_id
            ) AS counted_orders
            WHERE order_count > 1
            GROUP BY tpl_id
        )
        SELECT 
            u.tpl_id,
            u.total_customers,
            COALESCE(r.repeat_customers, 0) AS repeat_customers,
            CASE 
                WHEN u.total_customers > 0 
                THEN (COALESCE(r.repeat_customers, 0) * 1.0 / u.total_customers) * 100 
                ELSE 0 
            END AS retention_rate
        FROM unique_customers u
        LEFT JOIN repeat_customers r ON u.tpl_id = r.tpl_id
        ORDER BY retention_rate DESC;


    """
data = cursor.execute(w)
for i in data:
    print(i)
print('13 =============================')
# 25

w = """
        with purchases as (
            select register_user_id, SUM(total_cost) AS purchase_amount
            from orders
            group by register_user_id
        ),
        stats as (
            select 
                avg(purchase_amount) AS avg_purchase_amount,
                (avg(purchase_amount*purchase_amount) - avg(purchase_amount) * avg(purchase_amount)) AS variance
            FROM purchases
        )
        select 
            register_user_id,
            purchase_amount
        from 
            purchases
        cross join 
            stats
        where 
            purchase_amount > avg_purchase_amount + 3 * sqrt(variance)
            or purchase_amount < avg_purchase_amount - 3 * sqrt(variance)
        order by 
            purchase_amount DESC;

    """
data = cursor.execute(w)
for i in data:
    print(i)