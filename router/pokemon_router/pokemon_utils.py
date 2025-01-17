from ..queries import *

def save_types_in_tabels(pokemon_id, pokemon_types):
    for type in pokemon_types:
        insert_each_type(pokemon_id, type["type"]["name"])

def get_pokemon_data(pokemon_name):
    return get_pokemon_data_db(pokemon_name)

def get_pokemon_types(pokemon_id):
    return get_pokemon_types_db(pokemon_id)

def find_pokemon_roster(trainer_name):
    return find_pokemon_roster_db(trainer_name)

def find_pokemons_by_type(type):
    return find_pokemons_by_type_db(type)

def delete_pokemon_of_trainer_from_db(pokemon_name, trainer_name):
    return delete_pokemon_of_trainer_from_db_query(pokemon_name, trainer_name)


def return_next_form(pokemon_name,evolution_chain):
    chain = evolution_chain["chain"]
    for _ in range(2):
        if chain["species"]["name"] == pokemon_name :
            if chain["evolves_to"]:
                return chain["evolves_to"][0]["species"]["name"]
        else:
            chain = chain["evolves_to"][0]

def insert_to_pokemon_trainer_db(p_id,t_name):
    insert_to_pokemon_trainer_db_query(p_id,t_name)


def update_db_evolve(old_pokemon_name, new_pokemon_name, trainer_name):
    delete_pokemon_of_trainer_from_db(old_pokemon_name, trainer_name)
    pokemon_id = get_pokemon_data(new_pokemon_name)["id"]
    insert_to_pokemon_trainer_db(pokemon_id, trainer_name)