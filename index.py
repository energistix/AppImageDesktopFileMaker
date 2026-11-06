import os

APPIMAGE_FOLDER = os.path.expanduser("~/Documents/AppImages")
APPLICATIONS_FOLDER = os.path.expanduser("~/.local/share/applications/AppImages")

if not os.path.exists(APPLICATIONS_FOLDER):
    os.makedirs(APPLICATIONS_FOLDER)

image_files_names = os.listdir(APPIMAGE_FOLDER)
desktop_files_to_remove = os.listdir(APPLICATIONS_FOLDER)

for file_name in image_files_names:
    file_path = os.path.join(APPIMAGE_FOLDER, file_name)
    app_name = file_name.replace(".AppImage.new", "").replace(".AppImage", "")
    desktop_file_name = app_name + ".desktop"
    if desktop_file_name in desktop_files_to_remove:
        desktop_files_to_remove.remove(desktop_file_name)

    desktop_content = ["[Desktop Entry]"]
    desktop_content.append(f"Name={app_name}")
    desktop_content.append(f'Exec="{file_path}"')
    desktop_content.append("Type=Application")

    desktop_path = os.path.join(APPLICATIONS_FOLDER, desktop_file_name)
    with open(desktop_path, "w") as desktop_file:
        desktop_file.write("\n".join(desktop_content))

    print(f"Created {desktop_file_name}")

print()

for desktop_file_name in desktop_files_to_remove:
    print(f"Removing {desktop_file_name}")
    os.remove(os.path.join(APPLICATIONS_FOLDER, desktop_file_name))
