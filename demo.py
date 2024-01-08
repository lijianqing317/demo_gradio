import gradio as gr
def greet(name, test,intensity):
    return "Hello " * intensity + '-'+ test+'-'+ name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "text", "slider"],
    outputs=["text"],
)

demo.launch(share=False)
