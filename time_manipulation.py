import re

def find_time(x):
    if len(x) <= 2:
        return False
    else:
        if re.findall(r"P*H|M",x) == ['M']:
            return [int(s) for s in re.findall(r"\d+",x)][0]
        if re.findall(r"P*H|M",x) == ['H']:
            return [int(s) for s in re.findall(r"\d+",x)][0] * 60
        

