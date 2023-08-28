import reflex as rx



class State(rx.State):
    pass


def index() :
    return rx.vstack(
        rx.button(
            "班級1",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"100", "font-size": "35px","top":"-100"},
            border_radius="1em",
        ),
        rx.button(
            "班級2",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"100", "font-size": "35px","top":"-50"},
            border_radius="1em",
        ),
        rx.button(
            "班級3",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"100", "font-size": "35px","top":"0"},
            border_radius="1em",
        ),
        rx.button(
            "班級4",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"100", "font-size": "35px","top":"50"},
            border_radius="1em",
        ),
        rx.button(
            "班級5",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"100", "font-size": "35px","top":"100"},
            border_radius="1em",
        ),
    
    style={"background-color": "#FFFAF0", "height": "100vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )
    

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
