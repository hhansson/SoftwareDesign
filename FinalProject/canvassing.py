from Tkinter import*
from board_piece_final import*



class Board(Canvas):
    global scaling_factor

    scaling_factor=97

    def __init__(self, parent):
        Canvas.__init__(self, parent, background='forest green')    
        
        self.parent = parent
        self.parent.title("Othello")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()        
        self.game=Gameplay(self)
        self.bind("<1>", self.Move)        

    def centerWindow(self):
        self.w = scaling_factor*8
        self.h = scaling_factor*8

        self.sw = self.parent.winfo_screenwidth()
        self.sh = self.parent.winfo_screenheight()
        
        x = (self.sw - self.w)/2
        y = (self.sh - self.h)/2
        self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
        button=Button(self, text='Start',font="Helvetica 40",highlightbackground='forest green',background='forest green',bd=5,command=self.makeBoard)
        button.place(x=11*scaling_factor, y=3.5*scaling_factor)
    def makeBoard(self):
         logic = self.game
         #print logic.board
         #horizontal lines
         for n in range(1,9):
             self.create_line(0,scaling_factor*n,self.w,scaling_factor*n, fill = 'black', width=5)
         #vertical lines
         for n in range(1,9):
             self.create_line(scaling_factor*n,0,scaling_factor*n,self.w, fill = 'black',width=5)
         self.r=scaling_factor/4
         for coordinates in logic.board:
            if logic.board[coordinates] == 'white' or logic.board[coordinates] == 'black':
                 self.create_oval(int(coordinates[0])*scaling_factor+self.r,int(coordinates[1])*scaling_factor+self.r,(int(coordinates[0])+1)*scaling_factor-self.r,(int(coordinates[1])+1)*scaling_factor-self.r,fill=logic.board[coordinates],outline=logic.board[coordinates])
 
    def Move(self, event, point = None):
        #print "frame coordinates: %s,%s" % (event.x, event.y)
        if (event.x,event.y)<=(self.w,self.h):
            x=(int(event.x/scaling_factor)*scaling_factor)+(scaling_factor/2)
            y=(int(event.y/scaling_factor)*scaling_factor)+(scaling_factor/2)

            #self.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,fill='black',outline='black')
            #print(x-self.r,y-self.r,x+self.r,y+self.r)
            #print (str(int(event.x/scaling_factor)),str(int(event.y/scaling_factor)))    #returns coordinate that goes into logic code (maybe don't return this, but make it an input into code and output from code should be input of circle attributes)

            #self.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,fill='black',outline='black')
            #print(x-self.r,y-self.r,x+self.r,y+self.r)
            self.point = (int(event.x/scaling_factor)),(int(event.y/scaling_factor))    #returns coordinate that goes into logic code (maybe don't return this, but make it an input into code and output from code should be input of circle attributes)
            
            #print self.point
            self.game.updateBoard(self.point)
            #self.makeBoard()

def main():
    logic = Gameplay()
    #boarddict=logic.board
    #print board
    #root = Tk()
    #Board(root)
    #root.mainloop()
if __name__ == '__main__':
    main() 