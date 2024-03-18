def email_redactar():
    titulo = "Redacta un email de venta"
    texto_1 = "Actúa como un experto en copywriting. Necesito enviar un correo electrónico a nuestra base de clientes actuales presentando nuestro nuevo producto "
    descripcion = input("Describir Producto")
    texto_2 = " El correo debe resaltar las características principales, cómo mejora respecto a productos anteriores y ofrecer un descuento exclusivo para los destinatarios. Si tienes preguntas sobre mi producto, házmelas antes de empezar."
    frase = texto_1 +  descripcion +  texto_2
    print(frase)   
    return frase, titulo



