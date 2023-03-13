from django.db import models
from datetime import datetime


# Create your models here.
# class library(models.Model):
#     name = models.CharField(max_length=20, null=False)
#     author = models.CharField(max_length=20, null=False)
#     pub_time = models.DateTimeField(default=datetime.now())
#     price = models.FloatField(default=0)
#
#     class Meta:
#         db_table = 'library'


# 出版社

class Publisher(models.Model):
    name = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return "<Publisher object: {} {}>".format(self.id, self.name, self.city)


"""
on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
on_delete=models.SET,         # 删除关联数据,
 a. 与之关联的值设置为指定值,设置：models.SET(值)
 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
"""


class Library(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    memo = models.TextField(null=True)
    # 创建外键,关联Publisher
    Publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "<library object: {} {}>".format(self.id, self.title, self.publish_date, self.price, self.memo,
                                                self.Publisher)

    class Meta:
        db_table = 'library'
        ordering = ['price']


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=11)
    # 创建多对多关联
    librarys = models.ManyToManyField(to='Library')

    def __str__(self):
        return "<Author object: {} {}>".format(self.id, self.name, self.age, self.phone, self.librarys)

    class Meta:
        db_table = 'author'
