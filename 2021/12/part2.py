from collections import defaultdict

with open('input.txt') as f:
    edge_graph = defaultdict(list)
    for line in f.readlines():
        (edge_start, edge_end) = line.strip().split("-")
        edge_graph[edge_start].append(edge_end)
        edge_graph[edge_end].append(edge_start)

# print(edge_graph.items())

valid_paths = []
def build_path(current_node, path_taken, has_second=False):
    for node in edge_graph[current_node]:
        current_path_taken = path_taken + [node]
        if node == 'end':
            valid_paths.append(current_path_taken)
        else:
            if node.isupper():
                build_path(node, current_path_taken, has_second)
            else:
                if node not in path_taken:
                    build_path(node, current_path_taken, has_second)
                elif not has_second and node not in ['start', 'end']:
                    build_path(node, current_path_taken, True)

for node in edge_graph['start']:
    current_path_taken = ['start'] + [node]
    build_path(node,current_path_taken)

for path in valid_paths:
    print(','.join(path))

print(len(valid_paths))
