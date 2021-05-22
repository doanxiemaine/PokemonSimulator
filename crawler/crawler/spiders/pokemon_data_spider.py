import scrapy
import json

class PokemonDataSpider(scrapy.Spider):
    name = 'pokemon_data'
    
    start_urls = []
    pokemons_file = open('pokemons.json', encoding = 'utf8')
    pokemons = json.load(pokemons_file)

    for pokemon in pokemons:
        start_urls.append(pokemon['link_info'])
    pokemons_file.close()

    def parse(self, response):
        for pokemon in response.css('main.main-content.grid-container'):
            yield {
                'name': pokemon.css('h1::text').get(),
                'type': pokemon.css('table.vitals-table > tbody > tr:nth-child(2) > td > a.type-icon::text').getall(),
                'base_exp': pokemon.css('table.vitals-table > tbody > tr:nth-child(4) > td::text')[1].get(),
                'base_stats': {
                    'hp': pokemon.css('table.vitals-table > tbody > tr:first-child > td.cell-num::text').get(),
                    'attack': pokemon.css('table.vitals-table > tbody > tr:nth-child(2) > td.cell-num::text').get(),
                    'defense': pokemon.css('table.vitals-table > tbody > tr:nth-child(3) > td.cell-num::text').get(),
                    'attack_speed': pokemon.css('table.vitals-table > tbody > tr:nth-child(4) > td.cell-num::text').get(),
                    'defense_speed': pokemon.css('table.vitals-table > tbody > tr:nth-child(5) > td.cell-num::text').get(),
                    'speed': pokemon.css('table.vitals-table > tbody > tr:nth-child(6) > td.cell-num::text').get(),
                    'total': pokemon.css('table.vitals-table > tfoot > tr > td.cell-total > b::text').get(),
                },
                'type_defenses': {
                    'normal': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(1)::attr(class)').get()[21:],
                    'fire': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(2)::attr(class)').get()[21:],
                    'water': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(3)::attr(class)').get()[21:],
                    'electric': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(4)::attr(class)').get()[21:],
                    'grass': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(5)::attr(class)').get()[21:],
                    'ice': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(6)::attr(class)').get()[21:],
                    'fighting': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(7)::attr(class)').get()[21:],
                    'poison': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(8)::attr(class)').get()[21:],
                    'ground': pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(9)::attr(class)').get()[21:],
                    'flying': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(1)::attr(class)').get()[21:],
                    'psychic': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(2)::attr(class)').get()[21:],
                    'bug': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(3)::attr(class)').get()[21:],
                    'rock': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(4)::attr(class)').get()[21:],
                    'ghost': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(5)::attr(class)').get()[21:],
                    'dragon': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(6)::attr(class)').get()[21:],
                    'drak': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(7)::attr(class)').get()[21:],
                    'steel': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(8)::attr(class)').get()[21:],
                    'fairy': pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(9)::attr(class)').get()[21:],
                }
            }