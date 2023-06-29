from django.db import models

# Create your models here.
# class Orders(models.Model):
   
#     name = models.CharField(max_length=100)
                            
#     email = models.EmailField(max_length=254)
#     phone_number = models.IntegerField()
#     description = models.CharField(max_length=250)
    
#     member = models.BooleanField()

#     def _str_(self):
#         return self.name
class Orders(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    description = models.CharField(max_length=250)
    def _str_(self):
        return self.name
    
class regForm(models.Model):
    firstname=models.CharField(max_length=100)
    # lastname=models.CharField(max_length=100)
    branchname=models.CharField(max_length=100)
    emailid = models.EmailField(max_length=254)
    phonenumber = models.IntegerField(null=True)
    def _str_(self):
        return self.name

    
