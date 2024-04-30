# Cutscenes-SR
此项目用于处理第二个动漫游戏里的 `.usm` 视频文件, 包括提取和转换视频文件, 以下是设置和运行此项目的步骤.
## 使用
### 克隆仓库
首先，你需要从GitHub仓库克隆代码到本地或下载发行版.

### FFMPEG
下载最新版的 FFMPEG 并将其可执行文件 `ffmpeg.exe` 放置在项目的 `cutscenes` 子目录下.
您可以从官网下载, 也可以从本项目第一个预览版本内找到所需文件.

### 准备输入文件
在项目根目录下创建一个名为 `input` 的文件夹(首次运行程序也会自动创建必要的目录), 并将你需要处理的 `.usm` 文件放入该文件夹中.
`.usm` 文件可以在 `[Game Name]\Game\[Game Name]_Data\StreamingAssets\Video\Windows` 内找到.

### 运行项目
打开终端或命令行界面, 运行 `py main.py` 命令启动程序.

### 选择音频语言
根据提示选择音频语言, 输入对应的数字(0: 中文, 1: 英语, 2: 日语, 3: 韩语).

### 清理临时文件
程序执行完成后, 将询问是否清理临时文件.
如果需要清理, 输入 y ( 或直接按 Enter ) 确认清理, 否则跳过清理步骤.

### 输出文件
程序执行完成后, 将在 `output` 文件夹中生成对应的视频文件.

### 注意事项
- 请确保你的电脑上有足够的硬盘空间, 程序处理大量视频文件可能需要较长时间.
- 程序目前仅支持 Windows 操作系统, 其他操作系统请自行修改代码或使用 Docker 等容器化技术.
- 程序目前仅支持该游戏 `.usm` 转换, 其他游戏请参考下方表格.

### 维护
- [key(Iridium-SR)](https://github.com/tamilpp25/Iridium-SR)
- [key(PyCriUsm)](https://github.com/BUnipendix/PyCriUsm/tree/main/keygen/StarRail)
- [decrypt.pyd](https://github.com/BUnipendix/PyCriUsm)

## 参考
- [GI-Cutscenes](https://github.com/ToaHartor/GI-cutscenes)
- [PyCriUsm](https://github.com/BUnipendix/PyCriUsm)