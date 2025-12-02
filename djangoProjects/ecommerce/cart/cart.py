from decimal import Decimal
from store.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        #Returning user - obtain his existing session
        cart = self.session.get('session_key')
       
        if 'session_key' not in request.session :
            cart = self.session['session_key'] = {} #New user - Create a new session for the user

        self.cart = cart #save the session of the car to have access in any part of our page   
    
    def add(self, product, product_qty):
        product_id = str(product.id)
        
        # Lógica para agregar o actualizar
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty 
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
        
        # Marcar la sesión como modificada para que Django la guarde
        self.session.modified = True
         
         
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
            
            
    
    def __len__(self):
        return sum( item['qty'] for item in self.cart.values() )
     
    
    def __iter__(self):
        all_products_ids = self.cart.keys()
        products = Product.objects.filter(id__in = all_products_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)] ['product'] = product 
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty'] #total price in this item cart
            yield item            
            
    
    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
        
    

        