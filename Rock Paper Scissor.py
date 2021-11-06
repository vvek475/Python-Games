import random
def play():
    user = input("r for rock\np for papr\ns fpr scsr\nChoose one from above : ")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return 'It\'s a tie'
    if is_win(user,computer):
        return 'you won'
    return 'you lost'
def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
user='y'
while user!='n':
    print(play())
    user=input("Do u want to continue y/n : ")