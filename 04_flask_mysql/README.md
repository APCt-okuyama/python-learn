# Flask + MySQL

## Azure Database Server for MySQL
```
RG_NAME=az-example-python
LOCATION=japaneast
az mysql server create --resource-group $RG_NAME --name example-mysql-server --location $LOCATION --sku-name GP_Gen5_2 \
--admin-user <USERNAME> --admin-password <PASSWORD>
```

ローカルPCからの接続許可 (必要であれば)
```
az mysql server firewall-rule create --resource-group $RG_NAME \
--server example-mysql-server \
--name AllowMyIP \
--start-ip-address 192.168.1.75 --end-ip-address 192.168.1.75
```
14.132.153.117

DBの作成 (必要な分だけ作成)
```
az mysql db create --resource-group $RG_NAME --server-name example-mysql-server --name exampledb1
```
--admin-user apcadmin --admin-password Password@123
# mysql コマンド

接続
```
mysql -h example-mysql-server.mysql.database.azure.com -u apcadmin@example-mysql-server -p
mysql>
```

DB作成(管理者で)
```
CREATE DATABASE exampledb1;
```

ユーザを作成して権限を与える
```
CREATE USER 'apcuser1'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON exampledb1 . * TO 'apcuser1'@'%';
FLUSH PRIVILEGES;
```

db操作
```
show databases;
use exampledb1; 
SHOW GRANTS FOR 'apcuser1'@'%';
select database();
```

table作成
```
create table user (
id int auto_increment not null primary key,
name varchar(256) not null 
);
desc user;

show tables;
show full tables;

insert into user (name) values ("aaa");
insert into user (name) values ("bbb");
insert into user (name) values ("ccc");
```

# python + mysql
pythonアプリからのCRUD操作

```
pip install mysql-connector-python
```