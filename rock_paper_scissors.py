import random as r
u = input('rps')
c = r.choice(['scissors', 'paper', 'rock'])
print(u, c)
if u == c:
    print('tie')
elif u == 'scissors' and c == 'paper':
    print('You win')
else:
    print('You lose')














