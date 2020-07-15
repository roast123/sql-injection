# sql-injection
This a sql injection automation script,based on an error sql injection.


We need to build PHP environment and target machine by ourselves.
To build PHP environment,i used phpstudy and payed attention to the php version .the newest version cant usege.
To build target machine ,i used sqli-labs.
the following is how to set.
      下载 sqli-labs，这是一个印度程序员编写的用来学习 sql 注入的教程。
      下载地址：https://github.com/Audi-1/sqli-labs，下载后务必将 sql 的版本
      调到 5.5 以上，因为这样你的数据库内才会 information_schema 数据库，方便进行
      实验测试。将之前下载的源码解压到 www 目录下，修改 sql-connections/db-creds.inc 文件当中的 mysql 账号密码。
      Sqli-labs 靶机中 Less1-Less4 是基于报错的 SQL 注入，使用它作为靶机测试程序即可。
      
      在 VMWorkstations 中搭建实验环境，即：MAMP=Windows Server、Apache、
      MySQL 和 PHP，可以使用 Wamp 包搭建 PHP 集成开发环境，安装包是 Wampserver。或
      者使用 phpStudy 软件包，phpStudy 是一个 PHP 调试环境的程序集成包。该程序包集
      成最新的 Apache+PHP+MySQL+phpMyAdmin+ZendOptimizer,一次性安装,无须配置即可
      使用,是非常方便、好用的 PHP 调试环境 。对学习 PHP 的新手来说，环境配置是一件
      很困难的事；对老手来说也是一件烦琐的事。因此无论你是新手还是老手，该程序包
      都是一个不错的选择。
      phpstudy：http://down.php.cn/PhpStudy20180211.zip
      所需安装环境支持包：http://www.pc6.com/softview/SoftView_104246.html
