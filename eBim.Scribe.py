import flet as ft
from zoneinfo import ZoneInfo
from datetime import datetime

class program():

    def main(page: ft.Page):
        page.window_title_bar_hidden = True
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

        tabs_list = [ft.Tab(text="eBim", content=ft.Column([create_input_field()]))]
        

        def add_tab(event):
            new_tab = ft.Tab(text=f"eBim {len(tabs_list)+1}", content=ft.Column([create_input_field()]))
            tabs_list.append(new_tab)  
            tabs_control.tabs = tabs_list  
            tabs_control.selected_index = len(tabs_list) - 1 
            page.update()

        tabs_control = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=tabs_list,
            expand=0,            
        
        )
        add_tab_button = ft.IconButton(icon="ADD", on_click=add_tab)
        page.add(add_tab_button)
        page.add(tabs_control)


    ft.app(target=main)