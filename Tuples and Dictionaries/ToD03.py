"""
We represent scores of batsmen across a sequence of matches in a two level dictionary as follows: 
d = {'match1': {'player1':57, 'player2':38}, 
'match2': {'player3':9, 'player1':42}, 
'match3': {'player2':41, 'player4':63, 'player3':91} 
}
Each match is identified by a string, as is each player. The scores are all integers. 
Define a Python function highestscore(d) that reads a dictionary d of this form and identifies the player with the highest total score. 
Your function should return a pair (playername, topscore) where playername is the name of the player with the highest score, and topscore is an integer, 
the total score of playername. 
The input will be such that there are never any ties for highest total score.
"""

d = {
  'match1': {
    'player1':57, 
    'player2':38
    },
  'match2': {
    'player3':9, 
    'player1':42
    },
  'match3': {
    'player2':41, 
    'player4':63, 
    'player3':91
    }
}

def highscore(a):
  score = dict()
  for match in a:
      for plr in d[match]:
          if plr in score:
              score[plr] += d[match][plr]
          else:
              score[plr] = d[match][plr]
  best = max(score, key=score.get)
  return best, score[best]

p, s = highscore(d)
print(p, s)

"""
Output:
player3 100
"""
