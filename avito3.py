def determine_winner(matches):
    kosya_win_count = 0
    ksyusha_win_count = 0
    draw_count = 0

    for match in matches:
        kosya_move, ksyusha_move = match.split()
        
        if kosya_move == ksyusha_move:
            draw_count += 1
        elif (kosya_move == 'R' and ksyusha_move == 'S') or \
             (kosya_move == 'S' and ksyusha_move == 'P') or \
             (kosya_move == 'P' and ksyusha_move == 'R'):
            kosya_win_count += 1
        else:
            ksyusha_win_count += 1

    total_matches = len(matches)
    kosya_percent = (kosya_win_count / total_matches) * 100
    ksyusha_percent = (ksyusha_win_count / total_matches) * 100
    draw_percent = (draw_count / total_matches) * 100

    if kosya_win_count > ksyusha_win_count:
        winner = "Костя"
    elif ksyusha_win_count > kosya_win_count:
        winner = "Ксюша"
    else:
        return f"Ничья\nW: {kosya_percent:.2f}%\nD: {draw_percent:.2f}%\nL: {ksyusha_percent:.2f}%"

    return f"{winner}\nW: {kosya_percent:.2f}%\nD: {draw_percent:.2f}%\nL: {ksyusha_percent:.2f}%"

def main():
    import sys
    input = sys.stdin.read().strip().split('\n')
    
    results = determine_winner(input)
    print(results)

if __name__ == "__main__":
    main()

'''
Костя и Ксюша играют в Камень - Ножницы - Бумага. На вход подаются n строчек (n - произвольное целое число от 0 до 20), в которых записаны их ходы. Напишите программу, которая определит, кто выиграл в большем количестве партий и покажет статистику победителя в процентах.
R - камень (rock)
S - ножницы (scissors)
P - бумага (paper)
Формат данных на входе:
R R
R S
P P
R P
S R
, где первый символ - ход Кости, второй - ход Ксюши.

На выходе нужно указать победителя на основе партии из n игр и указать его статистику - победы (W), ничьи (D) и поражения (L).
Если количество побед у игроков равно, то вместо имени победителя нужно написать "Ничья".

Формат данных на выходе (два знака после запятой, после двоеточия - пробел):
Ксюша
W: 40.00%
D: 40.00%
L: 20.00%

Sample Input:
P S
S P
P P
P S
R S
P R
P P
S S
P P
P S

Sample Output:
Ничья
W: 30.00%
D: 40.00%
L: 30.00%
Напишите программу. Тестируется через stdin → stdout
'''
