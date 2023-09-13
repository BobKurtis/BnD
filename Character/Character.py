class Character:
    def create_new_character(self, attributes_list):
        character = dict(
            name=attributes_list[0],
            sprite_file=attributes_list[1],
            speed=attributes_list[2],
            health=attributes_list[3],
            wisdom=attributes_list[4],
            stress=attributes_list[5],
            attackRange=attributes_list[6]

        )
        return character
