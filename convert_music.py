
import os
from glob import glob
from shutil import move


encryption_file_path = [
	"/users/tenx/music/网易云音乐",
	"/Users/tenx/Library/Containers/com.tencent.QQMusicMac/Data/Library/Application Support/QQMusicMac/iQmc",
]

normal_file_path = [
	"/users/tenx/music/网易云音乐",
	"/users/tenx/music/QQ音乐",
	"/users/tenx/downloads"
]
mymusic_file_path = "/users/tenx/music/MyMusic"
moved_encrypted_file_path = "/users/tenx/downloads/encrypt_file"


def move_encrypted_file(dst_path: list):
	for path in dst_path:
		os.chdir(path)

		encryption_fmt = ['*.qmc', '*.mflac', '*.qmcflac', '*.ncm', '*.xm', '*.mgg', '*.kwm',]
		encryption_file = []
		for ept_fmt in encryption_fmt:
			for name in glob(ept_fmt):
				encryption_file.append(name)

		if encryption_file:
			for ept_file in encryption_file:
				if ept_file not in os.listdir():
					move(ept_file, moved_encrypted_file_path)
				else:
					os.remove(ept_file)

def move_normal_file(dst_path: list):
	normal_music_fmt = ['*.flac', '*.mp3']
	my_music_file = [os.path.basename(i) for i in os.listdir(mymusic_file_path)]
	
	for path in dst_path:
		os.chdir(path)
		normal_fmt_file = []
		for fmt in normal_music_fmt:
			normal_fmt_file.extend(glob(fmt))

		if normal_fmt_file:
			for file in normal_fmt_file:
				if file not in my_music_file:
					move(os.path.abspath(file), mymusic_file_path)

def main():
	move_encrypted_file(encryption_file_path)
	move_normal_file(normal_file_path)
	print("All files are transferred")

if __name__ == '__main__':
	main()