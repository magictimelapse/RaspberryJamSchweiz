from getch import getch

def gibPfeilTaste():
    if getch() == '\033':
        getch()
        a = getch()
        if a == 'A':
                return "oben"
        elif a == 'B':
                return "unten"
               
        elif a == 'C': 
            return "rechts"
        elif a =='D':        
                return "links"
 
