#modeulos
import pyrebase #pip install pyrebase3
import flet
from flet import *
import datetime
from functools import partial

#configuración firebase
config = {
    "apiKey": "AIzaSyDO_jda0pd2gZJ4YpLuhwanb97hk70HoiY",
    "authDomain": "textil-sync.firebaseapp.com",
    "projectId": "textil-sync",
    "storageBucket": "textil-sync.appspot.com",
    "messagingSenderId": "299772389651",
    "appId": "1:299772389651:web:f87f6cf0dc0d05dd9592e6",
    #set database to none
    "databaseURL": "",
  }

#inicio de firebase
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

#VISTA DE MI APP---------------------
class UserWidget(UserControl):
    def __init__(
            self,
            title:str,
            sub_title:str,
            btn_name:str,
            func,
    ):
        #TITULO
        self.title = title
        #SUBTITULO
        self.sub_title = sub_title
        #BOTON
        self.btn_name = btn_name
        #FUNCION
        self.func = func

        super().__init__()
    #INPUTS
    def InputTextField(self, text:str, hide: bool):
            return Container(
                alignment=alignment.center,
                content=TextField(
                    height=48,
                    width=255,
                    bgcolor="#f0f3f6",
                    text_size=12,
                    color="black",
                    border_color="transparent",
                    hint_text=text,
                    filled=True,
                    cursor_color="black",
                    hint_style=TextStyle(
                         size=11,
                         color="black",
                    ),
                    password=hide,
                ),
            )
    # BOTON INICIAR SESIÓN/REGISTRAR
    def signInOption(self, path: str, name: str):
        return Container(
            content=ElevatedButton(
                content=Row(
                    alignment='center',
                    spacing=4,
                    controls=[
                        Image(
                            src=path,  # Ruta de la imagen del PATH
                            width=30,
                            height=30,
                        ),
                        Text(
                            name,
                            color='black',
                            size=10,
                            weight='bold',
                        ),
                    ],
                ),
                style=ButtonStyle(
                        shape={"": RoundedRectangleBorder(radius=10)},
                        bgcolor={"": "#f0f3f6"},
                ),
            ),
        )

#-------------------------------------

#SE DEFINE VARIABLE PARA CONTENIDO-------------------------------
    def build(self):
#TITULOS----------------------------------------------------
        self._title = Container(
            alignment=alignment.center,
            content=Text(
                self.title, #Mandas a llamar la variable // Aqui mando a llamar UI del titulo de la pagina
                size=15,
                text_align='center',
                weight='bold',
                color='black',
            ),
        )
#------------------------------------------------------------
#SUBTITULOS--------------------------------------------------
        self._sub_title = Container(
            alignment=alignment.center,
            content=Text(
                self.sub_title,
                size=10,
                text_align='center',
                color='black',
            ),
        )
#----------------------------------------------------------------
#BOTONES---------------------------------------------------------
        self._sign_in = Container(
            content=ElevatedButton(
                on_click=partial(self.func),
                content=Text(
                    self.btn_name,
                    size=11,
                    weight="bold",
                ),
                style=ButtonStyle(
                    shape={"": RoundedRectangleBorder(radius=10)},
                    color={"": "white"},
                ),
                height=48,
                width=255,
            )
        )

#----------------------------------------------------------------

# aqui se retorna las clases de UI -----------
        return Column(
            horizontal_alignment='center',
            controls = [
                Container(padding=10),
                self._title,
                self._sub_title,
                Column(
                    spacing=12,
                    controls=[
                        self.InputTextField("Correo Electronico",
                                            False),
                        self.InputTextField("Contraseña",
                                            True),
                    ]
                ),
                Container(padding=15),
                self._sign_in,
                Container(padding=15),
                Column(
                     horizontal_alignment="center",
                     controls=[
                          Container(
                               content=Text(
                                    "También puedes ingresar con:",
                                    size=10,
                                    color="black",
                               )
                          ),
                          self.signInOption("./assets/facebook.png", "Facebook"),
                          self.signInOption("./assets/google.png", "Google"),
                     ],
                ),
            ],
        )
#-----------------------------------------------------------------------
    
def main(page:Page):
    page.title = "Textil Sync ERP"
    page.bgcolor = "#f0f3f6"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _main_column_():
        return Container(
            width=280, 
            height=600, 
            bgcolor="#ffffff",
            padding=12,
            border_radius=35,
            content=Column(
                spacing=20,
                horizontal_alignment="center",
            ),
        )
    
    #REGISTRO EN FIREBASE 
    def _register_user(e):
        try:
            auth.create_user_with_email_and_password(
                _register_.controls[0].controls[3].controls[0].content.value,
                _register_.controls[0].controls[3].controls[1].content.value
            )
            #SI SE REGISTRA EN FIREBASE ENTONCES IMPRIME OK EN LA TERMINAL
            print("Registro Existoso!")

        except Exception as e:
            print(e)

    #INICIAR SESION EN FIREBASE
    def _sign_in(e):
        try:
            user = auth.sign_in_with_email_and_password(
                _sign_in_.controls[0].controls[3].controls[0].content.value,
                _sign_in_.controls[0].controls[3].controls[1].content.value
            )

            info = auth.get_account_info(user["idToken"])

            #print(info) - ACTIVA ESTE PRINT PARA VERIFICAR LA INFO DEL USUARIO QUE DESEA INGRESAR.
            data = ["createdAt","lastLoginAt",]

            for key in info:
                if key == 'users': 
                    for item in data:
                        print(item + "" + datetime.datetime.fromtimestamp(int(info[key][0][item]) / 1000).strftime("%D - %H:%M %p"))
            #LIMPIA LOS INPUTS LOGIN AL UTILIZARSE
            _sign_in_.controls[0].controls[3].controls[0].content.value = None
            _sign_in_.controls[0].controls[3].controls[1].content.value = None
            _sign_in_.controls[0].controls[3].update()

        except:
            print("Email o Contraseña Incorrecto...")
    

    _sign_in_ = UserWidget(
        "Bienvenido a Textil-Sync", 
        "Inicia sesión para ver más contenido :) ",
        "Iniciar sesión",
        _sign_in,
    )
    
    _register_ = UserWidget(
        "Crea tu nueva cuenta",
        "Registra tu nueva cuenta ! ",
        "Registrate",
        _register_user,
    )

    _sign_in_main = _main_column_()
    _sign_in_main.content.controls.append(Container(padding=15))
    _sign_in_main.content.controls.append(_sign_in_)

    _reg_main = _main_column_()
    _reg_main.content.controls.append(Container(padding=15))
    _reg_main.content.controls.append(_register_)

    page.add(
        Row(
            alignment='center',
            spacing=25,
            controls=[
                _sign_in_main,
                _reg_main,
            ],
        )
    )


if __name__ == "__main__":
    flet.app(target=main, assets_dir='assets')