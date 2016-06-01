#coding=utf-8
import urllib2,time,re

def apitesting(self):
     #判断请求方式
    if method == 'GET':
        url = url + data
        try:
            result = urllib2.urlopen(url).read()
            result=result.decode('utf-8')
            if re.search(check,result):
                print u"验证成功"
            else:
                print u"Error:验证失败"
                print check,result
        except Exception, e:
            print u"请求出错"
            print e.code
            print e.read()


    if method == 'POST':
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        data = urllib2.quote(str(data))
        req = urllib2.Request(url+data,data,headers)
        #构造一个请求信息，返回的req就是一个构造好的请求
        try:
            response = urllib2.urlopen(req)
            result = response.read()
            if re.search(check,result):
                print u"验证成功"
            else:
                print u"Error:验证失败"
                print check,result

        except Exception, e:
            print u"请求出错"
            print e.code