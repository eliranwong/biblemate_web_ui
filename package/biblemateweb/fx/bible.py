from nicegui import ui

def luV(event):
    b, c, v = event.args
    ui.notify(f"b: {b}, c: {c}, v: {v}")
    
    # Create a context menu at the click position
    with ui.context_menu() as menu:
        ui.menu_item('Bible Commentaries', on_click=lambda: ui.navigate.to('/tool/commentary'))
        ui.menu_item('Cross-references', on_click=lambda: ui.navigate.to('/tool/xref'))
        ui.menu_item('Treasury of Scripture Knowledge', on_click=lambda: ui.navigate.to('/tool/tske'))
        ui.menu_item('Discourse Analysis', on_click=lambda: ui.navigate.to('/tool/discourse'))
        ui.menu_item('Morphological Data', on_click=lambda: ui.navigate.to('/tool/morphology'))
        ui.menu_item('Translation Spectrum', on_click=lambda: ui.navigate.to('/tool/translations'))
    menu.open()