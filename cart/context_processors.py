from .cart import Cart


def cart(request):
    # context processor crt works on all pages of site
    return {'cart': Cart(request)}
