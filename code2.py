from guizero import App, Text, PushButton, Picture, Box, Window, TextBox

c1_score = 0
c2_score = 0

def action1(app):
  global c1_score
  global c2_score
  c1_score = 0
  c2_score = 0
  window2 = Window(app,title = "Enter contestants name:", width = 300, height = 300)
  text9 = Text(window2, " ",size = 20, color = 'Blue')
  text10 = Text(window2, "Contestant 1:",size = 20, color = 'Blue')
  input_box1 = TextBox(window2, width = 20)
  text11 = Text(window2, " ",size = 20, color = 'Blue')
  text12 = Text(window2, "Contestant 2:",size = 20, color = 'Green')
  input_box2 = TextBox(window2, width = 20)
  text13 = Text(window2, " ",size = 20, color = 'Blue')
  button4 = PushButton(window2, lambda: action4(app,input_box1, input_box2), text="Submit", padx = 5, pady = 5)
  button4.text_size = 14
  
  window2.show()
 
def action2():
  global c1_score
  if not c1_score == 9:
    c1_score +=1
    text17.value = str(c1_score)
  else:
    text17.value = str(10)
    text18.value = "You Won" 
    text23.value = "You Lost" 
    button2.disable()
    button3.disable()
    
def action3():
  global c2_score
  if not c2_score == 9:
    c2_score +=1
    text22.value = str(c2_score)
  else:
    text22.value = str(10)
    text23.value = "You Won" 
    text18.value = "You Lost" 
    button2.disable()
    button3.disable()
    
def action4(app,input_box1, input_box2):
  global text17 
  global text22 
  global text18 
  global text23 
  c1_name  = input_box1.value
  print(c1_name)
  c2_name  = input_box2.value
  print(c2_name)
  button2.enable()
  button3.enable()
  window3 = Window(app,"Contestant 1 Score", width = 300, height = 300)
  text14 = Text(window3, " ",size = 30, color = 'Blue')
  text15 = Text(window3, f"Welcome {c1_name}!",size = 20, color = 'Blue')
  text16 = Text(window3, " ",size = 20, color = 'Blue')
  text17 = Text(window3, "0",size = 80, color = 'Blue')
  text18 = Text(window3, " ",size = 20, color = 'Blue')
  window3.show()
  
  window4 = Window(app,"Contestant 2 Score", width = 300, height = 300)
  text19 = Text(window4, " ",size = 30, color = 'Green')
  text20 = Text(window4, f"Welcome {c2_name}!",size = 20, color = 'Green')
  text21 = Text(window4, " ",size = 20, color = 'Green')
  text22 = Text(window4, "0",size = 80, color = 'Green')
  text23 = Text(window4, " ",size = 20, color = 'Green')
  window4.show()
    
# Set up the app
app = App("Spelling Bee Control Panel", width=800, height=700, layout="grid")

picture1 = Picture(app, image="spelling_bee_banner.png", grid=[0,0,8,4])
text1 = Text(app, " ",size = 20, grid=[3,4])
button1 = PushButton(app, lambda: action1(app), text="Start a new round", grid=[2,5,4,1],padx = 5, pady = 5)
button1.text_size = 22
text2 = Text(app, " ",size = 20, grid=[1,6])

c1_box = Box(app, border = 1, grid=[2,7], width = 300, height = 250)
text3 = Text(c1_box, " ",size = 20)
text4 = Text(c1_box, "Contestant 1",size = 20, color = 'Blue')
text5 = Text(c1_box, " ",size = 20)
button2 = PushButton(c1_box, action2, text="Correct", padx = 50, pady = 30)
button2.text_size = 14
button2.text_color = 'Blue'
button2.disable()

c2_box = Box(app, border = 1, grid=[5,7], width = 300, height = 250)
text6 = Text(c2_box, " ",size = 20)
text7 = Text(c2_box, "Contestant 2",size = 20, color = 'Green')
text8 = Text(c2_box, " ",size = 20)
button3 = PushButton(c2_box, action3, text="Correct", padx = 50, pady = 30)
button3.text_size = 14
button3.text_color = 'Green'
button3.disable()

app.display()

