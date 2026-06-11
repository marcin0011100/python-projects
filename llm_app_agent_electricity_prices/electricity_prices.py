import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_electricity_prices(time):
    prompt = f"What are the electricity prices at {time}?"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    time = "2024-06-01 14:00"
    prices = get_electricity_prices(time)
    print(f"Electricity prices at {time}: {prices}")
