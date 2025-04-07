import os

NOTES_FILE = "notes.txt"

# Load notes from file
def load_notes():
    notes = {}
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            for line in file:
                title, content = line.strip().split("::", 1)
                notes[title] = content
    return notes

# Save notes to file
def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        for title, content in notes.items():
            file.write(f"{title}::{content}\n")

# Add a note
def add_note(notes):
    title = input("Enter note title: ")
    if title in notes:
        print("A note with this title already exists.")
        return
    content = input("Enter note content: ")
    notes[title] = content
    print("Note added successfully.")

# View all notes
def view_notes(notes):
    if not notes:
        print("No notes to display.")
        return
    for title, content in notes.items():
        print(f"\nTitle: {title}\nContent: {content}\n" + "-"*30)

# Search note
def search_note(notes):
    title = input("Enter title to search: ")
    if title in notes:
        print(f"\nTitle: {title}\nContent: {notes[title]}")
    else:
        print("Note not found.")

# Delete note
def delete_note(notes):
    title = input("Enter title to delete: ")
    if title in notes:
        del notes[title]
        print("Note deleted.")
    else:
        print("Note not found.")

# Main menu
def main():
    notes = load_notes()

    while True:
        print("\n--- Notes Builder ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Note")
        print("4. Delete Note")
        print("5. Save & Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            search_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            save_notes(notes)
            print("Notes saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
