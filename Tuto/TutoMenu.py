from simple_term_menu import TerminalMenu

def helloworld(type):
    print("hello world".upper() if type == "upper"
          else "hello world")
#endef

options = ["hello world", "HELLO WORLD"]
menu = TerminalMenu(options)
index = menu.show()

if index == 0:
    helloworld("normal")
elif index == 1:
    helloworld("upper")