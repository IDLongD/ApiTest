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
    test = forms.ALL_FIELDS
    name = forms.CharField(label = "接口名称" , max_length = 50)
    url = forms.URLField(label = "接口连接" , max_length = 200)
    notes = forms.CharField(label = "接口备注",required=False)

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
            return render_to_response('success.html',{'name':name,"jieguo":" 接口新增成功"})
    else:
        uf = AddForm()
    return render_to_response('addapi.html',{'uf':uf})


class AddCaseForm(forms.Form):
    apiname = forms.ModelChoiceField(label = "接口名称",queryset = apilist.objects.all(),required =True)
    mothed = forms.TypedChoiceField(label = "请求方法" ,choices = (("GET", "GET"), ("POST", "POST")))
    name = forms.CharField(label = "用例名称" ,max_length = 50)
    data = forms.CharField(label = "请求数据" )
    check = forms.CharField(label = "检查点" ,max_length = 100)
    notes = forms.CharField(label = "备注" ,required=False)

#新增用例
def addcase(request):
    if request.method == "POST":
        form = AddCaseForm(request.POST)
        if form.is_valid():
            #获取表单信息
            cd = form.cleaned_data
            case = apicase()
            case.apiname = cd['apiname']
            case.apiurl = apilist.objects.get(name = case.apiname).url
            case.mothed = cd['mothed']
            case.name = cd['name']
            case.data = cd['data']
            case.check = cd['check']
            case.notes = cd['notes']
            #将表单写入数据库
            case.save()
            #返回新增成功页面
            return render_to_response('success.html',{'name':case.name,"jieguo":"用例新增成功"})
    else:
        form = AddCaseForm()
    return render_to_response('addcase.html',{"form":form})

#接口get请求测试
def apitest(request):
    t = loader.get_template("result.html")
    url = apicase.objects.get(id = 5).apiurl
    check = apicase.objects.get(id = 5).check
    data = apicase.objects.get(id = 5).data
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


class AddProjectForm(forms.Form):
    name = forms.CharField(label = "项目名称" ,max_length = 50)
    casej = forms.MultipleChoiceField(label = "选择用例",choices=apicase.objects.values_list("id","name"), widget=forms.CheckboxSelectMultiple())
    notes = forms.CharField(label = "备注" ,required=False)

def addproject(request):
     if request.method == "POST":
        forp = AddProjectForm(request.POST)
        if forp.is_valid():
            #获取表单信息
            cd = forp.cleaned_data
            pro = project()
            pro.name = cd['name']
            pro.casej = cd['casej']
            pro.notes = cd['notes']
            #将表单写入数据库
            pro.save()
            #返回新增成功页面
            return render_to_response('success.html',{'name':pro.name,"jieguo":"项目新建成功"})
     else:
        forp = AddProjectForm()
     return render_to_response('project.html',{"forp":forp})

#项目列表
def project_list(requests):
    t = loader.get_template("project_list.html")
    projectList = project.objects.all().order_by("id")
    #apiList = {"id":1,"ApiName":"a","ApiUrl":"aa","ApiNotes":"aaa"}
    c = Context({ "projectList": projectList })
    return  HttpResponse(t.render(c))

def goproject(requests,id):
    t = loader.get_template("project_result.html")
    casej = project.objects.get(id = id).casej
    #数据库信息显示的是 casej = [u'17', u'18']
    coo = []
    for cs in eval(casej):
        case = apicase.objects.get(id = cs)
        url = case.apiurl
        check = case.check
        data = case.data
        url = url + "?" + data
        req = urllib2.Request(url)
        r = urllib2.urlopen(req)
        code = r.getcode()
        result = r.read()
        #c = Context({"check":check,"url":url,"code":code,"result":result})
        if re.search(check,result):
            i = {"check":check,"url":url,"code":code,"result":"pass"}
            coo.append(i)
        else:
            i = {"check":check,"url":url,"code":code,"result":"pass"}
            coo.append(i)
        time.sleep(0.2)
    c = Context({"coo":coo})
    return  HttpResponse(t.render(c))