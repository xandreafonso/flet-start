import flet as ft

def main(page: ft.Page):
    
    # Função para trocar de tela
    def navigate_to(event, route):
        screen_area.content.clean() # content_area.controls.clear()
        if route == "Tela1":
            screen_area.content = screen1 # content_area.controls.append(screen1)
        elif route == "Tela2":
            screen_area.content = screen2
        page.update()

    # Topo com texto "Logo" e botão de configurações
    top_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(value="Logo", size=20),
                ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda event: print("Configurações")),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        # bgcolor=ft.colors.BLUE,  # Define o background como azul
    )
    

    # Menu lateral
    sidebar_menu = ft.Column(
        controls=[
            ft.ListTile(title=ft.Text("Tela 1"), on_click=lambda event: navigate_to(event, "Tela1")),
            ft.ListTile(title=ft.Text("Tela 2"), on_click=lambda event: navigate_to(event, "Tela2")),
        ]
    )

    # Telas
    screen1 = ft.Text("Tela 1")
    screen2 = ft.Text("Tela 2")

    # Área de conteúdo das telas
    screen_area = ft.Container(content=screen1, expand=True, alignment=ft.alignment.top_left)

    # Layout principal
    main_layout = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(content=sidebar_menu, width=200),
                ft.VerticalDivider(width=1),
                ft.Container(content=screen_area, expand=True)  # Área de conteúdo que será atualizada
            ],
            #expand=True
            alignment=ft.MainAxisAlignment.START,
            spacing=0
        ),
        # bgcolor=ft.colors.YELLOW,  # Define o background como amarelo
        expand=True,
    ) 

    divider = ft.Container(
        content=ft.Divider(height=1, color=ft.colors.GREY),
        # bgcolor=ft.colors.BLACK,
    )

    # Adicionando topo e layout principal à página
    page.controls.append(top_bar)
    page.controls.append(divider)
    page.controls.append(main_layout)

    page.spacing = 0
    page.padding = 0
    
    page.update()

# Inicia o aplicativo
ft.app(target=main)
