from django.shortcuts import render, get_object_or_404
from .models import Client


def clients(request):
    clients = Client.objects.all()
    context = {'clients':clients}
    return render(request, 'clients/clients.html', context )


def client(request, c_id):
    client = get_object_or_404(Client, pk = c_id)
    context = {'client':client}
    return render(request, 'clients/client.html', context)





    


    



