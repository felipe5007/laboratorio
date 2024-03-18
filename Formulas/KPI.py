
def ticket_promedio(cliente, ingresos_totales , transacciones_de_venta):
    # El ticket promedio es el  indicador que demuestra el comportamiento de compra de tus clientes. 
    # Te entrega lo que ellos gastan e promedio por compra a tu negocio
    formula = ingresos_totales / transacciones_de_venta
    print (f"El ticket promedio que genera {cliente} es {formula}")
    return formula

def rentabilidad_clientes(cliente, ingresos, costos_gastos):
    #Sirve para calcular la rentabilidad de un cliente en un periodo determinado, contrastando cuánto dinero ingresa por efectos de ese cliente, 
    # contra el gasto que te genera. Con este dato puedes saber quiénes son tus clientes más rentables y cuáles pueden estar generando perdidas en tu negocio. 
    formula = ( ingresos - costos_gastos ) / costos_gastos
    print (f"La rentabilidad que genera {cliente} es {formula}")
    return formula

def margen(cliente, ingresos_totales, costos_gastos_totales):
    # Permite medir cuánto margen porcentual está generando nuestro negocio. 
    # Nos permite saber la magnitud de lo que estamos ganando, en relación a lo que efectivamente nos genera un ingreso. 
    # Es decir, cuánto del dinero que nos ingresa efectivamente es una ganancia. 
    formula = (ingresos_totales - costos_gastos_totales ) / ingresos_totales
    
    print (f"El margen porcentual que genera {cliente} es {formula}")
    return formula

def margen_neto(cliente, ingresos_totales, costos_gastos_totales):
    #Permite medir cuánto margen en $ está generando nuestro negocio. 
    #Finalmente, es tan importante que nos permite saber si realmente estamos ganando o no lo que esperamos. 
    formula = ingresos_totales - costos_gastos_totales
    print (f"El Margen neto que genera {cliente} es {formula}")
    return formula

def tasa_de_retencion_clientes(cliente, clientes_anteriores, clientes_anteriores_return ):
    #Este KPI me sirve para entender  cuántos de los clientes de un periodo determinado vuelven a comprar a mi 
    # negocio en otro periodo posterior. Es decir, mide de cierta forma la fidelidad  que logro generar en mi clientela. 
    formula = clientes_anteriores_return / clientes_anteriores
    print (f"La Tasa de retención que genera {cliente} es {formula}")
    return formula

def tasa_conversion(cliente, cantidad_ventas_totales, cantidad_contactos_posible_clientes):
    # Muestra cómo va nuestro negocio en cuanto a qué parte de los posibles interesados en ser nuestros clientes, 
    # termina siéndolo efectivamente. Sirve para saber si estamos haciendo los esfuerzos correctos a la hora de 
    # dirigirnos a nuestros prospectos de venta. 

    formula = cantidad_ventas_totales / cantidad_contactos_posible_clientes
    print (f"La tasa de conversion que genera {cliente} es {formula}")
    return formula  

def roi(cliente, ingresos_inversion, costos_inversion ):
    # También conocido como Retorno Sobre  la Inversión, esta métrica te permite saber cuánto ganó tu negocio a través de ciertas inversiones. 
    # Para calcularlo, es necesario dividir los ingresos de una inversión en particular por los costos de esa inversión. 
    formula = ingresos_inversion / costos_inversion
    print (f"El ROI que genera {cliente} es {formula}")
    return formula
    





def copiar(cliente, ):
    #
    formula = ""
    print (f"El  que genera {cliente} es {formula}")
    return formula