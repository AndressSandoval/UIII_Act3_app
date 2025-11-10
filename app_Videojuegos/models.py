from django.db import models
from django.contrib import admin


class Empleado(models.Model):
    imagen = models.ImageField(upload_to='empleados/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    cliente_referido = models.ForeignKey('Cliente', on_delete=models.SET_NULL, blank=True, null=True, related_name='referidos')
    producto_asignado = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, blank=True, null=True, related_name='clientes_asignados')
    producto_interes = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, blank=True, null=True, related_name='ventas_realizadas')
    producto = models.CharField(max_length=200)
    fecha_venta = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=100)
    folio = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Venta {self.folio} - {self.cliente}"


admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Venta)
