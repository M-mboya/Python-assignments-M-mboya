# File Read & Write Challenge 🖋️
try:
    # Ask the user for a filename
    filename = input("Filereadass.py: Enter the name of the file to read/write: ")

    # --- Read a file ---
    file = open(filename, "r", encoding="utf-8")
    data = file.read()
    print("\nOriginal Content:\n", data)
    file.close()

    # --- Modify content (make uppercase) and write to new file ---
    new_file = "modified_" + filename
    file = open(new_file, "w", encoding="utf-8")
    file.write(data.upper())
    file.close()

    # --- Append to the new file ---
    file = open(new_file, "a", encoding="utf-8")
    file.write("\n# This line was appended to the modified file.")
    file.close()

    print(f"\n✅ Modified content saved in '{new_file}' with an extra line appended!")

# --- Error Handling Lab 🧪 ---
except FileNotFoundError:
    print("❌ File not found. Please check the name and try again.")
except Exception as e:
    print("❌ An error occurred:", e)
