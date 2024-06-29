import os
import subprocess
import cutscenes.demux as demux

def handleUsmExtract(usm_path):
    decrypt = demux.UsmDemuxer(usm_path)
    decrypt.export(output_path)

def handleMediaMerge(v, ad, otfi):
    cmd = [ffmpeg_path, '-i', v, '-i', ad, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental',
           otfi]
    subprocess.call(cmd)

def handleSuffixConvert(ifi, ofi, iext, oext, ona):
    ffmpeg_cmd = [ffmpeg_path, "-i", ifi, ofi]
    subprocess.call(ffmpeg_cmd)

def handleUsmConvert():
    videos = []
    language_map = {"_0": "audio_cn", "_1": "audio_en", "_2": "audio_jp", "_3": "audio_kr"}

    for file in os.listdir(output_path):
        file_path = os.path.join(output_path, file)
        file_name, file_suffix = os.path.splitext(file)

        if file_suffix == ".ivf":
            output_mp4 = f"{output_path}/{file_name}_temp.mp4"
            videos.append(output_mp4)
            handleSuffixConvert(file_path, output_mp4, "ivf", "mp4", file_name)
        elif file_suffix == ".adx":
            output_mp3 = f"{output_path}/{file_name}_temp.mp3"
            for suffix, key in language_map.items():
                if suffix in file_name:
                    globals()[key] = output_mp3
                    break
            handleSuffixConvert(file_path, output_mp3, "adx", "mp3", file_name)

    audio_config = {0: audio_cn, 1: audio_en, 2: audio_jp, 3: audio_kr}
    for video in videos:
        if ("Loop" in video and video.endswith("_temp.mp4")) or (video.split("_temp")[0] in video):
            new_video = video.replace("_temp.mp4", ".mp4")
            os.rename(video, new_video)
        else:
            if audio_country in audio_config:
                new_video = video.replace("_temp.mp4", ".mp4")
                handleMediaMerge(video, audio_config[audio_country], new_video)

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(root_path, "cutscenes/ffmpeg.exe")
    input_path = os.path.join(root_path, "input")
    output_path = os.path.join(root_path, "output")
    audio_cn = audio_en = audio_jp = audio_kr = None

    if not os.path.exists(input_path):
        os.makedirs(input_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for file in os.listdir(input_path):
        if file.endswith('.usm'):
            file_path = os.path.join(input_path, file)
            handleUsmExtract(file_path)

    audio_country = int(input('选择音频语言: [ 0: cn, 1: en, 2: jp, 3: kr ]: '))

    handleUsmConvert()

    clean_flag = input("是否清理临时文件? (\033[92my\033[0m/n) ")
    if clean_flag.lower() in ['y', 'yes', '']:
        for file in os.listdir(output_path):
            if any(suffix in file for suffix in ['_temp', '.ivf', '.adx']):
                os.remove(os.path.join(output_path, file))
