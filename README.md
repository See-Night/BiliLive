# BiliLive

[![Python](https://img.shields.io/badge/Python-3.6+-blue)](https://python.org) ![MIT](https://img.shields.io/badge/Licence-MIT-red)

BiliLive是一个基于Python的Bilibili直播自动录制脚本。

<strong style="color: red;">注意：</strong>在使用之前请确保你的设备上已经安装了[Python](https://python.org)环境。

## 安装

BiliLive提供脚本和二进制两种使用方法，择一即可。

#### 获取脚本

如果你的设备上装有Git，你可以直接用Git从Github上将仓库克隆下来。

```bash
git clone https://github.com/See-Night/BiliLive.git
```

如果你对Git一无所知又不想了解，你可以直接从[这里](https://raw.githubusercontent.com/See-Night/BiliLive/master/BiliLive)下载脚本。

#### 安装依赖

BiliLive仅依赖于 `requests` 模块。

```bash
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

<small>在命令行中运行以上命令可以自动安装。</small>

## 运行

BiliLive脚本采用纯命令行的形式工作，在使用之前你至少需要了解一下路径的概念。你可以直接双击运行它，也可以使用命令行+参数的方式运行。以下只介绍命令行形式的运行方法。

```bash
# 进入BiliLive所在的目录
cd BiliLive

# 运行脚本
python BiliLive.py -r <roomid> -o <outdir>
# 或者
python BiliLive.py
```

- `roomid` ：直播间ID
- `outdir` ：视频输出路径

如果你加了参数，脚本会直接根据参数的值监听并录制直播；如果没有加参数，则需要按照提示输入相应的参数。

如果是Windows系统的话，理论上可以双击脚本文件去运行。

**举个栗子**：

```bash
python BiliLive -r 12235923 -o "D:\Video"
```

这个命令让脚本监听 `12235923` 直播间，当开始直播以后进行录制，并保存到 `D:\Video` 路径下。

> 脚本运行时不能关闭命令行，否则脚本会自动停止工作。

![bililive](./public/bililive.gif)