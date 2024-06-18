from reactpy import component, html, run

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
    
run(ListComponent)