import streamlit as st
from TicToc import get_val,validate
import numpy as np
import math
def main():
    menu=["Play","Instruction","About"]
    option=st.sidebar.selectbox("Menu",menu)

    if option=="Play":
        st.subheader("Let Quants decide who will win !")
        st.write("Computer --> |0>")
        st.write("User     --> |1>")
        ini='|m>'
        if 'board' not in st.session_state:
            st.session_state.board=np.array([[ini,ini,ini],[ini,ini,ini],[ini,ini,ini]])
            st.session_state.available_moves=[0,1,2,3,4,5,6,7,8,9]
        moves=st.selectbox("Move a move!",st.session_state.available_moves)
        if moves==1:
            if st.session_state.board[0,0]==ini:
                st.session_state.board[0,0]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==2:
            if st.session_state.board[0,1]==ini:
                st.session_state.board[0,1]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==3:
            if st.session_state.board[0,2]==ini:
                st.session_state.board[0,2]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==4:
            if st.session_state.board[1,0]==ini:
                st.session_state.board[1,0]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==5:
            if st.session_state.board[1,1]==ini:
                st.session_state.board[1,1]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==6:
            if st.session_state.board[1,2]==ini:
                st.session_state.board[1,2]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)   
        elif moves==7:
            if st.session_state.board[2,0]==ini:
                st.session_state.board[2,0]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==8:
            if st.session_state.board[2,1]==ini:
                st.session_state.board[2,1]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        elif moves==9:
            if st.session_state.board[2,2]==ini:
                st.session_state.board[2,2]=get_val()
                user_flag=validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                comp_sq=np.random.randint(1,9)
                col=(comp_sq-1)%3
                row=math.floor((comp_sq-1)/3)
                com_val=get_val()
                if st.session_state.board[row,col]==ini:
                    st.session_state.board[row,col]=com_val
                com_flag=validate(st.session_state.board)
                if not com_flag:
                    return 0
                st.write("Computer's Move: ",comp_sq)
                st.write("Computer's Value: ",com_val)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)     
    elif option=="Instruction":
        st.subheader("Instructions")
        
        info="""
        Created using Qiskit and Streamlit.


        
        
        
        
        User have |1> assigned 
        
        
        
        
        Computer has |0> assigned
            
            There is superposititon of both staes initially so ,
                there could be chances that your assigned value can be changed to |0>

        Be Safe,
        Happy Coding. 
        
        """
        st.write(info)
    else :
        st.subheader("ABOUT")
        about="""
            Hello All,
                This is developed as a experiment in order to learn basics of Quantum Computation.
                
                
                pip install qiskit
                pip install streamlit






           Developed with love by Ayush Baluni.
        """
        st.write(about)



if __name__=='__main__':
   condition= main()
   if condition==0:
    st.subheader("Game Over!")