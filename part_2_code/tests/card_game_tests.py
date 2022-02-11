import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card = Card('Spades', 3)

    # @unittest.skip("delete this line to run the test")
    def test_check_for_ace_fail(self):
        card = self.card
        result = CardGame.check_for_ace(self, card)
        self.assertEqual(False, result)

    # @unittest.skip("delete this line to run the test")
    def test_check_for_ace_pass(self):
        card = self.card
        card.value = 1
        result = CardGame.check_for_ace(self, card)
        self.assertEqual(True, result)

    # @unittest.skip("delete this line to run the test")
    def test_highest_card_card_1_highest(self):
        card_1 = self.card
        card_2 = Card('Clubs', 2)
        result = CardGame.highest_card(self, card_1, card_2)
        self.assertEqual(card_1, result)

    # @unittest.skip("delete this line to run the test")
    def test_highest_card_card_2_highest(self):
        card_1 = self.card
        card_2 = Card('Clubs', 4)
        result = CardGame.highest_card(self, card_1, card_2)
        self.assertEqual(card_2, result)

    # @unittest.skip("delete this line to run the test")
    def test_highest_card_same_value(self):
        card_1 = self.card
        card_2 = Card('Clubs', 3)
        result = CardGame.highest_card(self, card_1, card_2)
        self.assertEqual("The cards have the same value", result)

    # @unittest.skip("delete this line to run the test")
    def test_cards_total_no_cards(self):
        cards = []
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 0", result)

    # @unittest.skip("delete this line to run the test")
    def test_cards_total_one_card(self):
        card = self.card
        cards = [card]
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 3", result)

    # @unittest.skip("delete this line to run the test")
    def test_cards_total_two_cards(self):
        card_1 = self.card
        card_2 = Card('Clubs', 2)
        cards = [card_1, card_2]
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 5", result)