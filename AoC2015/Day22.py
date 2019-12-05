effects = [0,0,0] #Armour, poision, recharge

#Cost damage heal effects

def get_next(state,currentMana):
    global d
    found = []
    for i in d.keys():
        if d[i][0] <= currentMana:
            found.append(d[i])
    return found
from copy import deepcopy
class Fight():
    def __init__(self,PlayerMana, BossHP, PlayerHP,  BossDamage, PlayerArmour=0, BossArmour=0, effects=[0,0,0], movesBefore=[], total=0):
        self.BossHP = BossHP
        self.PlayerHP = PlayerHP
        self.PlayerMana = PlayerMana
        self.playerArmour = PlayerArmour
        self.BossDamage = BossDamage
        self.bossArmour = BossArmour
        self.movesBefore = movesBefore
        self.effects = effects
        self.total = total
        self.moveDic = {0:[53, 4, 0,{}], 1:[73, 2, 2,{}], 2:[113, 0, 0,{0:6}], 3:[173, 0, 0,{1:6}], 4:[229, 0, 0, {1:5}]}
        # Cost damage heal effects
    def eval_move(self, move):
        newState = [self.PlayerMana, self.BossHP, self.PlayerHP, self.BossDamage,
                    self.playerArmour, self.bossArmour]
        can_go = [0, 0, 0]
        if self.effects[0] > 0:
            self.playerArmour = 7
            self.effects[0] -= 1
        else:
            self.playerArmour = 0
            can_go[0] = 1
        if self.effects[1] > 0:
            self.BossHP -= 3
            self.effects[1] -= 1
        else:
            can_go[1] = 1

        if self.effects[2] > 0:
            self.PlayerMana += 101
            self.effects[2] -= 1
        else:
            can_go[2] = 1

        if self.BossHP <= 0:
            return (self.total, self.movesBefore, self.PlayerHP)

        #PlayerMove
        newState = [self.PlayerMana-move[0], self.BossHP-move[1], self.PlayerHP+move[2], self.BossDamage, self.playerArmour, self.bossArmour]

        self.isBossDead()

        newEffects = deepcopy(self.effects)
        if len(move[3].keys()) > 0:
            self.effects[list(move[3].keys())[0]] = list(move[3].values())[0]
            newEffects[list(move[3].keys())[0]] = list(move[3].values())[0]
            newState.append(newEffects)
        else:
            newState.append(self.effects)

        if self.effects[1] > 0:
            newState[1] -= 3
            newState[-1] -= 1
            print(newState[-1])
            if newState[1] <= 0:
                return (self.total, self.movesBefore, self.PlayerHP)

        damage = self.BossDamage-self.playerArmour
        if damage < 1:
            damage = 1
        newState[2] = self.bossMove()
        if self.PlayerHP <= 0:
            return (999999999, [])
        newMoves = deepcopy(self.movesBefore)
        newMoves.append(move)
        newState.append(newMoves)
        newState.append(self.total+move[0])
        if len(newState)==1:
            print(newState)
        return newState
    def bossMove(self):
        print(self.effects, "here")
        if self.effects[1] > 0:
            self.BossHP -= 3
            self.effects[1] -= 1
            self.isBossDead()

        damage = self.BossDamage-self.playerArmour
        if damage < 1:
            damage = 1
        return self.PlayerHP-damage

    def isBossDead(self):
        if self.BossHP <= 0:
            return (self.total, self.movesBefore, self.PlayerHP)

    def eval_effects(self):
        can_go = [0,0,0]
        if self.effects[0] > 0:
            self.playerArmour = 7
            self.effects[0] -= 1
        else:
            self.playerArmour = 0
            can_go[0] = 1
        if self.effects[1] > 0:
            self.BossHP -= 3
            self.effects[1] -= 1
        else:
            can_go[1] = 1

        if self.effects[2] > 0:
            self.PlayerMana += 101
            self.effects[2] -= 1
        else:
            can_go[2] = 1
        return can_go
    def gen_moves(self):
        possible = []
        for i in range(len(self.moveDic.keys())):
            if i-2 >= 0:
                if self.effects[i-2]==0:
                    possible.append(self.moveDic[i-2])
            else:
                possible.append(self.moveDic[i])
        return possible




graph = {}
seen = []
to_check = []
ans = set()
ans.add(99999)
Part1 = Fight(250, 13,10,8)
to_check.append(Part1)
c = 0
Part1 = Fight(*Part1.eval_move([173, 0, 0,{1:6}]))
print(Part1.BossHP)
"""
while to_check:
    n = to_check.pop(0)
    c += 1
    for nextMove in n.gen_moves():
        newState = n.eval_move(nextMove)
        if len(newState)==3:
            print(newState[1], "moves", newState[-1])
            ans.add(newState[0])
        else:
            try:
                newState = Fight(*newState)
                if newState not in to_check:
                    to_check.append(newState)
            except:
                pass

    print(min(ans))"""