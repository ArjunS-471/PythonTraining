import win32com.client

def create_word_document(file_path):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True

    doc = word.Documents.Add()

    selection = word.Selection
    selection.TypeText("Hello word document")
    selection.TypeParagraph()
    selection.TypeText("Automating work is fun!!")

    #save the document
    doc.SaveAs(file_path)
    #word.Quit()

create_word_document(r"C:\Users\Administrator\Desktop\UST_TRAINING\pywinAutomation\sample.docx")