#((a == b) or not (b < a)) and ((a < b) or (b == a + 1))
#Exercises 13–16 — assume a = 1 and b = 1.5. For each condition, state whether it evaluates to True or False.
a = 1
b = 1.5

result = ((a == b) or not (b < a)) and ((a < b) or (b == a + 1))
print("((a == b) or not (b < a)) and ((a < b) or (b == a + 1)):", result)
