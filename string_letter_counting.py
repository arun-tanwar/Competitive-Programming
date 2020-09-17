def string_letter_count(s):
    punctuations = '''0123456789`|+=-*!()-[]{};:'"\,<>./?@#$%^&*_~'''
    st=''
    for i in s:
        if i not in punctuations:
            st+=i
    if not len(st):
        return ''
    k = st.lower().replace(" ",'')
    s = sorted(list(set(k)))
    result = ''
    for i in s:
        count = k.count(i) 
        result+=str(count)+i
    return result
