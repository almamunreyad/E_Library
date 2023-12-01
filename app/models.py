from django.db import models

# Create your models here.

# for signup and login 
class SignUp(models.Model):
    image = models.FileField(upload_to='media/signup')
    name = models.CharField(max_length=250)
    student_id = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    c_password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=25)
    semester = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True)
    maritalStatus = models.CharField(max_length=150, null=True)
    birth_date = models.DateField(null=True)
    blood_group = models.CharField(max_length=10)
    comment = models.TextField()
    
    
# for about section 
class About(models.Model):
    about_image = models.ImageField(upload_to='media/about')
    about_title = models.CharField(max_length=120)
    about_desc = models.TextField()
    
# for mission section 
class Mission(models.Model):
    mission_image = models.ImageField(upload_to='media/mission')
    mission_title = models.CharField(max_length=120)
    mission_desc = models.TextField()
    
# for teams section 
class Team(models.Model):
    team_image = models.ImageField(upload_to='media/team')
    team_title = models.CharField(max_length=120)
    team_desc = models.TextField()
    

    
# for contact section 
class Contact(models.Model):
    contact_name = models.CharField(max_length=150)
    contact_id = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=80)
    contact_message = models.TextField()
    

# cse category add
class Category_Cse(models.Model):
    cse_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cse_category
    
class Category_Eee(models.Model):
    eee_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.eee_category
 
class Category_Eng(models.Model):
    eng_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.eng_category
 
class Category_Bba(models.Model):
    bba_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.bba_category
 
class Category_Law(models.Model):
    law_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.law_category
 
class Category_Civil(models.Model):
    civil_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.civil_category
 
class Category_Pharmacy(models.Model):
    pharmacy_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.pharmacy_category
 



class Cse(models.Model):
    cse_img = models.ImageField(upload_to='media/cse/')
    cse_category = models.ForeignKey(Category_Cse, on_delete= models.CASCADE, default=1)
    cse_book = models.CharField(max_length=150)
    cse_teacher = models.CharField(max_length=120)
    cse_file = models.FileField(upload_to='media/cse/')
    cse_date = models.DateField(null=True)
    
    
class Eee(models.Model):
    eee_img = models.ImageField(upload_to='media/eee/')
    eee_category = models.ForeignKey(Category_Eee, on_delete=models.CASCADE, default=1)
    eee_book = models.CharField(max_length=150)
    eee_teacher = models.CharField(max_length=120)
    eee_file = models.FileField(upload_to='media/eee/')
    eee_date = models.DateField(null=True)
    

class Eng(models.Model):
    eng_img = models.ImageField(upload_to='media/eng/')
    eng_category = models.ForeignKey(Category_Eng, on_delete=models.CASCADE, default=1)
    eng_book = models.CharField(max_length=150)
    eng_teacher = models.CharField(max_length=120)
    eng_file = models.FileField(upload_to='media/eng/')
    eng_date = models.DateField(null=True)
    

class Bba(models.Model):
    bba_img = models.ImageField(upload_to='media/bba/')
    bba_category = models.ForeignKey(Category_Bba, on_delete=models.CASCADE, default=1)
    bba_book = models.CharField(max_length=150)
    bba_teacher = models.CharField(max_length=120)
    bba_file = models.FileField(upload_to='media/bba/')
    bba_date = models.DateField(null=True)
    

class Law(models.Model):
    law_img = models.ImageField(upload_to='media/law/')
    law_category = models.ForeignKey(Category_Law, on_delete=models.CASCADE, default=1)
    law_book = models.CharField(max_length=150)
    law_teacher = models.CharField(max_length=120)
    law_file = models.FileField(upload_to='media/law/')
    law_date = models.DateField(null=True)
    
    
class Civil(models.Model):
    civil_img = models.ImageField(upload_to='media/civil/')
    civil_category = models.ForeignKey(Category_Civil, on_delete=models.CASCADE, default=1)
    civil_book = models.CharField(max_length=150)
    civil_teacher = models.CharField(max_length=120)
    civil_file = models.FileField(upload_to='media/civil/')
    civil_date = models.DateField(null=True)
    
    
class Pharmacy(models.Model):
    pharmacy_img = models.ImageField(upload_to='media/pharmacy/')
    pharmacy_category = models.ForeignKey(Category_Pharmacy, on_delete=models.CASCADE, default=1)
    pharmacy_book = models.CharField(max_length=150)
    pharmacy_teacher = models.CharField(max_length=120)
    pharmacy_file = models.FileField(upload_to='media/pharmacy/')
    pharmacy_date = models.DateField(null=True)
    
    
    
class Library(models.Model):
    library_img = models.ImageField(upload_to='media/library/')
    library_book = models.CharField(max_length=150)
    library_author = models.CharField(max_length=120)
    library_file = models.FileField(upload_to='media/library/')
    