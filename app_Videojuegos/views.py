from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, Venta
from django.http import HttpResponse

# Vista de inicio
def inicio_videojuegos(request):
    return render(request, 'cliente/inicio.html')

# Agregar Cliente
def agregar_cliente(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        empleado_id = request.POST.get('empleado_asignado')
        producto_interes = request.POST.get('producto_interes')
        imagen = request.FILES.get('imagen')

        empleado_obj = None
        if empleado_id:
            try:
                empleado_obj = Empleado.objects.get(id=empleado_id)
            except Empleado.DoesNotExist:
                empleado_obj = None

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion,
            empleado_asignado=empleado_obj,
            producto_interes=producto_interes,
            imagen=imagen
        )
        return redirect('ver_clientes')

    return render(request, 'cliente/agregar_cliente.html', {'empleados': empleados})

# Ver Clientes
def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

# Actualizar Cliente
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        empleado_id = request.POST.get('empleado_asignado')
        cliente.producto_interes = request.POST.get('producto_interes')
        imagen = request.FILES.get('imagen')

        if empleado_id:
            try:
                cliente.empleado_asignado = Empleado.objects.get(id=empleado_id)
            except Empleado.DoesNotExist:
                cliente.empleado_asignado = None
        else:
            cliente.empleado_asignado = None

        if imagen:
            cliente.imagen = imagen

        cliente.save()
        return redirect('ver_clientes')

    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente, 'empleados': empleados})

# Borrar Cliente
def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})
