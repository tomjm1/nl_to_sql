import openai
import os
from dotenv import load_dotenv

from fetch_data import fetch_data

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")
def generate_openapi_sql(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "I would like you to generate accurate sqlite compatible sql query for the question"},
                {"role": "assistant", "content": prompt}
            ]
        )
    code = response.choices[0].message.content
    result = '```sql\n' + code + '\n```'
    return code


def build_query_prompt(schema_details,query):

    input_str=f"""
    {schema_details}

    {query}

    - Ensure case sensitivity
    - Ensure NULL check
    - Do not add any special information or comment, just return the query

    The expected output is code only. Always use table name in column reference to avoid ambiguity
    """

    return input_str

def run_prompt(schema, prompt):
    full_prompt = build_query_prompt(schema_details=schema, query=prompt)
    sql_query = generate_openapi_sql(full_prompt)
    print("Open API Query :/n",sql_query)
    result=fetch_data(sql_query)
    return result

if __name__=="__main__":
    query = "How many visitors for the project id 10"

    example_schema = """
    CREATE TABLE page_events (
        id INTEGER PRIMARY KEY,
        project_id INTEGER,
        timestamp INTEGER,
        session_id TEXT,
        country TEXT,
        city TEXT,
        browser TEXT,
        operating_system TEXT,
        path TEXT
    )
    """
    full_prompt = build_query_prompt(example_schema, query=query)
    sql_query = generate_openapi_sql(full_prompt)
    print(sql_query)
    fetch_data(sql_query)
