#2022184025 윤지훈
import queue
# 상태를 나타내는 클래스, f(n) 값을 저장한다.
class State:
    id = 0
    def __init__(self, size, queens=[]):
        self.size = size                # 보드의 크기
        self.queens = queens            # 현재까지 배치된 퀸 위치
        self.depth = len(self.queens)   # 깊이

        self.id = State.id
        State.id += 1

    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
    def expand(self):
        result = []
        col = self.depth
        for row in range(self.size):
            new_queens = self.queens + [(col, row)]
            result.append(State(self.size, new_queens))
        return result

    # f(n)을 계산하여 반환한다.
    def f(self):
        return self.h()+self.g()

    # 겹치는 퀸 확인 및 점수 계산해 리턴
    def h(self):
        score = 0
        for i in range(len(self.queens)):
            c1, r1 = self.queens[i]
            for j in range(i + 1, len(self.queens)):
                c2, r2 = self.queens[j]
                # 같은 행
                if r1 == r2:
                    score += 1
                # 같은 대각선
                elif abs(c1 - c2) == abs(r1 - r2):
                    score += 1
        return score

    
    # 시작 노드로부터의 깊이를 반환한다.
    def g(self):
        return self.depth

    def __eq__(self, other):
        return self.queens == other.queens

    def __ne__(self, other):
        return self.queens != other.queens

    # 상태와 상태를 비교하기 위하여 less than 연산자를 정의한다.
    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()

    # 객체를 출력할 때 사용한다.
    def __str__(self):
        board = [["#" for j in range(self.size)] for i in range(self.size)]
        for c, r in self.queens:
            board[c][r] = 'Q'
        printing = "\n"
        for col in range(self.size):
            for row in range(self.size):
                printing += str(board[row][col]) + " "
            printing += "\n"
        return printing + "\n------------------"

# open 리스트는 우선순위 큐로 생성한다.
open_queue = queue.PriorityQueue()
closed_queue = [ ]
depth = 0
count = 0
visited = { 0:None }

board_size = int(input("보드의 크기를 입력하세요: "))
board = [["#" for j in range(board_size)] for i in range(board_size)]  # 초기 상태
open_queue.put(State(board_size))

while not open_queue.empty():
    current = open_queue.get()
    count += 1
    
    print(count)
    print(current)

    if current.depth == board_size:
        if current.h() == 0:
            print("탐색 성공")
            parent = visited[current.id]
            path = []
            while parent:
                path.insert(0, parent)
                parent = visited[parent.id]
            path.append(current)
            for node in path:
                print(node)
            print("탐색 횟수: ", count)
            print("2022184025 윤지훈")
            break
        else:
            continue

    closed_queue.append(current)

    for state in current.expand():
        if state.h() != 0:
            continue
        if state not in closed_queue and state not in open_queue.queue :
            open_queue.put(state)
            visited[state.id] = current
        else:
            print ('탐색 실패')