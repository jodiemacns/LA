AWS concepts
============

Understanding AWS
-----------------
- High level concepts

What is a cloud?  What is Amazon Web Services?
- Think it as a computer somewhere else.
- Useing there resourses.. like a big data center. 
- AWS is IAAS Cloud service provider.
 
Why do people use it.
---------------------
Backups
Sharing - other people / other device

Concepts
--------
1. High availibilty - Get it any where with a network connected.
2. Fault tolerent   - Backed up on multiple services.
		   - Your harddrive could fail.
3. Scalability  - As users grow, you can scale up
4. Elasticity   - You can also quicky srink on demand

Enterprise Usage:
-----------------
On-Premise servers 
Growth of 1000 users to 5000 users for example may need to double the servers.. 3-6 
- Overhead for maintaing and buying new servers.
- Maybe they over shoot the estimates.. they may waste money on buying servers.
-- Using the cloud the ramping up can be done in minutes.
-- Pricing can be done on demand basis.

--------------------------------------------------

1. Scalability  - As users grow, you can scale up
2. Elasticity   - You can also quicky srink on demand


Going to look at:
AWS 
VPC
EC2
RDS

How does Netflix use these services.

VPCS
----
Virtual private cloud (Your space)

Private section of aws where you can allow / restrict access to the resources.

FaceBook 

+-------------+     +-------------+  +-------------+   
| Homepage(Me)|     | Their HP    |  | Other HP    |
|             |     |             |  |             |
| Post        |     | Post        |  | Post        |
| Photos      |     | Photos      |  | Photos      |
| Videos      |     | Videos      |  | Videos      |
+-------------+     +-------------+  +-------------+

AWS

+-------------+     +-------------+  +-------------+   
| Homepage(Me)|     | Their       |  | Other       |
|             |     |             |  |             |
| EC2         |     | EC2         |  | EC2         |
| RDS         |     | RDS         |  | RDS         |
+-------------+     +-------------+  +-------------+


EC2
---

Virtual computer used how you want it to be.

RDS
---
Data Base 
- storing customer account information.

S3 
--
Unlimited Storage bucket
(Outside of VPC)
Long term storage of data.




