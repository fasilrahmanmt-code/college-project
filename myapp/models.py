from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_table(models.Model):
    LOGIN =models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=200)
    image=models.FileField()
    proof=models.FileField()

class college_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    status=models.CharField(max_length=50,default="pending")
    proof = models.FileField()

class notification_table(models.Model):
    Notification = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    Date=models.DateField()

class department_table(models.Model):
    department = models.CharField(max_length=200)
    details = models.CharField(max_length=200)

class course_table(models.Model):
    department_id = models.ForeignKey(department_table, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    details = models.TextField()
    fee = models.FloatField()

class course_request_table (models.Model):
    COLLEGE= models.ForeignKey(college_table,on_delete=models.CASCADE)
    COURSE = models.ForeignKey(course_table, on_delete=models.CASCADE)
    Date=models.DateField()
    status= models.CharField(max_length=200)

class data_set_table(models.Model):
    COURSE_REQ =models.ForeignKey(course_request_table,on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

class complaint_table(models.Model):
    USERID= models.ForeignKey(user_table, on_delete=models.CASCADE)
    complaint= models.CharField(max_length=200)
    Date = models.DateField()
    reply= models.CharField(max_length=200)

class article_table(models.Model):
    article_title = models.CharField(max_length=200)
    article_subject= models.CharField(max_length=200)
    Date = models.DateField()

class chatbot_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    Date = models.DateField()

class last_admission_table(models.Model):
    COLLEGE = models.ForeignKey(college_table, on_delete=models.CASCADE)
    COURSE_REQUEST=models.ForeignKey(course_request_table, on_delete=models.CASCADE)
    year=models.IntegerField()
    mark_starting=models.FloatField()
    mark_ending=models.FloatField()
    Date = models.DateField()

class chat_bot_result_table(models.Model):
    CHATBOT= models.ForeignKey(chatbot_table, on_delete=models.CASCADE)
    result = models.CharField(max_length=200)

class suggestion_table(models.Model):
    STUDENT_ID= models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion= models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    Date = models.DateField()

class scholership_table_new(models.Model):
    Name = models.CharField(max_length=200)
    Details = models.CharField(max_length=200)
    Date = models.DateField()
    Documents= models.FileField()


class job(models.Model):
    job_title = models.CharField(max_length=75)
    company = models.CharField(max_length=75)
    qualification = models.CharField(max_length=75)
    start_date = models.DateField()
    last_date = models.DateField()
    position = models.CharField(max_length=75)
    no_vacancy = models.IntegerField()
    link=models.TextField()


# scholership_table
# college course








