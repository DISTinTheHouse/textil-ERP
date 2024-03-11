import flet as ft

def checked(page: ft.Page):
# ---- FUNCIONES -----------
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        username = ft.TextField(label="Usuario", autofocus=True)
        password = ft.TextField(label="Contraseña")
        greetings = ft.Column()

        page.update()
# -------------------------
        

#---- MENÚ NAVBAR ----
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LEAK_ADD_ROUNDED, color="yellow"),
        leading_width=40,
        title=ft.Text("Textil-Sync"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT, 
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Iniciar Sesión"),
                    ft.PopupMenuItem(text="Crear cuenta"),  
                    ft.PopupMenuItem(), #Dividir
                    ft.PopupMenuItem(
                        text="Marcar como revisado", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
#------------------
    

#------- MENU BOTTOM -------
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.LIGHT_BLUE_200,
        inactive_color=ft.colors.GREY_600,
        active_color=ft.colors.LIGHT_BLUE_900,
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
        destinations=[
            ft.NavigationDestination(icon=ft.icons.LOGIN_ROUNDED, label="Iniciar Sesión"),
            ft.NavigationDestination(icon=ft.icons.APP_REGISTRATION_ROUNDED, label="Nuevo Usuario"),
        ]
    )
#----------------------------
    

#----- CONTENIDO ------------    
    page.add(ft.Text(
            spans=[
                ft.TextSpan(
                    "Inicia sesión o crea tu cuenta para ver más!",
                    ft.TextStyle(
                        size=50,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (0, 20), (150, 20), [ft.colors.RED, ft.colors.YELLOW]
                            )
                        ),
                    ),
                ),
            ],
        )
    )

#----------------------------

ft.app(target=checked)