tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread['past'] = tarot.pop(13)
spread['present'] = tarot.pop(22)
spread['future'] = tarot.pop(10)

#print(spread)
#for key, value in spread.items():
  #print('Your', key, 'is the', value,'card.')

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

lst = zip(letters, points)
letter_to_points = {key:value for key, value in lst}
#print(letter_to_points)
letter_to_points[' '] = 0

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

brownie_points = score_word('BROWNIE')
print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points
print(player_to_points)

def play_word(player, word):
    player_to_words[player].append(word)

play_word('player1', 'DICK')
print(player_to_words)
