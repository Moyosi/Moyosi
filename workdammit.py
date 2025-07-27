import streamlit as st
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
if os.path.exists('mood_data.json'):
    with open('mood_data.json', 'r') as file:
        mood_data = json.load(file)
    for key, value in mood_data.items():
        st.session_state[key] = value
st.title('📔Mood tracker')
if 'point' not in st.session_state:
    st.session_state.point =False

if  'removal' not in st.session_state:
    st.session_state.removal = []
task_removal = st.session_state.removal
left,middle,right = st.columns([1,1,1])
with left:
    with st.expander('About app'):
        st.write('''
                 This little app allows you to:
                     Track your mood
                     Track your habits
                     and I hope you enjoy it
                 ''')
with right:
    with st.expander('Disclaimer'):
        st.info('''
                 This app does not work perfectly and althouth the complete
                 task list is edited immediately , the main task list does not 
                 update immediately so there is no need to repeat actions
                 if no change is seen
                 '''
            )
if not 'Completed' in st.session_state :
    st.session_state['Completed'] = []
if "Mood" not in st.session_state:
    st.session_state["Mood"] = []


if "task" not in st.session_state:
    st.session_state["task"] = []
if not 'Journal entry' in st.session_state:
    st.session_state['Journal entry'] = []


    
mood = st.selectbox("Please select today's mood",['Happy','Sad','Pissed','Frustrated','Overloaded','Neutral','Verge of tears',
                                                 'Panic attack','Anxious'])
submit_mood = st.button('Submit your mood')
if submit_mood:
    st.session_state.button_usable = True
    time_of_mood = datetime.now().strftime('%d-%m %H:%M')
    st.session_state['Mood'].append(f'{mood} at {time_of_mood}')
task = st.text_input('What task would you like done today')
if task:
    norm = task.strip().capitalize()
    if not norm in st.session_state['task']:
        st.session_state['task'].append(norm.capitalize())

with st.expander('Tasks'):
    if st.session_state['task']:
        completed_tasks = st.selectbox('Tasks I wanna do',st.session_state['task'])
        completed = st.button('Task has been completed') 
        if completed:
            st.session_state['task'].remove(completed_tasks)
            task_display = completed_tasks.capitalize()
            time_of_comp = datetime.now().strftime('%d-%m %H:%M')
            st.session_state['Completed'].append(f'{task_display} -- {time_of_comp}')
            st.toast(f'You have completed {task_display}',icon='👌')
            
            
    else:
       st.write('Nothing to do ...')
        
        
for taskdone in task_removal:
    try:
        continue
    except ValueError:
        continue
    # ✅ Normalize completed task to match text input
    
    
    # ✅ Always append — no need to check for existing duplicate string
    
    st.write('Good to go babe')

side_for_chart, side, side_for_complete = st.columns([1, 1, 1])
with side_for_complete:
    with st.expander('Completed tasks'):
        # ✅ Render list if not empty
        if st.session_state['Completed']:
            for comp in st.session_state['Completed']:
                st.markdown(f'- {comp}')
        else:
            st.markdown("No tasks completed yet 💨")
with side_for_chart:
    if st.session_state['Mood']:
        with st.expander('Mood chart'):
            moods = [char.split(' at ')[0] for char in st.session_state['Mood']]
            clean_moods = [mood.encode('ascii', 'ignore').decode() for mood in moods]
            moods_count = pd.Series(moods).value_counts()
            base,ax = plt.subplots()
            moods_count.plot(kind='bar',ax = ax,color='orchid')
            st.pyplot(base)

with st.sidebar:
    with st.expander('Optional Journal Entry'):
        entry = st.text_area('What would you like to say')
    enter_entry = st.button('Save entry')
    if enter_entry:
        if entry:
            current = datetime.now().strftime('%d/%m %H:%M ')
            st.session_state['Journal entry'].append(entry + ' at ' + current)
    with st.expander('Entries'):
        if not st.session_state['Journal entry']:
            st.write('Hmm see your thoughts here')
        else:
            rev_entry = st.session_state['Journal entry'][::-1]
            for ent in rev_entry[:]:
                st.markdown(f'- {ent}')

try:
    with open("mood_data.json", "w") as file:
        json.dump(dict(st.session_state), file)
except Exception as e:
    st.error(f"Failed to save session state: {e}")
                