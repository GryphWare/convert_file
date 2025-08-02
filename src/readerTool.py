import pdfplumber

print("nhap ten file co trong duong dan cua ban: ")
target_file = input()

while (1):
    if ".pdf" not in target_file:
        print("ko thay file ban chi dinh hoac file cua ban ko phai pdf")
        target_file = input()
    else:
        break

text_file = ""

with pdfplumber.open(target_file) as pdf:
    for page in pdf.pages:
        text = page.extract_text(layout = True)
        if text:
            text_file += text + "\n"
        else:
            text_file += "\n"

#replace .pdf to .txt
target_file = target_file.replace(".pdf", ".txt")
print(f"result: {target_file}") #debug

with open(target_file, "w", encoding = "utf-8") as file:
    file.write(text_file)

print("done!")
