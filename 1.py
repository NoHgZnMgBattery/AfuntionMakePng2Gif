import os
import imageio

def merge_png_to_gif(input_folder,
                     output_folder,
                     output_gif_name,
                     duration,
                     compress,
                     loop,
                     dispose):
    os.makedirs(output_folder, exist_ok=True)
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    png_files.sort(key=lambda x: int(os.path.splitext(x)[0]))
    images = [imageio.imread(os.path.join(input_folder, f)) for f in png_files]

    base, ext = os.path.splitext(output_gif_name)
    counter = 1
    while os.path.exists(os.path.join(output_folder, output_gif_name)):
        output_gif_name = f"{base}_{counter}{ext}"
        counter += 1
    gif_path = os.path.join(output_folder, output_gif_name)

    # ✅ 使用 v2 写法，支持 disposal
    with imageio.get_writer(gif_path,
                            format='GIF',
                            mode='I',
                            duration=duration,
                            loop=0 if loop else 1,
                            optimize=compress,
                            disposal=2 if dispose else 1) as writer:
        for img in images:
            writer.append_data(img)

if __name__ == '__main__':
    merge_png_to_gif(
        input_folder = r"D:\Pic2Gif-master\input",
        output_folder = r"D:\Pic2Gif-master\out",
        output_gif_name = "output.gif",
        duration = 0.1,
        compress = False,      # 不压缩，保质量
        loop = True,           # 无限循环
        dispose = True         # 每帧前清空画布（透明背景干净）
    )