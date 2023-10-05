from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
            return self.name + ' - ' + self.email
        
class Feedback(models.Model):
    name=models.CharField(max_length=122)
    desc=models.TextField()
    
    def __str__(self):
            return 'Feedback From ' + self.name
        
class Full_stack_developer(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    GENDER = (
       ('male', 'Male'),
       ('female', 'Female'), 
       ('others', 'Others'),
       )
    gender=models.CharField(max_length=100,default = "", choices = GENDER)
    Qualification=models.CharField(max_length=50)
    COMPETENCE=(      
        ('fresher','Fresher'),
        ('experienced','Experienced'),
        )
    competence = models.CharField(max_length=100,default = "",choices = COMPETENCE)
    city=models.CharField(max_length=122)
    desc=models.TextField()
    file = models.FileField(max_length=100)
    
    def __str__(self):
            return 'Request From ' + self.name + ' - ' + self.email
        
class UI_UX_Designer(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    GENDER = (
       ('male', 'Male'),
       ('female', 'Female'), 
       ('others', 'Others'),
       )
    gender=models.CharField(max_length=100,default = "", choices = GENDER)
    Qualification=models.CharField(max_length=50)
    COMPETENCE=(      
        ('fresher','Fresher'),
        ('experienced','Experienced'),
        )
    competence = models.CharField(max_length=100,default = "",choices = COMPETENCE)
    city=models.CharField(max_length=122)
    desc=models.TextField()
    file = models.FileField(max_length=100)
    
    def __str__(self):
            return 'Request From ' + self.name + ' - ' + self.email
        
class Front_End_Developer(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    GENDER = (
       ('male', 'Male'),
       ('female', 'Female'), 
       ('others', 'Others'),
       )
    gender=models.CharField(max_length=100,default = "", choices = GENDER)
    Qualification=models.CharField(max_length=50)
    COMPETENCE=(      
        ('fresher','Fresher'),
        ('experienced','Experienced'),
        )
    competence = models.CharField(max_length=100,default = "",choices = COMPETENCE)
    city=models.CharField(max_length=122)
    desc=models.TextField()
    file = models.FileField(max_length=100)
    
    def __str__(self):
            return 'Request From ' + self.name + ' - ' + self.email
        
        
class Technical_Lead(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    GENDER = (
       ('male', 'Male'),
       ('female', 'Female'), 
       ('others', 'Others'),
       )
    gender=models.CharField(max_length=100,default = "", choices = GENDER)
    Qualification=models.CharField(max_length=50)
    COMPETENCE=(      
        ('fresher','Fresher'),
        ('experienced','Experienced'),
        )
    competence = models.CharField(max_length=100,default = "",choices = COMPETENCE)
    city=models.CharField(max_length=122)
    desc=models.TextField()
    file = models.FileField(max_length=100)
    
    def __str__(self):
            return 'Request From ' + self.name + ' - ' + self.email
        
        
class Engineering_Manager(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    GENDER = (
       ('male', 'Male'),
       ('female', 'Female'), 
       ('others', 'Others'),
       )
    gender=models.CharField(max_length=100,default = "", choices = GENDER)
    Qualification=models.CharField(max_length=50)
    COMPETENCE=(      
        ('fresher','Fresher'),
        ('experienced','Experienced'),
        )
    competence = models.CharField(max_length=100,default = "",choices = COMPETENCE)
    city=models.CharField(max_length=122)
    desc=models.TextField()
    file = models.FileField(max_length=100)
    
    def __str__(self):
            return 'Request From ' + self.name + ' - ' + self.email
