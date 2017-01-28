Commands
========

<pre><code>
mysql -p
SHOW DATABASES;
CREATE DATABASE dbtest;
USE DATABASE dbCustomerInfo;

CREATE TABLE tblCustomerIDInfo(custID varchar(10) PRIMARY KEY, custInfoFirstName varchar(50), custInfoLastName varchar(50), custInfoAddr1 varchar(50), custInfoAddr2 varchar(50), custInfoCityName varchar(50), custInfoState varchar(10), custInfoZipCode varchar(10),custInfoPhone varchar(12));

SHOW FIELDS FROM tblCustomerInfo;
mysql> SHOW FIELDS FROM tblCustomerIDInfo;
<code></pre>

<pre><code>
 +-------------------+-------------+------+-----+---------+-------+
 | Field             | Type        | Null | Key | Default | Extra |
 +-------------------+-------------+------+-----+---------+-------+
 | custID            | varchar(10) | NO   | PRI | NULL    |       |
 | custInfoFirstName | varchar(50) | YES  |     | NULL    |       |
 | custInfoLastName  | varchar(50) | YES  |     | NULL    |       |
 | custInfoAddr1     | varchar(50) | YES  |     | NULL    |       |
 | custInfoAddr2     | varchar(50) | YES  |     | NULL    |       |
 | custInfoCityName  | varchar(50) | YES  |     | NULL    |       |
 | custInfoState     | varchar(10) | YES  |     | NULL    |       |
 | custInfoZipCode   | varchar(10) | YES  |     | NULL    |       |
 | custInfoPhone     | varchar(12) | YES  |     | NULL    |       |
 +-------------------+-------------+------+-----+---------+-------+

Constraints 
-----------
rules that need to apply to the table. 


MariaDB Oracal fork of mysql
============================
Install on Centos 7
-------------------

https://downloads.mariadb.org/mariadb/repositories/#mirror=babylon-ca&distro=CentOS&distro_release=centos7-amd64--centos7&version=5.5

cd /etc/yum.repos.d/
vim MariaDB.repo (Copy and paste the info from the page.)

sudo yum update
sudo yum install MariaDB-server MariaDB-client


