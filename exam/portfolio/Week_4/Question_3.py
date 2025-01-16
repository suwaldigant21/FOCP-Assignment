"""3. Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHurthe name should be displayed asArthur."""

def greetings(name):
    name = name.capitalize()
    return f"Hello {name}!"

name = input("Enter your name: ")
print(greetings(name))