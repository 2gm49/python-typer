import time

def Typer(text, delay, wait):
    count = len(text)

    timebetween = "time.sleep(delay)"
    waitafter = "time.sleep(wait)"

    textlist = []
    count = 0

    for i in text:
        textlist.append(i)
        print(f"{textlist[count]}", end="", flush=True)
        count = count + 1
        eval(timebetween)
    eval(waitafter)
    

Typer("hello", 0.2, 1)
