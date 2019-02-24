#1   O
#2  /|\
#3  /\
#   123
player1 = True
player2 = False
m_lst = []
def disp(temp_wrd_len,temp_shw1,temp_shw2,temp_shw3,lst):
    # print(temp_shw1,temp_shw2,temp_shw3)
    import os
    os.system('cls')
    print('Guess this word:\n')
    for i in range(1,temp_wrd_len+1):
        # print('i',i)
        if i == temp_shw1 or i == temp_shw2 or i == temp_shw3:
            # print('_ ', end='')
            m_lst.append(lst[i-1])
            print(lst[i-1]+" ", end = '')
        else:
            print('_ ', end = '')
            m_lst.append('_')
            # print(lst[i-1]+" ", end = '')
    # print(m_lst)
def disp_act(guess_word,pos2,m_lst):
    m_lst[pos2] = guess_word
    for i in range(len(m_lst)):
        print(m_lst[i]+" ",end = '')



import random as r
print('Player 1 turn:')
word = input('Enter the word>>')
while player1 == True:
    wrd_len = len(word)
    o_lst = []
    for i in word:
        o_lst.append(i)
        # print(lst)
    t_lst = o_lst.copy()
    c_lst = o_lst.copy()
    print('o_lst', o_lst)
    print('t_lst', t_lst)
    print(len(t_lst))
    player1 = False
    player2 = True

    if wrd_len <= 3:
        shw1 = r.randint(1,len(t_lst)-1)
        del(t_lst[shw1-1])
        c_lst[shw1-1] = " "
        shw2 = None
        shw3 = None
        print('t_lst',t_lst)
        print('o_lst',o_lst)
        disp(wrd_len,shw1,shw2,shw3,o_lst)

    elif wrd_len <= 7:
        shw1 = r.randint(1,len(t_lst)-1)
        print('shw1',shw1)
        del(t_lst[shw1-1])
        c_lst[shw1-1] = " "
        print(c_lst)
        shw2 = r.randint(1,len(t_lst)-2)
        print('shw2', shw2)
        if shw1 != shw2:
            del(t_lst[shw2-1])
            c_lst[shw2-1] = " "
        shw3 = None
        print('t_lst',t_lst)
        print('o_lst',o_lst)
        print('c_lst', c_lst)
        disp(wrd_len,shw1,shw2,shw3,o_lst)
    else:
        shw1 = r.randint(1,len(t_lst)-1)
        del(t_lst[shw1-1])
        c_lst[shw1-1] = " "
        shw2 = r.randint(1,len(t_lst)-2)
        if shw1 != shw2:
            del(t_lst[shw2-1])
            c_lst[shw2-1] = " "
        shw3 = r.randint(1,len(t_lst)-3)
        if shw2 != shw3:
            del(t_lst[shw3-1])
            c_lst[shw3-1] = " "
        disp(wrd_len,shw1,shw2,shw3,o_lst)

print('\n\nPlayer 2 turn:')
# hangman = [[' O ', '', ''], ['/','|',r'\\'],['/',' ',' '], ['/',' ',r'\\']]
def disp_hangman(wrong_count):
    hangman1 = [[' O ', '', ''], ['/','|',r'\\'],['/',' ',' '], ['/',' ',r'\\']]
    hangman2 = [[' O ', '', ''], ['/','|',r'\\'],['/',' ',r'\\'],['','','']]
    if wrong_count < 2:
        t_wrong_count = 1
    elif wrong_count < 5:
        t_wrong_count = 2
    elif wrong_count < 6:
        t_wrong_count = 3
    else: t_wrong_count = 4
    print('___\n |')
    for i in range(t_wrong_count):
        hangman = hangman1
        if wrong_count == 6:
            hangman = hangman2
        for j in range(3):
            if j<2:
                if i==0 and j ==1:
                    continue
                else:
                    print(hangman[i][j], end = '')
                # print('\ni,j',i,j)
                if i+j == wrong_count-1:
                    break
            else:
                print(hangman[i][j])
                # print('\ni,j',i,j)
                if i+j == wrong_count-1:
                    break

wrong_count = 0
while player2 == True:
    if wrong_count < 6 and t_lst != []:
        # position = int(input('Enter position>>'))
        guess_word = input('\nEnter your letter>>')
        if guess_word not in t_lst:#word:
            wrong_count += 1
            # print('cont', wrong_count)
            print('Lives remaining:', 6-wrong_count)
            disp_hangman(wrong_count)
        else:
            pos1 = t_lst.index(guess_word)
            del(t_lst[pos1])
            pos2 = c_lst.index(guess_word)
            disp_act(guess_word,pos2,m_lst)
            c_lst[pos2] = " "
            # print('c_lst', c_lst)

    else:
        print('\n\nGame Over!')
        break
