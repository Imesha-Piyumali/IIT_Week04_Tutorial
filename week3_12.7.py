# Write a Python program to convert 250 minutes into hours and minutes and print both values.
# Total minutes
total_minutes = 250

# Convert to hours and minutes
hours = total_minutes // 60   # integer division gives hours
minutes = total_minutes % 60  # remainder gives minutes

# Print result
print("Hours:", hours)
print("Minutes:", minutes)
