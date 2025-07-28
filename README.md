
# PNG to GIF Converter

## 介绍
这是一个Python脚本，用于将指定文件夹中的PNG文件按文件名称序号从小到大顺序合并为一个GIF文件。该脚本提供了以下功能：
- 按文件名称的序号排序PNG文件
- 自定义生成的GIF文件的间隔时间
- 选择是否压缩生成的GIF文件
- 选择是否循环播放生成的GIF文件
- 自动生成多个GIF文件并避免文件名重复

## 安装依赖
在运行脚本之前，请确保已安装以下Python库：
- `imageio`

可以通过以下命令安装依赖：
```bash
pip install imageio
```

## 使用方法

### 函数定义
```python
def merge_png_to_gif(input_folder, output_folder, output_gif_name, duration, compress, loop):
```

### 参数说明
- `input_folder` (str): 存放PNG文件的输入文件夹路径。
- `output_folder` (str): 输出GIF文件的文件夹路径。
- `output_gif_name` (str): 输出GIF文件的名称。
- `duration` (float): GIF中每帧图片的间隔时间，单位为秒。
- `compress` (bool): 是否压缩生成的GIF文件。`True`表示压缩，`False`表示不压缩。
- `loop` (bool): 是否循环播放生成的GIF文件。`True`表示循环播放，`False`表示播放一次后停止。

### 示例调用
```python
input_folder_path = r"D:\Pic2Gif-master\input"
output_folder_path = r"D:\Pic2Gif-master\out"
merge_png_to_gif(input_folder_path, output_folder_path, 'output.gif', 0.1, compress=False, loop=True)
```

### 示例输出
假设`input`文件夹中有以下PNG文件：
- `1.png`
- `2.png`
- `3.png`

运行上述代码后，将在`out`文件夹中生成一个名为`output.gif`的GIF文件，该文件按PNG文件名称的序号从小到大顺序排列，每帧的间隔时间为0.1秒，不压缩，循环播放。

如果`output.gif`已经存在，则会生成`output_1.gif`，依此类推。

## 注意事项
1. 确保`input_folder`和`output_folder`路径正确。
2. 确保`input_folder`中所有PNG文件的文件名都是数字（例如`1.png`、`2.png`等），以便按序号排序。
3. 如果`output_folder`不存在，脚本会自动创建该文件夹。


### 说明
- **`输入文件夹`**：存放所有需要合并的PNG文件的文件夹路径。
- **`输出文件夹`**：生成的GIF文件将保存到这个文件夹中。
- **`输出GIF文件名`**：生成的GIF文件的名称。
- **`间隔时间`**：GIF中每帧图片的间隔时间，单位为秒。
- **`是否压缩`**：选择是否对生成的GIF文件进行压缩。
- **`是否循环`**：选择生成的GIF文件是否循环播放。
