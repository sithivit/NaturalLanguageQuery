from query_generator import generate_sql_query

# Example usage
if __name__ == "__main__":
    query = "Find the names of all users"
    sql = generate_sql_query(query)
    print(sql)