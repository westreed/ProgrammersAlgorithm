# 
# https://www.acmicpc.net/problem/1655

from collections import deque

class CenterGame:
    def __init__(self, N):
        # self.game_map = deque()
        self.game_map = []
        self.count = 0
    
    def push(self, number):
        if self.count < 2:
            self.game_map.append(number)
            self.game_map.sort()
            self.count += 1
            print(self.game_map)
            print("값", self.game_map[(self.count-1) // 2])
            if self.count == 2:
                self.game_map = deque(self.game_map)
        else:
            if self.game_map[0] > number:
                self.count += 1
                print(self.game_map)
                print("값", self.game_map[0])
            elif self.game_map[-1] >= number:
                self.game_map.popleft()
                self.game_map.appendleft(number)
                self.count += 1
                print(self.game_map)
                print("값", self.game_map[0])
            elif self.game_map[-1] < number:
                # self.game_map.pop()
                # self.game_map.append(number)
                print(self.game_map)
                print("값", self.game_map[0])


    
    def _print_center(self):
        ceter_value = self.game_map[self.center]
        print("값", ceter_value)

if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    N = int(input())
    game = CenterGame(N)
    for _ in range(N):
        game.push(int(input()))