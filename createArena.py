import pandas as pd
import numpy as np
import random


class Arena:
    arena = None
    boardOwn = None
    boardShelling = None
    ships = None
    col = None
    shipLabel = '.'

    randDirectionC = None
    randDirectionR = None

    def __init__(self):
        self.arena = np.zeros((10, 10))
        self.col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.boardOwn = pd.DataFrame(self.arena, columns=self.col)
        self.boardShelling = pd.DataFrame(self.arena, columns=self.col)
        self.ships = [['K', 'K', 'K'], ['K', 'K', 'K'], ['K', 'K'], ['K', 'K'], ['K', 'K'],
                      ['K'], ['K'], ['K'], ['K'], ['K', 'K', 'K', 'K']]
        self.rand_start_position()
        self.add_ship()

    def rand_start_position(self):
        self.randDirectionC = self.col.index(random.choice(self.col))
        self.randDirectionR = random.randint(0, len(self.boardOwn.index) - 1)

    def add_ship(self):
        while len(self.ships) > 0:
            if self.checks(self.ships[0], self.randDirectionR, self.randDirectionC):
                del self.ships[0]
                self.rand_start_position()
            else:
                self.rand_start_position()

        print(f'МОЯ ДОСКА \n{self.boardOwn}')
        print(f'ДОСКА ПРОТИВНИКА \n {self.boardShelling}')

    def checks(self, ship, rRow, rCol):
        if self.check_r(ship, rRow, rCol):
            for sh in range(0, len(ship)):
                self.boardOwn.loc[rRow, self.col[rCol + sh]] = self.shipLabel
            return True
        if self.check_l(ship, rRow, rCol):
            for sh in range(0, len(ship)):
                self.boardOwn.loc[rRow, self.col[rCol - sh]] = self.shipLabel
            return True
        if self.check_up(ship, rRow, rCol):
            for sh in range(0, len(ship)):
                self.boardOwn.loc[rRow - sh, self.col[rCol]] = self.shipLabel
            return True
        if self.check_down(ship, rRow, rCol):
            for sh in range(0, len(ship)):
                self.boardOwn.loc[rRow + sh, self.col[rCol]] = self.shipLabel
            return True
        else:
            self.rand_start_position()
            return False

    def check_r(self, ship, rRow, rCol):
        try:
            rowStart = self.check_zero(rRow - 1)
            rowFin = self.check_zero(rRow + 1)
            colStart = self.check_zero(rCol - 1)
            colFin = self.check_zero(rCol + len(ship))
            zone = self.boardOwn.loc[rowStart:rowFin, self.col[colStart]: self.col[colFin]]

        except Exception as e:
            print(e)
            return False
        check_len_ship = (len(self.col) >= rCol + len(ship))
        if check_len_ship and self.check_zone(zone):
            return True
        else:
            return False

    def check_l(self, ship, rRow, rCol):
        try:
            rowStart = self.check_zero(rRow - 1)
            rowFin = self.check_zero(rRow + 1)
            colStart = self.check_zero(rCol-len(ship))
            colFin = self.check_zero(rCol+1)
            zone = self.boardOwn.loc[rowStart:rowFin, self.col[colStart]: self.col[colFin]]
        except Exception as e:
            print(e)
            return False
        check_len_ship = (rCol-1 >= len(ship))
        if check_len_ship and self.check_zone(zone):
            return True
        else:
            return False

    def check_up(self, ship, rRow, rCol):
        try:
            rowStart = self.check_zero(rRow - len(ship))
            rowFin = self.check_zero(rRow + 1)
            colStart = self.check_zero(rCol-1)
            colFin = self.check_zero(rCol+1)
            zone = self.boardOwn.loc[rowStart:rowFin, self.col[colStart]: self.col[colFin]]
        except Exception as e:
            print(e)
            return False
        check_len_ship = (rRow - 1 >= len(ship))
        if check_len_ship and self.check_zone(zone):
            return True
        else:
            return False

    def check_down(self, ship, rRow, rCol):
        try:
            rowStart = self.check_zero(rRow-1)
            rowFin = self.check_zero(rRow+len(ship))
            colStart = self.check_zero(rCol-1)
            colFin = self.check_zero(rCol+1)
            zone = self.boardOwn.loc[rowStart:rowFin, self.col[colStart]:self.col[colFin]]
        except Exception as e:
            print(e)
            return False
        check_len_ship = (10 >= rRow + len(ship))
        if check_len_ship and self.check_zone(zone):
            return True
        else:
            return False

    @staticmethod
    def check_zone(zone):
        if Arena.shipLabel in zone.values:
            return False
        else:
            return True

    @staticmethod
    def check_zero(er):
        if er < 0:
            er = 0
            return er
        if er > 9:
            er = 9
            return er
        else:
            return er


Arena()
