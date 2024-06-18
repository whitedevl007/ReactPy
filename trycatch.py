from reactpy import component, html, run, use_state

@component
def Hellocomponent():
    return html.div(
        html.h1("Hello World!")
    )

 
@component
def generateList(items):
    final_item = [html.li(i) for i in items]
    return html.ul(final_item)
    
    
@component
def ListComponent():
    tasks = [
        'Do yoga',
        'Drink',
        'Code',
        'Sleep'
    ]
    
    return html.div(
        html.h1("My Todo List !!"),
        generateList(tasks)
    )
    
# run(ListComponent)



''' creating counter '''


def increment(old_val):
    new_val = old_val + 5
    return new_val

@component
def Counter():
    num, set_num = use_state(0)
    
    def handle_click(event):
        set_num(increment)
    
    return html.div(
        html.h1(num),
        html.button({"on_click": handle_click}, "Increment by 5")
    )
    
# run(Counter)



''' creating dynamic todo app to add task to list '''

@component
def TodoList():
    task, set_task = use_state('')
    task_list, set_tasklist = use_state([])
    
    def handle_input(event):
        set_task(event['target']['value'])
        
    def handle_submit(event):
        set_tasklist(task_list + [task])
        
    return html.div(
        html.h1("My Todo App !!!"),
        html.input({"on_change":handle_input}),
        html.button({"on_click": handle_submit}, "Add Task"),
        generateList(task_list)
    )
    
    
    
run(TodoList)