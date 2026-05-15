# ============================================================
# FILE: 01_variables_datatypes.py
# TOPIC: Variables & Data Types
# WEEK: 1 | AI Engineer Roadmap 2026
# ============================================================



# ── 1. Variables & Types ─────────────────────────────────────

name = "Arfat"
age = 23
cgpa = 8.5
is_enrolled = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_enrolled))




# ── 2. Type Conversion ───────────────────────────────────────

num_str = "42"
num_int = int(num_str)
print(num_int + 8)        # 50 aana chahiye

price = 99.99
print(int(price))         # 99 aana chahiye




# ── 3. F-Strings ─────────────────────────────────────────────

student = "Arfat"
marks = 95
print(f"{student} ne {marks} marks laaye!")
print(f"Percentage: {marks / 100:.2f}")




# ── 4. Temperature Conversion ─────────────────────────────────

temperature = 96.6 # Fahrenheit
celsius = (temperature - 32)
celsius = celsius * 5 
celsius = celsius / 9 
# print(f"Temperature in Celsius: {celsius:}")
print("read in celsius is : ", celsius)


year = "2026"
print(type(year))          # humm ne dekh ki is ka type kya hai 
int_year = int(year)       # fir is ko string se integer me convert kiya 
print(type(int_year))      # fir dekh ki ab iska type kya hai aur fir is integer ko 4 se add kiya
year_short = int(year[2:4])
result = year_short + 4
print(result) 