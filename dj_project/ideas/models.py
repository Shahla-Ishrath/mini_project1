from django.db import models
from django .contrib .auth .models import User

# Create your models here.

project_list=(
    (0,'mini project'),
    (1,'main project'),
    (2,'live project')
)


class Master(models.Model):
    created_user=models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    class Meta:
        abstract=True
    
class course(Master):
    course=models.CharField(max_length=250)
    Active=models.BooleanField() 
    def __str__(self):
        return self.course


class Project_ideas(Master):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    Project_type=models.IntegerField(choices=project_list,null=False,blank=False)
    description=models.TextField()
    project_title=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.Project_ideas


class Technology(Master):
    Technology=models.CharField(max_length=250)
    Active=models.BooleanField() 
    def __str__(self):
        return self.Technology