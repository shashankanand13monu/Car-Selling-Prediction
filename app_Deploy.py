import gradio as gr
import pandas as pd
import numpy as np
import pickle
import sklearn
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

import gradio as gr
def car(Year,owners,sp,fuel,distance,tyype,trans):
  if fuel =="PETROL":
    p,d=1,0
  if fuel =="DIESEL":
    p,d=0,1
  if fuel =="CNG":
    p,d=0,0
  year = 2022-Year
  if tyype=="Individual":
    st=1
  else:
    st=0
  if trans=="Manual":
    t=1
  else:
    t=0
  error = "【 𝗘𝗿𝗿𝗼𝗿 𝟰𝟬𝟰 : 𝗩𝗮𝗹𝘂𝗲 𝗠𝗶𝘀𝘀𝗶𝗻𝗴 】"
  prediction=model.predict([[sp,distance,owners,year,d,p,st,t]])
  output=round(prediction[0],2)
  ou= str(output)
  if Year==0 or distance==0 or sp==0:
    return error
  else:
    return "The Price of Will be  ₹" + ou  + "L !"
# face = gr.Interface(fn=start, inputs=["text", "checkbox","N", gr.inputs.Slider(0, 100),gr.inputs.Radio(["add", "subtract", "multiply"])], outputs=["text", "number"])
# face.launch()
ts= """ 
Used Car  Price  Prediction"""
# ---------------------------------INPUTS :------------------------------

# in1=gr.inputs.Textbox(placeholder="En",label="MO")
in2=gr.inputs.Number(label='Which Model (Year)【*】',default=0)
in3= gr.inputs.Slider(0, 10,1,label="No. of Previous Owners eg.1,2,3")
in4=gr.inputs.Number(label='Kilometeres Drived【*】',default=0)
in5= gr.inputs.Radio(["PETROL", "DIESEL", "CNG"])
in6=gr.inputs.Dropdown(["Individual", "Dealer"],label="You Are")
in7=gr.inputs.Dropdown(["Automatic", "Manual"],label="Transmission Type")
in8=gr.inputs.Number(label='Showroom Price ₹(in LAKHS)【*】',default=0)

interface = gr.Interface(fn=car,
                         inputs=[in2,in3,in8,in5,in4,in6,in7],
                         outputs=["text"],title=ts,theme="peach",css="""
                         .gradio_bg[theme=default] .gradio_interface .panel_button.submit {

	background-color: rgba(99, 102, 241, var(--tw-bg-opacity));

}
.gradio_bg[theme=peach] .gradio_interface .panel_header {
  font-family: Arial, Helvetica, sans-serif;;
  font-size: 17px;
}
.gradio_page .title{
  font-family: "Copperplate",Fantasy;
  font-size: 47px;
}"""
                         )
interface.launch(inline=False,share=True)