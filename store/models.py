from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        # En el admin se verá como 'Categories'
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list-category", args=[self.slug])


class Product(models.Model):
    # Relación con categoría (Ej: Shooter, Terror, Suscripción)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    
    title = models.CharField(max_length=250)
    
    # TRUCO: Usamos 'brand' para la Plataforma (Xbox, PS5, PC) o Desarrolladora.
    # default='General' para que no quede vacío.
    brand = models.CharField(
        max_length=250, 
        default='General',
        verbose_name='Plataforma / Desarrollador' 
    )
    
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product-info", args=[self.slug])