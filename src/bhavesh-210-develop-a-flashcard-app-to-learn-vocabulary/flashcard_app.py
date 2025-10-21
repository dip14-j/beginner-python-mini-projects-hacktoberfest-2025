import json
import os
import random


def load_flashcards():
    """Load flashcards from flashcards.json in the same directory."""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "flashcards.json")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("❌ Flashcard file not found: flashcards.json")
        return []

    except json.JSONDecodeError:
        print("❌ Error reading flashcard file. Please check JSON format.")
        return []


def save_flashcards(flashcards):
    """Save flashcards back to flashcards.json."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "flashcards.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(flashcards, file, indent=4, ensure_ascii=False)


def add_flashcard(flashcards):
    """Add a new flashcard to the list."""
    question = input("Enter the word: ").strip()
    answer = input("Enter its meaning: ").strip()

    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("✅ Flashcard added successfully!\n")


def practice_flashcards(flashcards):
    """Start practicing flashcards randomly."""
    if not flashcards:
        print("⚠️ No flashcards available. Add some first!")
        return

    print("\n🎯 Starting Flashcard Practice! Type 'exit' anytime to stop.\n")

    while True:
        flashcard = random.choice(flashcards)
        print(f"👉 Word: {flashcard['question']}")
        user_input = input("Your answer (or type 'exit'): ").strip()

        if user_input.lower() == "exit":
            print("\n👋 Exiting practice mode.\n")
            break

        print(f"✅ Correct meaning: {flashcard['answer']}\n")


def view_flashcards(flashcards):
    """Display all stored flashcards."""
    if not flashcards:
        print("⚠️ No flashcards to show.")
        return

    print("\n📚 Your Flashcards:")
    for idx, card in enumerate(flashcards, start=1):
        print(f"{idx}. {card['question']} ➡️ {card['answer']}")
    print()


def main():
    """Main menu loop for the Flashcard App."""
    flashcards = load_flashcards()

    while True:
        print("=== 🧠 Flashcard App ===")
        print("1️⃣  Add Flashcard")
        print("2️⃣  View Flashcards")
        print("3️⃣  Practice Flashcards")
        print("4️⃣  Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            view_flashcards(flashcards)
        elif choice == "3":
            practice_flashcards(flashcards)
        elif choice == "4":
            print("👋 Thanks for using the Flashcard App! Goodbye.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
