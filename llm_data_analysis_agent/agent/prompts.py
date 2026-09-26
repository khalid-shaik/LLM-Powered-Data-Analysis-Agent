
def create_sql_prompt(schema, question):
    """
    Create a prompt that converts a natural-language
    question into a SQLite SQL query.
    """

    prompt = f"""
You are a professional data analyst.

You are working with a SQLite table named "data".

Here is the table schema:

{schema}

The user has asked this question:

{question}

Your task is to generate a SQL query that answers
the user's question.

Rules:

1. Generate only a SELECT query.
2. Use only the table named "data".
3. Use only columns that exist in the schema.
4. Do not create, update, delete, insert, or modify data.
5. Do not use markdown code fences.
6. Return only the SQL query.
7. Make the SQL compatible with SQLite.
8. Do not explain the query.
9. Do not add any text before or after the SQL query.

SQL query:
"""

    return prompt
