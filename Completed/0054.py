value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
plyr1wins = 0
unknown = 0
for line in open("p054_poker.txt"):
    cards = line.split()
    plyrs = [cards[:5],cards[5:]]
    # suit only factors into flush
    flush = [ all( card[1]==plyr[0][1] for card in plyr[1:]) for plyr in plyrs ]
    # stop considering suit, convert to #s for ease of value comp
    hands = []
    for plyr in plyrs:
        hand = {}
        for card in plyr:
            hand[value[card[0]]] = hand.get(value[card[0]],0) + 1
        hands.append(hand)
    #hands = [ sorted([value[card[0]] for card in plyr]) for plyr in plyrs ]
    # is straight?
    straight = [len(hand)==5 and min(hand)==max(hand)-4 for hand in hands]
    #straight = [len(set(hand))==5 and hand[0]==hand[4]-4 for hand in hands]
    ranks = []
    for plyr in [1,2]:
        plyr -= 1
        bags = list(hands[plyr].values())
        rank = 0
        # straight flush    17=8+9
        # 4K                16
        if 4 in bags: rank = 16
        # 3K+2K             10=7+3
        # flush             9
        if flush[plyr]: rank += 9
        # straight          8
        if straight[plyr]: rank += 8
        # 3K                7
        if 3 in bags: rank += 7
        # 2K+2K             6=3+3
        # 2K                3
        rank += bags.count(2) * 3
        # trash             0
        ranks.append(rank)
    if ranks[0] == ranks[1]:
        if ranks[0] in [8,9,17]: # tie break straight or flush
            hands = [ [value[card[0]] for card in plyr] for plyr in plyrs ]
            for card in hands[0][:]:
                if card in hands[1]:
                    hands[0].remove(card)
                    hands[1].remove(card)
            if max(hands[0]) > max(hands[1]): plyr1wins += 1; continue
        if ranks[0] >= 7: # tie break 3 or 4 of a kind
            if max(hands[0],key=lambda x:hands[0]) \
             > max(hands[1],key=lambda x:hands[1]): plyr1wins += 1; continue
        if ranks[0] >= 3: # tie break pair or pair of pairs
            hands = [
                sorted([ card * (1 if hand[card]==1 else 100) for card in hand])
                for hand in hands]
            for card in hands[0][:]:
                if card in hands[1]:
                    hands[0].remove(card)
                    hands[1].remove(card)
        # high card
        if max(hands[0]) > max(hands[1]): plyr1wins += 1
    if ranks[0] > ranks[1]:
        plyr1wins += 1
print(plyr1wins)
