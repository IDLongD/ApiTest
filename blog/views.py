#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import apilist
from blog.models import apicase
from blog.models import *
from django import forms
from django.shortcuts import render_to_response
import urllib2,time,re
from django.shortcuts import render

def blog(request):
    return render_to_response("index.html")

def project(request):
    return render_to_response("project.html")

def result(request):
    return render_to_response("result.html")

#接口列表
def api_list(requests):
    t = loader.get_template("api_list.html")
    apiList = apilist.objects.all().order_by("id")
    #apiList = {"id":1,"ApiName":"a","ApiUrl":"aa","ApiNotes":"aaa"}
    c = Context({ "apiList": apiList })
    return  HttpResponse(t.render(c))

#删除接口、
def delete_api(requests,id):
    t = loader.get_template("success.html")
    name = apilist.objects.get(id = id).name
    s = apilist.objects.get(id = id)
    s.delete()
    c = Context({ "name": name ,"jieguo":"接口删除成功"})
    return  HttpResponse(t.render(c))


#用例列表
def api_case(request):
    t = loader.get_template("api_case.html")
    apiCase = apicase.objects.all().order_by("id")
    c = Context({ "apiCase": apiCase })
    return  HttpResponse(t.render(c))

#删除用例
def delete_case(requests,id):
    t = loader.get_template("success.html")
    name = apicase.objects.get(id = id).name
    s = apicase.objects.get(id = id)
    s.delete()
    c = Context({ "name": name ,"jieguo":"用例删除成功"})
    return  HttpResponse(t.render(c))


class AddForm(forms.Form):
    name = forms.CharField(label = "接口名称" , max_length = 50)
    url = forms.URLField(label = "接口连接" , max_length = 200)
    notes = forms.CharField(label = "接口备注")

#新增接口
def addapi(request):
    if request.method == "POST":
        uf = AddForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            name = uf.cleaned_data['name']
            url = uf.cleaned_data['url']
            notes = uf.cleaned_data['notes']
            #将表单写入数据库
            api = apilist()
            api.name = name
            api.url = url
            api.notes = notes
            api.save()
            #返回新增成功页面
            return render_to_response('success.html',{'name':name})
    else:
        uf = AddForm()
    return render_to_response('addapi.html',{'uf':uf})


class AddCaseForm(forms.Form):
    apiname = forms.CharField(label = "接口名称" ,max_length = 50)
    apiurl = forms.URLField(label = "接口链接" )
    name = forms.CharField(label = "用例名称" ,max_length = 50)
    mothed = forms.CharField(label = "请求方法" ,max_length = 20)
    data = forms.CharField(label = "请求数据" )
    check = forms.CharField(label = "检查点" ,max_length = 100)
    notes = forms.CharField(label = "备注" )

#新增用例
def addcase(request):
    if request.method == "POST":
        uf = AddCaseForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            apiname = uf.cleaned_data['apiname']
            apiurl = uf.cleaned_data['apiurl']
            name = uf.cleaned_data['name']
            mothed = uf.cleaned_data['mothed']
            data = uf.cleaned_data['data']
            check = uf.cleaned_data['check']
            notes = uf.cleaned_data['notes']
            #将表单写入数据库
            case = apicase()
            case.apiname = apiname
            case.apiurl = apiurl
            case.mothed = mothed
            case.data = data
            case.check = check
            case.notes = notes
            case.name = name
            case.save()
            #返回新增成功页面
            return render_to_response('success.html',{'name':name})
    else:
        uf = AddCaseForm()
    return render_to_response('addcase.html',{'uf':uf})


def apitest(request):
    t = loader.get_template("result.html")
    url = apicase.objects.get(id = 4).apiurl
    check = apicase.objects.get(id = 4).check
    data = apicase.objects.get(id = 4).data
    url = url + "?" + data
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    code = r.getcode()
    result = r.read()
    #c = Context({"check":check,"url":url,"code":code,"result":result})

    if re.search(check,result):
        c = Context({"url":url,"code":code,"result":"pass"})
        return  HttpResponse(t.render(c))
    else:
        c = Context({"check":check,"url":url,"code":code,"result":result})
        return  HttpResponse(t.render(c))


def apiget(request,id):
    apicase = apicase.objects.get( id = 4)
    return {"url": apicase.apiurl,"check":apicase.check}
