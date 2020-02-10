zip_code = '92839'

if len(zip_code) == 5:
    check = 'valid'
else:
    check = 'invalid'

# another weay to have it done in one line:
check = 'valid' if len(zip_code) == 5 else 'invalid'
print(check)