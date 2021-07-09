from docx import Document

document = Document('test.docx')
# document.save('test2.docx')
for paragraph in document.paragraphs:
    if 'ali' in paragraph.text:
        inline = paragraph.runs
        # Loop added to work with runs (strings with same style)
        for i in range(len(inline)):
            if 'ali' in inline[i].text:
                text = inline[i].text.replace('ali', 'karim')
                inline[i].text = text
        print(paragraph.text)

document.save('dest.docx')
