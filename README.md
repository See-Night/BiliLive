DDMonitor
==============================
直播录播脚本  
------------------------------

#### 需要streamlink+ffmpeg支持。  
#### 以下安装方法仅适用于Linux系统，Windows系统请自行解决  
> ffmpeg  
> http://www.ffmpeg.org/download.html  
> streamlink  
> https://streamlink.github.io/  

安装：
```
$ sudo wget https://Dreammer12138.github.io/Documents/DDMonitor/install
$ sudo ./install
```

启动：

```shell
$ ./Monitor -r 12235923 -o /root/video
```



## Monitot 参数
在Monitor命令后面添加参数可以修改一些默认设置
* `-r / --room roomid` 设置roomid
* `-o / --outpath` 设置保存地址  
#### 建议将路径添加到环境变量中
