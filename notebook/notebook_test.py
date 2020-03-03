from menu import Menu
from notebook import Note, Notebook

print('##########################################################################')
note1 = Note('first note')

print('note1.memo:', note1.memo)
print(f'note1.match("first"): {note1.match("first")}')
print()
note2 = Note('second note', tags='2nd')
print('note2.memo:', note2.memo)
print('note2.tags:', note2.tags)
print(f'note2.match("2"): {note2.match("2")}')
print()
print()
print('isinstance(note1, Note): ', isinstance(note1, Note))
print('isinstance(note1, object): ', isinstance(note1, object))
print('isinstance(note1.id, int): ', isinstance(note1.id, int))
print('isinstance(note1.memo, str): ', isinstance(note1.memo, str))
print('dir(note1.id): ')
print()
print(dir(note1.id))
print()
print('##########################################################################')
print()
notebook1 = Notebook()
notebook1.new_note('1st note in notebook1', tags='1st')
notebook1.new_note('another note added', tags='add')
notebook1.new_note('this one is a mistake_e ad', tags='e_e')
print('notebook1.notes: ', [(note.memo, note.tags)
                            for note in notebook1.notes])
print('notebook1.search("ad"): ', [
      (note.memo, note.tags) for note in notebook1.search("ad")])
id_note3 = notebook1.notes[2].id
print()
print(f'id of note3: {id_note3}')
print(f'notebook1.modify_memo({id_note3},"changed memo"): ')
notebook1.modify_memo(id_note3, "changed memo")
print('notebook1.notes: ', [(note.memo, note.tags)
                            for note in notebook1.notes])
print()
print(f'notebook1.modify_tags({id_note3},"changed tags"): ')
notebook1.modify_tags(id_note3, "changed tags")
print('notebook1.notes: ', [(note.memo, note.tags)
                            for note in notebook1.notes])
print()
print()
print('isinstance(notebook1, Notebook): ', isinstance(notebook1, Notebook))
print('isinstance(notebook1, object): ', isinstance(notebook1, object))
print('isinstance(notebook1.__str__, str): ',
      isinstance(notebook1.__str__, str))
print('isinstance(notebook1.__str__, object): ',
      isinstance(notebook1.__str__, object))
print('isinstance(notebook1.__init__, object): ',
      isinstance(notebook1.__init__, object))
print('isinstance(notebook1.new_note, object): ',
      isinstance(notebook1.new_note, object))
print()
print('##########################################################################')
print()

print('dir(Note):')
print(dir(Note))
print()

print('dir(Notebook):')
print(dir(Notebook))
print()

print('universal attributes and methods for all classes:')
print([x for x in dir(Menu) if x in dir(Note)])
print()

print('##########################################################################')
