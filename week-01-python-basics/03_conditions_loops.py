# ============================================================
# FILE: 03_conditions_loops.py
# TOPIC: Conditions & Loops
# WEEK: 1 | AI Engineer Roadmap 2026
# ============================================================

# ── 1. if-elif-else ──────────────────────────────────────────

marks = 78

if marks >= 90: 
    print ("Grade: A")

elif marks >= 75:
    print ("Grade: B")

elif marks >= 60:
    print ("Grade: C")

else: 
    print ("Grade: F")




# ── 2. Ternary Operator — one-liner condition ─────────────────

age = 23 
stetus = "Adult" if age >= 18 else "Minor" # can wrir in one line 
print (stetus)



# ── 3. for loop — range ───────────────────────────────────────

for i in range(5): #i is a variable
    print(i)          # 0 1 2 3 4

for i in range(1,6):  #i is a variable
    print(i)          # 1 2 3 4 5

for i in range(0,10,2):  #i is a variable
    print (i)          # 0 2 4 6 8


# ── 4. for loop — list ─────────────────────────────────────

skills = ["Python", "SQL", "ML", "Deep Learning"]
for skill in skills: # skill is a variable
    print (skill)     # Python SQL ML Deep Learning


# ── 5. enumerate — index bhi chahiye saath mein ───────────────

skills = ["python", "sql", "ml", "deep lerning"]
for index, skill in enumerate(skills): # index and skill are variables
    print (f"{index + 1 }. {skill}")


# ── 6. while loop ────────────────────────────────────────────

count =1 
while count <= 5: # jab tak count 5 se chota ya barabar hai tab tak loop chalega
    print (f"count : {count}")   # 1 2 3 4 5    
    count += 1 # count ko 1 se barhaya ja raha hai (count = count + 1)



# ── 7. break & continue ──────────────────────────────────────

for i in range(10):
    if i == 3:
        continue      # 3 skip kar do
    if i == 7:
        break         # 7 pe ruk jao
    print(i)         # 0 1 2 4 5 6






num = 7

for i in range(7,70+1,7):
    print(f"7 * {i//7}  = {i}") # 7 14 21 28 35 42 49 56 63 70



sentance = "Arfat is becoming an AI Engineer"
for char in sentance:
   if char in "aeiouAEIOU": # agar char vowel hai to print karo
       print(char)