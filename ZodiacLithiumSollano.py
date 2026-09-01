import sys

year_input = input("Enter your birth year: ")

year = int(year_input)

if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
    sys.exit()

zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

zodiac_index = (year - 1900) % 12

print(f"Your Chinese Zodiac Sign is : {zodiac_signs[zodiac_index]}")