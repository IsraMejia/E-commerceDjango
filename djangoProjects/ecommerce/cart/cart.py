
class Cart():

    def __init__(self, request):
        self.session = request.session
        #Returning user - obtain his existing session
        cart = self.session.get('session_key')
       
        if 'session_key' not in request.session :
            cart = self.session['session'] = {} #New user - Create a new session for the user

        self.cart = cart #save the session of the car to hava access in any part of our page   
        