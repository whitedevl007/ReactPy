from reactpy import component, html, run

@component
def Hellocomponent():
    return html.div(
        html.h1("Hello World!")
    )
    
run(Hellocomponent)