# DDMonitor

[![Python](https://img.shields.io/badge/Python-3.6+-blue)](https://python.org)

DDMonitor 是一个基于Python的Bilibili直播自动录制脚本，它使用了[@Passkou]('https://github.com/Passkou')开发的[bilibili-api](https://github.com/Passkou/bilibili-api)项目（顺手也抄了点代码🤣）。

在使用之前请确保你的设备上已经安装了[Python](https://python.org)环境。

## 获取脚本

如果你的设备上装有Git，你可以直接用Git从Github上将仓库克隆下来。

```bash
$ git clone https://github.com/See-Night/DDMonitor.git
```

如果你对Git一无所知又不想了解，你可以直接从[Releases](https://github.com/See-Night/DDMonitor/releases/latest)下载脚本。

## 安装依赖

DDMonitor仅依赖于[bilibili-api](https://github.com/Passkou/bilibili-api)和[aiohttp](https://docs.aiohttp.org)，你只需要安装这两个依赖就可以。

```bash
$ pip3 install bilibili-api aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple
```

<small>在命令行中运行以上命令可以自动安装。</small>

## 运行脚本

DDMonitor脚本采用纯命令行的形式工作，在使用之前你至少需要了解一下路径的概念。

```bash
# 进入DDMonitor所在的目录
$ cd DDMonitor

# 运行脚本
$ ./Monitor -r <roomid> -o <outdir>
```

- `roomid` ：直播间ID
- `outdir` ：视频输出路径

**举个栗子**：

```bash
$ ./Monitor -r 12235923 -o "D:\Video"
```

这个命令让脚本监听 `12235923` 直播间，当开始直播以后进行录制，并保存到 `D:\Video` 路径下。

!> 脚本运行时不能关闭命令行，否则脚本会自动停止工作。

## Docker 容器

DDMonitor默认提供了Docker镜像，你可以直接PULL下来用。

```bash
$ docker pull seenight/ddmonitor
```

```bash
$ docker run -p <outdir>:/app -d seenight/ddmonitor -r <roomid> -o .
```

* `outdir` ：输出路径
* `roomid` ：直播房间ID

