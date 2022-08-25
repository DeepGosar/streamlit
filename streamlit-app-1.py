# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:46:58 2022

@author: deep.gosar
"""

import streamlit as st

mytsks = []

def addTask():
    tsk = st.text_input('Enter your tasks', key = 1, placeholder = 'Enter a task')
    mytsks.append(tsk)

def cmpltTask(task):
    mytsks.remove(task)


st.button('Add Task', on_click = addTask())

st.write("Your tasks:")
for task in mytsks:
    st.checkbox(task, help ='Check to mark as completed', on_change = cmpltTask(task))