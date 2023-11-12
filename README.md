# EmergenSea
Python script that closes the app you are using when clicking a hotkey and opens your web browser instead.

A friend requested this from me, so I just made it for fun. What they asked:
```
Yo Ray, is it possible to make a script where if i press for example “Z” it closes the current 
thing i have opened and switches to my browser almost acting like an emergency button.
```

# How does it work 

Just run the py script and click the keybind when you want it to happen.

You can chage some configuration parameters at the top of the script:
```py
hotkey_1 = 'ctrl+1'
url_to_open = "https://www.youtube.com/jjkay03"
minimize = True  # Set to True if you want to minimize instead of closing
```
