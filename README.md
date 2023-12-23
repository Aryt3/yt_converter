# Youtube-Converter

> [!NOTE]
>
> This is a small project of mine which provides a WebGUI for downloading youtube videos, either as `mp3` or `mp4`.
> Although there are many solutions online for this usecase I was getting annoyed by the unnecessary bloatware, that's why I created my own application.

## Documentation

For the convertion I use 2 different pip libraries and 1 external software solution required by 1 library. <br/>
I implemented the library `pytube` for downloading the youtube video files such as audio and video. <br/>
I than used the library `pydub` and its dependency `ffmpeg` for convertion to an actual audio-file.