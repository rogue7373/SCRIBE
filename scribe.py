import flet as ft
from zoneinfo import ZoneInfo
from datetime import datetime

def main(page: ft.Page):
    page.window_title_bar_hidden = True
    page.window_movable = True
    page.window_resizable = True
    page.window_min_height = 600
    page.window_min_width = 320
    page.window_opacity = .95
    page.auto_scroll = True

    def insert_timestamp(event):
        pacifictime = datetime.now(ZoneInfo('America/Los_Angeles')).replace(tzinfo=None).isoformat(sep=" ",timespec="seconds")
        event.control.value += f"\n{pacifictime} >>> "
        page.update()
    
    def create_input_field():
        input_field = ft.TextField(
            min_lines=20,max_lines=20, autocorrect=True, hint_text="Start scribing!",
            enable_suggestions=True, multiline=True,shift_enter=True, on_submit=insert_timestamp,show_cursor=True,on_focus=insert_timestamp
            )
        return input_field

    prefabtab = ft.Tab(text="eBim",content=ft.Column([create_input_field()]))
    prefabtabs = []

    def add_tabs():

        ft.View.update()
        

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[prefabtab],
        expand=1,
    )
    page.add(t)


ft.app(target=main)
