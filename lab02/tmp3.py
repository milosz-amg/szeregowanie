from queue import PriorityQueue


class Task:
    def __init__(self, processing_time, index):
        self.processing_time = processing_time
        self.index = index

    def __str__(self):
        return f"processing_time: {self.processing_time}, index:{self.index}"


class Vertex:

    def __init__(self, successors, number, index):
        self.successors = successors
        self.predecessor_number = number
        self.index: int = index
        self.visited = False

    def sort_successors(self):
        self.successors.sort()

    def __lt__(self, other):
        return self.index < other.index

    def __gt__(self, other):
        return self.index > other.index

    def __eq__(self, other):
        return self.index == other.index

    def __str__(self):
        return f"[{self.index}] successors: {self.successors}, predecessor_number:{self.predecessor_number}"


class Vertices:
    def __init__(self, vertices):
        self.vertex = vertices
        self.zero_predecessors_pq: PriorityQueue[Vertex] = PriorityQueue()
        self.to_visit = len(vertices)

    def init_priority(self):
        for vertex in self.vertex:
            if vertex.predecessor_number == 0:
                self.zero_predecessors_pq.put(vertex)

    def sort_vertex_successors(self):
        for vertex in self.vertex:
            vertex.sort_successors()

    def delete_vertex(self, index: int):
        for successor in self.vertex[index].successors:
            successor_vert = self.vertex[successor]
            successor_vert.predecessor_number -= 1
            if successor_vert.predecessor_number == 0 and not successor_vert.visited:
                self.zero_predecessors_pq.put(successor_vert)
        self.to_visit -= 1

    def __str__(self):
        return "\n".join([str(vertex) for vertex in self.vertex])


size_operation, size_edges = map(int, input().split())

operations = []
for item in range(size_operation):
    processing_time = int(input())
    operations.append(Task(processing_time, item))

vertices = Vertices([Vertex([], 0, i) for i in range(size_operation)])
for edge in range(size_edges):
    start, end = map(int, input().split())
    vertices.vertex[start - 1].successors.append(end - 1)
    vertices.vertex[end - 1].predecessor_number += 1

vertices.sort_vertex_successors()
vertices.init_priority()


def kahn_algorithm(vertices):
    output = []
    while vertices.to_visit > 0:
        vertex = vertices.zero_predecessors_pq.get()
        output.append(vertex.index + 1)
        vertices.delete_vertex(vertex.index)
        vertex.visited = True

    return output


output = kahn_algorithm(vertices)
print(*output, sep="\n")

print(sum([task.processing_time for task in operations]))