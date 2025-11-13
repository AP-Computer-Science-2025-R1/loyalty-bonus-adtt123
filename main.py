print("Hi! Welcome to the clothing suggester.")
print("This program calculates in celsius because fahrenheit sucks! :)")
print("What is the weather forecast for tomorrow?")

def temp():
    weather_ = input("Temperature: ")
    weather = int(weather_)
    if weather >= 20:
        print("Wear a light-colored thin T-Shirt and shorts.")
    elif weather > 10 and weather < 20:
        print("Wear jeans and a T-shirt.")
    elif weather > 5 and weather < 10:
        print("Wear a hoodie and sweatpants.")
    elif weather < 5:
        print("Wear a jacket and sweatpants.")

def rain():
    rain = input("Will it rain?: ")
    if rain == "yes":
        print("Make sure to bring an umbrella or raincoat!")
    elif rain == "y":
        print("Make sure to bring an umbrella or raincoat!")
    elif rain == "no":
        print("No umbrella needed, bring some shades for the sun!")
    else:
        print("Please put in a valid input.")

temp()
rain()
