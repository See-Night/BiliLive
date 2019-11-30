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
`$ ./Monitor`  
更新：
`$ ./Monitor --upgrade`  
更改监视直播间： 
```
直播间信息在roomid.json文件中储存，修改前请及时进行备份  
$ sudo vim /usr/DDMonitor/roomid.json
将文件中的uid改成直播间号码，nickname改成主播ID  
{
	"user": [{
		"uid": "",			<-这里在双引号中填写直播间号码
		"nickname": ""		<-这里在双引号中填写主播的ＩＤ
	}]
}
保存退出，启动Monitor
```
  
## Monitot 参数
在Monitor命令后面添加参数可以修改一些默认设置
* `-l / --log path` 设置log的储存位置  
* `--upgrade` 更新  
  
#### 建议将路径添加到环境变量中
