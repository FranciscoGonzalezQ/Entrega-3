class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session('carrito')
        if not carrito:
            self.session['carrito'] = []
            self.carrito = self.session['carrito']
        else:
            self.carrito = carrito
            
    def agregar(self, producto): 
        sku = str(producto.id)  
        if sku in self.carrito.keys():
            self.carrito[sku] ={
            'producto_id': producto.id,
            'nombre': producto.nombre,
            'acumulado': producto.precio,
            'cantidad': 1
            }
        else:
            self.carrito[sku]["cantidad"] +=1
            self.carrito[sku]["acumulado"] += producto.precio  
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
        
    def eliminar(self, producto):
        sku = str(producto.id)  
        if sku in self.carrito():
            del self.carrito[sku]
            self.guardar_carrito()
            
    def restar(self, producto):
        sku = str(producto.id)  
        if sku in self.carrito.keys():
            self.carrito[sku]["cantidad"] -=1
            self.carrito[sku]["acumulado"] -= producto.precio
            if self.carrito[sku]["cantidad"] == 0: self.eliminar(producto)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session['carrito'] = []
        self.session.modified = True