# mst-solver
> A desktop application based on PyQt5 to solve the minimum spanning tree problem. The app also implement clustering by using the MST algorithm.

![Screenshot of the App](https://i.imgur.com/xDhGVl2.png)

## Usage
1. Clone the repository
2. Install the dependencies
3. Run the app by `python src/ui.py`
4. Choose the input file (the format of the input file is an adjacency matrix of the graph, see the files in `test` for examples)
5. If you want to add or remove edges, the top three top input boxes are for you. The first one is the start vertex, the second one is the end vertex, and the last one is the weight of the edge. After you input the information, click the `Add` button to add the edge, or click the `Del` button to remove the edge. When you are deleting an edge you don't need to input the weight.
6. If you want to add or remove vertices, the middle input box is for you. Input the vertex number you want to add or remove, and click the `Add` or `Del` button.
7. Select the algorithm you want to use, and click the `Find MST` button to find the MST of the graph.
8. For the clustering part, you can choose the number of clusters you want to have by inputing the number at the bottom input box, and click the `Find Cluster` button to find the clusters of the graph.
9. The `reset` button is for you to reset the graph to the original graph.

## Requirements
- Python 3.6+
- PyQt5
- matplotlib

## Contributors
- [Marthen](https://github.com/Marthenn)