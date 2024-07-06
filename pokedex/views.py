from django.http import HttpResponse
from django.template import loader
from .models import Pokemon

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


