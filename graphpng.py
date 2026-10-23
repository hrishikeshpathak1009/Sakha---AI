from graph import graph

with open("graph.mmd", "w") as f:
    f.write(graph.get_graph().draw_mermaid())