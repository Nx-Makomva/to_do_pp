def includes_todo(notes):

    str_notes = str(notes)

    if str_notes:
        return '#TODO' in str_notes
    raise Exception('Input is empty, please write a task')
