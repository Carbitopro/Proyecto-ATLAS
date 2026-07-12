full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        'The character should have a name'
    if len(name) > 10:
        return 'The character name should not be longer than 10 characters'
    if ' ' in name:
        return 'The character name should not contain spaces'
    stats = {'STR': strength, 'INT': intelligence, 'CHA': charisma}
    for stat in stats.values():
        if not isinstance(stat, int):
            return 'The stats should all be numbers'
        if stat < 1:
            return 'All stats should be greater than 1'
        if stat > 4:
            return 'All stats should be less than 4'
        if sum(stats.values()) != 7:
            return 'The character should start 7 points'
        character_string = name
        for key in ['STR', 'INT', 'CHA']:
            stat = stats[key]

            character_string += f'\n{key}{full_dot * stat} {empty_dot * (10 - stat)}'
        return character_string


print(create_character('ren', 2, 2, 3))
