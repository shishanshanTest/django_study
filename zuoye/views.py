from django.db.models import Sum, Avg
from django.db import connection
from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from .models import Teacher, Student, Score, Course


def zuoye(requests):
    return HttpResponse('这是作业的首页')


"""
查询平均成绩大于60分的同学的id和平均成绩；

查询所有同学的id、姓名、选课的数量、总成绩；

查询姓“李”的老师的个数；

查询没学过“李老师”课的同学的id、姓名；

查询学过课程id为1和2的所有同学的id、姓名；

查询学过“黄老师”所教的“所有课”的同学的id、姓名；

查询所有课程成绩小于60分的同学的id和姓名；

查询没有学全所有课的同学的id、姓名；

查询所有学生的姓名、平均分，并且按照平均分从高到低排序；

查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分；

查询没门课程的平均成绩，按照平均成绩进行排序；

统计总共有多少女生，多少男生；

将“黄老师”的每一门课程都在原来的基础之上加5分；

查询两门以上不及格的同学的id、姓名、以及不及格课程数；

查询每门课的选课人数；
"""


# 查询平均成绩大于60分的同学的id和平均成绩；
def index(request):
    results = Score.objects.values('student_id').annotate(score_avg=Avg('number')).filter(number__gte=60)
    for result in results:
        print(result)
        print(type(result))

    print(connection.queries)
    return HttpResponse('index')


# 查询所有同学的id、姓名、选课的数量、总成绩；
def index1(request):
    result = Student.objects.select_related('score')
    return HttpResponse('index1')
