import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input(tooltip="Enter file path")
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input2 = sg.Input(tooltip="Enter destination folder")
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window(title="File Compression", 
                   layout=[[label1, input1, choose_button1], 
                          [label2, input2, choose_button2],
                          [compress_button]])

window.read()
window.close()