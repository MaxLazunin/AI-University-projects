import random
import cart
import bag
import decors

bag = bag.Bag()
card_1 = cart.Card()
card_2 = cart.Card()

keg = bag.get_keg()
card_1.card_generator()
card_1.cross_numeral(keg)
card_2.card_generator()
card_2.cross_numeral(keg)


keg = bag.get_keg()
card_1.card_generator()
card_1.cross_numeral(keg)
card_2.card_generator()
card_2.cross_numeral(keg)




