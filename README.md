# rename jpg file

This script renames jpg files based on EXIF date information.

The script assumes that the jpg files have DateTimeOriginal tag (36867) and DateTimeDigitized tag (36868).  The file name is decided as follows.

* Read DateTimeOriginal tag ('YYYY:MM:DD hh:mm:ss') and convert it to 'YYYYMMDD_hhmmss.JPG'.
* Add '_counter' suffix when the files have the same timestamp.

## preparation

```shell
pip install -r requirements.txt
```

## usage

```shell
python rename.py '/path/to/src' '/path/to/dst'
```
