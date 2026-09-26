
from agent.llm import ask_llm
from agent.prompts import create_sql_prompt


def generate_sql(schema, question):
    """
    Convert a natural-language question into
    a SQL query using the Ollama LLM.
    """

    prompt = create_sql_prompt(
        schema,
        question
    )

    sql_query = ask_llm(
        prompt
    )

    # Remove unnecessary whitespace
    sql_query = sql_query.strip()

    # Remove markdown code fences if the LLM adds them
    sql_query = sql_query.replace(
        "```sql",
        ""
    )

    sql_query = sql_query.replace(
        "```",
        ""
    )

    return sql_query.strip()
