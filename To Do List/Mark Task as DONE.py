tasks = ['Hello']
def done_task():
    for x in tasks:
        text = str(x)
        strikethrough_text = ''.join([char + '\u0336' for char in text])
        print(strikethrough_text)


done_task()