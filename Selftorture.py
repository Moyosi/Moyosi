import streamlit as st 
import time
import string
import random
st.title('So this little nigga lets u play around with different functions')

work = st.selectbox('Pick a function',['Convert to binary','From binary to base10','Sum of digits','Factorial','Reverse','Palindrome checker','Fibonnacci sequence','Password generator','Password validator'])
if work.lower() == 'convert to binary':
    
    work = True
    num = st.slider('Choose your number',1,50)
    fake_ans = ''
    max_it = 300
    if num == 0:
        print('0')
        work = False
    while num != 1 and max_it >= 5 and work:
        max_it -= 1
        if num % 2 == 0:
            num = num / 2
            fake_ans += '0'
        elif num % 2 == 1:
            num = (num - 1)/ 2
            fake_ans += '1'
    if num == 1 :
        fake_ans += '1'
    ans = fake_ans[::-1]
    with st.spinner("⏳ Calculating your result..."):
        time.sleep(2)
        st.success(f"✅ Done! Here's your answer: {ans}")
    
elif work.lower() == 'from binary to base10':
    works =True
    binary = st.number_input('Hey so type in an integer',min_value= 0,format="%d")
    ans = 0
    message = st.empty()
    ok = False
    try:
        binary = int(binary)
    except ValueError:
        works = False
        message.error("Please enter a valid number.")
        st.stop()
    str_version = str(binary)
    need = []
    for stuff in range(1,(len(str_version)+1)):
        need.append(stuff)
    for number in str_version:
        if number == '1' or number == '0':
            ok = True
        else:
            st.error('Invalid number')
            st.stop()
        
    for thing in range(0,len(str_version)):
        workable = -need[thing]
        worker = str_version[workable]
        workeri = int(worker)
        temp = workeri * (2**thing)
        ans += temp
    with st.spinner('Computing'):
        time.sleep(2)
        st.write(f'{ans}')
elif work == 'Fibonnacci sequence':
    degree = st.slider('How many numbers in the sequence would you like generated',1,50)
    x = 0
    y = 1
    l = []
    r =1
    while r <= degree:
        r += 1
        l.append(x)
        x,y = y,x+y
    for item in l:
        st.markdown(f'- {item}')
elif work == 'Factorial':
    degree = st.slider('What factorial',1,20)
    x = degree 
    sts = 1
    while x >= 1:
        sts = sts * x
        x -= 1
    with st.spinner('Calculating'):
        time.sleep(2)
        st.write(f'{sts}')
elif work == 'Palindrome checker':
    phrase = st.text_input('Please input the phrase to be checked')
    bar = st.progress(0)
    work_phr = ''
    p = False
    for i in range(100):
        time.sleep(0.02)  
        bar.progress(i + 1)
    for char in phrase:
        if char.isspace():
            p = True
        elif char in string.punctuation:
            p = True
        else:
            work_phr += char.lower()
    if work_phr == work_phr[::-1]:
        if p:
            st.write(f'"{phrase} is a palindrome phrase"')
        else:
            st.write(f'"{phrase} is a palindrome word."') 
    else:
        st.write(f'"{phrase} is not a palindrome"')

elif work == 'Reverse':
   
    phrase = st.text_input(' What phrase would you like me to reverse')
    prog = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        prog.progress(1 + i)
    phrase_list = phrase.split()
    rev_list = phrase_list[::-1]
    rev_p = ' '.join(rev_list)
    st.write(rev_p.capitalize())
elif work == 'Sum of digits':
    number = st.slider('Pick a number',1,100)
    sums = 0
    
    str_version = str(number)
    stuff = len(str_version)
    for s in range(0,stuff):
        sums += int(str_version[s])
    with st.spinner('Calculation in progress'):
        time.sleep(2)
        st.write(sums)
elif work == 'Password generator':
    length =st.slider('How long do you want the password to be',6,16)
    n = 1
    password = ''
    prog = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        prog.progress(1 + i)
    while n <= length:
        n +=1
        base = string.ascii_letters + string.digits + '@%$£&?#'
        password += random.choice(base)
    st.write(password)
elif work == 'Password validator':
    password = st.text_input('Please place your password to be validated')
    reasons = []
    if not any(char.islower() for char in password):
        reasons.append('There must be atleast one lower case')
    if not any(char.isupper() for char in password):
        reasons.append('There must be atleast one upper case')
    if not any(char in '@%$£&?#' for char in password):
        reasons.append('Must contain at least one of the following symbols @%$£&?#')
    if not any(char.isdigit() for char in password):
        reasons.append('Must contain at least one digit')
    if len(password) < 6:
        reasons.append('Too short')
    if len(password) > 16:
        reasons.append('Too long')
    if reasons:
        for reason in reasons:
            st.write(reason)
    else:
        st.write('Valid password')
        