from modules.FileManager import *
from pathlib import Path
import streamlit as st
from modules import *
import numpy as np
import sympy as sp


def matrix_power(A, n):
    if n < 0:
        raise ValueError("Exponent n must be non-negative")
    if n == 0:
        return np.identity(A.shape[0])  # Ma trận đơn vị
    else:
        return np.linalg.matrix_power(A, n)


def sidebarConfig(sidebar):
    with sidebar:
        pass

def customsGroup(current_dir):
    css__custom = f'{current_dir}/assets/styles/custom.css'
    Custom_CSS(st, css__custom)
    Custom_Code(st, """
            <div class="main__title"> 
                <h3> Bài tập ma trận và định thức <h3>
            <div/>        
        """)
def main(sidebar):
    root_directory = "assets/exercises/matrices_determinants"
    # file_manager = os.path.join(root_directory)
    with st.expander("Bài tập ma trận", expanded=False):
        file_path = "assets/exercises/matrices_determinants/Bai-tap-ma-tran.pdf"
        download_button("Bài tập ma trận", file_path)
        st.header("Bài 1:")
        st.image(root_directory + "/image/b11.png")
        A = np.array([[2,1,-1], [0,1,-4]])
        B = np.array([[-2,1, 0], [-3, 2,2]])

        col_code, col_result = st.columns(2)
        with col_code:
            st.write("Code")
            code = '''
                import numpy as np
                A = np.array([[2,1,-1], [0,1,-4]])
                B = np.array([[-2,1, 0], [-3, 2,2]])
                # 3A+2B
                print(3*A+2*B)
                
                # 3A-2B
                print(3*A-2*B)
            '''
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.latex("3A+2B")
            st.write(3*A+2*B)
            st.latex("3A-2B")
            st.write(3*A-2*B)
        # ====================================== #
        col_code, col_result = st.columns(2)
        with col_code:
            st.write("Code")
            code = '''
                import numpy as np
                A = np.array([[2,1,-1], [0,1,-4]])
                B = np.array([[-2,1, 0], [-3, 2,2]])
                result = np.dot(A.T, A)
                print(result)
            '''
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.latex("A^T A")
            st.write(np.dot(A.T, A))
            st.latex("AA^T")
            st.write(np.dot(A, A.T))
        # ======================== #
        st.header("Bài 2:")
        st.image(root_directory + "/image/b12.png")
        
        A = np.array([[4,0,5], [-1,3,2]])
        B = np.array([[1,1,1], [3,5,7]])
        C = np.array([[2,-3], [0,1]])
        
        col_code, col_result = st.columns(2)
        with col_code:
            st.write("Code")
            code = '''
                import numpy as np
                A = np.array([[4,0,5], [-1,3,2]])
                B = np.array([[1,1,1], [3,5,7]])
                C = np.array([[2,-3], [0,1]])
                
                # A + B
                print(A+B)
                
                # A - B
                print(A-B)
                
                # 2A
                print(2*A)
                
                # -3B
                print(-3*B)
                
                # 2A - 3B
                print(2*A-3*B)
                
                # AT.C
                print(np.dot(A.T, C))
                
                # C.A + B
                print(np.dot(C, A) + B)
                
                # (C.A)T - 2BT
                print(np.dot(C, A).T - (2*B).T)
            '''
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            # A + B
            st.latex("A + B")
            st.write(A+B)
            # A - B
            st.latex("A - B")
            st.write(A-B)
            # 2A
            st.latex("2A")
            st.write(2*A)
            # -3B
            st.latex("-3B")
            st.write(-3*B)
            # 2A - 3B
            st.latex("2A - 3B")
            st.write(2*A-3*B)
            # AT.C
            st.latex("A^T C")
            st.write(np.dot(A.T, C))
            # C.A + B
            st.latex("C.A + B")
            st.write(np.dot(C, A) + B)
            # (C.A)T - 2BT
            st.latex("(C.A)^T - 2B^T")
            st.write(np.dot(C, A).T - (2*B).T)
    # ======================== #
        st.header("Bài 3: Tính các tích sau")
        st.image(root_directory + "/image/b13a.png")
        A = np.array([[1,-3,2], [3,-4,1], [2,-5,3]])
        B = np.array([[2,5,6], [1,2,5], [1,3,2]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,-3,2], [3,-4,1], [2,-5,3]])
            B = np.array([[2,5,6], [1,2,5], [1,3,2]])
            print(np.dot(A, B))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.dot(A, B))
            
        st.image(root_directory + "/image/b13b.png") 
        A = np.array([[5,0,2,3] ,[4,1,5,3] ,[3,1,-1,2]])
        B = np.array([[6],[-2],[7],[4]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[5,0,2,3] ,[4,1,5,3] ,[3,1,-1,2]])
            B = np.array([[6],[-2],[7],[4]])
            print(np.dot(A, B))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.dot(A, B))
                   
        st.image(root_directory + "/image/b13d.png") 
        A = np.array([[3,1,1], [2,1,2],[1,2,3]])
        B = np.array([[1,1,-1], [2,-1,1], [1,0,1]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[3,1,1], [2,1,2],[1,2,3]])
            B = np.array([[1,1,-1], [2,-1,1], [1,0,1]])
            print(np.dot(A, B))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.dot(A, B))        
               
        st.image(root_directory + "/image/b13e.png")  
        A = np.array([[1,2,1], [0,1,2] ,[3,1,1]])
        B = np.array([[2,3,1] ,[-1,1,0] ,[1,2,-1]])
        C = np.array([[1,2,1] ,[0,1,2] ,[3,1,1]])
        AB = np.dot(A,B)
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,2,1], [0,1,2] ,[3,1,1]])
            B = np.array([[2,3,1] ,[-1,1,0] ,[1,2,-1]])
            C = np.array([[1,2,1] ,[0,1,2] ,[3,1,1]])
            AB = np.dot(A,B)
            print(np.dot(AB, C))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.dot(AB, C))       
    # ======================== #
        st.header("Bài 4:")        
        st.image(root_directory + "/image/b14a.png")
        A = np.array([[0,1,0], [0,0,1], [0,0,0]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            
            def matrix_power(A, n):
                if n < 0:
                    raise ValueError("Exponent n must be non-negative")
                if n == 0:
                    return np.identity(A.shape[0])  # Ma trận đơn vị
                else:
                    return np.linalg.matrix_power(A, n)
            
            A = np.array([[0,1,0], [0,0,1], [0,0,0]])
            print(matrix_power(A, 2))
            print(matrix_power(A, 3))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.latex("A^2")
            st.write(matrix_power(A, 2))
            st.latex("A^3")
            st.write(matrix_power(A, 3))
        st.image(root_directory + "/image/b14b.png")
        A = np.array([[1,2,1], [0,1,2], [3,1,1]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            
            def matrix_power(A, n):
                if n < 0:
                    raise ValueError("Exponent n must be non-negative")
                if n == 0:
                    return np.identity(A.shape[0])  # Ma trận đơn vị
                else:
                    return np.linalg.matrix_power(A, n)
            
            A = np.array([[1,2,1], [0,1,2], [3,1,1]])
            print(matrix_power(A, 2))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(matrix_power(A, 2))
            
        st.image(root_directory + "/image/b14c.png")
        A = np.array([[2, 1], [1, 3]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[2, 1], [1, 3]])
            print(matrix_power(A, 3))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(matrix_power(A, 3))
        st.image(root_directory + "/image/b14d.png")
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            n = int(input("Nhập n: "))
            A = np.array([[1, 1], [0, 1]])
            print(matrix_power(A, n))
            ''' 
            st.code(code, language='python')
        with col_result:
            with st.form("b14d"):
                n = st.number_input("Nhập n", value=0)
                submitted = st.form_submit_button()
                if submitted:
                    A = np.array([[1, 1], [0, 1]])
                    st.write("Result")
                    st.write(matrix_power(A, n))
        
    # ======================== #
        st.header("Bài 5: Tính AB - BA")        
        st.image(root_directory + "/image/b15a.png")
        A = np.array([[1, 2], [4, -1]])
        B = np.array([[2, -3], [-4, 1]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1, 2], [4, -1]])
            B = np.array([[2, -3], [-4, 1]])
            print(np.dot(A,B) - np.dot(B,A))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.dot(A,B) - np.dot(B,A))
        
        st.image(root_directory + "/image/b15c.png")
        A = np.array([[1,1,1],[0,1,1],[0,0,1]])
        B = np.array([[7,5,3],[0,7,5],[0,0,7]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,1,1],[0,1,1],[0,0,1]])
            B = np.array([[7,5,3],[0,7,5],[0,0,7]])
            print(np.dot(A,B) - np.dot(B,A))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.dot(A,B) - np.dot(B,A))
    # ======================== #
        st.header("Bài 6:  Tìm ma trận nghịch đảo của ma trận")        
        st.image(root_directory + "/image/b16a.png")   
        A = np.array([[1,0,3],[2,1,1],[3,2,2]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,0,3],[2,1,1],[3,2,2]])
            print(np.linalg.inv(A))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.linalg.inv(A))     
        
        st.image(root_directory + "/image/b16b.png") 
        A = np.array([[1,3,2],[2,1,3],[3,2,1]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,3,2],[2,1,3],[3,2,1]])
            print(np.linalg.inv(A))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.linalg.inv(A))            
        st.image(root_directory + "/image/b16c.png")        
        A = np.array([[-1,1,1,1],[1,-1,1,1],[1,1,-1,1],[1,1,1,-1]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[-1,1,1,1],[1,-1,1,1],[1,1,-1,1],[1,1,1,-1]])
            print(np.linalg.inv(A))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.linalg.inv(A))            
        st.image(root_directory + "/image/b16d.png")        
        A = np.array([[0,1,1,1],[-1,0,1,1],[-1,-1,0,1],[-1,-1,-1,0]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[0,1,1,1],[-1,0,1,1],[-1,-1,0,1],[-1,-1,-1,0]])
            print(np.linalg.inv(A))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write(np.linalg.inv(A))          
              
        st.image(root_directory + "/image/b16e.png")
        col_code, col_result = st.columns(2)    
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            n = int(input("Nhập n: "))
            matrix = np.zeros((n, n))
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j] = 1
            print(matrix)
            print(np.linalg.inv(matrix))
            ''' 
            st.code(code, language='python')
        with col_result:
            # st.write(np.linalg.inv(A))  
            with st.form("b16e"):
                n = st.number_input("Nhập n", value=0)
                submitted = st.form_submit_button()
                if submitted:
                    matrix = np.zeros((n, n))
                    for i in range(n):
                        for j in range(i, n):
                            matrix[i][j] = 1
                    
                    st.write("Ma trận nxn")
                    st.write(matrix)     
                    st.write("Result")
                    st.write(np.linalg.inv(matrix))        
        st.image(root_directory + "/image/b16f.png") 
        col_code, col_result = st.columns(2)    
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            n = int(input("Nhập n: "))
            a = int(input("Nhập a: "))
            matrix = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if i == j:
                        matrix[i][j] = 1 + a
                    else:
                        matrix[i][j] = 1
            print(matrix)
            print(np.linalg.inv(matrix))
            ''' 
            st.code(code, language='python')
        with col_result:
            # st.write(np.linalg.inv(A))  
            with st.form("b16f"):
                n = st.number_input("Nhập n", value=0)
                a = st.number_input("Nhập a", value=0)
                submitted = st.form_submit_button()
                if submitted:
                    matrix = np.zeros((n, n))
                    for i in range(n):
                        for j in range(n):
                            if i == j:
                                matrix[i][j] = 1 + a
                            else:
                                matrix[i][j] = 1
                    
                    st.write("Ma trận nxn")
                    st.write(matrix)     
                    st.write("Result")
                    st.write(np.linalg.inv(matrix))       
        
    with st.expander("Bài tập định thức", expanded=True):
        file_path = "assets/exercises/matrices_determinants/Bai-tap-đinh-thuc-tu-luan.pdf"
        download_button("Bài tập định thức", file_path)
        st.header("Bài 1: Tính các định thức sau")        
        st.image(root_directory + "/image/b21a.png")   
        A = np.array([[4,-1,3],[4,1,0],[2,-2,5]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[4,-1,3],[4,1,0],[2,-2,5]])
            print(round(np.linalg.det(A)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("det(A) = ",round(np.linalg.det(A)))
        st.image(root_directory + "/image/b21a.png")   
        A = np.array([[3, -1, 6], [5, 2, 7], [8, 9, 4]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[3, -1, 6], [5, 2, 7], [8, 9, 4]])
            print(round(np.linalg.det(A)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("det(A) = ",round(np.linalg.det(A)))
        # ======================== #
        st.header("Bài 2:")
        st.image(root_directory + "/image/b22.png")
        x = sp.symbols('x')
        A = sp.Matrix([[x, 1, 3],[5, 3, 2],[1, 4, 3]])
        equation=sp.Eq(sp.det(A),40)
        ans=sp.solve(equation,x)
        
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import sympy as sp
            x=sp.symbols('x')
            A=sp.Matrix([[x, 1, 3],[5, 3, 2],[1, 4, 3]])
            equation=sp.Eq(sp.det(A),40)
            ans=sp.solve(equation,x)
            print("X là: ", " or ".join(map(str, ans)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("X là: ", " or ".join(map(str, ans)))
        # ======================== #
        st.header("Bài 3: Tính định thức sau:")
        st.image(root_directory + "/image/b23.png")
        
        A = np.array([[3,0,0,0],[5,1,2,0],[2,6,0,-1],[-6,3,1,0]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A=np.array([[3,0,0,0],[5,1,2,0],[2,6,0,-1],[-6,3,1,0]])
            print(round(np.linalg.det(A)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("det(A) = ", round(np.linalg.det(A)))
        # ======================== #
        st.header("Bài 4: Tính det:")
        st.image(root_directory + "/image/b24.png")
        
        A = np.array([[1, 5, 7, 2],[2, 6, 8, 3],[3, 0, 9, 0],[4, 0, 1, 0]])
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A=np.array([[1, 5, 7, 2],[2, 6, 8, 3],[3, 0, 9, 0],[4, 0, 1, 0]])
            print(round(np.linalg.det(A)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("det(A) = ", round(np.linalg.det(A)))
        # ======================== #
        st.header("Bài 5: Tìm 𝑥 thỏa mãn đẳng thức:")
        st.image(root_directory + "/image/b25.png")
        x = sp.symbols('x')
        A = sp.Matrix([[x, 1, 3],[5, 3, 2],[1, 4, 3]])
        ans = sp.Eq(sp.det(A),40)
        
        x = sp.symbols('x')
        A=sp.Matrix([[1, -1, 0, -1],[-2, 3, x, 4],[3, -2, 5, 3],[2, -1, 4, 3]])
        ans = sp.solve(sp.det(A), x)
        
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import sympy as sp
            x = sp.symbols('x')
            A=sp.Matrix([[1, -1, 0, -1],[-2, 3, x, 4],[3, -2, 5, 3],[2, -1, 4, 3]])
            ans = sp.solve(sp.det(A), x)
            print("X là: ", " or ".join(map(str, ans)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("X là: ", " or ".join(map(str, ans)))
        # ======================== #
        st.header("Bài 6: Tìm 𝑥 biết")
        st.image(root_directory + "/image/b26.png")        
        x = sp.symbols('x')
        A=sp.Matrix([[1, -1, 0, -1],[-2, 3, x, 4],[3, -2, 5, 3],[2, -1, 4, 3]])
        ans = sp.solve(sp.det(A), x)
        
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import sympy as sp
            x=sp.symbols('x')
            A=sp.Matrix([[x, 1, 3],[5, 3, 2],[1, 4, 3]])
            equation=sp.Eq(sp.det(A),40)
            ans=sp.solve(equation,x)
            print(ans)
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("X là: ", " or ".join(map(str, ans)))
        # ======================== #
        st.header("Bài 7:")
        st.image(root_directory + "/image/b27.png")
        
        A = np.array([[1,0,1,0],[0,1,0,1]])
        B = np.array([[1,0],[0,1],[1,2],[1,1]])
        C = np.dot(A,B)
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,0,1,0],[0,1,0,1]])
            B = np.array([[1,0],[0,1],[1,2],[1,1]])
            C = np.dot(A,B)
            print(round(np.linalg.det(matrix_power(C, 2))))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Ma trận C: ")
            st.write(C)
            st.write("Result")
            st.write("det(C^2) = ", round(np.linalg.det(matrix_power(C, 2))))
        # ======================== #
        st.header("Bài 8:")
        st.image(root_directory + "/image/b28.png")
        
        A = np.array([[1,0,1,0],[0,1,0,1]])
        B=np.array([[1,0],[0,1],[1,2],[1,1]])
        D = np.dot(B,A)
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,0,1,0],[0,1,0,1]])
            B = np.array([[1,0],[0,1],[1,2],[1,1]])
            D = np.dot(B,A)
            print(round(np.linalg.det(2*D)))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Ma trận D: ")
            st.write(D)
            st.write("Result")
            st.write("det(2D) = ", round(np.linalg.det(2*D)))
            
        # ======================== #
        st.header("Bài 9: Tìm 𝑥 biết")
        st.image(root_directory + "/image/b29.png")
        x = sp.symbols('x')
        A=sp.Matrix([[1, 1, 1, 1],[4, 5, x+11, 8],[3, 4, 10, 7],[2, 3, 5, 4]])
        equation=sp.Eq(sp.det(A), 2)
        ans=sp.solve(equation, x)
        
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import sympy as sp
            x=sp.symbols('x')
            A=sp.Matrix([[1, 1, 1, 1],[4, 5, x+11, 8],[3, 4, 10, 7],[2, 3, 5, 4]])
            equation=sp.Eq(sp.det(A), 2)
            ans=sp.solve(equation, x)
            print(ans)
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Result")
            st.write("X là: ", " or ".join(map(str, ans)))
        # ======================== #
        st.header("Bài 10: Cho ma trận 𝐴3×3 thỏa mãn |𝐴| = 3. Tính |𝐴𝑇𝐴|, |𝐴3| và |3𝐴|.")
        st.markdown("Định thức của một ma trận chuyển vị là bằng định thức của ma trận gốc: ")
        st.latex("|A^T| = |A|")
        st.markdown("Định thức của một ma trận nhân với một hằng số là bằng hằng số đó mũ với bậc của ma trận, trong đó n là kích thước của ma trận. ")
        st.latex("|kA| = k^n * |A|")
        st.markdown("Định thức của một ma trận nhân với một ma trận khác là bằng tích của định thức của hai ma trận đó:")
        st.latex("|AB| = |A| * |B|")
        st.subheader("Giải:")
        st.markdown("Định thức của ma trận A đã được cho là")
        st.latex("|A| = 3.")
        st.markdown("Định thức của ma trận chuyển vị A^T cũng bằng |A|, vì vậy:")
        st.latex("|A^T| = 3")
        st.markdown("Định thức của ma trận 3A là 3^n * |A|, trong đó n là kích thước của ma trận (n = 3), vì vậy:")
        st.latex("|3A| = 3^3 * 3 = 27 * 3 = 81")
        st.markdown("Định thức của ma trận A^TA là |A^T| * |A|, vì vậy:")
        st.latex("|A^TA| = 3 * 3 = 9")
        st.markdown("Định thức của ma trận A^3 là |A|^3, vì vậy:")
        st.latex("|A^3| = 3^3 = 27")
        
    # ======================== #
        st.header("Bài 11:")
        st.image(root_directory + "/image/b28.png")
        
        A = np.array([[1,2,0,0],[2,1,0,0],[0,0,1,3],[0,0,3,1]])
        AAT = np.dot(A,A.T)
        A1 = np.linalg.inv(A)
        col_code, col_result = st.columns(2)     
        with col_code:
            st.write("Code")
            code = '''
            import numpy as np
            A = np.array([[1,2,0,0],[2,1,0,0],[0,0,1,3],[0,0,3,1]])
            AAT = np.dot(A,A.T)
            A1 = np.linalg.inv(A)
            
            print(round(np.linalg.det(A)))
            print(round(np.linalg.det(AAT)))
            print(np.linalg.det(A1))
            ''' 
            st.code(code, language='python')
        with col_result:
            st.write("Ma trận D: ")
            st.write(D)
            st.write("Result")
            st.write("det(A) = ", round(np.linalg.det(A)))    
            st.write("det(AAT) = ", round(np.linalg.det(AAT)))    
            st.write("det(A1) = ", round(np.linalg.det(A1)))    
    
def matrices_determinants(sidebar):
    current_dir = Path(".")
    sidebarConfig(sidebar)
    customsGroup(current_dir)
    main(sidebar)