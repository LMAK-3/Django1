from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	#return HttpResponse(html_base +'<h2>Mi web personal </h2>')
	return render(request, 'core/home.html')
def about(request):
	return render(request, 'core/about.html')
	#return HttpResponse(html_base +'<h2>Acerca de </h2>')
def portafolio(request):
	return render(request, 'core/portafolio.html')
		#return HttpResponse(html_base +"""<h1>Portafolio<h1>
		#<p>Trabajos realizados</p>
		#""")
def contact(request):
	return render(request, 'core/contact.html')
	#return HttpResponse(html_base +"""<h1>Contáctenos</h1>
		#<p>Datos de Ubicación</p
		#""")