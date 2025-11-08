from nicegui import ui

# Global variable to track current layout
current_layout = 1  # 1, 2, or 3
area1_container = None
area2_container = None
area1_wrapper = None
area2_wrapper = None
splitter = None
is_lt_sm = False

@ui.page('/')
def page_home(q: str | None = None):
    create_menu()
    create_content_areas()

def create_menu():
    """Create horizontal navigation bar at the top"""
    with ui.header().classes('items-center'):
        with ui.row().classes('items-center gap-4'):
            ui.button('Swap Layout', on_click=swap_layout, icon='swap_horiz')
            ui.button('Example Page 1', on_click=load_example_page_1, icon='description')
            ui.button('Example Page 2', on_click=load_example_page_2, icon='article')

def check_breakpoint(ev):
    global is_lt_sm, splitter

    # prefer the well-known attributes
    width = getattr(ev, 'width', None)

    # fallback: some versions wrap data inside an attribute (try common names)
    if width is None:
        for maybe in ('args', 'arguments', 'data', 'payload'):
            candidate = getattr(ev, maybe, None)
            if isinstance(candidate, dict) and 'width' in candidate:
                width = candidate['width']
                break
    if width is None:
        print('Could not determine width from event:', ev)
        return
    is_lt_sm = width < 640   # tailwind sm = 640px
    if splitter:
        if is_lt_sm:
            splitter.props('horizontal')
        else:
            splitter.props(remove='horizontal')

def create_content_areas():
    """Create two scrollable areas with responsive layout"""
    global area1_container, area2_container, area1_wrapper, area2_wrapper, splitter, is_lt_sm
    
    ui.on('resize', check_breakpoint)

    # Create splitter with initial horizontal layout
    splitter = ui.splitter(value=100, horizontal=is_lt_sm).classes('w-full').style('height: calc(100vh - 64px)')
    
    with splitter.before:
        area1_wrapper = ui.column().classes('w-full h-full')
        with area1_wrapper:
            area1_container = ui.scroll_area().classes('w-full h-full p-4')
            with area1_container:
                ui.label('Area 1').classes('text-2xl font-bold mb-4')
                ui.label('This is the first scrollable area').classes('text-gray-600')
    
    with splitter.after:
        area2_wrapper = ui.column().classes('w-full h-full')
        with area2_wrapper:
            area2_container = ui.scroll_area().classes('w-full h-full p-4')
            with area2_container:
                ui.label('Area 2').classes('text-2xl font-bold mb-4')
                ui.label('This is the second scrollable area').classes('text-gray-600')
    
    # Set initial visibility (Area 1 visible, Area 2 hidden)
    update_visibility()

def swap_layout():
    """Swap between three layout modes"""
    global current_layout
    
    current_layout = (current_layout % 3) + 1
    update_visibility()
    ui.notify(f'Switched to Layout {current_layout}')

def update_visibility():
    """Update visibility of areas based on current layout"""
    global current_layout, area1_wrapper, area2_wrapper, splitter
    
    if current_layout == 1:
        # Area 1 visible, Area 2 invisible - maximize Area 1
        area1_wrapper.set_visibility(True)
        area2_wrapper.set_visibility(False)
        splitter.set_value(100)  # Move splitter to maximize Area 1
    elif current_layout == 2:
        # Both areas visible - 50/50 split
        area1_wrapper.set_visibility(True)
        area2_wrapper.set_visibility(True)
        splitter.set_value(50)  # Move splitter to middle
    elif current_layout == 3:
        # Area 1 invisible, Area 2 visible - maximize Area 2
        area1_wrapper.set_visibility(False)
        area2_wrapper.set_visibility(True)
        splitter.set_value(0)  # Move splitter to maximize Area 2

def load_example_page_1():
    """Load example content in Area 1"""
    global area1_container
    
    area1_container.clear()
    with area1_container:
        ui.label('Example Page 1').classes('text-3xl font-bold mb-4 text-blue-600')
        ui.label('This is example content for testing Area 1').classes('text-lg mb-2')
        
        for i in range(1, 21):
            ui.label(f'Line {i}: Sample text content for Area 1').classes('mb-2')
    
    ui.notify('Loaded Example Page 1 in Area 1')

def load_example_page_2():
    """Load example content in Area 2"""
    global area2_container
    
    area2_container.clear()
    with area2_container:
        ui.label('Example Page 2').classes('text-3xl font-bold mb-4 text-green-600')
        ui.label('This is example content for testing Area 2').classes('text-lg mb-2')
        
        for i in range(1, 21):
            ui.label(f'Line {i}: Sample text content for Area 2').classes('mb-2')
    
    ui.notify('Loaded Example Page 2 in Area 2')

# Run the app
ui.run(port=9999)