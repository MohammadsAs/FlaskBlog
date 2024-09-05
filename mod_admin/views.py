from . import admin


@admin.route('/')
def admin_index():
    return "Hello from admin Index"
