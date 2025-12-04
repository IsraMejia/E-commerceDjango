from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404

def store(request):
    all_products = Product.objects.all()
    context = {'my_products': all_products}
    return render(request , 'store/store.html' ,  context )

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def list_category(request , category_slug = None ):                # Define la función de vista. Acepta la petición (request) y el slug de la categoría (category_slug). 
    category = get_object_or_404(Category, slug = category_slug)    # Busca un objeto Category con el slug coincidente. Si no lo encuentra, lanza un error 404.
    products = Product.objects.filter(category = category)          # Filtra el Modelo Product para obtener todos los productos que pertenecen a la 'category' obtenida en la línea anterior.
    
    return render(request, 'store/list-category.html', { 'category' : category, 'products': products })    # Renderiza la plantilla HTML, pasando la 'category' y la lista de 'products' (ambos como diccionario 'context') a la plantilla.

def product_info(request, product_slug):
    product = get_object_or_404(Product, slug = product_slug) #trae los datos del producto que tiene el mismo slug en la base de datos
    context = {'product': product} #Dictionary that defines how we can reach the object of the product, to the HTML
    return render(request, 'store/product-info.html', context)