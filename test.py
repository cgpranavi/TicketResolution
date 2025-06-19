from google.cloud import storage
import pandas as pd
import openai  

def get_ticket_data(bucket_name, file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    data = blob.download_as_text()
    df = pd.read_csv(pd.compat.StringIO(data))
    return df

def ai_query_on_tickets(df, user_query):
    # Use LLM to generate pandas code or filter logic
    prompt = f"""You have this ticket data with columns: {', '.join(df.columns)}.
    Write pandas code to answer: "{user_query}".
    Only return the code."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    code = response['choices'][0]['message']['content']
    # Optionally, execute the code 
    # result = eval(code)
    # return result
    return code

# Example usage
bucket = "your-bucket"
file = "tickets.csv"
df = get_ticket_data(bucket, file)
query = input("Ask about a ticket: ")
print(ai_query_on_tickets(df, query))