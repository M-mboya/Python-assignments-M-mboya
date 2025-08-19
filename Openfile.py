def modify_content(content):
    """
    Modify file content before saving to new file.
    For now, we'll make the text uppercase.
    """
    return content.upper()


def main():
    try:
        # --- Ask the user for filename ---
        input_file = input("Enter the filename to read: ").strip()

        # --- Try reading the file ---
        with open(input_file, "r") as f:
            content = f.read()

        print("\n--- Original File Content ---")
        print(content)

        # --- Modify the content ---
        modified = modify_content(content)

        # --- Save to a new file ---
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified)

        print(f"\n✅ Modified content has been saved in '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the name and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to open this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
