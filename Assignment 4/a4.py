class Note:
    def __init__(self,memo,tags = []):
        self.memo = memo
        self.tags = tags
    def print_memo(self):
        print(f"Message: {self.memo}")
        print("\tTags: ",end = "")
        for tag in self.tags:
            print(tag,end = " ")
        print()
class Notebook:
    def __init__(self):
        self.notes = []
    def add_note(self):
        message = input("What memo do you want to write? ")
        tags = []
        while True:
            temp = input("Add Tag (or type \"quit\") ")
            if temp == "quit":
                break
            else:
                tags.append(temp)
        new_note = Note(message,tags)
        self.notes.append(new_note)
    def find_notes_by_tag(self, tag):
        size = len(self.notes)
        matchs = []

        for x in range(0, size, 1):
            tagsSize = len(self.notes[x].tags)
            for i in range(0, tagsSize, 1):
                if(self.notes[x].tags[i] == tag):
                    matchs.append(self.notes[x])
        return matchs
    def print_unique_tags(self):
        unique = set()
        size = len(self.notes)

        for x in range(0, size, 1):
            tagsSize = len(self.notes[x].tags)
            for i in range(0, tagsSize, 1):
                unique.add(self.notes[x].tags[i])

        for tag in unique:
            print(tag)

    def print_notebook(self):
        for note in self.notes:
            note.print_memo()

if __name__ == "__main__":
  notebook1 = Notebook()
  notebook1.add_note()
  notebook1.add_note()
  notebook1.print_notebook()

  # Use these to test your newly-
  tagFind = input("Enter the tag you want to search for: ")
  memos = notebook1.find_notes_by_tag(tagFind)
  for memo in memos:
    memo.print_memo()
  notebook1.print_unique_tags()
