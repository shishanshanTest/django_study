from django.db.models import Sum, Avg, Count, Q, F, Max, Min
from django.db import connection
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
from django.http.response import HttpResponse
from django.views import View

from .models import Teacher, Student, Score, Course


def zuoye(requests):
    return render(requests, 'zuoye.html')


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
    students = Student.objects.annotate(score_avg=Avg('score__number')).filter(score_avg__gt=60).values('id',
                                                                                                        'score_avg')
    for student in students:
        print(student)
    return HttpResponse('index')


# 查询所有同学的id、姓名、选课的数量、总成绩；
def index1(request):
    students = Student.objects.annotate(score_num=Count('score__course_id'), score_sum=Sum('score__number')).values(
        'id', 'name', 'score_num', 'score_sum')
    for student in students:
        print(student)
    return HttpResponse('index1')


# 查询姓“李”的老师的个数；
def index2(request):
    # teachers = Teacher.objects.filter(name__contains='李') # 包含“李”字的
    teachers = Teacher.objects.filter(name__startswith='李')  # 以“李”开头的
    for teacher in teachers:
        print(teacher.id, teacher.name)
    print(connection.queries[-1])
    return HttpResponse('index2')


# 查询没学过“李老师”课的同学的id、姓名；
def index3(request):
    # 自己
    # teachers = Teacher.objects.filter(name='李老师').values('id')
    # print(type(teachers))  # <class 'django.db.models.query.QuerySet'>
    # students = Student.objects.exclude(score__course__teacher_id__in=teachers)
    # exclude 排除满足条件的数据，返回一个新的queryset

    # 老师
    students = Student.objects.exclude(score__course__teacher__name='李老师').values('id', 'name')
    # 可以通过下划线一直联表
    for student in students:
        print(student)
    for sql in connection.queries:
        print(sql)
        print('*' * 30)
    return HttpResponse('index3')


# 查询学过课程id为1和2的所有同学的id、姓名；
def index4(request):
    # students = Student.objects.filter(score__course_id__in=[1, 2]).values('id','name')
    students = Student.objects.filter(score__course_id__in=[1, 2]).values('id', 'name').distinct()
    for student in students:
        print(student)
    print(connection.queries[-1])
    return HttpResponse('index4')


# 查询学过“黄老师”所教的“所有课”的同学的id、姓名；
def index5(request):
    # teacher = Teacher.objects.filter(name='黄老师').values('id')
    # students = Student.objects.filter(score__course__teacher_id__in=teacher).values('id', 'name').distinct()
    # for student in students:
    #     print(student)

    students = Student.objects.filter(score__course__teacher__name='黄老师').values('id', 'name').distinct()
    for student in students:
        print(student)

    for sql in connection.queries:
        print(sql)
        print('*' * 30)
    return HttpResponse('index5')


# 查询所有课程成绩小于60分的同学的id和姓名；
def index6(request):
    students = Student.objects.filter(score__number__lt=60).values('id', 'name', 'score__course_id')
    for student in students:
        print(student)
    print(connection.queries[-1])
    return HttpResponse('index6')


# 查询没有学全所有课的同学的id、姓名；
def index7(request):
    # teacher_count = Teacher.objects.annotate(teacher_count=Count('teacher_id')).values('teacher_count')
    course_count = Course.objects.count()
    print(course_count, type(course_count))
    students = Student.objects.annotate(course_count=Count('score__course_id')).exclude(
        course_count=course_count).values('id', 'name')
    for student in students:
        print(student)
    print(connection.queries[-1])
    return HttpResponse('index7')


# 查询所有学生的姓名、平均分，并且按照平均分从高到低排序；
def index8(request):
    students = Student.objects.annotate(score_avg=Avg('score__number')).values('id', 'score_avg').order_by('-score_avg')
    for student in students:
        print(student)
    for sql in connection.queries:
        print(sql)
        print('*' * 30)
    return HttpResponse('index8')


# 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分；
def index9(request):
    courses = Course.objects.annotate(max_number=Max('score__number'), min_number=Min('score__number')).values('id',
                                                                                                               'name',
                                                                                                               'max_number',
                                                                                                               'min_number')
    for course in courses:
        print(course)
    return HttpResponse('index9')


# 查询每门课程的平均成绩，按照平均成绩进行排序；
def index10(request):
    coureses = Course.objects.annotate(course_avg=Avg('score__number')).order_by('course_avg')
    for courese in coureses:
        print(courese.course_avg)
    for sql in connection.queries:
        print(sql)
        print('*' * 30)
    return HttpResponse('index10')


# 统计总共有多少女生，多少男生；
def index11(request):
    # max_num = Student.objects.filter(gendet=1).count()
    # nv_num = Student.objects.filter(gendet=2).count()
    # print(max_num, nv_num)

    rows = Student.objects.aggregate(nan_num=Count('gendet', filter=Q(gendet=1)),
                                     nv_num=Count('gendet', filter=Q(gendet=2)))
    print(rows)
    for sql in connection.queries:
        print(sql)
        print('*' * 30)
    return HttpResponse('index11')


# 将“黄老师”的每一门课程都在原来的基础之上加5分；
def index12(request):
    # 自己
    # course_ids = Course.objects.filter(teacher__name='黄老师').values('id')
    # Score.objects.filter(course_id__in=course_ids).update(number=F('number') + 5)

    # 老师
    Score.objects.filter(course__teacher__name="黄老师").update(number=F('number') + 5)
    return HttpResponse('index12')


# 查询两门以上不及格的同学的id、姓名、以及不及格课程数；
def index13(request):
    students1 = Student.objects.filter(score__number__lt=60).annotate(bjg_num=Count('score__number')).filter(
        bjg_num__gt=2)

    for student in students1:
        print(student.id, student.name, student.bjg_num)
    for sql in connection.queries:
        print(sql)
        print('*' * 30)
    return HttpResponse('index13')


# 查询每门课的选课人数；
def index14(request):
    nums = Course.objects.annotate(num=Count('score__student_id')).values('score__course_id', 'score__course__name',
                                                                          'num')
    for num in nums:
        print(num)
    print(nums)
    for sql in connection.queries:
        print(sql)
        print('*' * 30)

    for key, value in request.META.items():
        print("{}:{}".format(key, value))
    return HttpResponse('index14')


from .forms import MessageBoardForm

# class Message(View):
#     def get(self, request):
#         form = MessageBoardForm()
#         return render(request, 'index.html', {'from': form})
#
#     def post(self, request):
#         message_form = MessageBoardForm(request.POST)
#         if message_form.is_valid():
#             title = message_form.cleaned_data.get('title')
#             content = message_form.cleaned_data.get('content')
#             email = message_form.cleaned_data.get('email')
#             reply = message_form.cleaned_data.get('reply')
#             return render(request, 'index.html', {'from': message_form})
#         else:
#             return HttpResponse('fail')

from django.shortcuts import render, redirect
from django.views import View
from .forms import MessageBoardForm
from .models import Message


class MessageView(View):
    def get(self, request):
        form = MessageBoardForm()
        messages = Message.objects.all()
        return render(request, 'message.html', {'form': form, 'messages': messages})

    def post(self, request):
        message_form = MessageBoardForm(request.POST)
        if message_form.is_valid():
            title = message_form.cleaned_data.get('title')
            content = message_form.cleaned_data.get('content')
            email = message_form.cleaned_data.get('email')
            reply = message_form.cleaned_data.get('reply')
            message = Message(title=title, content=content, email=email, reply=reply)
            message.save()
            return redirect('message')
        else:
            return HttpResponse('fail')
