import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure plots directory exists
PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

def plot_histograms(df, columns):
    for col in columns:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Distribution of {col}')
        plt.savefig(f"{PLOTS_DIR}/hist_{col}.png")
        plt.close()

def plot_boxplots(df, columns):
    for col in columns:
        plt.figure()
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.savefig(f"{PLOTS_DIR}/box_{col}.png")
        plt.close()

def plot_heatmap(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig(f"{PLOTS_DIR}/correlation_heatmap.png")
    plt.close()
