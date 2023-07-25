<div align="center">




<!--<h2> 😭 SadTalker： <span style="font-size:12px">Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation </span> </h2> -->

  <a href='https://arxiv.org/abs/2211.12194'><img src='https://img.shields.io/badge/ArXiv-PDF-red'></a> &nbsp; <a href='https://sadtalker.github.io'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yqty/SadTalker/blob/main/sadtalker改进版python310.ipynb) &nbsp; [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/vinthony/SadTalker) &nbsp; [![sd webui-colab](https://img.shields.io/badge/Automatic1111-Colab-green)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/video/stable/stable_diffusion_1_5_video_webui_colab.ipynb) &nbsp; [![Replicate](https://replicate.com/cjwbw/sadtalker/badge)](https://replicate.com/cjwbw/sadtalker) 


<br>
<div>
    <sup>1</sup> Xi'an Jiaotong University &emsp; <sup>2</sup> Tencent AI Lab &emsp; <sup>3</sup> Ant Group &emsp; 
</div>
<br>
<i><strong><a href='https://arxiv.org/abs/2211.12194' target='_blank'>CVPR 2023</a></strong></i>
<br>
<br>


![sadtalker](https://user-images.githubusercontent.com/4397546/222490039-b1f6156b-bf00-405b-9fda-0c9a9156f991.gif)

<b>TL;DR: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; single portrait image 🙎‍♂️  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; audio 🎤  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; talking head video 🎞.</b>

<br>

</div>
😭 SadTalker：用于定制化音频驱动的单图像脸部动画的真实 3D 运动系数学习
🔥 稳定扩散 webui的扩展现已上线。点击此处查看更多详情。
🔥 全图像模式已上线！点击此处查看更多详情。
🔥 新模式例如，静态模式，参考模式，缩放模式现已上线以满足更好和个性化的应用。
🔥 非常高兴在 bilibili，Youtube 和 推特 #sadtalker上看到更多社区演示。
⚙️ 1. 安装
来自社区的教程：中文windows教程 | 日语课程

Linux:
安装anaconda，python和git。
创建环境并安装需求项。
📎
git clone https://github.com/Winfredy/SadTalker.git

  cd SadTalker 

  conda create -n sadtalker python=3.8

  conda activate sadtalker

  pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

  conda install ffmpeg

  pip install -r requirements.txt

  ### tts 是可选的 gradio 演示。 
  ### pip install TTS

Windows (中文 windows 教程):
安装 Python 3.10.6，并勾选 "Add Python to PATH"。
手动安装 git（或者通过 scoop 使用 scoop install git）。
安装 ffmpeg，按照这个教程 （或者通过 scoop 使用 scoop install ffmpeg）。
下载我们的 SadTalker 代码库，例如运行 git clone https://github.com/Winfredy/SadTalker.git。
从↓下方下载 checkpoint 和 gfpgan。
以非管理员用户身份从 Windows Explorer 运行 start.bat，会启动 gradio WebUI 演示。
Macbook:
有关 Macbook 上的安装和 Docker 文件的更多提示可以在 此处找到。

📥 2. 下载训练过的模型
你可以运行以下脚本将所有模型放在正确的位置。

📎
bash scripts/download_models.sh

其他备选选项：

我们也提供一个离线补丁 (gfpgan/)，因此，在生成时不会下载任何模型。

Google Driver：从这个链接 (主检查点)和 gfpgan (离线补丁)下载我们的预训练模型

Github 发布页面：从最新的 github 发布页面下载所有文件，然后，将其放在 ./checkpoints。

百度云盘：我们在 checkpoints, 提取码: sadt. 和 gfpgan, 提取码: sadt. 提供下载模型

🔮 3. 快速入门 (最佳实践).
WebUI 演示:
在线：Huggingface | SDWebUI-Colab | Colab

Autiomatic1111 稳定扩散 webui 扩展 (本地)：请参考 Autiomatic1111 稳定扩散 webui 文档 。

Gradio 演示 (本地, 强烈推荐!)： 可以通过以下操作运行类似我们 hugging-face 演示 的演示：

📎
## 你需要提前通过 `pip install tts` 手动安装 TTS。
python app.py

Gradio 演示 (本地, 强烈推荐!)：

windows: 只需双击 webui.bat，需求项将会自动安装。
Linux/Mac OS: 运行 bash webui.sh 来启动 webui。
自行使用：
根据默认配置使一张肖像图像动起来：
📎
python inference.py --driven_audio <audio.wav> \
                    --source_image <video.mp4 or picture.png> \
                    --enhancer gfpgan

结果将会被保存在 results/$SOME_TIMESTAMP/*.mp4 中。

生成全身/图像：
使用 --still 生成一个自然的全身视频。你可以添加 enhancer 来提升生成视频的质量。

📎
python inference.py --driven_audio <audio.wav> \
                    --source_image <video.mp4 or picture.png> \
                    --result_dir <a file to store results> \
                    --still \
                    --preprocess full \
                    --enhancer gfpgan

在 >>> 最佳实践文档 <<< 中可以找到更多示例，配置和技巧。

🛎 引用
如果你在研究中发现我们的工作有用，请引用：

📎
@article{zhang2022sadtalker,
  title={SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation},
  author={Zhang, Wenxuan and Cun, Xiaodong and Wang, Xuan and Zhang, Yong and Shen, Xi and Guo, Yu and Shan, Ying and Wang, Fei},
  journal={arXiv preprint arXiv:2211.12194},
  year={2022}
}

💗 致谢
Facerender 的代码大量借鉴了zhanglonghao 的 face-vid2vid 复现 和 PIRender。我们感谢作者分享了他们的精彩代码。在训练过程中，我们还使用了来自 Deep3DFaceReconstruction 和 Wav2lip 的模型。我们感谢他们的精彩工作。

同时查看我们使用的以下优秀的第三方库：

面部工具：https://github.com/xinntao/facexlib
面部增强：https://github.com/TencentARC/GFPGAN
图像/视频增强：https://github.com/xinntao/Real-ESRGAN
🥂 扩展：
SadTalker-Video-Lip-Sync 来自@Zz-ww：SadTalker的视频唇同步
🥂 相关工作
StyleHEAT: 通过预训练的 StyleGAN 进行一次性的高分辨率可编辑的脸部讲话生成 (ECCV 2022)
CodeTalker: 具有离散运动先验的基于语音的 3D 面部动画 (CVPR 2023)
VideoReTalking: 对野生环境中脸部讲话视频编辑的基于音频的唇同步 (SIGGRAPH Asia 2022)
DPE: 分离姿态和表情用于通用视频肖像编辑 (CVPR 2023)
3D GAN Inversion with Facial Symmetry Prior (CVPR 2023)
T2M-GPT: 利用离散表示从文本描述生成人体运动 (CVPR 2023)
📢 免责声明
这不是腾讯的官方产品。此代码库只能用于个人/研究/非商业目的。

LOGO：颜色和字体建议：ChatGPT，logo 字体：Montserrat Alternates 。

所有演示图像和音频的版权均来自社区用户或来自稳定扩散的生成。如果你觉得不舒服，请随时联系我们。
