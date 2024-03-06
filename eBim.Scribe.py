import sys
import flet as ft
from zoneinfo import ZoneInfo
from datetime import datetime

class program():

    def main(page: ft.Page):
        page.window_title_bar_buttons_hidden = True
        page.window_resizable = True
        page.window_min_height = 680
        page.window_min_width = 320
        page.window_opacity = .95
        page.auto_scroll = True

    def main(page: ft.Page):
        def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
            )
            selected_files.update()

        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_files = ft.Text()

        page.overlay.append(pick_files_dialog)
    def main(page: ft.Page):
        def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
            )
            selected_files.update()

        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_files = ft.Text()

        page.overlay.append(pick_files_dialog)
        
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

        tabs_list = []

        def add_tab(event):
            new_tab = ft.Tab(text=f"eBim {len(tabs_list)+1}", content=ft.Column([create_input_field()]))
            tabs_list.append(new_tab)  
            tabs_control.tabs = tabs_list  
            tabs_control.selected_index = len(tabs_list) - 1 
            page.update()
        
        def close_tab(event):
              
            tabs_control.tabs = tabs_list  
            tabs_control.selected_index = len(tabs_list)
            tabs_list.pop()
            page.update()

        def close_app(event):
            print("exit")
            sys.exit()

        def check_item_clicked(e):
                    e.control.checked = not e.control.checked
                    add_tab(e)
                    e.control.checked = not e.control.checked
                    page.update()

        page.appbar = ft.AppBar(
        leading=ft.PopupMenuButton(tooltip="Create Notes",icon=ft.icons.NOTE_ALT,items=[ft.PopupMenuItem(text="Add Tab",checked=False,on_click=add_tab),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Remove Tab",checked=False,on_click=close_tab),
                    ]),
        leading_width=50,
        title=ft.Text("eBim SCRIBE"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            # ft.PopupMenuButton(icon=ft.icons.SAVE_ALT,tooltip="Save Notes",
            #     items=[
            #         ft.PopupMenuItem(),
            #         ft.PopupMenuItem(text="Save Tabs",checked=False,on_click=lambda _: pick_files_dialog.pick_files(
            #             allow_multiple=True
            #         ))
            #     ]
            # ),
        ],
    )

        tabs_control = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=tabs_list,
            expand=0,            
        
        )
        add_tab_button = ft.IconButton(icon="PLAYLIST_ADD", on_click=add_tab)
        add_close_app_button = ft.IconButton(icon="CLOSE", on_click=close_app,)
        add_close_tab_button = ft.IconButton(icon="PLAYLIST_REMOVE", on_click=close_tab,)

        page.add(tabs_control)


    ft.app(target=main)