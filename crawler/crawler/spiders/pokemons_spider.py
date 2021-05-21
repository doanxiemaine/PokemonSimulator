import scrapy

class PokemonsSpider(scrapy.Spider):
    name = 'pokemons'

    start_urls = [
        'https://pokemondb.net/pokedex/all',
    ]

    def parse(self, response):        
        for pokemon in response.css('table[id=pokedex] > tbody > tr > td.cell-name'):
            yield {
                'name': pokemon.css('a.ent-name::text').get(),
                'link_info': 'https://pokemondb.net' + pokemon.css('a.ent-name::attr(href)').get(),
            }
        