import os

APPIMAGE_FOLDER = os.path.expanduser("~/Documents/AppImages")
APPLICATIONS_FOLDER = os.path.expanduser("~/.local/share/applications/")

file_names = os.listdir(APPIMAGE_FOLDER)

for file_name in file_names:
    file_path = os.path.join(APPIMAGE_FOLDER, file_name)
    app_name = file_name.replace(".AppImage.new", "").replace(".AppImage", "")
    desktop_content = ["[Desktop Entry]"]
    desktop_content.append(f"Name={app_name}")
    desktop_content.append(f'Exec="{file_path}"')
    desktop_content.append("Type=Application")

    desktop_path = os.path.join(APPLICATIONS_FOLDER, app_name + ".desktop")
    with open(desktop_path, "w") as desktop_file:
        desktop_file.write("\n".join(desktop_content))

    print(file_name)
    print("\n".join(desktop_content))
    print()
