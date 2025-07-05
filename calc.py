import flet as ft

def main(page:ft.Page):
    page.title="Calculator App"

    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)
    
    page.add(

        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,

            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="AC"),
                            ft.ElevatedButton(text="+/-"),
                            ft.ElevatedButton(text="%"),
                            ft.ElevatedButton(text="/"),
                        ]
                    ),

                    ft.Row(
                        controls=[
                        ft.ElevatedButton(text="7"),
                        ft.ElevatedButton(text="8"),
                        ft.ElevatedButton(text="9"),
                        ft.ElevatedButton(text="*"),
                            ]
                    ),
                    
                    ft.Row(
                        controls=[
                        ft.ElevatedButton(text="4"),
                        ft.ElevatedButton(text="5"),
                        ft.ElevatedButton(text="6"),
                        ft.ElevatedButton(text="-"),
                        ]
                    ),

                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="4"),
                            ft.ElevatedButton(text="5"),
                            ft.ElevatedButton(text="6"),
                            ft.ElevatedButton(text="-"),
                        ]
                    ),
                    
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="1"),
                            ft.ElevatedButton(text="2"),
                            ft.ElevatedButton(text="3"),
                            ft.ElevatedButton(text="+"),
                        ]
                    ),
                    
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="0", expand=2),
                            ft.ElevatedButton(text="."),
                            ft.ElevatedButton(text="="),
                        ]
                    ),

                ]
            )
        )












        
        
    )

if __name__ == "__main__":
    ft.app(target=main)
