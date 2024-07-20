from django.http import HttpResponse
from django.template import loader

from .models import Pokemon
from pokedex.forms import PokemonForm
from django.shortcuts import redirect, render



def index(request):
    #LLamamos al modelo pokemon que tiene una lista de pokemones y los ordenamos por tipo
    #SI quieres saber mas estudia ORM ''
    pokemons = Pokemon.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


#Crearemos la vista add pokemon
#EL request obtiene los datos enviados desde el formulario por el metodo "post" 
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
        
    return render(request, 'add_pokemon.html', {'form':form})