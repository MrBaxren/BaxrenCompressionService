import os
import threading
import time
from pydub import AudioSegment
from PIL import Image
import zipfile

def clear_screen():
    os.system('clear')

def print_header():
    print("\033[34mBaxrenCompressionService\033[0m")
    print("\033[94m____________________________________________________\033[0m")
    print("\033[94m|                                                  |\033[0m")
    print("\033[94m|  _______  _______  _______  |\033[0m")
    print("\033[94m| |       ||       ||       |\033[0m")
    print("\033[94m| |  B  | ||  C  | ||  S  |\033[0m")
    print("\033[94m| |_______||_______||_______|\033[0m")
    print("\033[94m|                                                  |\033[0m")
    print("\033[94m|__________________________________________________|\033[0m")
    print("\033[94mDesteklenen Dosya Tipleri:\033[0m")
    print("\033[94m- Text Dosyaları (.txt)\033[0m")
    print("\033[94m- Görseller (.png, .jpeg)\033[0m")
    print("\033[94m- Ses Dosyaları (.mp3)\033[0m")

def compress_file(file_name, compression_ratio):
    try:
        for root, dirs, files in os.walk("/"):
            for file in files:
                if file == file_name:
                    file_path = os.path.join(root, file)
                    if file_name.endswith(".txt"):
                        output_file = file_path + "_compressed.txt"
                        with open(file_path, 'r') as input_file:
                            with open(output_file, 'w') as output_file:
                                output_file.write(input_file.read())
                        print(f"{file_name} dosyası başarıyla sıkıştırıldı.")
                        return
                    elif file_name.endswith(".png") or file_name.endswith(".jpeg"):
                        output_file = file_path + "_compressed.png"
                        img = Image.open(file_path)
                        img.save(output_file, optimize=True, quality=100 - compression_ratio)
                        print(f"{file_name} dosyası başarıyla sıkıştırıldı.")
                        return
                    elif file_name.endswith(".mp3"):
                        output_file = file_path + "_compressed.mp3"
                        sound = AudioSegment.from_file(file_path)
                        sound.export(output_file, format="mp3", bitrate=str(compression_ratio) + "k")
                        print(f"{file_name} dosyası başarıyla sıkıştırıldı.")
                        return
        print(f"{file_name} dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")

def print_status():
    while True:
        print("DEVAM EDİYOR...", end='\r')
        time.sleep(1)

def main():
    clear_screen()
    print_header()
    file_name = input("Dosya adı girin: ")
    compression_ratio = int(input("Dosya boyutunu küçültmenin yüzdeliğini girin (%): "))
    status_thread = threading.Thread(target=print_status)
    status_thread.daemon = True
    status_thread.start()
    compress_file(file_name, compression_ratio)
    print("\nİŞLEM BİTTİ")

if __name__ == "__main__":
    os.environ['TERM'] = 'xterm'
    main()
