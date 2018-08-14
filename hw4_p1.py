continue_or_not="y"
while continue_or_not=="y":
	rank=["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]#牌的大小
	suit=["SPADE","HEART","DIAMOND","CLUB"]#牌的花色
	deckcard=[]
	for i in rank:#總共五十二張牌
		for j in suit:
			deckcard.append(i+"-"+j)
	import random
	random.shuffle(deckcard)#洗牌
	index=random.randint(0,len(deckcard)-1)
	card_number=[]
	p_hand=[deckcard[0],deckcard[1]]
	for card in p_hand:
		card1=card.split("-")
		card_number=card_number+[card1[0]]
	total_number=0
	for number in card_number:#判定抽到的兩張牌的大小總和
		for n in rank:
			if number==n:
				if number=="KING" or number=="QUEEN" or number=="JACK":
					total_number+=10
				elif number=="ACE":
					total_number+=11
				else:
					total_number+=int(n)
	if total_number==21:#判定是否已經 blackjack
		print("Your value is Blackjack! (21)")
	print("Your current value is",total_number)
	print("with the hand: "+", ".join(p_hand)+"\n")
	i=0
	use=0
	while True and total_number!=21:
		hit_or_stay=input("Hit or stay?(Hit = 1, Stay = 0):")#決定是否繼續抽牌
		print()
		while not (hit_or_stay=="0" or hit_or_stay=="1"):
			print("Invalid input. Try again.")
			hit_or_stay=input("Hit or stay?(Hit = 1, Stay = 0):")
			print()
		if hit_or_stay=="0":
			break
		if hit_or_stay=="1":
			i=i+1
			p_hand.append(deckcard[2+i])
			card_h=deckcard[2+i].split("-")
			card_number=card_number+[card_h[0]]
			print("You draw",deckcard[2+i],"\n")
			for n in rank:
				if card_h[0]==n:
					if card_h[0]=="KING" or card_h[0]=="QUEEN" or card_h[0]=="JACK":
						total_number+=10
					elif card_h[0]=="ACE":
						total_number+=11
					else:
						total_number+=int(card_h[0])
			
			while total_number>21 and card_number.count("ACE")>0 and (not use==card_number.count("ACE")):#判定手牌是否有么點
				total_number-=10
				use+=1
			print("Your current value is",total_number)
			if total_number>21:#判定是否已經爆牌
				print("Your current value is Bust!(>21)")
				print("with the hand: "+", ".join(p_hand)+"\n")
				break
			if total_number==21:#判定是否已經blackjack
				print("Your value is Blackjack! (21)")
				print("with the hand: "+", ".join(p_hand)+"\n")
				break
			print("with the hand: "+", ".join(p_hand)+"\n")
	#============================================================================
	card_number_d=[]
	d_hand=[deckcard[2+i+1],deckcard[2+i+2]]
	for card in d_hand:
		card1=card.split("-")
		card_number_d=card_number_d+[card1[0]]
	total_number_d=0
	for number in card_number_d:
		for n in rank:
			if number==n:
				if number=="KING" or number=="QUEEN" or number=="JACK":
					total_number_d+=10
				elif number=="ACE":
					total_number_d+=11
				else:
					total_number_d+=int(n)
	if total_number_d==21:
		print("Dealer's value is Blackjack! (21)")
	print("Dealer's current value is",total_number_d)
	print("with the hand: "+", ".join(d_hand)+"\n")
	j=0
	use=0
	while total_number_d<17:#若莊家手牌小於十七，則繼續抽牌直到手牌大小大於等於十七為止
		if True:
			j+=1
			d_hand.append(deckcard[2+i+2+j])
			card_h=deckcard[2+i+2+j].split("-")
			card_number_d=card_number_d+[card_h[0]]
			print("Dealer draw",deckcard[2+i+2+j],"\n")
			for n in rank:
				if card_h[0]==n:
					if card_h[0]=="KING" or card_h[0]=="QUEEN" or card_h[0]=="JACK":
						total_number_d+=10
					elif card_h[0]=="ACE":
						total_number_d+=11
					else:
						total_number_d+=int(card_h[0])
			while total_number_d>21 and card_number_d.count("ACE")>0 and (not use==card_number_d.count("ACE")):
				total_number_d-=10
				use+=1
			print("Dealer's current value is",total_number_d)
			if total_number_d>21:
				print("Dealer's current value is Bust!(>21)")
				print("with the hand: "+", ".join(d_hand)+"\n")
				break
			if total_number_d==21:
				print("Dealer's value is Blackjack! (21)")
				print("with the hand: "+", ".join(d_hand)+"\n")
				break
			print("with the hand: "+", ".join(d_hand)+"\n")
	if total_number==21 and (not total_number_d==21):
		print("****You beat the dealer !****")
	elif total_number_d==21 and (not total_number==21):
		print("****Dealer wins !****")
	elif total_number>21 and total_number_d<=21:
		print("****Dealer wins !****")
	elif total_number_d>21 and total_number<=21:
		print("****You beat the dealer !****")
	elif total_number>21 and total_number_d>21:
		print("****You tied the dealer. Nobody wins.****")
	elif total_number==21 and total_number_d==21:
		print("****You tied the dealer. Nobody wins.****")
	elif total_number==total_number_d:
		print("****You tied the dealer. Nobody wins.****")
	elif total_number<21 and total_number_d<21:
		p_difference=21-total_number
		d_difference=21-total_number_d
		if p_difference>d_difference:
			print("****Dealer wins !****")
		elif p_difference<d_difference:
			print("****You beat the dealer !****")
	print()
	continue_or_not=input("Want to play again ? (y/n): ")#是否繼續遊玩
	while not (continue_or_not=="y" or continue_or_not=="n"):
		print("Invalid input. Try again.")
		print()
		continue_or_not=input("Want to play again ? (y/n): ")
	if continue_or_not=="y":
		print("===================================================")
		print()



