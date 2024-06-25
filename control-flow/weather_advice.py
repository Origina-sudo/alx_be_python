# weather_advice.py

# Prompt the user to input the current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Provide clothing recommendations based on the input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don’t forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
