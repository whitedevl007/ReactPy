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
    
run(Counter)