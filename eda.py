import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import matplotlib.pyplot as plt
import seaborn as sns

def summary(df):
    """Generate a summary of a pandas DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to summarize.

    Returns:
        pandas.DataFrame: A summary DataFrame containing data types,
        uniqueness, missing values, and descriptive statistics.
    """
    print(f'Dataframe shape: {df.shape}')
    summ = pd.DataFrame(df.dtypes, columns=['Data Type'])
    summ['# Unique'] = df.nunique().values
    summ['Missing'] = df.isna().sum()
    summ['Missing %'] = ((df.isna().sum() / len(df)) * 100).round(1)
    desc = pd.DataFrame(df.describe(include='all').transpose())
    summ['Min'] = desc['min'].values
    summ['Max'] = desc['max'].values
    summ['Mean'] = desc['mean'].values
    summ['Standard Deviation'] = desc['std'].values

    return summ

def isna(df):
    """
    Prints the percentage of missing values in each column of the DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame for which missing values percentages are calculated.
    """
    print((df.isna().sum() / df.shape[0]) * 100)

def stratified_train_val_test_split(data, target_col, test_size=0.2, val_size=0.3, random_state=42):
    """
    Perform stratified train-validation-test split on the dataset.

    Parameters:
    -----------
    data : pandas DataFrame
        Input DataFrame containing the dataset.
    target_col : str
        Name of the target column.
    test_size : float, optional (default=0.2)
        Proportion of data to include in the test set.
    val_size : float, optional (default=0.3)
        Proportion of the remaining data after test split to include in the validation set.
    random_state : int, optional (default=42)
        Random state for reproducibility.

    """
    split = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    for train_val_index, test_index in split.split(data, data[target_col]):
        train_val_data = data.iloc[train_val_index].copy()
        test_data = data.iloc[test_index].copy()

    split = StratifiedShuffleSplit(n_splits=1, test_size=val_size, random_state=random_state) 
    for train_index, val_index in split.split(train_val_data, train_val_data[target_col]):
        X_train, X_val = train_val_data.drop(target_col, axis=1).iloc[train_index].copy(), train_val_data.drop(target_col, axis=1).iloc[val_index].copy()
        y_train, y_val = train_val_data[target_col].iloc[train_index].copy(), train_val_data[target_col].iloc[val_index].copy()

    X_test = test_data.drop(target_col, axis=1)
    y_test = test_data[target_col]

    return X_train, y_train, X_val, y_val, X_test, y_test

def plot_eda(df, col_name, full_name, continuous):
    """
    Visualize a variable with bar plots or box plots and KDE plots, faceted on the loan grade.
    - df: DataFrame containing the data.
    - col_name: the variable name in the dataframe.
    - full_name: the full variable name.
    - continuous: True if the variable is continuous, False if categorical.
    """
    fig, axs = plt.subplots(1, 2, figsize=(14, 4))

    if continuous:
        sns.boxplot(x='TARGET', y=col_name, data=df, ax=axs[0])
        axs[0].set_ylabel('')
        axs[0].set_title(full_name + ' by Target')
    else:
        grade_rates = df.groupby(col_name)['TARGET'].value_counts(normalize=True).unstack().fillna(0)
        grade_rates.plot(kind='bar', stacked=True, ax=axs[0], colormap='viridis')
        axs[0].set_ylabel('Share of Target')
        axs[0].set_xlabel(full_name)
        axs[0].set_title('Target by ' + full_name)

    if continuous:
        for target in sorted(df['TARGET'].unique()):
            target_data = df.loc[df['TARGET'] == target, col_name]
            if not target_data.empty:
                sns.kdeplot(target_data, ax=axs[1], label=f'Target {target}', shade=True)
        axs[1].set_title(full_name + ' Distribution by Target')
        axs[1].legend(title='Target')
    else:
        grade_ct = pd.crosstab(df[col_name], df['TARGET'])
        sns.heatmap(grade_ct, annot=False, fmt="d", cmap="YlGnBu", ax=axs[1])
        axs[1].set_title('Cross-tab ' + full_name + ' by Target')
        plt.tight_layout()

    plt.tight_layout()
    plt.show()