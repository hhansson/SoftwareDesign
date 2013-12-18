from Tkinter import*
from canvassing import*


class Gameplay(object):
    '''Defines legal movements for pieces'''
 
    def __init__(self,grid):
        self.grid=grid
        self.pieces_to_change = set()
        self.board = {}
        for i in range(8):
            for k in range (8):
                self.board[i,k] = 'E'
        self.board[3,4]='black'
        self.board[3,3]='white'
        self.board[4,3]='black'
        self.board[4,4]='white'
        self.playernum = 1
        self.event_space = 0
        print self.board
        print 'Initializing.'

    def pre_direct(self):
        self.pieces_to_change = set()
        self.event_space = 0
        self.playernum += 1
        if self.playernum%2 == 0:
            self.player = 'white'
        if self.playernum%2 == 1:
            self.player = 'black'
        if self.player == 'black':
            self.oppcolor = 'white'
        else:
            self.oppcolor = 'black'

    def Change(self, pieces):
        for coord in pieces:
            print coord
            self.board[coord] = self.player
            self.event_space += 1
            self.pieces_to_change = set()


        #return self.player

    def direct1(self,player,space):
        '''checks diagonal positive positive (northeast): x+1, y-1'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if space[0]+i == 8:
                    break
                if space[1]-i == -1:
                    break
                if self.board[(space[0]+i),(space[1]-i)] == oppcolor:
                    self.pieces_to_change.add(((space[0]+i),(space[1]-i)))
                if self.board[(space[0]+i),(space[1]-i)] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]+i),(space[1]-i)] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct1'
        print self.board[space]

    def direct2(self,player,space):
        '''checks upward(north): x+0, y-1'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            print '1'
            for i in range(1,8):
                if (space[1]-i) == -1:
                    print '2'
                    break
                if self.board[(space[0]),(space[1]-i)] == oppcolor:
                    print '3'
                    self.pieces_to_change.add(((space[0]),(space[1]-i)))
                if self.board[(space[0]),(space[1]-i)] == 'E':
                    print '4'
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]),(space[1]-i)] == self.player:
                    print '5'
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct2'
        print self.board[space]

    def direct3(self,player,space):
        '''checks diagonal negative positive (northwest): x-1, y-1'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if (space[0]-i) == -1:
                    break
                if (space[1]-i) == -1:
                    break
                if self.board[(space[0]-i),(space[1]-i)] == oppcolor:
                    self.pieces_to_change.add(((space[0]-i),(space[1]-i)))
                if self.board[(space[0]-i),(space[1]-i)] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]-i),(space[1]-i)] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct3'
        print self.board[space]


    def direct4(self,player,space):
        '''checks left(west): x-1, y+0'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if (space[0]-i) == -1:
                    break
                if self.board[(space[0]-i),(space[1])] == oppcolor:
                    self.pieces_to_change.add(((space[0]-i),(space[1])))
                if self.board[(space[0]-i),(space[1])] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]-i),(space[1])] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct4'
        print self.board[space]

    def direct5(self,player,space):
        '''checks diagonal negative negative (southwest): x-1, y+1'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if (space[0]-i) == -1:
                    break
                if (space[1]+i) == 8:
                    break
                if self.board[(space[0]-i),(space[1]+i)] == oppcolor:
                    self.pieces_to_change.add(((space[0]-i),(space[1]+i)))
                if self.board[(space[0]-i),(space[1]+i)] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]-i),(space[1]+i)] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct5'
        print self.board[space]

    def direct6(self,player,space):
        '''checks downward (south): x+0, y+1'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if (space[1]+i) == 8:
                    break
                if self.board[(space[0]),(space[1]+i)] == oppcolor:
                    self.pieces_to_change.add(((space[0]),(space[1]+i)))
                if self.board[(space[0]),(space[1]+i)] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]),(space[1]+i)] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct6'
        print self.board[space]

    def direct7(self,player,space):
        '''checks diagonal positive negative (southeast): x+1, y+1'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if (space[0]+i) == 8:
                    break
                if (space[1]+i) == 8:
                    break
                if self.board[(space[0]+i),(space[1]+i)] == oppcolor:
                    self.pieces_to_change.add(((space[0]+i),(space[1]+i)))
                if self.board[(space[0]+i),(space[1]+i)] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]+i),(space[1]+i)] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct7'
        print self.board[space]

    def direct8(self,player,space):
        '''checks right (east): x+1, y+0'''
        self.pieces_to_change = set()
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E':
            for i in range(1,8):
                if (space[0]+i) == 8:
                    break
                if self.board[(space[0]+i),(space[1])] == oppcolor:
                    self.pieces_to_change.add(((space[0]+i),(space[1])))
                if self.board[(space[0]+i),(space[1])] == 'E':
                    self.pieces_to_change = set()
                    break
                if self.board[(space[0]+i),(space[1])] == self.player:
                    if i >= 2:
                        self.Change(self.pieces_to_change)
                        break
                    else:
                        break
        print 'direct8'
        print self.board[space]

    def fill_event(self,space):
        if self.event_space >= 1:
            self.board[space] = self.player


    
    def updateBoard(self,coordinate):
        print self.pre_direct()
        print self.direct1(self.player,coordinate)
        print self.direct2(self.player,coordinate)
        print self.direct3(self.player,coordinate)
        print self.direct4(self.player,coordinate)
        print self.direct5(self.player,coordinate)
        print self.direct6(self.player,coordinate)
        print self.direct7(self.player,coordinate)
        print self.direct8(self.player,coordinate)
        print self.fill_event(coordinate)
        # print self.empty_space(coordinate,self.player)
        self.grid.makeBoard()
        print self.board
        black = 0
        white = 0
        for coordinates, value in self.board.items():
            if value == "black":
                black += 1
            elif value == "white":
                white += 1
        print 'black:' + str(black)
        print 'white:' + str(white)

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    
   

    root = Tk()
    gui = Board(root)
    root.mainloop()

    print("done looping")

    #coordinate = gui.point
    #print coordinate


   

    #test_game.empty_space(coordinate,test_game.player)
    # print test_game.board



