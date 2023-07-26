import os
import sys
import gradio as gr
from src.gradio_demo import SadTalker
from pyngrok import ngrok

try:
    import webui  # in webui
    in_webui = True
except:
    in_webui = False

# 切换音频文件的可见性
def toggle_audio_file(choice):
    if choice == False:
        return gr.update(visible=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True)

# 切换视频参考文件的值的可见性
def ref_video_fn(path_of_ref_video):
    if path_of_ref_video is not None:
        return gr.update(value=True)
    else:
        return gr.update(value=False)

# 创建SadTalker实例，初始化模型
def sadtalker_demo(
    checkpoint_path="checkpoints", config_path="src/config", warpfn=None
):
    sad_talker = SadTalker(checkpoint_path, config_path, lazy_load=True)

    # 创建Gradio界面
    with gr.Blocks(analytics_enabled=False) as sadtalker_interface:
        gr.Markdown(
            "<div align='center'> <h2> 😭 SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation (CVPR 2023) </span> </h2> \
                    <a style='font-size:18px;color: #efefef' href='https://arxiv.org/abs/2211.12194'>Arxiv</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \
                    <a style='font-size:18px;color: #efefef' href='https://sadtalker.github.io'>Homepage</a>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \
                     <a style='font-size:18px;color: #efefef' href='https://github.com/Winfredy/SadTalker'> Github </div>"
        )

        # 源图片
        with gr.Row().style(equal_height=False):
            with gr.Column(variant="panel"):
                with gr.Tabs(elem_id="sadtalker_source_image"):
                    with gr.TabItem("上传图片"):
                        with gr.Row():
                            source_image = gr.Image(
                                label="源图片",
                                source="upload",
                                type="filepath",
                                elem_id="img2img_image",
                            ).style(width=512)

        # 驱动音频
        with gr.Tabs(elem_id="sadtalker_driven_audio"):
            with gr.TabItem("上传或使用TTS"):
                with gr.Column(variant="panel"):
                    driven_audio = gr.Audio(
                        label="输入音频", source="upload", type="filepath"
                    )

                    # 文字转语音
                    if sys.platform != "win32" and not in_webui:
                        from src.utils.text2speech import TTSTalker

                        tts_talker = TTSTalker()
                        with gr.Column(variant="panel"):
                            input_text = gr.Textbox(
                                label="通过文本生成音频",
                                lines=5,
                                placeholder="请输入文本，我们将使用 @Coqui.ai TTS 生成音频。",
                            )
                            tts = gr.Button(
                                "生成音频",
                                elem_id="sadtalker_audio_generate",
                                variant="primary",
                            )
                            tts.click(
                                fn=tts_talker.test,
                                inputs=[input_text],
                                outputs=[driven_audio],
                            )

        # 设置选项
        with gr.Column(variant="panel"):
            with gr.Tabs(elem_id="sadtalker_checkbox"):
                with gr.TabItem("设置"):
                    gr.Markdown(
                        "需要帮助？请访问我们的[最佳实践页](https://github.com/OpenTalker/SadTalker/blob/main/docs/best_practice.md)了解更多详细信息"
                    )
                    with gr.Column(variant="panel"):
                        pose_style = gr.Slider(
                            minimum=0,
                            maximum=46,
                            step=1,
                            label="姿势风格",
                            value=0,
                        )  #
                        size_of_image = gr.Radio(
                            [256, 512],
                            value=256,
                            label="人脸模型分辨率",
                            info="使用256/512模型？",
                        )  #
                        preprocess_type = gr.Radio(
                            ["裁剪", "调整大小", "完整", "扩展裁剪", "扩展完整"],
                            value="裁剪",
                            label="预处理",
                            info="如何处理输入图像？",
                        )
                        is_still_mode = gr.Checkbox(
                            label="静态模式（减少手部动作，适用于预处理选项`完整`）"
                        )
                        batch_size = gr.Slider(
                            label="生成中的批处理大小",
                            step=1,
                            maximum=10,
                            value=2,
                        )
                        enhancer = gr.Checkbox(label="GFPGAN作为面部增强器")
                        submit = gr.Button(
                            "生成",
                            elem_id="sadtalker_generate",
                            variant="primary",
                        )

        # 创建生成的视频
        with gr.Tabs(elem_id="sadtalker_genearted"):
            gen_video = gr.Video(label="生成的视频", format="mp4").style(
                width=256
            )

        # 根据warpfn是否存在设置生成按钮的回调函数
        if warpfn:
            submit.click(
                fn=warpfn(sad_talker.test),
                inputs=[
                    source_image,
                    driven_audio,
                    preprocess_type,
                    is_still_mode,
                    enhancer,
                    batch_size,
                    size_of_image,
                    pose_style,
                ],
                outputs=[gen_video],
            )
        else:
            submit.click(
                fn=sad_talker.test,
                inputs=[
                    source_image,
                    driven_audio,
                    preprocess_type,
                    is_still_mode,
                    enhancer,
                    batch_size,
                    size_of_image,
                    pose_style,
                ],
                outputs=[gen_video],
            )

    return sadtalker_interface

# 主函数
if __name__ == "__main__":
    ngrok.set_auth_token("2T2uKcVHFVIQj5JxFkarQQi3Lb1_4QzQC5bUULf5PZLSBHySz")

    # 创建一个外链
    public_url = ngrok.connect("localhost:7860")
    print("网站链接:", public_url)

    demo = sadtalker_demo()
    demo.queue()
    demo.launch()
