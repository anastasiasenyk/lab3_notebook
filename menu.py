"""class: menu"""
import sys
from notebook import Notebook, Note


class Menu:  # class
    """Display a menu and respond to choices when run."""
    def __init__(self):  # method
        self.notebook = Notebook()   # attribute
        self.choices = {   # attribute
                "1": self.show_notes,
                "2": self.search_notes,
                "3": self.add_note,
                "4": self.modify_note,
                "5": self.quit
                }

    def display_menu(self):  # method
        print("""Notebook 

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
        """)

    def run(self):  # method
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):  # method
        """
        show memo
        :param notes: str
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def search_notes(self):  # method
        """
        search by filter
        """
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):  # method
        """
        add note with last_id+1
        """
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def modify_note(self):  # method
        """
        modify memo or tags of note by its id
        """
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):  # method
        """
        quit from menu
        """
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

