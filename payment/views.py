from django.shortcuts import render
from cart.cart import Cart
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import uuid # Para generar códigos de juego aleatorios

def checkout(request):
    # Revisar si hay items en el carrito
    cart = Cart(request)
    if cart.__len__() == 0:
        return render(request, 'store/store.html') # O redirigir a tienda si está vacío

    return render(request, 'payment/checkout.html')

def complete_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # 1. Recuperar info del carrito para el correo
        cart = Cart(request)
        total_price = cart.get_total()
        
        # Generamos un código de juego falso (Ej: A1B2-C3D4-E5F6)
        game_code = str(uuid.uuid4()).upper()[:18]

        # 2. Construir el mensaje del correo
        items_list = ""
        for item in cart:
            items_list += f"- {item['product'].title} (${item['product'].price})\n"

        subject = f"Confirmación de Orden Falsa - Dinamita Studios"
        message = f"""
        HOLA {name.upper()},

        **********************************************************
        ESTO ES UNA PRUEBA. NO SE HA REALIZADO NINGÚN CARGO REAL.
        **********************************************************
        **********************************************************
        NO SE ADQUIRIO NINGUN JUEGO O SUSCRIPCION REALMENTE
        **********************************************************

        Gracias por "comprar" en Dinamita Studios.
        
        Resumen de tu pedido ficticio:
        {items_list}
        
        Total "pagado": ${total_price}
        
        TU CÓDIGO DE CANJE (FALSO):
        {game_code}
        
        Disfruta tus juegos imaginarios.
        
        Atte: El equipo de Desarrollo.
        """
        
        # 3. Enviar Correo (Manejamos error por si falla el SMTP para que no rompa la demo)
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error enviando correo simulado: {e}")

        # 4. Limpiar el Carrito
        cart.clear()

        # 5. Responder a AJAX con el código para mostrarlo en la pantalla de éxito
        return JsonResponse({'success': True, 'game_code': game_code})

def payment_success(request):
    # Recuperamos el código si viene por parámetro GET (opcional)
    game_code = request.GET.get('code', 'CODE-XXXX-XXXX')
    return render(request, 'payment/payment-success.html', {'game_code': game_code})

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')