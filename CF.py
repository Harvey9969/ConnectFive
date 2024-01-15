def run_game():
  board = []
  for i in range(19):
    board.append([]) 

    for j in range(19):
      board[i].append("  ")


  def show():
    print('------------------------------------------------------------------------------------------------')
    for i in range (19):
      print('|', end='')
      for j in range (19):
        print(' '+board[i][j]+' |', end = '')
      row = str(i+1)
      if len(row) == 1:
        row = "0"+row
      print('', row)
      print('------------------------------------------------------------------------------------------------')
    print("  01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   17   18   19")
  show()
  list_for_r = []
  list_for_w = []
  def check_player_wins(board, location):
    # list_for_r = []
    # list_for_w = []
    x = location[0] - 1
    y = location[1] - 1
    c = board[x][y] 
    for dx, dy in  [[1, 0], [0, 1], [-1, 1], [-1, -1], [0, -1], [-1, 0], [1, 1], [1, -1]]: 
      connect_number = 0
      for i in range(5):
        x2 = x + i * dx
        y2 = y + i * dy
        if x2 >= 0 and x2 <= 18 and y2 >= 0 and y2 <= 18 and board[x2][y2] == c:
          connect_number += 1
        else:  
          connect_number = 0
          x0 = x2 - dx
          y0 = y2 - dy
          for j in range(5):
            x3 = x0 - j * dx
            y3 = y0 - j * dy
            # print(connect_number)
            if x3 >= 0 and x3 <= 18 and y3 >= 0 and y3 <= 18 and board[x3][y3] == c:
              connect_number += 1
            elif x3 >= 0 and x3 <= 18 and y3 >= 0 and y3 <= 18 and board[x3][y3] == '  ':
              # print(x3, y3)
              connect_number += 6
              # print(connect_number)
              show()
              break
            else:           
              break
          break
      if connect_number == 5:
        return True    
      if connect_number == 10:  # if 4 pieces are connect and the next place is a space (trigger connent_number += 6)
        # print(x3, y3)
        board[x3][y3] = '❌' # the space will become x
        location1 = [x3, y3]
        if round % 2 == 1: # add to different list depend on the round by determine whether it's for red or white
          list_for_r.append(location1) 
        else:
          list_for_w.append(location1)
      if connect_number == 9:
        if board[x3-dx][y3-dy] == c and board[x3+2*dx][y3+2*dy]  == c and board[x3+3*dx][y3+3*dy] == c and board[x3+dx][y3+dy]: # the last input for player must connect with two other pieces. the only piece need to check is the one that has a space between it
          # print(x3, y3)
          board[x3][y3] = '❌' # if the condition exist, make the space become x
          location1 = [x3, y3]
          if round % 2 == 1:  # add to the corresponding list
            list_for_r.append(location1)
          else:
            list_for_w.append(location1)
          break
      if connect_number == 8: 
        # print(x3, y3)
        if board[x3+dx][y3+dy] == c and board[x3+2*dx][y3+2*dy] == c and board[x3-dx][y3-dy] == c and board[x3-2*dx][y3-2*dy] == c: # the 8 exist only when there are two pieces of two seperate by a space
          board[x3][y3] = '❌' # if the condition exist, make the space become x
          location1 = [x3, y3]
          if round % 2 == 1: # add the x location to the corresponding list
            list_for_r.append(location1)
          else:
            list_for_w.append(location1)
          break
      if connect_number == 7: 
        if board[x3+dx][y3+dy] == c and board[x3-dx][y3-dy] == c and board[x3-2*dx][y3-2*dy] == c and board[x3-3*dx][y3-3*dy] == c: # another space there are three piece that are connected
          board[x3][y3] = '❌'# if the condition exist, make the space become x
          location1 = [x3, y3]
          if round % 2 == 1: # add the x location to the corresponding list
            list_for_r.append(location1)
          else:
            list_for_w.append(location1)
          break
      print(list_for_r) 
      print(list_for_w)
      if round % 2 == 0:
        for i in list_for_r:
          if i[0] == location[0]-1 and i[1] == location[1]-1:
            list_for_r.remove(i)
            break
          else:
            board[i[0]][i[1]] =  '  '
        for i in list_for_w:
          if i[0] == location[0]-1 and i[1] == location[1]-1:
            list_for_w.remove(i)
            break
          else:
            board[i[0]][i[1]] = '❌'
      else:
        for i in list_for_w:
          if i[0] == location[0]-1 and i[1] == location[1]-1:
            list_for_w.remove(i)
            break
          else:
            board[i[0]][i[1]] = '  '
        for i in list_for_r:
          if i[0] == location[0]-1 and i[1] == location[1]-1:
            list_for_r.remove(i)
            break
          else:
            board[i[0]][i[1]] = '❌'
      show()

    return False    


      

  print('\nGame Start!\n')
  round = 1
  all_location = []
  while round < 362:
    location = [int(x) for x in input("(Pick a location!(row, column) 01, 01 ~ 19, 19)").split()]
    while location[0] > 19 or location[1] > 19 or board[location[0]-1][location[1]-1] == '🔴' or board[location[0]-1][location[1]-1] == '⚪':
        if location[0] > 19 or location[1] > 19:
            print('Choose number less than or equal to 19')
        else:
            print('Spot already taken, choose an other spot')
        location = [int(x) for x in input("(Pick a location!(row, column) 01, 01 ~ 19, 19)").split()]
    # print(location)
    all_location.append(location)
    #print(all_location)
    print('Round ' + str(round))
    if round % 2 == 1:
        board[location[0]-1][location[1]-1] = '🔴'
    else:
        board[location[0]-1][location[1]-1] = '⚪'
    show()
    current_player_win = check_player_wins(board, location)

    if current_player_win:
      if round % 2 == 1:
        print('Red player win') 
      else:
        print('White player win')
      break


    # regret_or_not = input("Would you like to regret your choice? ") 
    # while regret_or_not == "yes":
    #   if regret_or_not == "yes":
    #     board[all_location[-1][0]-1][all_location[-1][1]-1] = '  '
    #     all_location.pop()
    #     round-=1
    #     show()
    #   regret_or_not = input("Would you like to regret again? ")

    round += 1 

while True:
  run_game()
  if input("Would you like to play another round? (yes or no)") != "yes":
    break



#❌❌❌❌❌❌❌ ⚪⚪⚪⚪🔴🔴🔴🔵🔵🔵