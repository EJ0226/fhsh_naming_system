import reflex as rx


class InputBlurState(rx.State):
    text: str = " "

    def set_text(self, text: str):
        self.text = text.upper()


config = rx.Config(
 app_name="my_app_name",
 db_url="postgresql://user:password@localhost:5432/my_db",#到時候要改
 frontend_port=3001,
)

def index() :
    return rx.vstack(
        rx.link(
            rx.button(
                "班級1",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"100", "font-size": "35px","top":"-100"},
                border_radius="1em",
            ),
            href="/student-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "班級2",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"100", "font-size": "35px","top":"-50"},
                border_radius="1em",
            ),
            href="/student-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "班級3",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"100", "font-size": "35px","top":"0"},
                border_radius="1em",
            ),
            href="/student-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "班級4",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"100", "font-size": "35px","top":"50"},
                border_radius="1em",
            ),
            href="/student-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "班級5",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"100", "font-size": "35px","top":"100"},
                border_radius="1em",
            ),
            href="/student-route",
            button=True,
        ),
    
    style={"backgroundColor": "#FFFAF0", "height": "100vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )
def student():
    return rx.vstack(
        rx.text(InputBlurState.text),
        rx.link(
            rx.button("←",style={"font-size":"45px","left":"-150","top":"-50"},bg="#FFFAF0"),
            href="/",
            button=True
        ),
        rx.input(
            placeholder="                Search",
            font_size="1.2em",
            on_blur=InputBlurState.set_text,
            border_radius="6em",
            border_color="#698694",
            style={"height":"60px","top":"-100px","width":"-200px"}
        ),
        rx.link(
            rx.button(
                "學生1",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生2",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生3",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生4",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生5",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生6",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生7",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生8",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生9",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生10",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
        rx.link(
            rx.button(
                "學生11",
                color="#000000",
                bg="#FFFFFF",
                style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
                border_radius="1em",
            ),
            href="/check-route",
            button=True,
        ),
    style={"backgroundColor": "#FFFAF0", "height": "145vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )
def check():
        return rx.vstack(
        rx.link(
            rx.button(
                "←",
                bg="#FFFAF0",
                color="#000000",
                font_size="48px",
                style={"top":"0","left":"-150px"}
            ),
            href="/student-route",
            button=True
        ),    
        rx.box(
            "班級 31116",
            color="#000000",
            font_size="30px",
            style={"top":"40"}
        ),
        rx.box(
            "姓名 楊沁璇",
            color="#000000",
            font_size="30px",
            style={"top":"40"}
        ),
        rx.box(
            "學號 11035032",
            color="#000000",
            font_size="30px",
            style={"top":"40"}
        ),
        rx.box(
            " ",
            bg="#000000",
            width="70%",
            style={"height":"300px"}
        ),
        rx.hstack(
            rx.button(
                "X",
                border_radius="3em",
                color="#698694",
                bg="#FFFFFF",
                style={"height":"70px","width":"100px","top":"50","right":"30"}

            ),
            rx.button(
                "✓",
                border_radius="3em",
                color="#FFFFFF",
                bg="#698694",
                style={"height":"70px","width":"100px","top":"50","left":"30"}
            )
        ),
        rx.button(
            "複點錯誤",
            border_radius="3em",
            bg="#3D3D3D",
            color="#FFFFFF",
            style={"height":"50px","width":"200px","top":"70"}
        ),
    style={"backgroundColor": "#FFFAF0", "height": "99vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index,)
app.add_page(student , route="/student-route")
app.add_page(check , route="/check-route")
app.compile()
