import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4 , "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": None}

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return self.rank + " of " + self.suit

  def set_Value(self, new_val):
    self.value = new_val

class Deck:
  def __init__(self):
    self.all_cards = []
    for s in suits:
      for r in ranks:
        self.all_cards.append(Card(s,r))

  def shuffle(self):
    random.shuffle(self.all_cards)

  def remove_card(self):
    return self.all_cards.pop()

  def __str__(self):
    for c in self.all_cards:
      print(str(c))
    return ""

deck = Deck()
deck.shuffle()

class Player: 
  def __init__(self, chips):
    self.player_deck = []
    self.current_bet = 0
    self.chips = chips
    self.player_total = 0
    print("You have {} chips".format(self.chips))

    isBetRunning = True
    while(isBetRunning):
      try:
        self.current_bet = int(input("Place your bet: "))
      except:
        print("Incorrect input. Please try again." + "\n")
      else:
        if (self.current_bet > self.chips):
          print("Your current bet is greater than your current amount of chips which are {}".format(self.chips) + "\n")
        else:
          print("{} has been placed".format(self.current_bet) + "\n")
          isBetRunning = False

    for i in range(0,2):
      self.player_deck.append(Deck.remove_card(deck))
      print("You have a {}".format(self.player_deck[-1]))
      if (self.player_deck[-1].rank == "Ace"):
        isRunning = True
        while(isRunning):
          try:
            result = int(input("Place value of Ace to be either 1 or 11: "))
          except:
            print("Incorrect input. Please insert an integer." + "\n")
          else:
            if (result != 1 and result != 11):
              print("Incorrect input. Please insert a 1 or 11." + "\n")
            else:
              self.player_deck[-1].set_Value(result)
              self.player_total += self.player_deck[-1].value
              isRunning = False
      else:
        self.player_total += self.player_deck[-1].value

    print("Player's current total is {}".format(self.player_total) + "\n")

  def hit(self):
    self.player_deck.append(Deck.remove_card(deck))
    print(str("You got a {}".format(self.player_deck[-1]) + "\n"))
    if (self.player_deck[-1].rank == "Ace"):
      isRunning = True
      while(isRunning):
        try:
          result = int(input("Place value of Ace to be either 1 or 11: "))
        except:
          print("Incorrect input. Please insert an integer." + "\n")
        else:
          if (result != 1 and result != 11):
            print("Incorrect input. Please insert a 1 or 11." + "\n")
          else:
            self.player_deck[-1].set_Value(result)
            self.player_total += self.player_deck[-1].value
            isRunning = False
    else:
        self.player_total += self.player_deck[-1].value

  def check_total(self):
    if (self.player_total > 21):
      return("Bust!")
    else:
      return("Your current total is {}".format(self.player_total))

  def win(self):
    print("Congratulations Player has Won!")
    self.chips += self.current_bet
    print("Player's current # of chips is {}".format(self.chips) + "\n")

  def loss(self):
    print("Player has lost")
    self.chips -= self.current_bet
    print("Player's current # of chips is {}".format(self.chips) + "\n")
  
  def set_bet(self):
    isBetRunning = True
    while(isBetRunning):
      try:
        self.current_bet = int(input("Place your bet: "))
      except:
        print("Incorrect input. Please try again." + "\n")
      else:
        if (self.current_bet > self.chips):
          print("Your current bet is greater than your current amount of chips which are {}".format(self.chips) + "\n")
        else:
          print("{} has been placed".format(self.current_bet) + "\n")
          isBetRunning = False

class Dealer:

  def __init__(self, chips):
    self.chips = chips
    self.dealer_deck = []
    self.dealer_total = 0
    rand_num = random.randint(0,1)
    self.hidden = rand_num

    for i in range(0,2):
      self.dealer_deck.append(Deck.remove_card(deck))
      if (self.dealer_deck[-1].rank == "Ace"):
        if i != self.hidden:
          self.dealer_deck[-1].set_Value(11)
          self.dealer_total += 11
          print("Dealer sets Ace to 11")
      else:
        self.dealer_total += self.dealer_deck[-1].value

    if (self.hidden == 0): 
      print("Dealer has {}".format(self.dealer_deck[1]) + "\n")
    else:
      print("Dealer has {}".format(self.dealer_deck[0]) + "\n")

  def check_total(self):
    if (self.dealer_total > 21):
      return("Dealer has Bust!")
    else:
      return("Dealer's current total is {}".format(self.dealer_total))

  def display_cards(self):
    for i in range(0,len(self.dealer_deck)):
      if (self.dealer_deck[i].rank == "Ace" and self.dealer_deck[i].value == None):
        if (self.dealer_total + 11 <= 21):
          print("Dealer has set value to 11")
          self.dealer_deck[i].set_Value(11)
          self.dealer_total += 11
        else:
          print("Dealer has set value to 1")
          self.dealer_deck[i].set_Value(1)
          self.dealer_total += 1
      print("Dealer has a {}".format(self.dealer_deck[i]))
    
    print("Dealer's current total is {}".format(self.dealer_total)+"\n")

  def hit(self):
    print("Dealer hit" + "\n")
    self.dealer_deck.append(Deck.remove_card(deck))
    print(str("Dealer got a {}".format(self.dealer_deck[-1]) + "\n"))
    if (self.dealer_deck[-1].rank == "Ace"):
      if (self.dealer_total + 11 <= 21):
        print("Dealer has set value to 11")
        self.dealer_deck[-1].set_Value(11)
        self.dealer_total += 11
      else:
        print("Dealer has set value to 1")
        self.dealer_deck[-1].set_Value(1)
        self.dealer_total += 1
    else:
      self.dealer_total += self.dealer_deck[-1].value

  def win(self,player):
    self.chips += player.current_bet

  def loss(self, player):
    self.chips -= player.current_bet

class Runner:

  def run_player(self, player, dealer):

    res = "result"
    compl = False

    while(compl != True):
      res = input("Hit or stay?: ")
      if (res.lower() == "stay"):
        print("\n" * 10)
        return True
      elif (res.lower() == "hit"):
        player.hit()
        print(player.check_total())
        if (player.check_total() == "Bust!"):
          player.loss()
          dealer.win(player)
          print("Dealer's total of chips is now {}".format(dealer.chips) + "\n")
          return False
          
  def run_dealer(self,player,dealer):

    if (dealer.chips <= 0):
      return "Dealer has lost!"
    elif(player.chips <= 0):
      return "Player has lost!"

    dealer.display_cards()
    if (dealer.dealer_total < 17):
      dealer.hit()
      if(dealer.check_total() == "Dealer has Bust!"):
        print(dealer.check_total())
        player.win()
        dealer.loss(player)
        print("Dealer's total of chips is now {}".format(dealer.chips)+ "\n")
    
    if (dealer.dealer_total >= 17 and dealer.dealer_total <= 21):
      if (dealer.dealer_total > player.player_total):
        print("Dealer has won!")
        dealer.win(player)
        player.loss()
        print("Dealer's total of chips is now {}".format(dealer.chips))
      elif(dealer.dealer_total == player.player_total):
        print("Draw!")
      else:
        dealer.loss(player)
        player.win()
        print("Dealer's total of chips is now {}".format(dealer.chips))

class Main:
  def runner(self):
    r = Runner()
    d = Dealer(100)
    p = Player(100)

    playing = True

    while(playing):
      res = r.run_player(p,d)
      if (res == False):
        curr_player_chips = p.chips
        curr_dealer_chips = d.chips
        if (curr_player_chips <= 0 or curr_dealer_chips <= 0):
          print("Game Over")
          playing = False
        else:
          p = Player(curr_player_chips)
          d = Dealer(curr_dealer_chips)
          r.run_player(p,d)
      else :
        r.run_dealer(p,d)
        curr_player_chips = p.chips
        curr_dealer_chips = d.chips
        if (curr_player_chips <= 0 or curr_dealer_chips <= 0):
          print("Game Over")
          playing = False
        else:
          p = Player(curr_player_chips)
          d = Dealer(curr_dealer_chips)

m = Main()
m.runner()

