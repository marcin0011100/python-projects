from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_electricity_price(time, location="Poland"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that provides electricity prices based on the time of day."
            },
            {
                "role": "user",
                "content": f"What is the electricity price at {time} in {location}?"
            }
        ]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    time = "14:00"
    location = "Poland"
    price = get_electricity_price(time, location)
    print(f"The electricity price at {time} in {location} is: {price}")
