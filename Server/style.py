from colorama import Fore, Style

BOLD = '\033[1m'
END = '\033[0m'

ITAL = '\x1B[3m'
ITAL_END = '\x1B[0m'

def color(text):
    if "/color" in text:
        try:
            x = text.split()
            color = x[1].upper()
            text = " ".join(x[2:])
            text = f'{getattr(Fore,color)}{text}{Style.RESET_ALL}'
            return text
        except:
            return text
    return text 


def bold(text):
    try:
        if "**" in text:
            i = text.find("**")
            j = text.rfind("**")
            newText = text[:i]+BOLD+text[i+2:j]+END+text[j+2:]
            return newText
    except:
        return text 
    return text

def italics(text):
    try:
        if "__" in text:
            i = text.find("__")
            j = text.rfind("__")
            newText = text[:i]+ITAL+text[i+2:j]+ITAL_END+text[j+2:]
            return newText
    except:
        return text 
    return text    
        
