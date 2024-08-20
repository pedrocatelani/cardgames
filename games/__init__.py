import random as rd

class Cards:
    naipe_list = ('Copas','Ouro','Espadas','Paus')
    card_list = ('10','9','8','7','6','5','4','3','2','ace','king','queen','jack')

    card_name = ''
    card_naipe = ''
    card = ''

    def create_card(self):
        self.card_name = rd.choice(self.card_list)
        self.card_naipe = rd.choice(self.naipe_list)
        self.card = f'{self.card_name.capitalize()} de {self.card_naipe.capitalize()}'

    def get_info(self) -> dict:
        return {
            'card': self.card,
            'naipe': self.card_naipe,
            'name': self.card_name
        }

    def get_info_value(self) -> dict:
        if self.card_name in ['queen','king','jack']:
            card = 10
        elif self.card_name == 'ace':
            card = 1
        else:
            card = self.card_name

        return {
            'card': self.card,
            'naipe': self.card_naipe,
            'value': card
        }