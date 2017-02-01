Commands
========
Delete something:

mysql -p
SHOW DATABASES;
CREATE DATABASE dbtest;
USE DATABASE dbCustomerInfo;
CREATE TABLE tblCustomerInfo(custInfoFirstName varchar(50), custInfoLastName varchar(50), custInfoAddr1 varchar(50), custInfoAddr2 varchar(50), custInfoCityName varchar(50), custInfoState varchar(10), custInfoZipCode varchar(10),custInfoPhone varchar(12));
```
CREATE TABLE tblCustomerIDInfo(custID varchar(10) PRIMARY KEY, custInfoFirstName varchar(50), custInfoLastName varchar(50), custInfoAddr1 varchar(50), custInfoAddr2 varchar(50), custInfoCityName varchar(50), custInfoState varchar(10), custInfoZipCode varchar(10),custInfoPhone varchar(12));
```
```
SHOW FIELDS FROM tblCustomerInfo;
mysql> SHOW FIELDS FROM tblCustomerIDInfo;
```

``` 
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
```
Constraints 
-----------
- rules that need to apply to the table. 


MariaDB Oracal fork of mysql
============================

Install on Centos 7
-------------------

https://downloads.mariadb.org/mariadb/repositories/#mirror=babylon-ca&distro=CentOS&distro_release=centos7-amd64--centos7&version=5.5
```
cd /etc/yum.repos.d/
vim MariaDB.repo (Copy and paste the info from the page.)

sudo yum update
sudo yum install MariaDB-server MariaDB-client
```
Insert Into
===========
```
NSERT  INTO tblCustomerInfo(custInfoFirstName, custInfoLastName,custInfoAddr1,custInfoAddr2,custInfoCityName,custInfoState,custInfoZipCode,custInfoPhone) VALUES ('Sean', 'Mace', '121 Main Street', '', 'Any town', 'NY', '43211', '2123445333');

SELECT * FROM tblCustomerInfo;

CREATE TABLE tblCustomerInfoBkup(custInfoFirstName varchar(50), custInfoLastName varchar(50), custInfoAddr1 varchar(50), custInfoAddr2 varchar(50) , custInfoCityName varchar(50), custInfoState varchar(10), custInfoZipCode varchar(10) ,custInfoPhone varchar(12));

INSERT  INTO tblCustomerInfoBkup(custInfoFirstName, custInfo
LastName,custInfoAddr1,custInfoAddr2,custInfoCityName,custInfoState,custInfoZipCode,custInfoPhone) VALUES ('John', 'Jonson', '111 Main Street', '', 'Any town', 'NY', '43211 ', '2123445544')
INSERT INTO tblCustomerInforBkup SELECT * FROM tblCustomerInfo;
```

SELECT FROM
===========
```
SELECT custInfoCityName, custInfoState FROM tblCustomerInfo;

MariaDB [dbCustomerInfo]> SELECT custInfoLastName FROM tblCustomerInfo WHERE custInfoState='NY';

MariaDB [dbCustomerInfo]> SELECT custInfoLastName FROM tblCustomerInfo where custInfoLastName<>'Smith';
+------------------+
| custInfoLastName |
+------------------+
| Mace             |
+------------------+
1 row in set (0.00 sec)
```

Alter Table
===========
```
-Add or drop table stuff
ALTER TABLE tblCustomerInfoBkup ADD custInfoDOB varchar(10);

ALTER TABLE tblCustomerInfoBkup ALTER COLUMN custInfoDOB year;

MariaDB [dbCustomerInfo]> ALTER TABLE tblCustomerInfoBkup ALTER COLUMN custInfoDOB year;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'year' at line 1
MariaDB [dbCustomerInfo]> 

ALTER TABLE tblCustomerInfoBkup MODIFY COLUMN custInfoDOB year;
```
DELETE FROM
===========
```
DELETE FROM tblCustomerInfoBkup WHERE custInfoLastName<>'Smith';
DELETE FROM tblCustomerInfoBkup WHERE custInfoLastName<>'Smith' AND custInfoLastName='mace';
```

CREATE INDEX
============
When you want to find information more efficently.
Updateing will take more time to update.

ONLY on colums that will be searched often.
```
CREATE INDEX indexCustInfoID ON tblCustomerIDInfo (custID);
CREATE INDEX indexCustInfoNames ON tblCustomerIDInfo (custInfoFirstName,custInfoLastName);
```
DROP TABLE
==========

TRUNCATE
========
Removing the data from the table.

Auto Increment
==============
```
MariaDB [dbCustomerInfo]> CREATE TABLE tblEmpInfo(empID int PRIMARY KEY AUTO_INCREMENT, empLastName varchar(50), empSSN varchar(11));
Query OK, 0 rows affected (0.01 sec)

MariaDB [dbCustomerInfo]> SHOW FIELDS FROM tblEmpInfo;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| empID       | int(11)     | NO   | PRI | NULL    | auto_increment |
| empLastName | varchar(50) | YES  |     | NULL    |                |
| empSSN      | varchar(11) | YES  |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
3 rows in set (0.01 sec)

MariaDB [dbCustomerInfo]> INSERT INTO tblEmpInfo (empLastName, empSSN) VALUES ('Smith', '11111111111');
Query OK, 1 row affected (0.01 sec)

MariaDB [dbCustomerInfo]> SELECT * FROM tblEmpInfo;
+-------+-------------+-------------+
| empID | empLastName | empSSN      |
+-------+-------------+-------------+
|     1 | Smith       | 11111111111 |
|     2 | Jones       | 22222222222 |
+-------+-------------+-----------

MariaDB [dbCustomerInfo]> ALTER TABLE tblEmpInfo AUTO_INCREMENT=1000;
Query OK, 2 rows affected (0.02 sec)               
Records: 2  Duplicates: 0  Warnings: 0

MariaDB [dbCustomerInfo]> INSERT INTO tblEmpInfo (empLastName, empSSN) VALUES ('Jonson', '33333333333');                                                                    
Query OK, 1 row affected (0.01 sec)

MariaDB [dbCustomerInfo]> INSERT INTO tblEmpInfo (empLastName, empSSN) VALUES ('son', '33111333333');                                                                       
Query OK, 1 row affected (0.00 sec)

MariaDB [dbCustomerInfo]> SELECT * FROM tblEmpInfo;  
+-------+-------------+-------------+
| empID | empLastName | empSSN      |
+-------+-------------+-------------+
|     1 | Smith       | 11111111111 |
|     2 | Jones       | 22222222222 |
|  1000 | Jonson      | 33333333333 |
|  1001 | son         | 33111333333 |
+-------+-------------+-------------+
4 rows in set (0.00 sec)

TRUNCATE TABLE tblCustomerInfoBkup;

MariaDB [dbCustomerInfo]> ALTER TABLE tblCustomerIDInfo MODIFY custID int AUTO_INCREMENT;
Query OK, 0 rows affected (0.02 sec)               
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [dbCustomerInfo]> SHOW FIELDS FROM tblCustomerIDInfo;
+-------------------+-------------+------+-----+---------+----------------+
| Field             | Type        | Null | Key | Default | Extra          |
+-------------------+-------------+------+-----+---------+----------------+
| custID            | int(11)     | NO   | PRI | NULL    | auto_increment |
| custInfoFirstName | varchar(50) | YES  | MUL | NULL    |                |
| custInfoLastName  | varchar(50) | YES  |     | NULL    |                |
| custInfoAddr1     | varchar(50) | YES  |     | NULL    |                |
| custInfoAddr2     | varchar(50) | YES  |     | NULL    |                |
| custInfoCityName  | varchar(50) | YES  |     | NULL    |                |
| custInfoState     | varchar(10) | YES  |     | NULL    |                |
| custInfoZipCode   | varchar(10) | YES  |     | NULL    |                |
| custInfoPhone     | varchar(12) | YES  |     | NULL    |                |
+-------------------+-------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

MariaDB [dbCustomerInfo]> 

```
