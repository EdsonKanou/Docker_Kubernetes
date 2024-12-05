from django.db import models

class Category (models.Model):
    nom = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_add']  #pour les classer par ordre de creation
# Create your models here.  
    def __str__(self):
        return self.nom


class Product(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.IntegerField()
    description = models.TextField()
    #on_delete=models.CASCADE : pour dire que si on supprime ca n'affecte pas l'autre 
    category = models.ForeignKey(Category, related_name="categorie", on_delete=models.CASCADE) 
    img = models.ImageField(upload_to='photos', verbose_name='My Photo', blank=True)
    image=models.CharField(max_length=5000)
    date_add=models.DateTimeField(auto_now=True)

    class Meta:
        ordering =["-date_add"]

    def __str__(self):
        return self.titre