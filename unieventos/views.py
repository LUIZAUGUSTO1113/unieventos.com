# utilização das bibliotecas do django, bem como os import necessários para as funções
from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

# função responsável por autenticar e retornar para o sistema o usuário que veio do app authentication
# função também responsável por carregar na url /home os últimos 3 eventos criados
def home(request):
    events = Event.objects.all()[:3]

    # Check if user is authenticated
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    context = {
        'events': events,
        'user': user,
    }
    
    return render(request, 'unieventos/main.html', context)

# função responsável pela exibição de todos os eventos criados    
def events(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'unieventos\events.html', context)

# função responsável pela exibição detalhada do evento criado
def event_detail(request, pk):
    try:
        user = request.user
        event = Event.objects.get(pk=pk)
    except event.DoesNotExist:
        response = HttpResponse(status=404)
        response.content = b'Event not found.'
        return response

    context = {
        'event': event,
        'user' : user,
    }

    return render(request, 'unieventos/event_detail.html', context)

# função responsável por atribuir ao usuário a criação de um evento
@login_required
def create_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        event_date = request.POST['event_date']
        image = request.FILES.get('image')

        # apresenta erro se o usuário não adicionou uma foto ao criar o evento
        if not image:
            messages.error(request, "O evento deve conter uma imagem")
            return render(request, 'unieventos/create_event.html')

        #  etapas para criar a relação entre o evento e o seu criador (o usuário logado)
        event = Event.objects.create(
            name=name,
            image=image,
            description=description,
            event_date=event_date,
            creator=request.user,
        )

        messages.success(request, "Evento criado com sucesso!")
        return redirect('unieventos:home')  # Redireciona para a lista de eventos

    return render(request, 'unieventos/create_event.html')

# função responsável pela inscrição do usuário
# NÃO DESENVOLVIDO! - VISUALIZAR O READ.MR


# função responsável pela exibição da url /about
def about(request):
    return render(request, 'unieventos/about.html')