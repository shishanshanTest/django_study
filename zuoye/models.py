from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    gendet = models.SmallIntegerField()

    class Meta:
        db_table = 'student'


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "course"


class Score(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    number = models.FloatField()

    class Meta:
        db_table = 'score'


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher'


class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    email = models.EmailField()
    reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
