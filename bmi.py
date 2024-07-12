def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_weight():
    print("Please enter your weight in kilograms:")
    weight_input = input()
    while not weight_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a valid weight in kilograms:")
        weight_input = input()
    weight = float(weight_input)
    return weight

def get_height():
    print("Please enter your height in meters:")
    height_input = input()
    while not height_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a valid height in meters:")
        height_input = input()
    height = float(height_input)
    return height

def display_results(weight, height, bmi, category):
    print("\nCalculating your BMI...\n")
    print(f"Your weight: {weight:.2f} kg")
    print(f"Your height: {height:.2f} meters")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

def get_weight_confirmation(weight):
    print(f"You have entered your weight as {weight:.2f} kg.")
    print("Is this correct? (yes/no)")
    confirmation = input().strip().lower()
    while confirmation not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        confirmation = input().strip().lower()
    return confirmation == 'yes'

def get_height_confirmation(height):
    print(f"You have entered your height as {height:.2f} meters.")
    print("Is this correct? (yes/no)")
    confirmation = input().strip().lower()
    while confirmation not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        confirmation = input().strip().lower()
    return confirmation == 'yes'

def main():
    print("Hello,Welcome to the BMI Calculator")
    
    weight = get_weight()
    while not get_weight_confirmation(weight):
        weight = get_weight()
    
    height = get_height()
    while not get_height_confirmation(height):
        height = get_height()
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    display_results(weight, height, bmi, category)

if __name__ == "__main__":
    while True:
        main()
        print("\nWould you like to calculate another BMI? (yes/no)")
        restart = input().strip().lower()
        while restart not in ['yes', 'no']:
            print("Invalid input. Please type 'yes' or 'no'.")
            restart = input().strip().lower()
        if restart == 'no':
            print("come back later!")
            break