from store.models import Category, Product
from django.utils.text import slugify

# --- 1. CREAR CATEGORÍAS ---
categories_list = ['Shooter', 'Accion', 'Terror', 'Historia', 'Multijugador', 'Suscripciones', 'DinamitaPass']
categories_objs = {}

print("--- Creando Categorías ---")
for name in categories_list:
    cat, created = Category.objects.get_or_create(name=name, defaults={'slug': slugify(name)})
    categories_objs[name] = cat
    print(f"Categoria: {name}")

# --- 2. LISTA ORIGINAL (Tus 10 productos) ---
new_products_data = [
    {"title": "Nintendo Switch Online + Expansión", "category": "Suscripciones", "brand": "Nintendo", "price": 49.99, "description": "Suscripción Individual 12 Meses. Disfruta del juego en línea y accede a una biblioteca creciente de juegos clásicos."},
    {"title": "DOOM Eternal", "category": "Shooter", "brand": "Bethesda", "price": 39.99, "description": "Los ejércitos del infierno han invadido la Tierra. Conviértete en el Slayer."},
    {"title": "Cyberpunk 2077: Ultimate", "category": "Accion", "brand": "CD Projekt Red", "price": 59.99, "description": "Historia de acción y aventura de mundo abierto en Night City."},
    {"title": "Dead Space (Remake)", "category": "Terror", "brand": "EA Motive", "price": 59.99, "description": "Isaac Clarke debe sobrevivir en la USG Ishimura."},
    {"title": "Minecraft", "category": "Multijugador", "brand": "Mojang Studios", "price": 29.99, "description": "Explora mundos infinitos y construye todo."},
    {"title": "Assassin's Creed Mirage", "category": "Historia", "brand": "Ubisoft", "price": 49.99, "description": "Eres Basim, un astuto ladrón callejero en Bagdad."},
    {"title": "Mortal Kombat 1", "category": "Accion", "brand": "NetherRealm", "price": 69.99, "description": "Descubre un renacido universo de Mortal Kombat."},
    {"title": "Final Fantasy XVI", "category": "Historia", "brand": "Square Enix", "price": 69.99, "description": "El ocaso se cierne sobre Valisthea y sus Cristales Madre."},
    {"title": "Hollow Knight", "category": "Accion", "brand": "Team Cherry", "price": 14.99, "description": "Forja tu propio camino en Hallownest."},
    {"title": "Forza Horizon 5", "category": "Multijugador", "brand": "Playground Games", "price": 59.99, "description": "Explora los vibrantes paisajes de México."}
]

# --- 3. NUEVOS PRODUCTOS (40 Adicionales) ---
additional_products = [
    # SHOOTERS
    {"title": "Call of Duty: Modern Warfare III", "category": "Shooter", "brand": "Activision", "price": 69.99, "description": "La guerra ha cambiado. Únete a la Task Force 141."},
    {"title": "Halo Infinite: Campaña", "category": "Shooter", "brand": "Xbox Game Studios", "price": 59.99, "description": "El Jefe Maestro regresa para enfrentarse al enemigo más despiadado."},
    {"title": "Overwatch 2: Invasion Bundle", "category": "Shooter", "brand": "Blizzard", "price": 14.99, "description": "Acceso a las misiones de historia de Invasión y monedas."},
    {"title": "Gears 5", "category": "Shooter", "brand": "The Coalition", "price": 39.99, "description": "La guerra total desciende. Kait Diaz se separa para descubrir su conexión con el enemigo."},
    {"title": "Borderlands 3", "category": "Shooter", "brand": "2K Games", "price": 59.99, "description": "El shooter-looter original regresa con miles de millones de armas."},
    {"title": "BioShock: The Collection", "category": "Shooter", "brand": "2K Games", "price": 49.99, "description": "Regresa a las ciudades de Rapture y Columbia en 1080p."},

    # ACCION / AVENTURA
    {"title": "Elden Ring", "category": "Accion", "brand": "FromSoftware", "price": 59.99, "description": "Levántate, Sinluz, y déjate guiar por la gracia para brandir el poder del Anillo de Elden."},
    {"title": "God of War Ragnarök", "category": "Accion", "brand": "Santa Monica Studio", "price": 69.99, "description": "Kratos y Atreus deben viajar a cada uno de los nueve reinos."},
    {"title": "Spider-Man 2", "category": "Accion", "brand": "Insomniac Games", "price": 69.99, "description": "Los Spider-Men, Peter Parker y Miles Morales, regresan para una nueva aventura."},
    {"title": "The Legend of Zelda: Tears of the Kingdom", "category": "Accion", "brand": "Nintendo", "price": 69.99, "description": "Una aventura épica a través de la tierra y los cielos de Hyrule."},
    {"title": "Hades", "category": "Accion", "brand": "Supergiant Games", "price": 24.99, "description": "Desafía al dios de los muertos mientras hackeas y cortas para salir del inframundo."},
    {"title": "Devil May Cry 5", "category": "Accion", "brand": "Capcom", "price": 29.99, "description": "La amenaza del poder demoníaco ha vuelto a amenazar al mundo."},
    {"title": "Star Wars Jedi: Survivor", "category": "Accion", "brand": "Respawn", "price": 69.99, "description": "La historia de Cal Kestis continúa en esta aventura galáctica."},

    # TERROR
    {"title": "Resident Evil 4 (Remake)", "category": "Terror", "brand": "Capcom", "price": 59.99, "description": "La supervivencia es solo el comienzo. Leon S. Kennedy regresa."},
    {"title": "Silent Hill 2 (Remake)", "category": "Terror", "brand": "Konami", "price": 69.99, "description": "Habiendo recibido una carta de su esposa fallecida, James se dirige a donde compartieron tantos recuerdos."},
    {"title": "The Outlast Trials", "category": "Terror", "brand": "Red Barrels", "price": 29.99, "description": "Sobrevive a las terapias de control mental solo o con amigos."},
    {"title": "Phasmophobia", "category": "Terror", "brand": "Kinetic Games", "price": 13.99, "description": "Terror psicológico cooperativo en línea para 4 jugadores."},
    {"title": "Alien: Isolation", "category": "Terror", "brand": "Sega", "price": 39.99, "description": "Descubre el verdadero significado del miedo en una atmósfera de terror constante."},
    {"title": "Alan Wake 2", "category": "Terror", "brand": "Remedy", "price": 59.99, "description": "Una serie de asesinatos rituales amenaza a Bright Falls."},

    # HISTORIA / RPG NARRATIVO
    {"title": "The Last of Us Part I", "category": "Historia", "brand": "Naughty Dog", "price": 69.99, "description": "Disfruta de la emotiva historia y los inolvidables personajes de Joel y Ellie."},
    {"title": "Red Dead Redemption 2", "category": "Historia", "brand": "Rockstar Games", "price": 59.99, "description": "Arthur Morgan y la banda de Van der Linde son forajidos a la fuga."},
    {"title": "The Witcher 3: Wild Hunt", "category": "Historia", "brand": "CD Projekt Red", "price": 39.99, "description": "Eres Geralt de Rivia, cazador de monstruos a sueldo."},
    {"title": "Baldur's Gate 3", "category": "Historia", "brand": "Larian Studios", "price": 59.99, "description": "Reúne a tu grupo y regresa a los Reinos Olvidados en una historia de compañerismo y traición."},
    {"title": "Persona 5 Royal", "category": "Historia", "brand": "Atlus", "price": 59.99, "description": "Ponte la máscara de Joker y únete a los Ladrones Fantasma de Corazones."},
    {"title": "Detroit: Become Human", "category": "Historia", "brand": "Quantic Dream", "price": 39.99, "description": "¿Hasta dónde llegarías para ser libre? Una historia interactiva neo-noir."},

    # MULTIJUGADOR / DEPORTES
    {"title": "EA Sports FC 25", "category": "Multijugador", "brand": "EA Sports", "price": 69.99, "description": "La nueva era del juego de todos. Más de 19,000 jugadores con licencia."},
    {"title": "Rocket League: Pack de Inicio", "category": "Multijugador", "brand": "Psyonix", "price": 4.99, "description": "Incluye el coche Endo, ruedas, calcomanías y 500 créditos."},
    {"title": "Among Us", "category": "Multijugador", "brand": "Innersloth", "price": 4.99, "description": "Un juego de trabajo en equipo y traición en el espacio."},
    {"title": "Mario Kart 8 Deluxe", "category": "Multijugador", "brand": "Nintendo", "price": 59.99, "description": "Compite con tus amigos o lucha contra ellos en un modo de batalla revisado."},
    {"title": "Street Fighter 6", "category": "Multijugador", "brand": "Capcom", "price": 59.99, "description": "Aquí llega el nuevo contendiente de Capcom. Evolución del combate."},
    {"title": "It Takes Two", "category": "Multijugador", "brand": "Hazelight", "price": 39.99, "description": "Embárcate en el viaje más loco de tu vida, puramente cooperativo."},
    {"title": "Super Smash Bros. Ultimate", "category": "Multijugador", "brand": "Nintendo", "price": 59.99, "description": "Luchadores y mundos de juegos legendarios chocan en el enfrentamiento definitivo."},

    # SUSCRIPCIONES
    {"title": "Xbox Game Pass Ultimate (1 Mes)", "category": "Suscripciones", "brand": "Microsoft", "price": 16.99, "description": "Juega a cientos de juegos de alta calidad en consola, PC y la nube."},
    {"title": "PlayStation Plus Extra (3 Meses)", "category": "Suscripciones", "brand": "Sony", "price": 39.99, "description": "Descubre tu próxima gran aventura con un catálogo de cientos de juegos."},
    {"title": "Steam Wallet $20", "category": "Suscripciones", "brand": "Valve", "price": 20.00, "description": "Tarjeta de regalo digital para usar en la tienda de Steam."},
    {"title": "Roblox Gift Card", "category": "Suscripciones", "brand": "Roblox Corp", "price": 10.00, "description": "Obtén Robux para mejorar tu avatar o comprar habilidades en juegos."},
    {"title": "Spotify Premium Individual", "category": "Suscripciones", "brand": "Spotify", "price": 9.99, "description": "Música sin anuncios. Escucha tus canciones favoritas sin interrupciones."},

    # DINAMITAPASS (Categoría Exclusiva de tu tienda)
    {"title": "DinamitaPass", "category": "DinamitaPass", "brand": "Dinamita Store", "price": 99.99, "description": "Juega en todas las plataformas pagando solo una suscripcion."}, 
]

# --- 4. UNIR Y CARGAR PRODUCTOS ---
# Unimos la lista original con la nueva
new_products_data.extend(additional_products)

print(f"\n--- Cargando {len(new_products_data)} Productos ---")

for p in new_products_data:
    # Usamos .get() para evitar errores si la categoría no existe (aunque las creamos arriba)
    cat_obj = categories_objs.get(p["category"])
    
    if not cat_obj:
        print(f"Error: La categoría '{p['category']}' no fue encontrada para '{p['title']}'")
        continue

    prod, created = Product.objects.get_or_create(
        title=p["title"],
        defaults={
            'category': cat_obj,
            'brand': p["brand"],
            'price': p["price"],
            'description': p["description"],
            'slug': slugify(p["title"]),
            'image': '' 
        }
    )
    status = "Creado" if created else "Ya existe"
    print(f"[{status}] {p['category'][:4].upper()} - {p['title']}")