# Install

- 依赖库安装

```shell
#语音识别库
pip install SpeechRecognition
pip install google-api-python-client
pip install google-cloud-speech
pip install oauth2client

# 文本比对库
pip install diff_match_patch

# html转pdf库
pip install pdfkit
```

- 依赖软件安装

  https://wkhtmltopdf.org/downloads.html 

  下载安装，并把安装路径添加到path_wkpdf后（源文件11行）



# Run

```shell
python speech_recongnition_compare.py recording
```

recording为录音所在目录相对路径，会读取文件下所有wav文件，语音识别，按照文件名前6位所示文本id与文本库中寻找文本比对。