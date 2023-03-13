from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import reverse, redirect


# Create your views here.

def library(request):
    return HttpResponse('librarys页面')


def library_list(request):
    return HttpResponse('library列表页面')


"""
第一种请求地址：http://127.0.0.1:8000/library/detail/1212
"""


def library_detail_1(request, library_id):
    text = '您查看的library id是%s' % library_id

    return HttpResponse(text)


"""
第二种使用查询字符串方式
url：http://127.0.0.1:8000/library/detail/?library_id=11
"""


def library_detail_2(request):
    library_id = request.GET.get('library_id')
    text = "您要查询的library id 是 {}".format(library_id)
    return HttpResponse(text)


"""
如果需要反转url，那么需要使用到path中的name参数，如果有应用命名空间和实力命名空间，需要加上
应用命名空间：实例命名空间
如果反转的url有参数那么
"""


def library_detail(request):
    "如果没有登录，那么就反转到librarys页面"
    username = request.GET.get('username')
    password = request.GET.get('password')
    library_id = request.GET.get('library_id')
    print("-" * 30)
    print(username, password, library_id)
    print("-" * 30)

    if username:
        if password:
            return HttpResponse('您查询的library id是{}'.format(library_id))
        else:
            return HttpResponse('请您输入密码')
    else:
        return redirect(reverse('library:library_detail_1', kwargs={'library_id': 222}))
