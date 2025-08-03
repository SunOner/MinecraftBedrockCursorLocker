import win32gui
import win32api
import time

def find_minecraft_window():
    def enum_callback(hwnd, results):
        if win32gui.IsWindowVisible(hwnd):
            class_name = win32gui.GetClassName(hwnd)
            title = win32gui.GetWindowText(hwnd)
            if class_name == "ApplicationFrameWindow" and "Minecraft" in title:
                results.append(hwnd)
    results = []
    win32gui.EnumWindows(enum_callback, results)
    return results[0] if results else None

def get_window_bounds(hwnd):
    rect = win32gui.GetClientRect(hwnd)
    top_left = win32gui.ClientToScreen(hwnd, (rect[0], rect[1]))
    bottom_right = win32gui.ClientToScreen(hwnd, (rect[2], rect[3]))
    return (top_left[0], top_left[1], bottom_right[0], bottom_right[1])

def cursor_in_bounds(pos, bounds):
    x, y = pos
    left, top, right, bottom = bounds
    return left <= x <= right and top <= y <= bottom

def clamp_cursor_to_bounds(bounds):
    left, top, right, bottom = bounds
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2
    win32api.SetCursorPos((center_x, center_y))

hwnd = find_minecraft_window()
if hwnd:
    bounds = get_window_bounds(hwnd)
    print(f"Window found. Bounds: {bounds}")
    paused = False
    try:
        while True:
            alt_pressed = win32api.GetAsyncKeyState(0x12) & 0x8000
            key1_pressed = win32api.GetAsyncKeyState(0x31) & 0x8000
            key2_pressed = win32api.GetAsyncKeyState(0x32) & 0x8000
            
            if alt_pressed and key1_pressed:
                paused = not paused
                print("Pause activated" if paused else "Pause deactivated")
                time.sleep(0.5)
            
            if alt_pressed and key2_pressed:
                print("Script stopped (Alt+2).")
                break
            
            if not paused:
                pos = win32api.GetCursorPos()
                if not cursor_in_bounds(pos, bounds):
                    clamp_cursor_to_bounds(bounds)
            
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Script stopped (Ctrl+C).")
else:
    print("Minecraft window not found.")