
class Cart():

    def __init__(self, request):
        self.session = request.session
        #Returning user - obtain his existing session
        cart = self.session.get('session_key')
       
        if 'session_key' not in request.session :
            cart = self.session['session'] = {} #New user - Create a new session for the user

        self.cart = cart #save the session of the car to have access in any part of our page   
    
    def add(self, product, product_quantity):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['product_quantity'] = product_quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_quantity}
            
        self.session.modified = True 
        