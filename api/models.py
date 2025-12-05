from django.db import models

class Mpikambana(models.Model):
    Anarana = models.CharField(max_length=50, null=True,blank=False)
    Fanampiny = models.CharField(max_length=50, null=True,blank=False)
    Totem = models.CharField(max_length=50, null=True,blank=False)
    Andraikitra = models.CharField(max_length=50, null=True,blank=False)
    
    def __str__(self):
        return self.Anarana
    

class Sampana(models.Model):
    Anarana = models.CharField(max_length=50, null=True,blank=False)
        
    def __str__(self):
        return self.Anarana