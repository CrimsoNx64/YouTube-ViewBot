
#   _____      _                     _   _ 
#  / ____|    (_)                   | \ | |
# | |     _ __ _ _ __ ___  ___  ___ |  \| |
# | |    | '__| | '_ ` _ \/ __|/ _ \| . ` |
# | |____| |  | | | | | | \__ \ (_) | |\  |
#  \_____|_|  |_|_| |_| |_|___/\___/|_| \_|

#YouTube ViewBot
#Dont do too many views at once else your pc will probably crash

import webbrowser

link=input("Enter the YouTube URL: ")

views=int(input("Enter the amount of views: "))

for i in range (0,views):#opens the tab however many times the user wanted it to
    webbrowser.open(link)#opens link
