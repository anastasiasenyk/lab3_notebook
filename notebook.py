"""class: note, notebook"""
import datetime

# Store the next available id for all new notes
last_id = 0


class Note:  # class
    """
    Represent a note in the notebook.
    """

    def __init__(self, memo, tags=''):  # method
        # __init__ create an object for class
        """
        initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        :param memo: str
        :param tags: str
        """""
        self.memo = memo  # attribute
        self.tags = tags   # attribute
        self.creation_date = datetime.date.today()   # attribute
        global last_id
        last_id += 1
        self.id = last_id   # attribute

    def match(self, filter):  # method
        """
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        :param filter: str
        :return: bool
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    Represent a collection of notes that can be tagged,
    modified, and searched.
    """

    def __init__(self):  # method __init__
        # __init__ create an object for class
        """Initialize a notebook with an empty list."""
        self.notes = []  # attribute

    def __str__(self):  # method __str__
        # represents the class objects as a string
        """
        return notes
        """
        if not self.notes:
            return '[]'
        return str(self.notes)

    def new_note(self, memo, tags=''):  # method
        """
        Create a new note and add it to the list.
        :param memo: str
        :param tags: str
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):  # method
        """
        Locate the note with the given id.
        :param note_id: str
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):  # method
        """
        Find the note with the given id and change its
        memo to the given value.
        :param note_id: str
        :param memo: str
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):  # method
        """Find the note with the given id and change its
        tags to the given value.
        :param note_id: str
        :param tags: str
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):  # method
        """Find all notes that match the given filter
        string.
        :param filter: str"""
        return [note for note in self.notes if
                note.match(filter)]


first_notebook = Notebook()  # object

print(isinstance(first_notebook, object))  # True

print(type(first_notebook.notes))  # <class 'list'> -> notes - атрибут (змінна)


print(type(first_notebook.new_note('hello world')))  # <class 'NoneType'>
print(first_notebook)
print(first_notebook.search('world'))  # [<__main__.Note object at 0x1145b3730>] -> search() - метод
