class Cart():

    def __init__(self, request):
        self.session = request.session

        # get current session key if it exists
        cart = self.session.get('session_key')

        # if user is new no session key, create it

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # cart available on all pages of site
        self.cart = cart

