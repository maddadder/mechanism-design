import axelrod as axl
me = axl.Human(name='me')
players = [axl.ForgivingTitForTat(), me]
match = axl.Match(players, turns=5)
match.play() 
print(match.result)
print(match.sparklines())
print(match.scores())
print(match.final_score())
