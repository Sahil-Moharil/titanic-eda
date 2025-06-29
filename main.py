from modules.data_loader import load_data
from modules.data_summary import show_basic_info
from modules.visualizer import plot_histograms, plot_boxplots, plot_heatmap
from modules.outlier_detector import detect_outliers_iqr

# Load Data
df = load_data("data/titanic.csv")

# Summary Info
show_basic_info(df)

# Visualizations
numeric_cols = ['Age', 'Fare']
plot_histograms(df, numeric_cols)
plot_boxplots(df, numeric_cols)
plot_heatmap(df)

# Detect Outliers
for col in numeric_cols:
    outliers = detect_outliers_iqr(df, col)
    print(f"\nOutliers in {col}:\n", outliers[[col]])
