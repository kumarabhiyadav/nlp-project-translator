from translate import Translator
translator= Translator(to_lang="hi")
translation = translator.translate("This is a dog")
print(translation)
f = open("output.txt", "w", encoding="utf-8")
f.write(translation)