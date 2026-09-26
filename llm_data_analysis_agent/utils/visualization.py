import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_histogram(df, column):
    """Create a histogram for a numerical column."""

    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )

    return fig


def create_bar_chart(df, column):
    """Create a bar chart for a categorical column."""

    value_counts = (
        df[column]
        .value_counts()
        .head(15)
        .reset_index()
    )

    value_counts.columns = [column, "Count"]

    fig = px.bar(
        value_counts,
        x=column,
        y="Count",
        title=f"Distribution of {column}"
    )

    return fig


def create_scatter_plot(df, x_column, y_column):
    """Create a scatter plot between two numerical columns."""

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{x_column} vs {y_column}"
    )

    return fig


def create_correlation_heatmap(df):
    """Create a correlation heatmap."""

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return None

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig


def get_numerical_columns(df):
    """Return numerical columns."""

    return df.select_dtypes(
        include="number"
    ).columns.tolist()


def get_categorical_columns(df):
    """Return categorical columns."""

    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()