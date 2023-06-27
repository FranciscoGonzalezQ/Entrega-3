def total_carrito (request):
    total = 0
    if request.user.is_authenticated:
        if request.session['carrito']:
            for key, in request.session['carrito'].items(): 
                total += int(key["acumulado"])
                
    return {"total_carrito":total}