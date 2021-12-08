import MoonLanguage

while True:
    text = input('ml >')
    result, error = MoonLanguage.run('test', text)
    if error: print(error.as_string())
    else: print(result)
