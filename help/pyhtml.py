def div(value:str, htmlclass:str=None):
    lclass = "" if htmlclass == None else f" class='{htmlclass}'"
    return f"<div{lclass}>\n\t{value}\n</div>"
def ul(items:list, htmlclass:str=None, htmlid:str=None):
    lclass = "" if htmlclass == None else f" class='{htmlclass}'"
    lid = "" if htmlid == None else f" id='{htmlid}'"
    value = ""
    for item in items:
        value += f"<li>{item}</li>\n\t"
    return f"<ul{lclass}{lid}>\n\t{value}\n</ul>"
