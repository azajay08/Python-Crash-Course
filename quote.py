name = 'john lennon'
quote = "Life is what happens to you while you're\nbusy making other plans."
italic = "\x1B[3m"
normal = "\x1B[0m"
print(f'{name.title()} once said "{quote}"\n')

print(f'"{quote}" - {italic}{name.title()}\n')

print(f'{name.title()} once said "{quote}"\n')

print(f'"{quote}" - {italic}{name.title()}{normal}\n')

print(f'{name.title()} once said "{quote}"\n')

print(f'"{quote}" - {italic}{name.title()}{normal}\n')


