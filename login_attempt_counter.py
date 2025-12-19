

print("🔐 Login Attempt Counter")
print("------------------------")

correct_password = "Ansh001"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter your password: ")

    if password == correct_password:
        print("✅ Login successful!")
        break
    else:
        attempts += 1
        print(f"❌ Wrong password. Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("🔒 Account locked! Too many failed login attempts.")
