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
            data = {
                'name': pokemon.css('h1::text').get(),
                'type': pokemon.css('table.vitals-table > tbody > tr:nth-child(2) > td')[0].css('a.type-icon::text').getall(),
                'base_exp': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(4) > td::text')[1].get()),
                'base_stats': {
                    'hp': int(pokemon.css('table.vitals-table > tbody > tr:first-child > td.cell-num::text').get()),
                    'attack': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(2) > td.cell-num::text').get()),
                    'defense': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(3) > td.cell-num::text').get()),
                    'attack_speed': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(4) > td.cell-num::text').get()),
                    'defense_speed': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(5) > td.cell-num::text').get()),
                    'speed': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(6) > td.cell-num::text').get()),
                    'total': int(pokemon.css('table.vitals-table > tfoot > tr > td.cell-total > b::text').get()),
                },                
                'type_defenses': {
                    'normal': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(1)::attr(class)').get()[21:])/100,
                    'fire': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(2)::attr(class)').get()[21:])/100,
                    'water': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(3)::attr(class)').get()[21:])/100,
                    'electric': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(4)::attr(class)').get()[21:])/100,
                    'grass': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(5)::attr(class)').get()[21:])/100,
                    'ice': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(6)::attr(class)').get()[21:])/100,
                    'fighting': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(7)::attr(class)').get()[21:])/100,
                    'poison': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(8)::attr(class)').get()[21:])/100,
                    'ground': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(9)::attr(class)').get()[21:])/100,
                    'flying': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(1)::attr(class)').get()[21:])/100,
                    'psychic': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(2)::attr(class)').get()[21:])/100,
                    'bug': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(3)::attr(class)').get()[21:])/100,
                    'rock': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(4)::attr(class)').get()[21:])/100,
                    'ghost': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(5)::attr(class)').get()[21:])/100,
                    'dragon': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(6)::attr(class)').get()[21:])/100,
                    'dark': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(7)::attr(class)').get()[21:])/100,
                    'steel': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(8)::attr(class)').get()[21:])/100,
                    'fairy': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(9)::attr(class)').get()[21:])/100,
                },
            }
            data['moves'] = []
            for move in pokemon.css('table.data-table')[0].css('tbody > tr'):
                if (move.css('td.cell-icon.text-center::attr(data-filter-value)').get() != 'status') & (move.css('td.cell-num::text')[1].get() != '—'):
                    data['moves'].append({
                        'move_name': move.css('td.cell-name > a.ent-name::text').get(),
                        'move_type': move.css('td.cell-icon > a.type-icon::text').get(),
                        'move_category': move.css('td.cell-icon.text-center::attr(data-filter-value)').get(),
                        'move_power': int(move.css('td.cell-num::text')[1].get()),
                        'move_level_needed': int(move.css('td.cell-num::text')[0].get()),
                    })

            yield data 
            #{
            #    'name': pokemon.css('h1::text').get(),
            #    'type': pokemon.css('table.vitals-table > tbody > tr:nth-child(2) > td > a.type-icon::text').getall(),
            #    'base_exp': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(4) > td::text')[1].get()),
            #    'base_stats': {
            #        'hp': int(pokemon.css('table.vitals-table > tbody > tr:first-child > td.cell-num::text').get()),
            #        'attack': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(2) > td.cell-num::text').get()),
            #        'defense': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(3) > td.cell-num::text').get()),
            #        'attack_speed': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(4) > td.cell-num::text').get()),
            #        'defense_speed': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(5) > td.cell-num::text').get()),
            #        'speed': int(pokemon.css('table.vitals-table > tbody > tr:nth-child(6) > td.cell-num::text').get()),
            #        'total': int(pokemon.css('table.vitals-table > tfoot > tr > td.cell-total > b::text').get()),
            #    },
            #    'type_defenses': {
            #        'normal': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(1)::attr(class)').get()[21:]),
            #        'fire': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(2)::attr(class)').get()[21:]),
            #        'water': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(3)::attr(class)').get()[21:]),
            #        'electric': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(4)::attr(class)').get()[21:]),
            #        'grass': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(5)::attr(class)').get()[21:]),
            #        'ice': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(6)::attr(class)').get()[21:]),
            #        'fighting': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(7)::attr(class)').get()[21:]),
            #        'poison': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(8)::attr(class)').get()[21:]),
            #        'ground': int(pokemon.css('table.type-table-pokedex > tr')[1].css('td:nth-child(9)::attr(class)').get()[21:]),
            #        'flying': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(1)::attr(class)').get()[21:]),
            #        'psychic': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(2)::attr(class)').get()[21:]),
            #        'bug': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(3)::attr(class)').get()[21:]),
            #        'rock': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(4)::attr(class)').get()[21:]),
            #        'ghost': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(5)::attr(class)').get()[21:]),
            #        'dragon': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(6)::attr(class)').get()[21:]),
            #        'drak': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(7)::attr(class)').get()[21:]),
            #        'steel': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(8)::attr(class)').get()[21:]),
            #        'fairy': int(pokemon.css('table.type-table-pokedex:nth-child(2) > tr')[1].css('td:nth-child(9)::attr(class)').get()[21:]),
            #    },
            #}