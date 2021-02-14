import todo.main

def test_add():
    todo.main._remove_todo('', all_flag=True)
    todo.main._add_todo('foo')
    dic = todo.main._load_todos()
    assert dic['foo'] == 'Not Yet'
    
