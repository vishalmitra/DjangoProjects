from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class  fun(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    director =models.CharField(blank=True,max_length=100)
    verdict =models.BooleanField(default=False)
    slug= models.SlugField(default="",blank=True,editable=True ,null=False,db_index=True)
     



    def get_absolute_url(self):
        return reverse("moviedetailspage", args=[self.slug] )


    """def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super().save(*args,**kwargs)
    """

    def __str__(self):
        return f"{self.title} {self.rating} {self.director} {self.verdict}"



class Country(models.Model):
    name= models.CharField(max_length=25)
    code=models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "Countries"


    def __str__(self):
        return f" {self.name}   {self.code}"



class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    postalcode = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural= "Address_of_the_author"


    def __str__(self):
        return f" {self.street} {self.city} {self.postalcode} "


class author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address=models.OneToOneField(Address,on_delete= models.CASCADE,null=True)

    #we created null eqauals to true beacuse we will get clash due to already preasent data  in author fields





    def full_name(self):
        return f"{self.first_name +self.last_name}"


    def __str__(self):
        return self.full_name()


class Books(models.Model):

    title= models.CharField(max_length=50)
    author =models.ForeignKey(author,on_delete=models.CASCADE,related_name="books")
    copies_sold =models.IntegerField(validators=[MinValueValidator(0)])

    published_countries=models.ManyToManyField(Country,null=False)






    def __str__(self):
        return f"{self.title} {self.author} {self.copies_sold} "








    
