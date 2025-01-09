import os
import graphviz
from graphviz import Digraph

def setup_graphviz_path():
    """Adds the Graphviz bin folder to the system's PATH."""
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

def create_mind_map():
    """Creates and renders a mind map for Machine Learning concepts."""
    mind_map = Digraph(format="svg", comment="Combined Mind Map: Day 1 and Day 2")

    # Graph settings
    mind_map.graph_attr.update({
        'rankdir': 'TB',  # Top to Bottom
        'splines': 'ortho',  # Orthogonal edges
        'nodesep': '0.8',  # Increased node separation
        'ranksep': '0.8',  # Increased rank separation
        'bgcolor': 'lightgray',
        'fontsize': '12',
        'fontname': 'Arial',
        'margin': '0'
    })

    # Node settings
    mind_map.node_attr.update({
        'shape': 'box',
        'style': 'filled',
        'fontname': 'Arial',
        'fontsize': '10',
        'margin': '0.2,0.1',
        'penwidth': '1.0'  # Thicker border for nodes
    })

    # Edge settings
    mind_map.edge_attr.update({
        'color': 'black',
        'fontsize': '9',
        'fontname': 'Arial',
        'arrowsize': '0.8',
        'penwidth': '1.0'  # Thicker edges
    })

    # Root node
    mind_map.node("ML", "Machine Learning\n(Day 1 + Day 2)", shape="ellipse", color="lightblue", fontname="Arial Bold", penwidth='2.0')

    # Main nodes
    main_nodes = {
        "EDA": "Exploratory Data Analysis",
        "Unsupervised Learning": "Unsupervised Learning",
        "Supervised Learning": "Supervised Learning"
    }
    for key, value in main_nodes.items():
        mind_map.node(key, value, color="orange" if key == "EDA" else "lightyellow" if key == "Unsupervised Learning" else "lightgreen")

    # Day 1 branches
    mind_map.node("SL", "Supervised Learning", color="lightgreen")
    mind_map.node("UL", "Unsupervised Learning", color="lightyellow")
    mind_map.node("Regression", "Regression", color="pink")

    # Day 1 sub-branches
    day1_sub = {
        "SL_Regression": "Regression\n(Linear, Logistic)",
        "SL_Classification": "Classification",
        "UL_Clustering": "Clustering\n(K-Means, DBSCAN)",
        "UL_Dimensionality": "Dimensionality Reduction\n(PCA, t-SNE)",
        "EDA_Scatter": "Scatter Plots",
        "EDA_Histogram": "Histograms",
        "EDA_BoxPlot": "Box Plots",
        "EDA_Correlation": "Correlation Analysis",
        "Regression_Linear": "Linear Regression",
        "Regression_Polynomial": "Polynomial Regression",
        "Regression_Logistic": "Logistic Regression",
        "Regression_Feature": "Feature Importance"
    }
    for key, value in day1_sub.items():
        mind_map.node(key, value)

    # Connecting Day 1 branches
    mind_map.edges([
        ("SL", "SL_Regression"),
        ("SL", "SL_Classification"),
        ("UL", "UL_Clustering"),
        ("UL", "UL_Dimensionality"),
        ("EDA", "EDA_Scatter"),
        ("EDA", "EDA_Histogram"),
        ("EDA", "EDA_BoxPlot"),
        ("EDA", "EDA_Correlation"),
        ("Regression", "Regression_Linear"),
        ("Regression", "Regression_Polynomial"),
        ("Regression", "Regression_Logistic"),
        ("Regression", "Regression_Feature")
    ])

    # Day 2 branches
    day2_nodes = {
        "Logistic": "Logistic Regression\n(Day 2)",
        "KMeans": "K-Means Clustering\n(Day 2)",
        "OverUnder": "Overfitting & Underfitting\n(Day 2)",
        "Eval": "Model Evaluation\n(Day 2)"
    }
    for key, value in day2_nodes.items():
        color = "pink" if key == "Logistic" else "lightyellow" if key == "KMeans" else "orange" if key == "OverUnder" else "purple"
        mind_map.node(key, value, color=color)

    # Day 2 sub-branches
    day2_sub = {
        "Log_App": "Applications:\nSpam Detection,\nDisease Prediction",
        "Log_Prob": "Predicts Probabilities\n(0/1)",
        "K_App": "Applications:\nCustomer Segmentation",
        "K_Steps": "Steps:\nChoose K,\nAssign Points,\nUpdate Centroids",
        "Over": "Overfitting:\nToo Complex,\nPoor Generalization",
        "Under": "Underfitting:\nToo Simple,\nMisses Patterns",
        "CrossVal": "Cross-Validation",
        "Metrics": "Metrics:\nAccuracy,\nPrecision,\nRecall"
    }
    for key, value in day2_sub.items():
        mind_map.node(key, value)

    # Connecting Day 2 branches
    mind_map.edges([
        ("Logistic", "Log_App"),
        ("Logistic", "Log_Prob"),
        ("KMeans", "K_App"),
        ("KMeans", "K_Steps"),
        ("OverUnder", "Over"),
        ("OverUnder", "Under"),
        ("Eval", "CrossVal"),
        ("Eval", "Metrics")
    ])

    # Connect main topics to the root node
    mind_map.edge("ML", "Supervised Learning", style="dashed", color="blue")
    mind_map.edge("ML", "Unsupervised Learning", style="dashed", color="blue")
    mind_map.edge("ML", "EDA", style="dashed", color="blue")
    mind_map.edge("ML", "Regression", style="dashed", color="blue")

    # Render mind map
    file_path = "ML_Mind_Map_Day1_Day2"
    mind_map.render(file_path, view=False)

    return f"{file_path}.svg"

if __name__ == "__main__":
    setup_graphviz_path()
    svg_path = create_mind_map()
    print(f"Mind map generated at {svg_path}")