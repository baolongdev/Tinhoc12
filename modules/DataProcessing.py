from modules.FileManager import *
from modules.Software import *
import streamlit as st
from PIL import Image
import tempfile
import cv2
import os


class DataProcessing:
    class Model:
        frame_skip = 2
        limited_image = 200 
        num_columns = 5
        upload_help = "Upload a file to convert"
        upload_button_text = "Upload"
        upload_button_text_desc = "Choose a file"
        folder_name = ""
        
        def set_list_path_images(self, list_path_images):
            if 'list_path_images' not in st.session_state:
                st.session_state['list_path_images'] = []
            st.session_state['list_path_images'].append(list_path_images)

        def get_list_path_images(self):
            if 'list_path_images' not in st.session_state:
                return []
            return st.session_state['list_path_images']
        
        def set_folder_path(self, folder_path):
            st.session_state['folder_path'] = folder_path

        def get_folder_path(self):
            if 'folder_path' not in st.session_state:
                return 0
            return st.session_state['folder_path']
        
        def set_results_VisualSFM(self, folder_path):
            st.session_state['results_VisualSFM'] = folder_path

        def get_results_VisualSFM(self):
            if 'results_VisualSFM' not in st.session_state:
                return None
            return st.session_state['results_VisualSFM']
        
        def set_mvsFile(self, folder_path):
            st.session_state['mvsFile'] = folder_path

        def get_mvsFile(self):
            if 'mvsFile' not in st.session_state:
                return None
            return st.session_state['mvsFile']
        
        pass
    
    def __init__(self, sidebar):
        self.sidebar = sidebar
        self.root_directory = "assets\data"
        self.file_manager = FileManager(self.root_directory)
        pass
    
    def view(self, model):
        placeholder_view = st.empty()
        with self.sidebar:
            model.folder_name = st.text_input("Folder Name")
            model.num_columns = st.number_input("Num columns", 3, 10, 5)
            with st.form("upload-form", clear_on_submit=True):
                uploaded_file = st.file_uploader(
                    model.upload_button_text_desc, accept_multiple_files=True,
                    type=['png', 'jpg', 'jpeg', 'mp4', 'avi', 'mov'],
                    help=model.upload_help,
                    key="uploaded_file" 
                )
                
                
                submitted = st.form_submit_button(model.upload_button_text)
                reset = st.form_submit_button("Reset")
                
            if reset:
                st.session_state.pop('set_list_path_images', None)
                st.session_state.pop('set_folder_path', None)
                st.session_state.pop('set_results_VisualSFM', None)
                st.session_state.pop('set_mvsFile', None)
                st.experimental_rerun()
                                
            if submitted and uploaded_file is not None:
                # if len(uploaded_file) < 5:
                #     with placeholder_view.container():
                #         st.warning("Dữ liệu mà bạn cung cấp không đủ số lượng")
                #         st.warning("Vui lòng bấm Reset để bắt đầu lại quá trình")
                #     return
                
                if model.folder_name == "":
                    with placeholder_view.container():
                        st.warning("Vui lòng điền thông tin Folder Name")
                elif self.file_manager.folder_exists(model.folder_name):
                    with placeholder_view.container():
                        st.warning("Tên thư mục đã tồn tại")
                else:
                    model.set_folder_path(
                        {
                            "folder_root": self.file_manager.create_folder(model.folder_name),
                            "folder_image": self.file_manager.create_folder(model.folder_name+"\Image"),
                            "data_output": self.file_manager.create_folder(model.folder_name+"\data_output"),
                        }
                    )
                    with st.spinner('Wait for it...'):
                        self.upload_file(model, uploaded_file)
                        self.run_VisualSFM(model, model.get_folder_path()["folder_image"], placeholder_view)
                        
        if model.get_results_VisualSFM() is not None and model.get_mvsFile() is not None:
            cols = st.columns([0.7, 0.3])
            self.render_view(model)
            
            with cols[-1]:
                with st.form("run-recontruction", clear_on_submit=True):
                    submitted = st.form_submit_button("run reconstruction", use_container_width=True)
                    log = st.container()
                    if submitted:
                        with st.spinner('Wait for it...'):
                            self.run_CMPMVS(model)
                        pass
                
                    
    def run_CMPMVS(self, model):
        st.toast("Start Reconstruction!")
        self.file_manager.run_command(f'CMPMVS.exe {model.get_mvsFile()}', path_software["CMPMVS"])
        folder_data = model.get_folder_path()["data_output"]
        folder_image = model.get_folder_path()["folder_image"]
        folder_root = model.get_folder_path()["folder_root"]
        self.file_manager.move_folder(f"{folder_image}/cmp.nvm.cmp/{model.get_results_VisualSFM()[0]}/data/_OUT", folder_data)
        self.file_manager.move_folder(f"{folder_image}/cmp.nvm.cmp/{model.get_results_VisualSFM()[0]}/data/_tmp/SGM/_tmp", f"{folder_data}/SGM")
        self.file_manager.move_folder(f"{folder_image}/cmp.nvm.cmp/{model.get_results_VisualSFM()[0]}/data/_tmp/REFINERC/_tmp", f"{folder_data}/REFINERC")
        self.file_manager.delete_folder(f"{folder_image}/cmp.nvm.cmp/{model.get_results_VisualSFM()[0]}/data/_tmp")
        self.file_manager.folder_to_zip(folder_data, f"{folder_root}/data_output.zip")
        st.toast("Done Reconstruction!")
    
    def render_view(self, model):
        image_paths = model.get_list_path_images()
        num_columns = model.num_columns
        groups = []
        for i in range(0, len(image_paths), num_columns):
            groups.append(image_paths[i:i+num_columns])
        with st.container():
            cols = st.columns(num_columns)
            for group in groups:
                for i, image_path in enumerate(group):
                    with cols[i]:
                        st.image(image_path)
                        st.text_input("abc", value=image_path, disabled=True, label_visibility="hidden")
          
    def run_VisualSFM(self, model, folder_image, placeholder_view):
        folder_image = folder_image.replace("\\", "/")
        self.file_manager.run_command(f'{path_software["VisualSFM"]} sfm+cmpmvs ./{folder_image} ./{folder_image}/cmp.nvm')
        model.set_results_VisualSFM(self.file_manager.get_subfolders(folder_image + "/cmp.nvm.cmp"))       
        model.set_mvsFile(os.path.join(os.getcwd(), folder_image, "cmp.nvm.cmp", model.get_results_VisualSFM()[0], "mvs.ini").replace("\\", "/"))
        
        if len(model.get_results_VisualSFM()) < 1 or len(model.get_results_VisualSFM()) > 1:
            with placeholder_view.container():
                st.warning("Dữ liệu mà bạn cung cấp không đủ số lượng hoặc có nhiều hơn một chủ thể")
                st.warning("Vui lòng bấm Reset để bắt đầu lại quá trình")
            self.file_manager.delete_folder(model.folder_name)
            model.set_results_VisualSFM(None)
            model.set_mvsFile(None)
            return False
        return True        
                            

    def upload_file(self, model, uploaded_file):
        count = 0
        folder_image = model.get_folder_path()["folder_image"]
        for file in uploaded_file:
            if file is not None:
                file_name = file.name.split(".")[0]
                extension = file.name.split(".")[-1]
                extension = extension.lower()
                if extension in ('png', 'jpg', 'jpeg'):
                    output_image_path = os.path.join(folder_image, f"{count}.jpg")
                    img = Image.open(file).convert("RGB")
                    img.save(output_image_path, format="JPEG")
                    model.set_list_path_images(output_image_path)
                    count += 1
                elif extension in ['mp4', 'avi', 'mov']:
                    tffile = tempfile.NamedTemporaryFile(delete=False)
                    tffile.write(file.read())
                    video_capture = cv2.VideoCapture(tffile.name)
                    frame_count = 0
                    model.frame_skip = 20
                    
                    while True:
                        ret, frame = video_capture.read()
                        if not ret:
                            break
                        if frame_count % model.frame_skip == 0:
                            output_image_path = os.path.join(folder_image, f"{count}.jpg")
                            cv2.imwrite(output_image_path, frame)
                            model.set_list_path_images(output_image_path)
                            count += 1
                        frame_count += 1
                        if frame_count / model.frame_skip > model.limited_image:
                            st.toast(f"Video {file_name} quá dài\n đã vượt giới hạn 200 ảnh")
                            break
                    video_capture.release()
                    cv2.destroyAllWindows()