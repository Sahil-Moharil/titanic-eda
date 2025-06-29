def show_basic_info(df):
    print("Shape of Data:", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDescriptive Stats:\n", df.describe())
