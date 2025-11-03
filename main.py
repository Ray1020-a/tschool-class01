a = float(input("請問身高 (單位 cm): "))
b = float(input("請問體重 (單位 kg): "))
bmi = round((b /((a / 100) ** 2)), 1)
if 18.5 <= bmi < 24:
    print(f"健康體位 BMI為 {bmi}")
else:
    print(f"體位異常 BMI為 {bmi}")