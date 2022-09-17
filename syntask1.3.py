class titandex:
    def __init__(self,name,height,strength,winning_streak):
        self.name = name
        self.height = height
        self.strength = strength
        self.winning_streak = winning_streak

    def TitanvsScout(self):
            n = int(input("number of battles between Titan and Scout: "))
            for i in range(n):
                sname = input("Enter scout name: ")
                sstr = int(input("Enter scout strength: "))
                if self.strength > sstr:
                    self.winning_streak = self.winning_streak + 1
                    print(self.name + " wins\n")
                    print("winning streak: " + str(self.winning_streak))
                elif self.strength < sstr:
                    self.winning_streak = 0
                    print(sname + " wins")
                    print(self.name + "'s winning streak reset")
                else:
                    self.winning_streak = 0
                    print("it's a draw")
                    print(self.name + "'s winning streak reset")
    def TitanvsTitan(self):
        n=int(input("enter number of battles between two Titans: "))
        for i in range(n):
            tname = input("enter name of titan: ")
            tstr = int(input("Enter strength of this titan: "))
            if tname.lower() == self.name.lower():
                print("A titan can't fight itself")
            elif self.strength > tstr:
                print(self.name+" wins")
                self.winning_streak = self.winning_streak + 1
                print(self.name+"'s winning streak:"+str(self.winning_streak))
            elif tstr > self.strength:
                self.winning_streak = 0
                print(tname + " wins")
                print(self.name+"'s winning streak reset")
            else:
                print("it's a draw")
                print(self.name+"'s winning streak reset")
name1 = input("name: ")
height1 = input("height: ")
strength1 = int(input("strength: "))
winning_streak = 0
titan1 = titandex(name1,height1,strength1,winning_streak)
titan1.TitanvsScout()
titan1.TitanvsTitan()