sec = int(input("Enter seconds: "))

# Convert seconds to hours, minutes, and seconds
hours = sec // 3600
rem_sec = sec % 3600
min = rem_sec // 60
sec = rem_sec % 60

# Display the result
print(f"Hours: {hours}")
print(f"Minutes: {min}")
print(f"Seconds: {sec}")
