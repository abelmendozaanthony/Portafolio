from django.shortcuts import render

def home_view(request):
    # Datos estáticos de ejemplo (sin base de datos)
    proyectos = [
        {
            'titulo': 'E-commerce Innova Electric',
            'descripcion': 'Plataforma web desarrollada con pasarela de pagos, filtros y gestión de productos.',
            'imagen': 'https://images.unsplash.com/photo-1557821552-1710517667fc?w=500&auto=format&fit=crop&q=60',
            'url_github': 'https://github.com/',
            'url_deploy': 'https://example.com',
            'tecnologias': ['Django', 'Tailwind CSS', 'Python']
        },
        {
            'titulo': 'Sistema Kiosko Don Miguel',
            'descripcion': 'Interfaz de auto-servicio y punto de venta adaptada para contenedores táctiles.',
            'imagen': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500&auto=format&fit=crop&q=60',
            'url_github': 'https://github.com/',
            'url_deploy': '',
            'tecnologias': ['Android Studio', 'WebView', 'PHP']
        }
    ]
    
    return render(request, 'portfolio/inicio.html', {'proyectos': proyectos})

# Create your views here.
