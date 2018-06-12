from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
class School(models.Model):
    school_name = models.CharField(max_length=200,unique=True)
    address = models.TextField()
    max_grade = models.IntegerField()

    def __str__(self):
        return self.school_name
class Profile(models.Model):
    roles = (
        ("admin","admin"),
        ("teacher","teacher")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    role = models.CharField(max_length=50,choices=roles)

    def __str__(self):
        return self.user.username
@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance,school=School.objects.get(id=1))
    instance.profile.save()


class Grade(models.Model):
    grade_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.grade_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=10)
    grade = models.ForeignKey(Grade,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.subject_name 

class Chapter(models.Model):
    ch_name = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE)
    grade = models.ForeignKey(Grade,on_delete = models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return self.ch_name

class Question(models.Model):
    difficulty_choices=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard"),
    )
    type_choices=(
        ("mcq","Mcq"),
        ("short","short answer"),
        ("long","long answer"),
        ("fb","fill in the blanks"),
        ("Tf","true or false"),
        ("Match","match the following")
    )
    question_type = models.CharField(max_length=50, choices=type_choices)
    difficulty = models.CharField(max_length=10, choices=difficulty_choices)
    question_text = models.TextField()
    chapter = models.ForeignKey(Chapter,on_delete = models.CASCADE)
    answer = models.TextField(null=True,blank = True)
    image = models.ImageField(upload_to="question",null=True,blank=True,help_text="200*50 is recommended")
    created_date = models.DateTimeField("created date")
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text
    def save(self,*args,**kwargs):
        if not self.id:
            self.created_date = timezone.now()
        return super(Question,self).save(*args, **kwargs)

class Choice(models.Model):
    choice_text = models.CharField(max_length = 100)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.choice_text
class Match(models.Model):
    question_text = models.CharField(max_length=100)
    answer_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="match",null=True,blank=True)

    def __str__(self):
        return self.question_text    

class Paper(models.Model):
    heading = models.CharField(max_length=100)
    created_date = models.DateTimeField("created date")
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    file_path = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    date = models.CharField(max_length=30)


    def __str__(self):
        return self.heading
    def save(self,*args,**kwargs):
        if not self.id:
            self.created_date = timezone.now()
        return super(Paper,self).save(*args,**kwargs)