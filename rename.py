import glob
import re
import shutil
import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_date(path):
    with Image.open(path) as im:
        exif = im.getexif()
    e = exif.get_ifd(0x8769)  # Exif情報の取得
    g = exif.get_ifd(0x8825)  # GPS情報の取得
    # print(e)

    # exif_dict = {TAGS[t]: e[t] for t in e}
    # gps_dict = {GPSTAGS[t]: g[t] for t in g}

    return e[36867], e[36868]


def convert_filename(p, original_datetime):
    m = p.match(original_datetime)
    year = m.group(1)
    month = m.group(2)
    day = m.group(3)
    hour = m.group(4)
    minute = m.group(5)
    second = m.group(6)
    return '{}{}{}_{}{}{}'.format(year, month, day, hour, minute, second)


def main():
    args = sys.argv
    if len(args) < 3:
        print('python rename.py src_path dst_path')
        return

    # match 'YYYY:MM:DD hh:mm:ss'
    p = re.compile(r'([\d]{4}):([\d]{2}):([\d]{2}) ([\d]{2}):([\d]{2}):([\d]{2})')
    src_path = args[1]
    dst_path = args[2]
    files = glob.glob('{}/*.JPG'.format(src_path))
    names = set()
    count = 0
    for i in range(2):
        file = files[i]
    # for file in files:
        # print(file)
        original_datetime, digitized_datetime = get_date(file)
        name = convert_filename(p, original_datetime)
        print(name)
        if name in names:
            count += 1
            dst_name = "{}_{}.JPG".format(name, count)
        else:
            names.add(name)
            count = 0
            dst_name = '{}.JPG'.format(name)
        dst = '{}/{}'.format(dst_path, dst_name)
        print(file, dst)
        shutil.copy2(file, dst)


if __name__ == '__main__':
    main()
