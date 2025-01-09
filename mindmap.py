from graphviz import Digraph

# ایجاد شیء Mind Map
mind_map = Digraph(format="png", comment="ML Concepts Mind Map")

# گره اصلی
mind_map.node("ML", "Machine Learning", shape="ellipse", style="filled", color="lightblue")

# شاخه‌های اصلی
mind_map.node("SL", "Supervised Learning", shape="box", style="filled", color="lightgreen")
mind_map.node("UL", "Unsupervised Learning", shape="box", style="filled", color="lightyellow")
mind_map.node("EDA", "Exploratory Data Analysis", shape="box", style="filled", color="orange")
mind_map.node("Regression", "Regression", shape="box", style="filled", color="pink")

# زیرشاخه‌های Supervised Learning
mind_map.node("SL_Regression", "Regression (Linear, Logistic)", shape="box")
mind_map.node("SL_Classification", "Classification", shape="box")
mind_map.edge("SL", "SL_Regression")
mind_map.edge("SL", "SL_Classification")

# زیرشاخه‌های Unsupervised Learning
mind_map.node("UL_Clustering", "Clustering (K-Means, DBSCAN)", shape="box")
mind_map.node("UL_Dimensionality", "Dimensionality Reduction (PCA, t-SNE)", shape="box")
mind_map.edge("UL", "UL_Clustering")
mind_map.edge("UL", "UL_Dimensionality")

# زیرشاخه‌های EDA
mind_map.node("EDA_Scatter", "Scatter Plots", shape="box")
mind_map.node("EDA_Histogram", "Histograms", shape="box")
mind_map.node("EDA_BoxPlot", "Box Plots", shape="box")
mind_map.node("EDA_Correlation", "Correlation Analysis", shape="box")
mind_map.edge("EDA", "EDA_Scatter")
mind_map.edge("EDA", "EDA_Histogram")
mind_map.edge("EDA", "EDA_BoxPlot")
mind_map.edge("EDA", "EDA_Correlation")

# زیرشاخه‌های Regression
mind_map.node("Regression_Linear", "Linear Regression", shape="box")
mind_map.node("Regression_Polynomial", "Polynomial Regression", shape="box")
mind_map.node("Regression_Logistic", "Logistic Regression", shape="box")
mind_map.node("Regression_Feature", "Feature Importance", shape="box")
mind_map.edge("Regression", "Regression_Linear")
mind_map.edge("Regression", "Regression_Polynomial")
mind_map.edge("Regression", "Regression_Logistic")
mind_map.edge("Regression", "Regression_Feature")

# ذخیره و رندر کردن Mind Map
file_path = "ML_Mind_Map"
mind_map.render(file_path, view=True)
