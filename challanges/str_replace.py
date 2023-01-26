def cleanText(text):
    text = text.replace("javascript", "**********")
    text = text.replace("php", "***")
    text = text.replace("java", "****")
    text = text.replace("html", "****")
    text = text.replace("css", "***")
    return text

tekst = "Programuje w php, php jest super, jebać java, lubie javascript ale css i html jest do dupy"

print(cleanText(tekst))