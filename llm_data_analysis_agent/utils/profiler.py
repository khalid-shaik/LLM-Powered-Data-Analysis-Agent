import pandas as pd


def get_dataset_summary(df):
    """Return basic information about the dataset."""

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "numerical_columns": len(
            df.select_dtypes(include="number").columns
        ),
        "categorical_columns": len(
            df.select_dtypes(include=["object", "category"]).columns
        )
    }

    return summary


def get_column_info(df):
    """Return information about every column."""

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    return column_info


def get_numeric_statistics(df):
    """Return statistical summary for numerical columns."""

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return pd.DataFrame()

    statistics = numeric_df.describe().T

    return statistics


def get_missing_value_report(df):
    """Return missing-value information."""

    missing = df.isnull().sum()

    missing_report = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    missing_report["Missing Percentage"] = (
        missing_report["Missing Values"]
        / len(df)
        * 100
    ).round(2)

    missing_report = missing_report[
        missing_report["Missing Values"] > 0
    ]

    return missing_report