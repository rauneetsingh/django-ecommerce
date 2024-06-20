from .cart import Cart

# Context Processor so our cart can work on all pages

def cart(request):
	# Return the default data from our Cart
	return {'cart': Cart(request)}