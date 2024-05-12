from enum import Enum
import random
import math

class OkeyTile:

    class Color(Enum):
        Black=0
        Blue=1
        Yellow=2 
        Red=3

    class Value(Enum):
        V1=0
        V2=1
        V3=2
        V4=3
        V5=4
        V6=5
        V7=6
        V8=7
        V9=8
        V10=9
        V11=10
        V12=11
        V13=12
    
    _color = Color(0)
    _value = Value(0)
    _intVal = 0
    _isOkey = False
    _isFalseOkey=False
    
    def __init__(self,color:Color,value:Value,isFalseOkey:bool=False,isOkey:bool=False):
        self._color = color
        self._value = value
        self._isFalseOkey = isFalseOkey
        self._isOkey = isOkey
        self._intVal = 13 * self._color.value + self._value.value

    @classmethod
    def from_int(cls,val:int):
        c = val // 13
        v = val % 13
        obj=cls(OkeyTile.Color(c),OkeyTile.Value(v))
        obj._intVal = val
        return obj

    def print(self):
        print(f"{self._color} {self._value} Okey:{self._isOkey} FalseOkey:{self._isFalseOkey}")
        return self
    

    def __lt__(self, other):
         return self._intVal < other._intVal
        
class OkeyTileStack:
    STACK_SIZE = 4 * 13
    LEN = 2 * STACK_SIZE + 2
    __arr=[0]*LEN

    stack=[]
    okeyColor=OkeyTile.Color.Black
    okeyValue=OkeyTile.Value.V1

    def __init__(self):
        pass

    def init(self):
        i = 0
        for j in range(0,self.STACK_SIZE+1):
            self.__arr[i] = j
            i+=1
        for j in range(0,self.STACK_SIZE+1):
            self.__arr[i] = j
            i+=1
        #52 false okey (always)
        return self

    def shuffle(self):
        n = len(self.__arr)-1
        while n > 1:
            k=random.randint(0,n)
            (self.__arr[k], self.__arr[n]) = (self.__arr[n], self.__arr[k])
            n-=1
        return self

    def fill_stack(self):
        if len(self.stack)>0:
            self.stack.clear()
        
        okeyColor = OkeyTile.Color(random.randint(0,3))
        okeyValue = OkeyTile.Value(random.randint(0,12))

        print(okeyColor)
        print(okeyValue)
        okey = 13 * okeyColor.value + okeyValue.value
        okeyMinusOne = 13 * okeyColor.value + math.ceil((okeyValue.value - 1) % 13)
        didRevealOkeyMinusOne = False
        for j in range(0,self.LEN):
            if(self.__arr[j] == okeyMinusOne) and (not didRevealOkeyMinusOne):
                didRevealOkeyMinusOne = True

            if self.__arr[j] == okey:
                tile = OkeyTile(color=okeyColor, value=okeyValue, isFalseOkey=False, isOkey=True)
                self.stack.append(tile)
            elif self.__arr[j] == 52:
                tile = OkeyTile(color=okeyColor, value=okeyValue, isFalseOkey=True,isOkey=False)
                self.stack.append(tile)
            else:
                self.stack.append(OkeyTile.from_int(self.__arr[j]))
        return self
    
    def draw(self):
        return self.stack.pop()


class State(Enum):
    Start=0
    Found1=1
    Found2=2
    Found=3
    Stop=4

class Player:
    tiles=[]
    starts=False
    name="Player"

    def __init__(self,name):
        self.name=name
    
    def take_tile(self,stack):
        self.tiles.append(stack.draw())
        return self
    def take_tiles(self,stack):
        for j in range(0,7):
            self.take_tile(stack=stack)
        return self
    def sort_tiles(self):
        self.tiles.sort()
        return self

    def print(self):
        for tile in self.tiles:
            tile.print()
        return self
    
    def same_color_increasing_numbers_set(self):
        self.sort_tiles()
        # j=0
        # arr=[]
        # while j<len(self.tiles)-1:
        #     i=j
        #     j+=1
        #     temp=[]w
        #     while (i+1<len(self.tiles)) and (self.tiles[i]._color==self.tiles[i+1]._color) and (self.tiles[i+1]._value.value==self.tiles[i]._value.value+1):
        #         temp.append(i)
        #         i+=1
        #         j=i
        #     if len(temp)>0:
        #         if len(temp)==1:
        #             temp.append(i)
        #         arr.append(temp)
        diff=[]
        for i in range(0,len(self.tiles)-1):
            diff.append(self.tiles[i+1]._intVal-self.tiles[i]._intVal)
        print(diff)

        j=0
        while j<len(self.tiles)-1:
            state=State.Start
            print("Start")
            for i in range(j,len(self.tiles)-1):
                if state==State.Start:
                    if diff[i]==0:
                        state=State.Start
                        print("Start")
                    elif diff[i]==1:
                        state=State.Found1
                        print("Found1")
                    elif diff[i]==2:
                        state=State.Stop
                        print("Stop")
                    elif diff[i]>=3:
                        state=State.Stop
                        print("Stop")
                    else:
                        state=State.Stop
                        print("Stop")
                
                elif state==State.Found1:
                    if diff[i]==0:
                        state=State.Found1
                        print("Found1")
                    elif diff[i]==1:
                        state=State.Found2
                        print("Found2")
                    elif diff[i]==2:
                        state=State.Stop
                        print("Stop")
                    elif diff[i]>=3:
                        state=State.Stop
                        print("Stop")
                
                elif state==State.Found2:
                    if diff[i]==0:
                        state=State.Found2
                        print("Found2")
                    elif diff[i]==1:
                        state=State.Found
                        print("Found")
                    elif diff[i]==2:
                        state=State.Stop
                        print("Stop")
                    elif diff[i]>=3:
                        state=State.Stop
                        print("Stop")
                        
                elif state==State.Found:
                    if diff[i]==0:
                        state=State.Found
                        print("Found")
                    elif diff[i]==1:
                        state=State.Found
                        print("Found")
                    elif diff[i]==2:
                        state=State.Stop
                        print("Stop")
                    elif diff[i]>=3:
                        state=State.Stop
                        print("Stop")
            
                elif state==State.Stop:
                    print("Stop")
                    print("----------")
                    j=i         
                    break
            j+=1

        return self

class OkeyTable:
    players=[]
    stack=[]

    def init(self):
        self.stack=OkeyTileStack()
        self.stack.init()
        self.stack.shuffle()
        self.stack.fill_stack()
        
        p1=Player("Player 1")
        p1.take_tiles(self.stack)
        p1.take_tile(self.stack)
        p1.starts=True
        self.players.append(p1)
        p1=Player("Player 2")
        p1.take_tiles(self.stack)
        self.players.append(p1)
        p1=Player("Player 3")
        p1.take_tiles(self.stack)
        self.players.append(p1)
        p1=Player("Player 4")
        p1.take_tiles(self.stack)
        self.players.append(p1)

        return self
    
    def print(self):
        print("Player 1:")
        self.players[0].print()
        print("Player 2:")
        self.players[1].print()
        print("Player 3:")
        self.players[2].print()
        print("Player 4:")
        self.players[3].print()

        return self
    
    
if __name__ == "__main__" :
    table=OkeyTable()
    table.init()


    table.players[0].same_color_increasing_numbers_set()
    table.players[0].print()
    