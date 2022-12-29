import random
x = ['búa', 'kéo', 'bao']
y = 0
while y < 10000:
    y = y + 1
    player = input('Mời bạn chọn (kéo, búa, bao): ')
    computer = random.choice(x)
    if player not in x:
        print('Không hợp lệ, vui lòng chọn lại')
    else:
        print('Bạn chọn '+ player +' máy chọn '+ computer)
    if player == computer:
        print('Hòa!')
    elif player == 'búa' :
        if computer == 'bao' :
            print('Bạn thua rồi!')
        else:
            print('Bạn đã thắng!')
    elif player == 'kéo' :
        if computer == 'búa' :
            print('Bạn thua rồi!')
        else:
            print('Bạn đã thắng!')
    elif player == 'bao' :
        if computer == 'búa' :
            print('Bạn đã thắng!')
        else:
            print('Bạn thua rồi!')
