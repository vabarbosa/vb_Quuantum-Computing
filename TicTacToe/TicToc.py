import qiskit
from qiskit import QuantumCircuit,Aer
import numpy as np
import streamlit as st
def superposition():
    circuit=QuantumCircuit(1,1)
    circuit.h(0)

    circuit.measure(0,0)
    simulator=Aer.get_backend('aer_simulator')
    result=simulator.run(circuit).result().get_counts()
    return result


def get_val():
    res=superposition()
    values=list(res.values())
    key=list(res.keys())
    val='|'+str(key[np.argmax(values)])+'>'
    return val


def validate(arr):
    flag=True
    zero='|0>'
    one='|1>'
    if arr[0,0]==one and arr[1,1]==one and arr[2,2]==one:
        st.success("User Won!")    
        flag=False
    elif arr[0,0]==zero and arr[1,1]==zero and arr[2,2]==zero:
        st.success("Computer Won!")    
        flag=False
    
    elif arr[0,2]==one and arr[1,1]==one and arr[2,0]==one:
        st.success("User Won!")    
        flag=False
    elif arr[0,2]==zero and arr[1,1]==zero and arr[2,0]==zero:
        st.success("Computer Won!")    
        flag=False
    
    elif arr[0,0]==one and arr[1,1]==one and arr[2,2]==one:
        st.success("User Won!")    
        flag=False
    elif arr[0,0]==zero and arr[1,1]==zero and arr[2,2]==zero:
        st.success("Computer Won!")    
        flag=False
        
    if not flag:
        return 0
    if flag:
        for index in [0,1,2]:
            if(list(arr[index])==[one,one,one]):
               st.success("User Won!")
               return 0    
        for index in [0,1,2]:
            if(list(arr[index])==[zero,zero,zero]):
               st.success("Computer Won!")  
               return 0
        for index in [0,1,2]:
            if(list(arr[:,index])==[one,one,one]):
                st.success("User Won!")    
                return 0
        for index in [0,1,2]:
            if(list(arr[:,index])==[zero,zero,zero]):
                st.success("Computer Won!")    
                return 0
        if "|m>" not in arr:
            st.write("Draw")
            return 0
    return 1
    
    