def cliente():
    nombre = input("Inserte nombre cliente")
    pagina =  input(f"Inserte el sitio web de {nombre}")
    social_media =  input(f"¿Cuenta con red social")
    return [nombre,pagina, social_media]

