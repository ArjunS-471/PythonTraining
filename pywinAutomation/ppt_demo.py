import win32com.client

def create_presentation(file_path):
    #Launch PowerPoint application
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = True #Make PowerPoint visible (set to False to run in the background)

    #Create a new presentation
    presentation = powerpoint.Presentations.Add()

    #Add as slide (ppLayoutTitle = 1)
    slide = presentation.Slides.Add(1,1)
    slide.Shapes[0].TextFrame.TextRange.Text = "Automating PowerPoint"
    slide.Shapes[1].TextFrame.TextRange.Text = "Using PyWin32 for Automation"

    #Save the presentation
    presentation.SaveAs(file_path)
    powerpoint.Quit()
    print(f"Powerpoint save to {file_path}")

#Example usage
create_presentation(r"C:\Users\Administrator\Desktop\UST_TRAINING\pywinAutomation\sample.ppt")