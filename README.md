# BiliLive

[![Python](https://img.shields.io/badge/Python-3.6+-blue)](https://python.org) ![MIT](https://img.shields.io/badge/Licence-MIT-red) [![Gitter](https://badges.gitter.im/See-Night/BiliLive.svg)](https://gitter.im/See-Night/BiliLive?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

📕中文说明 | [English Readme](./README.en.md)

BiliLive 是一个基于 Python 的 Bilibili 直播自动录制脚本。

<strong style="color: red;">注意：</strong>在使用之前请确保你的设备上已经安装了 [Python](https://python.org) 环境。

## 安装

### 获取脚本

如果你的设备上装有Git，你可以直接用Git从Github上将仓库克隆下来。

```bash
git clone https://github.com/See-Night/BiliLive.git
```

如果你对Git一无所知又不想了解，你可以直接从[这里](https://github.com/See-Night/BiliLive/releases/latest)下载脚本。

### 安装依赖

BiliLive 依赖 `requests` 和 `colorama` 模块。

对于 Python 3.11 及以上的版本，你可能需要通过 venv 虚拟环境来安装依赖模块；或者通过其他手段屏蔽 `This environment is externally managed` 的警告。详情请自行查阅官方文档，或其他网络资料。

```bash
python -m venv .venv
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests colorama
```

对于 Python 3.11 以下的版本，或者已经屏蔽掉以上报错的版本，你可以直接安装依赖模块。

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests colorama
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
python BiliLive.py -r 12235923 -o "D:\Video"
```

这个命令让脚本监听 `12235923` 直播间，当开始直播以后进行录制，并保存到 `D:\Video` 路径下。

> 脚本运行时不能关闭命令行，否则脚本会自动停止工作。

![bililive](./public/bililive.gif)

## Docker 部署

对于有大量直播录制需求的用户而言，批量、自动化的录制程序是非常重要的，此处仅提出一种基于 Docker 的部署方案以供参考。您可以使用库中的 `Dockerfile` 直接构建 Docker 容器，或者从 [Docker Hub](https://hub.docker.com/r/seenight/bililive) 上直接拉取我构建好的镜像：

```bash
docker pull seenight/bililive
```

### 单个容器启动

如果只需要启动单个容器，则直接创建一个容器即可。

```bash
docker run --name <container name> -v <local path>:/app/video -d seenight/bililive <room id>
```

- `container name` 容器名称，随便起个名字方便自己辨别即可
- `local path` 录制视频的保存路径，此路径为设备本地路径
- `room id` 直播间地址

### 多个容器启动

需要录制多个直播间的话建议用 shell 脚本进行启动。在启动脚本之前，你需要在脚本所在的目录下新建 `room_list.txt` 文件用来存储需要录制的直播间信息，其内容如下：

```
<room_id> <name>
```

- `room_id` 直播间地址
- `name` 名称；此处的名称用来区分不同直播间，同时也会用于 Docker 容器的名称；**此处不可以使用汉字**

例如：

```
6 LOL
22384516 umy
```

在创建好 `room_list.txt` 以后，执行 `auto.sh` 脚本即可启动、关闭直播录制：

```bash
# 给脚本添加运行权限
chmod u+x auto.sh

# 启动录制
./auto.sh start <local path>

# 关闭录制
./auto.sh stop
```

* `local path` 录制的视频存储的路径

如果要单独关闭某个直播间的录制，请单独关闭 Docker 容器。

## FAQ

如果在使用中遇到什么问题请到 [Gitter](https://gitter.im/See-Night/BiliLive?utm_source=share-link&utm_medium=link&utm_campaign=share-link) 提问交流。

## LICENSE

```
MIT License

Copyright (c) 2021 See-Night

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 致谢

感谢 [lovelyyoshino](https://github.com/lovelyyoshino) 和 [fython](https://github.com/fython) 等大佬整理和总结的B站 API，省去了我不少开发工作。
