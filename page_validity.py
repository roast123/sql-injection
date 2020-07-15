import urllib.request
class page_validity:
    def judge(url):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
        tempUrl = url
        try:
            opener.open(tempUrl)
            print(tempUrl + '  页面访问正常')
            return 1
        except urllib.error.HTTPError:
            print(tempUrl + '  页面访问出错,HTTPError')
            return 0
        except urllib.error.URLError:
            print(tempUrl + '  页面访问出错,URLError')
            return 0