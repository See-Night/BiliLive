# BiliLive

[![Python](https://img.shields.io/badge/Python-3.6+-blue)](https://python.org) ![MIT](https://img.shields.io/badge/Licence-MIT-red)

BiliLive（原BiliLive） 是一个基于Python的Bilibili直播自动录制脚本。

<strong style="color: red;">注意：</strong>在使用之前请确保你的设备上已经安装了[Python](https://python.org)环境。

## 安装

BiliLive提供脚本和二进制两种使用方法，择一即可。

### 1. 安装脚本

#### 获取脚本

如果你的设备上装有Git，你可以直接用Git从Github上将仓库克隆下来。

```bash
$ git clone https://github.com/See-Night/BiliLive.git
```

如果你对Git一无所知又不想了解，你可以直接从[这里](https://raw.githubusercontent.com/See-Night/BiliLive/master/BiliLive)下载脚本。

#### 安装依赖

BiliLive仅依赖于 `requests` 模块。

```bash
$ pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

<small>在命令行中运行以上命令可以自动安装。</small>

### 2. 二进制安装

访问[Releases]([Release DD Monitor · See-Night/BiliLive (github.com)](https://github.com/See-Night/BiliLive/releases/latest))，并下载符合你操作系统的文件。

## 运行

BiliLive脚本采用纯命令行的形式工作，在使用之前你至少需要了解一下路径的概念。

```bash
# 进入BiliLive所在的目录
$ cd BiliLive

# 运行脚本
$ ./Monitor -r <roomid> -o <outdir>
```

- `roomid` ：直播间ID
- `outdir` ：视频输出路径

**举个栗子**：

```bash
$ ./BiliLive -r 12235923 -o "D:\Video"
```

这个命令让脚本监听 `12235923` 直播间，当开始直播以后进行录制，并保存到 `D:\Video` 路径下。

> 脚本运行时不能关闭命令行，否则脚本会自动停止工作。



