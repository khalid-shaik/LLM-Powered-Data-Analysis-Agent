
import pandas as pd


def generate_basic_insights(df):
    """
    Generate automatic insights from the dataset.
    """

    insights = []

    # ==================================================
    # DATASET SIZE
    # ==================================================

    rows = df.shape[0]
    columns = df.shape[1]

    insights.append(
        f"The dataset contains {rows:,} rows and {columns} columns."
    )


    # ==================================================
    # MISSING VALUES
    # ==================================================

    missing_values = int(df.isnull().sum().sum())

    if missing_values == 0:

        insights.append(
            "The dataset does not contain any missing values."
        )

    else:

        insights.append(
            f"The dataset contains {missing_values:,} missing values."
        )


    # ==================================================
    # DUPLICATE ROWS
    # ==================================================

    duplicate_rows = int(df.duplicated().sum())

    if duplicate_rows == 0:

        insights.append(
            "No duplicate rows were found."
        )

    else:

        insights.append(
            f"The dataset contains {duplicate_rows:,} duplicate rows."
        )


    # ==================================================
    # NUMERICAL COLUMN INSIGHTS
    # ==================================================

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()


    for column in numerical_columns:

        # Skip completely empty columns

        if df[column].dropna().empty:
            continue

        mean_value = df[column].mean()

        min_value = df[column].min()

        max_value = df[column].max()


        insights.append(
            f"For '{column}', the average is "
            f"{mean_value:.2f}, the minimum is "
            f"{min_value:.2f}, and the maximum is "
            f"{max_value:.2f}."
        )


    # ==================================================
    # CATEGORICAL COLUMN INSIGHTS
    # ==================================================

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


    for column in categorical_columns:

        if df[column].dropna().empty:
            continue

        value_counts = df[column].value_counts()

        if not value_counts.empty:

            top_value = value_counts.index[0]

            top_count = value_counts.iloc[0]

            insights.append(
                f"In '{column}', the most frequent value "
                f"is '{top_value}' with {top_count:,} records."
            )


    # ==================================================
    # CORRELATION INSIGHTS
    # ==================================================

    if len(numerical_columns) >= 2:

        correlation = df[numerical_columns].corr()

        highest_correlation = None

        highest_pair = None


        for i in range(len(correlation.columns)):

            for j in range(i + 1, len(correlation.columns)):

                value = correlation.iloc[i, j]

                if pd.isna(value):
                    continue

                absolute_value = abs(value)

                if (
                    highest_correlation is None
                    or absolute_value > highest_correlation
                ):

                    highest_correlation = absolute_value

                    highest_pair = (
                        correlation.columns[i],
                        correlation.columns[j],
                        value
                    )


        if highest_pair is not None:

            col1 = highest_pair[0]

            col2 = highest_pair[1]

            correlation_value = highest_pair[2]


            insights.append(
                f"The strongest relationship between numerical "
                f"columns is between '{col1}' and '{col2}' "
                f"with a correlation of {correlation_value:.2f}."
            )


    return insights
