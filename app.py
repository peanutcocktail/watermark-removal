import gradio as gr
def predict(image):
  return truek

app = gr.Interface(
    fn=predict,
    inputs=[
      gr.Image(label="source image (no webp)", type="filepath", format="jpeg"),
      gr.Audio(label="source audio", type="filepath"),
      gr.Number(label="size", value=512, minimum=256, maximum=512, step=64, precision=0),
      gr.Number(label="steps", value=40, minimum=1, step=1, precision=0),
      gr.Number(label="fps", value=25, minimum=1, step=1, precision=0),
      gr.Slider(label="CFG Scale", value=3.5, minimum=0, maximum=10, step=0.01),
      gr.Number(label="pose weight", value=1.0),
      gr.Number(label="face weight", value=1.0),
      gr.Number(label="lip weight", value=1.0),
      gr.Number(label="face expand ratio", value=1.2),
    ],
    outputs=[gr.Video()],
)
app.launch()
