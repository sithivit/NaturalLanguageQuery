from transformers import pipeline
from db_analyzer import get_db_schema

def generate_sql_query(natural_language_query):
    # Load the language model
    nlp = pipeline("text2text-generation", model="t5-base")

    # Get the database schema
    schema = get_db_schema()

    # Combine the schema and the natural language query
    input_text = f"""
        This is the schema of a database. According to this schema and natural language query can you produce a sql query that would extract the same information with natural language query.
        Schema: {schema}
        Query: {natural_language_query}
        """

    # Generate the SQL command
    result = nlp(input_text, max_length=512, truncation=True)
    sql_command = result[0]['generated_text']

    return sql_command