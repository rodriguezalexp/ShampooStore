from flask import Flask, render_template

app = Flask(__name__)

# --- EL MOLDE (CLASE) ---
class Producto:
    def __init__(self, id, nombre, tipo, precio, descripcion, beneficios, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo  # 'Shampoo' o 'Acondicionador'
        self.precio = precio
        self.descripcion = descripcion
        self.beneficios = beneficios  # Esto será una lista
        self.imagen = imagen

# --- LOS PRODUCTOS REALES (INSTANCIAS) ---
# Creamos una lista para guardarlos todos
catalogo = [
    Producto(
        id=1,
        nombre="Brisa Cítrica",
        tipo="Shampoo Sólido",
        precio=25000,
        descripcion="Limpieza profunda con aceites esenciales de limón y naranja.",
        beneficios=["Control de grasa", "Brillo natural", "Biodegradable"],
        imagen="Brisa _Citrica.avif" # Recomendación: Quitar tilde al archivo real
    ),
    Producto(
        id=2,
        nombre="Nube de Coco",
        tipo="Acondicionador Sólido",
        precio=28000,
        descripcion="Hidratación extrema para cabellos secos o maltratados.",
        beneficios=["Desenredado fácil", "Nutrición profunda", "Sin siliconas"],
        imagen="Nube_de_Coco.avif"
    ),
    Producto(
        id=3,
        nombre="Carbón Activado & Detox",
        tipo="Shampoo Sólido", # Faltaba este
        precio=26000,
        descripcion="Limpieza profunda para cabellos con tendencia a caspa o polución.",
        beneficios=["Detox capilar", "Elimina toxinas"], # Faltaba este
        imagen="Carbon_Activado.avif"
    ),
    Producto(
        id=4,
        nombre="Lavanda Relajante",
        tipo="Acondicionador Sólido", # Faltaba este
        precio=24000,
        descripcion="Acondicionador suave que facilita el peinado y calma el cuero cabelludo.",
        beneficios=["Relajante", "Suavidad"], # Faltaba este
        imagen="Lavanda_Relajante.avif"
    ),
    Producto(
        id=5,
        nombre="Arroz y Karité",
        tipo="Shampoo Sólido", # Faltaba este
        precio=27500,
        descripcion="Nutrición ancestral para cabellos rizados y extra secos.",
        beneficios=["Fuerza", "Hidratación", "Rizos definidos"], # Faltaba este
        imagen="Arroz.avif"
    )
]

# --- LAS RUTAS ---
@app.route('/')
def inicio():
    return render_template('index.html', productos=catalogo)
@app.route('/producto/<int:id_producto>')
def detalle_producto(id_producto):
    # Buscamos el producto por su ID
    producto = next((p for p in productos if p.id == id_producto), None)
    
    if producto:
        # Configuramos el mensaje de WhatsApp
        # Cambia el número por el tuyo (con código de país)
        tel = "573001234567" 
        texto = f"Hola! Me interesa el {producto.nombre} que vi en la web. ¿Me das más información?"
        link_ws = f"https://wa.me/{tel}?text={urllib.parse.quote(texto)}"
        
        return render_template('producto.html', producto=producto, link_ws=link_ws)
    return "Producto no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)