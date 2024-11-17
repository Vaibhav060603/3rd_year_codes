from collections import defaultdict

def find(parent, i):
  """
  Finds the root of the set for a given node in the disjoint-set forest

  Args:
      parent: A list representing the parent of each node (disjoint-set forest)
      i: The node index to find the root for

  Returns:
      The root (index) of the set containing the node i
  """
  if parent[i] == i:
    return i
  return find(parent, parent[i])

def union(parent, rank, x, y):
  """
  Performs union by rank on two sets in the disjoint-set forest

  Args:
      parent: A list representing the parent of each node (disjoint-set forest)
      rank: A list representing the rank of each set (disjoint-set forest)
      x: The index of the first node
      y: The index of the second node
  """
  root_x = find(parent, x)
  root_y = find(parent, y)

  # Attach the smaller rank tree under the root of the larger rank tree
  if rank[root_x] < rank[root_y]:
    parent[root_x] = root_y
  elif rank[root_x] > rank[root_y]:
    parent[root_y] = root_x
  else:
    parent[root_y] = root_x
    rank[root_x] += 1

def kruskal_mst(graph):
  """
  Finds the minimum spanning tree of a connected, weighted graph using Kruskal's algorithm.

  Args:
      graph: A list of tuples representing edges (node1, node2, weight).

  Returns:
      A list of tuples representing the edges in the minimum spanning tree.
  """
  result = []  # To store the edges in the MST
  parent = [i for i in range(len(graph))]  # Initialize parent for disjoint-set forest
  rank = [0] * len(graph)  # Initialize rank for disjoint-set forest

  # Sort the edges by weight in non-decreasing order
  graph.sort(key=lambda edge: edge[2])

  # Iterate through sorted edges
  for edge in graph:
    u, v, weight = edge

    # Check if adding the edge creates a cycle (using disjoint-set forest)
    if find(parent, u) != find(parent, v):
      result.append(edge)
      union(parent, rank, u, v)

  return result

def get_user_graph():
  """
  Prompts user for graph structure and returns it as a list of edges

  Returns:
      A list of tuples representing edges (node1, node2, weight).
  """
  num_nodes = int(input("Enter the number of nodes in the graph: "))
  edges = []

  for i in range(num_nodes * (num_nodes - 1) // 2):
    start, end, weight = input(f"Enter edge {i+1} (format: start node end node weight): ").split()
    edges.append((start, end, int(weight)))

  return edges

if __name__ == "__main__":
  graph = get_user_graph()
  mst = kruskal_mst(graph)
  print("Minimum Spanning Tree:")
  for edge in mst:
    print(f"{edge[0]}--{edge[1]}: {edge[2]}")
