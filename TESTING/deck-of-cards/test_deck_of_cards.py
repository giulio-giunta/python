import unittest
from deck_of_cards_ori import Card, Deck

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card('2', 'Diamonds')
		
	def test_init(self):
		'''each instance of Card should have a value and suit'''
		self.assertEqual(self.card.value, '2')
		self.assertEqual(self.card.suit, "Diamonds")
	
	def test_repr(self):
		'''repr should should return a string of the form 'VALUE of SUIT'''
		self.assertEqual(repr(self.card),'2 of Diamonds')

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()
		
	def deck_init(self):
		'''each deck should have cards all cards with values and signs'''
		self.assertTrue(isinstance(self.deck.cards), list)
		self.assertEqual(len(self.deck.cards), 52)		
		
	def test_repr(self):
		'''repr should return a string of the form 'Deck of COUNT cards'''
		self.assertEqual(repr(self.deck), f'Deck of 52 cards')
		
	def test_count(self):
		'''each deck should have 52 cards'''
		self.deck.count()
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)
		
	def test_deal_sufficient_cards(self):
		'''deal should deal the number of cards specified'''
		cards = self.deck._deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)
		
	def test_deal_insufficient_cards(self):
		'''deal should deal the number of cards left in the deck'''
		cards = self.deck._deal(100)
		self.assertEqual(len(cards), 52)
		self.assertEqual(self.deck.count(), 0)

	def test_deal_no_cards(self):
		'''deal should throw a value error if the deck is empty'''
		self.deck._deal(self.deck.count())
		with self.assertRaises(ValueError):
			self.deck._deal(1)
			
	def test_deal_card(self):
		'''deal_card should deal a single card from the deck'''
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(self.deck.count(), 51)
		
	def test_deal_hand(self):
		'''deal_hand should deal the number of cards passed'''
		cards = self.deck.deal_hand(20)
		self.assertEqual(len(cards), 20)
		self.assertEqual(self.deck.count(), 32)
		
	def test_shuffle_full_deck(self):
		'''shuffle should shuffle the deck if the deck is full'''
		cards = self.deck.cards[:]
		self.deck.shuffle()
		self.assertNotEqual(cards, self.deck.cards)
		self.assertEqual(self.deck.count(), 52)
		
	def test_shuffle_not_full_deck(self):
		'''shuffle should throw a ValueError if the deck isn't full'''
		self.deck._deal(1)
		with self.assertRaises(ValueError):
			self.deck.shuffle()		

if __name__ == '__main__':
	unittest.main()