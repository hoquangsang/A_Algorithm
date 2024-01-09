import pygame
from maze import SearchSpace, Node
from const import*

def draw_path(g: SearchSpace, father: list, sc: pygame.Surface):
    current_id = g.goal.id
    path = []

    while current_id != -1:
        path.append(g.grid_cells[current_id])
        current_id = father[current_id]

    # Draw the path
    for idx in range(len(path) - 1):
        pygame.draw.line(sc, WHITE, path[idx].rect.center, path[idx + 1].rect.center, 1)
        pygame.time.delay(30)
        pygame.display.update()

def DFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.id]
    closed_set = set()
    father = [-1] * g.get_length()

    while open_set:
        current_id = open_set.pop()
        current_node = g.grid_cells[current_id]

        if g.is_goal(current_node):
            print("DFS complete")
            draw_path(g, father, sc)
            return

        # Kiểm tra nếu là ô start hoặc end, không đổi màu
        if current_node != g.start and current_node != g.goal:
            current_node.set_color(YELLOW, sc)  # Đánh dấu node hiện tại đã được thăm

        closed_set.add(current_id)

        for neighbor in g.get_neighbors(current_node):
            neighbor_id = neighbor.id
            if neighbor_id not in closed_set and neighbor_id not in open_set:
                open_set.append(neighbor_id)
                father[neighbor_id] = current_id

                # Đánh dấu màu RED cho các nút kề
                if neighbor != g.start and neighbor != g.goal:
                    neighbor.set_color(RED, sc)

        pygame.time.delay(10)
        pygame.display.update()

        # Chuyển màu node hiện tại sang màu BLUE khi không còn node kề
        if current_node != g.start and current_node != g.goal and current_id not in open_set:
            current_node.set_color(BLUE, sc)

    raise NotImplementedError('not implemented')



def BFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.id]
    closed_set = set()
    father = [-1] * g.get_length()

    while open_set:
        current_id = open_set.pop(0)
        current_node = g.grid_cells[current_id]

        if g.is_goal(current_node):
            print("BFS complete")
            draw_path(g, father, sc)
            return

        # Kiểm tra nếu là ô start hoặc end, không đổi màu
        if current_node not in [g.start, g.goal]:
            current_node.set_color(YELLOW, sc)  # Đánh dấu node hiện tại đã được thăm

        closed_set.add(current_id)

        for neighbor in g.get_neighbors(current_node):
            neighbor_id = neighbor.id
            if neighbor_id not in closed_set and neighbor_id not in open_set:
                open_set.append(neighbor_id)
                father[neighbor_id] = current_id

                # Đánh dấu màu RED cho các nút kề
                if neighbor not in [g.start, g.goal]:
                    neighbor.set_color(RED, sc)

        pygame.time.delay(5)
        pygame.display.update()

        # Chuyển màu node hiện tại sang màu BLUE khi không còn node kề
        if current_node not in [g.start, g.goal] and current_id not in open_set:
            current_node.set_color(BLUE, sc)

    raise NotImplementedError('not implemented')