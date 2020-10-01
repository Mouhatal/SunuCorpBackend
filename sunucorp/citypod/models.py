from django.db import models

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length =50)
    categoryDescription = models.TextField()
    categoryImg = models.ImageField(upload_to= 'image',null=True, blank=True)
    # categories = models.On(categories)

    def __str__(self):
        return str(self.categoryName) + ''

class SubCategory(models.Model):
    subCategoryName = models.CharField(max_length =50)
    subCategoryDescription = models.TextField()
    subCategoryImg = models.ImageField(upload_to= 'image', null=True, blank=True)
    category = models.ForeignKey(to = Category, related_name='categories', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.subCategoryName) + ''

class Element(models.Model):
    elementName= models.CharField(max_length =50)
    elementDescription = models.TextField()
    elementImg = models.ImageField(upload_to= 'image', null=True, blank=True)
    subCategory = models.ForeignKey(to = SubCategory, related_name='subcategories', on_delete=models.CASCADE, blank=True, null=True)
    categoryElement = models.ForeignKey(to = Category, related_name='category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.elementName) + ''

class Page(models.Model):
    pageName= models.CharField(max_length =50)
    pageDescription = models.TextField()
    pageFile = models.FileField(upload_to= 'image', blank=True, null=True)
    element = models.ForeignKey(to = Element, related_name='element', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.pageName) + ''