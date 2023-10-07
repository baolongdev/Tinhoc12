import os
import subprocess
import shlex
import shutil
import zipfile
import datetime
import streamlit as st
class FileManager:
    def __init__(self, root_directory):
        self.root_directory = root_directory


    def create_folder(self, foldername):
        full_path = os.path.join(self.root_directory, foldername)
        try:
            os.mkdir(full_path)
            print(f'Tạo thư mục "{full_path}" thành công.')
            return full_path
        except FileExistsError:
            print(f'Thư mục "{full_path}" đã tồn tại.')
        except Exception as e:
            print(f'Không thể tạo thư mục "{full_path}": {e}')

    def delete_file(self, filename):
        full_path = os.path.join( filename)
        try:
            os.remove(full_path)
            print(f'Xóa tệp tin "{full_path}" thành công.')
        except FileNotFoundError:
            print(f'Tệp tin "{full_path}" không tồn tại.')
        except Exception as e:
            print(f'Không thể xóa tệp tin "{full_path}": {e}')

    def delete_folder(self, foldername):
        full_path = os.path.join(foldername)
        try:
            shutil.rmtree(full_path)
            print(f'Xóa thư mục "{full_path}" thành công.')
        except FileNotFoundError:
            print(f'Thư mục "{full_path}" không tồn tại.')
        except OSError as e:
            print(f'Không thể xóa thư mục "{full_path}": {e}')

    def file_exists(self, filename):
        full_path = os.path.join(filename)
        return os.path.isfile(full_path)

    def folder_exists(self, foldername):
        full_path = os.path.join(self.root_directory, foldername)
        return os.path.isdir(full_path)

    def copy_folder(self, source_folder, destination_folder):
        source_path = os.path.join( source_folder)
        destination_path = os.path.join( destination_folder)

        try:
            shutil.copytree(source_path, destination_path)
            print(f'Sao chép thư mục "{source_folder}" thành công đến "{destination_folder}".')
        except Exception as e:
            print(f'Không thể sao chép thư mục: {e}')

    def move_folder(self, source_folder, destination_folder):
        source_path = os.path.join(source_folder)
        destination_path = os.path.join(destination_folder)

        try:
            shutil.move(source_path, destination_path)
            print(f'Di chuyển thư mục "{source_folder}" thành công đến "{destination_folder}".')
        except Exception as e:
            print(f'Không thể di chuyển thư mục: {e}')

    def add_folder(self, source_folder):
        try:
            current_directory = os.path.join( source_folder)
            # Đếm số thư mục đã tạo trong thư mục hiện tại
            num_folders_created = len([name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))])
            new_folder_name = os.path.join(current_directory, str(num_folders_created + 1))

            # Tạo thư mục mới với tên theo thứ tự "1", "2", "3", ...
            os.makedirs(new_folder_name)
            print(f'Tạo thư mục mới "{new_folder_name}" thành công.')
            return new_folder_name
        except Exception as e:
            print(f'Không thể tạo thư mục: {e}')

    def folder_to_zip(self, folder_to_compress, zip_filename):
        folder_path = os.path.join(folder_to_compress)
        zip_file_path = os.path.join(zip_filename)

        try:
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname=arcname)
            print(f'Nén thư mục "{folder_to_compress}" thành công thành "{zip_filename}".')
        except Exception as e:
            print(f'Không thể nén thư mục: {e}')

    def get_subfolders(self, source_folder):
        subfolders = []
        current_directory = os.path.join(source_folder)

        try:
            for entry in os.listdir(current_directory):
                entry_path = os.path.join(current_directory, entry)
                if os.path.isdir(entry_path):
                    subfolders.append(entry)
            return subfolders
        except Exception as e:
            print(f'Không thể lấy danh sách thư mục con: {e}')

    def get_subfiles(self, foldername, extension=None):
        full_path = os.path.join(self.root_directory, foldername)
        subfiles = []
        try:
            for entry in os.listdir(full_path):
                entry_path = os.path.join(full_path, entry)
                if os.path.isfile(entry_path):
                    if extension is None or entry.endswith(f".{extension}"):
                        subfiles.append(entry)
            return subfiles
        except Exception as e:
            print(f'Không thể lấy danh sách tệp tin con: {e}')

    def get_folder_size(self, folder_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size / 1024 / 1024 / 1024  

    def get_folder_time_info(self, folder_path):
        try:
            # Lấy thông tin thời gian tạo thư mục
            created_timestamp = os.path.getctime(folder_path)
            created_time = datetime.datetime.fromtimestamp(created_timestamp)

            # Lấy thông tin thời gian sửa đổi lần cuối
            modified_timestamp = os.path.getmtime(folder_path)
            modified_time = datetime.datetime.fromtimestamp(modified_timestamp)

            return {
                "created_time": created_time.strftime('%Y-%m-%d %H:%M:%S'),
                "modified_time": modified_time.strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f'Không thể lấy thông tin thời gian thư mục: {e}')
            return None

    def run_command(self, command, workingDirectory = None):
        current_directory = os.getcwd()
        if workingDirectory:
            os.chdir(workingDirectory)  
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Đọc đầu ra trong khi quá trình đang chạy
        for line in process.stdout:
            output = line.strip()
            print(output)
            if output != "":
                st.toast(output)
            
        # Chờ quá trình con hoàn thành và lấy kết quả trả về (exit code)
        process.wait()
        os.chdir(current_directory)
        return True

# # Sử dụng lớp FileManager với thư mục gốc "my_root_folder"
# file_manager = FileManager("my_root_folder")
# file_manager.create_file('example.txt')
# file_manager.create_folder('example_folder')
# file_manager.delete_file('example.txt')
# file_manager.delete_folder('example_folder')

# if file_manager.file_exists('example.txt'):
#     st.toast(f'Tệp tin "example.txt" tồn tại trong thư mục gốc "{file_manager.root_directory}".')
# else:
#     st.toast(f'Tệp tin "example.txt" không tồn tại trong thư mục gốc "{file_manager.root_directory}".')

# if file_manager.folder_exists('example_folder'):
#     st.toast(f'Thư mục "example_folder" tồn tại trong thư mục gốc "{file_manager.root_directory}".')
# else:
#     st.toast(f'Thư mục "example_folder" không tồn tại trong thư mục gốc "{file_manager.root_directory}".')
