
import streamlit as st
import pandas as pd

from utils.profiler import (
    get_dataset_summary,
    get_column_info,
    get_numeric_statistics,
    get_missing_value_report
)

from utils.visualization import (
    create_histogram,
    create_bar_chart,
    create_scatter_plot,
    create_correlation_heatmap,
    get_numerical_columns,
    get_categorical_columns
)

from utils.analyzer import (
    generate_basic_insights
)

from utils.sql_engine import (
    dataframe_to_sqlite,
    execute_sql_query,
    get_table_schema
)

from agent.analysis_agent import (
    generate_sql
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="LLM-Powered Data Analysis Agent",
    page_icon="📊",
    layout="wide"
)


# ==========================================================
# TITLE
# ==========================================================

st.title(
    "LLM-Powered Data Analysis Agent"
)

st.write(
    "Upload a CSV or Excel file to analyze your data "
    "using Python, Pandas, SQL and Ollama."
)


# ==========================================================
# FILE UPLOADER
# ==========================================================

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)


# ==========================================================
# PROCESS DATASET
# ==========================================================

if uploaded_file is not None:

    try:

        # ==================================================
        # LOAD DATASET
        # ==================================================

        if uploaded_file.name.lower().endswith(".csv"):

            df = pd.read_csv(
                uploaded_file
            )

        else:

            df = pd.read_excel(
                uploaded_file
            )


        st.success(
            "Dataset uploaded successfully!"
        )


        # ==================================================
        # DATASET OVERVIEW
        # ==================================================

        summary = get_dataset_summary(
            df
        )

        st.subheader(
            "Dataset Overview"
        )

        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Rows",
                summary["rows"]
            )


        with col2:

            st.metric(
                "Columns",
                summary["columns"]
            )


        with col3:

            st.metric(
                "Missing Values",
                summary["missing_values"]
            )


        with col4:

            st.metric(
                "Duplicate Rows",
                summary["duplicate_rows"]
            )


        # ==================================================
        # DATASET PREVIEW
        # ==================================================

        st.subheader(
            "Dataset Preview"
        )

        st.dataframe(
            df.head(20),
            use_container_width=True
        )


        # ==================================================
        # COLUMN INFORMATION
        # ==================================================

        st.subheader(
            "Column Information"
        )

        column_info = get_column_info(
            df
        )

        st.dataframe(
            column_info,
            use_container_width=True
        )


        # ==================================================
        # NUMERICAL STATISTICS
        # ==================================================

        st.subheader(
            "Numerical Statistics"
        )

        statistics = get_numeric_statistics(
            df
        )

        if not statistics.empty:

            st.dataframe(
                statistics,
                use_container_width=True
            )

        else:

            st.info(
                "No numerical columns found."
            )


        # ==================================================
        # MISSING VALUE ANALYSIS
        # ==================================================

        st.subheader(
            "Missing Value Analysis"
        )

        missing_report = get_missing_value_report(
            df
        )

        if not missing_report.empty:

            st.dataframe(
                missing_report,
                use_container_width=True
            )

        else:

            st.success(
                "No missing values found."
            )


        # ==================================================
        # COLUMN TYPES
        # ==================================================

        st.subheader(
            "Column Types"
        )

        numerical_columns = get_numerical_columns(
            df
        )

        categorical_columns = get_categorical_columns(
            df
        )

        col1, col2 = st.columns(2)


        with col1:

            st.write(
                "### Numerical Columns"
            )

            if numerical_columns:

                for column in numerical_columns:

                    st.write(
                        f"- {column}"
                    )

            else:

                st.write(
                    "None"
                )


        with col2:

            st.write(
                "### Categorical Columns"
            )

            if categorical_columns:

                for column in categorical_columns:

                    st.write(
                        f"- {column}"
                    )

            else:

                st.write(
                    "None"
                )


        # ==================================================
        # AUTOMATIC VISUALIZATIONS
        # ==================================================

        st.subheader(
            "Automatic Visualizations"
        )


        # ==================================================
        # HISTOGRAMS
        # ==================================================

        if numerical_columns:

            st.write(
                "### Numerical Distributions"
            )

            for column in numerical_columns[:6]:

                fig = create_histogram(
                    df,
                    column
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


        # ==================================================
        # BAR CHARTS
        # ==================================================

        if categorical_columns:

            st.write(
                "### Categorical Distributions"
            )

            for column in categorical_columns[:6]:

                if df[column].nunique() <= 30:

                    fig = create_bar_chart(
                        df,
                        column
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )


        # ==================================================
        # SCATTER PLOT
        # ==================================================

        if len(numerical_columns) >= 2:

            st.write(
                "### Numerical Relationship"
            )

            x_column = numerical_columns[0]

            y_column = numerical_columns[1]

            fig = create_scatter_plot(
                df,
                x_column,
                y_column
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


        # ==================================================
        # CORRELATION HEATMAP
        # ==================================================

        if len(numerical_columns) >= 2:

            st.write(
                "### Correlation Analysis"
            )

            correlation_fig = create_correlation_heatmap(
                df
            )

            if correlation_fig is not None:

                st.plotly_chart(
                    correlation_fig,
                    use_container_width=True
                )


        # ==================================================
        # AUTOMATIC DATA INSIGHTS
        # ==================================================

        st.subheader(
            "Automatic Data Insights"
        )

        insights = generate_basic_insights(
            df
        )

        for insight in insights:

            st.write(
                f"- {insight}"
            )


        # ==================================================
        # SQL ANALYSIS
        # ==================================================

        st.subheader(
            "SQL Analysis"
        )

        st.write(
            "Run SELECT queries directly on your uploaded dataset."
        )


        # ==================================================
        # CREATE SQLITE DATABASE
        # ==================================================

        connection = dataframe_to_sqlite(
            df,
            "data"
        )


        # ==================================================
        # TABLE SCHEMA
        # ==================================================

        st.write(
            "### SQL Table Schema"
        )

        schema = get_table_schema(
            connection,
            "data"
        )

        st.dataframe(
            schema,
            use_container_width=True
        )


        # ==================================================
        # MANUAL SQL QUERY
        # ==================================================

        default_query = """SELECT *
FROM data
LIMIT 10"""


        query = st.text_area(
            "Enter your SQL query",
            value=default_query,
            height=150
        )


        if st.button(
            "Run SQL Query"
        ):

            try:

                result = execute_sql_query(
                    connection,
                    query
                )

                st.write(
                    "### Query Result"
                )

                st.dataframe(
                    result,
                    use_container_width=True
                )

            except Exception as sql_error:

                st.error(
                    f"SQL Error: {sql_error}"
                )


        # ==================================================
        # AI DATA ANALYST
        # ==================================================

        st.subheader(
            "Ask AI About Your Data"
        )

        st.write(
            "Ask a question in normal English. "
            "Ollama will generate SQL and query your dataset."
        )


        # ==================================================
        # DATA SCHEMA FOR LLM
        # ==================================================

        schema_text = "\n".join(
            [
                f"{column}: {dtype}"
                for column, dtype
                in zip(
                    df.columns,
                    df.dtypes
                )
            ]
        )


        # ==================================================
        # USER QUESTION
        # ==================================================

        user_question = st.text_input(
            "Ask a question about your dataset",
            placeholder="Example: What is the average balance?"
        )


        # ==================================================
        # ASK AI
        # ==================================================

        if st.button(
            "Ask AI"
        ):

            if not user_question.strip():

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Ollama is analyzing your question..."
                ):

                    try:

                        # Generate SQL
                        generated_sql = generate_sql(
                            schema_text,
                            user_question
                        )


                        # Display generated SQL
                        st.write(
                            "### Generated SQL"
                        )

                        st.code(
                            generated_sql,
                            language="sql"
                        )


                        # Execute SQL
                        result = execute_sql_query(
                            connection,
                            generated_sql
                        )


                        # Display result
                        st.write(
                            "### Query Result"
                        )

                        st.dataframe(
                            result,
                            use_container_width=True
                        )


                    except Exception as ai_error:

                        st.error(
                            f"AI Analysis Error: {ai_error}"
                        )


        # ==================================================
        # COMPLETION MESSAGE
        # ==================================================

        st.success(
            "Data analysis completed successfully."
        )


    except Exception as e:

        st.error(
            f"Error while analyzing the file: {e}"
        )
