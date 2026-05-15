# ============================================================
# FILE: 02_strings_operators.py
# TOPIC: Strings & Operators
# WEEK: 1 | AI Engineer Roadmap 2026
# ============================================================

# ── 1. String Basics ─────────────────────────────────────────

name = "Arfat pathan"

print (name.upper())   # ARFAT PATHAN
print (name.lower())   # arfat pathan
print (name.title())   # Arfat Pathan
print (name.replace("pathan" , "khan"))  # Arfat khan (replaces "pathan" with "khan") but not changing the original string its a temporary change
print (name.strip())   # Arfat pathan (no change, but removes leading/trailing spaces if any)
print (len(name))     # 12 (length of the string) / count of characters in the string


# ── 2. String Slicing ────────────────────────────────────────

my_name = "arfat jamil pathan"

print  (my_name [0])       # 'a' (first character)
print  (my_name [6])       # 'j' (seventh character)
print  (my_name [12])     # 'p' (thirteenth character)
# but python apni counting 0 se start karta hai isliye ek numbar kam hoga actual position se
print  (my_name [0])       # 'a' (first character)
print  (my_name [-1])       # 'n' (last character)
print  (my_name[0:5])    # 'arfat' (first 5 characters)
print  (my_name[6:11])   # 'jamil' (characters from index 6 to 10)
print  (my_name[12:])    # 'pathan' (characters from index 12 to the end)
print (my_name[::2])    # 'af tjmlptn' (every second character)
print (my_name[::-1])   # 'nahtap limaj tafra' (reversed string)
# slicing 3 "S" pe kaam karte hai (start:stop:step) hum is ko position ke hisab se bhi use kar sakte hai aur negative bhi kar sakte hai




# ── 3. String Split & Join ───────────────────────────────────

sentence = "Hello, how are you doing today?"

words = sentence.split()   # sentence ko words me split karta hai (default separator is space)
print(words)

joined = "-".join(words)     # words ko "-" se jodta hai
print(joined)



# ── 4. String Check Methods ──────────────────────────────────

print ("arfat".isalpha())  # True (only letters)
print ("12345".isdigit())   # True (only digits)
print ("arfat123".isalnum()) # True (letters and digits)
print (" ".isspace())   # True (only whitespace)
print ("arfat".startswith("ar"))  # True (starts with "ar")
print ("arfat".endswith("fat"))    # True (ends with "fat")




# ── 5. Arithmetic Operators ──────────────────────────────────

a = 17
b = 5

print (a + b)  # 22 (addition)
print (a - b)  # 12 (subtraction)
print (a * b ) # 85 (multiplication)
print (a / b)  # 3.4 (float division)
print (a // b) # 3 (integer division)
print (a % b)  # 2 remainder (modulus)
print (a ** b) # 1419857 (exponentiation) (17 raised to the power of 5 = 17 * 17 * 17 *  17 * 17  = 1419857)




# ── 6. Comparison Operators ──────────────────────────────────

x = 10
y = 20

print (x == y)  # False (equality)
print (x != y)  # True (inequality)
print (x > y)   # False (greater than)
print (x < y)   # True (less than)
print (x >= y)  # False (greater than or equal to)
print (x <= y)  # True (less than or equal to)

print ("hi") 

# ── 7. Logical Operators ─────────────────────────────────────

age = 23
has_degree = True

print(age > 18 and has_degree)   # age > 18 is (True) and has_degree is (True), so the result is True = True and True = True
print(age < 18 or has_degree)    # age < 18 is (False) but has_degree is (True), so the result is True = False or True = True
print(not has_degree)  # False (negation of True is False) = (not True = False)


word = "madam"  # chek kar ki ye word palindrome hai ya nahi 
print(word == word[::-1])  # True (if the word is the same when reversed, it's a palindrome) = (madam == madam) = True
print(f"{word} is a palindrome: {word == word [::-1]}")



num1 = 24
num2 = 7 

print (f"num1 + num2 = {num1 + num2}")
print (f"num1 - num2 = {num1 - num2}")
print (f"num1 * num2 = {num1 * num2}")
print (f"num1 / num2 = {num1 / num2}")
print (f"num1 // num2 = {num1 // num2}")
print (f"num1 % num2 = {num1 % num2}")
print (f"num1 ** num2 = {num1 ** num2}")
       
    