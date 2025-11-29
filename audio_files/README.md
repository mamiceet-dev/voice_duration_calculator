# Audio Files Directory

This directory contains sample folders for organizing your audio files by format.

## Folder Structure

- **`gsm_files/`** - Place your GSM 6.10 format audio files here
- **`mp3_files/`** - Place your MP3 audio files here
- **`wav_files/`** - Place your WAV audio files here
- **`other_formats/`** - Place other audio formats (FLAC, OGG, M4A, AAC, WMA, OPUS, etc.) here

## Usage Examples

```bash
# Analyze GSM files
python ../gsm_duration_calculator.py gsm_files

# Analyze MP3 files with details
python ../mp3_duration_calculator.py mp3_files --details

# Analyze WAV files with details
python ../wav_duration_calculator.py wav_files --details

# Analyze all formats in other_formats folder
python ../audio_duration_calculator.py other_formats
```

---

# Ses Dosyaları Klasörü

Bu klasör, ses dosyalarınızı formata göre düzenlemek için örnek klasörler içerir.

## Klasör Yapısı

- **`gsm_files/`** - GSM 6.10 formatındaki ses dosyalarınızı buraya yerleştirin
- **`mp3_files/`** - MP3 ses dosyalarınızı buraya yerleştirin
- **`wav_files/`** - WAV ses dosyalarınızı buraya yerleştirin
- **`other_formats/`** - Diğer ses formatlarını (FLAC, OGG, M4A, AAC, WMA, OPUS, vb.) buraya yerleştirin

## Kullanım Örnekleri

```bash
# GSM dosyalarını analiz et
python ../gsm_duration_calculator.py gsm_files

# MP3 dosyalarını detaylı analiz et
python ../mp3_duration_calculator.py mp3_files --details

# WAV dosyalarını detaylı analiz et
python ../wav_duration_calculator.py wav_files --details

# other_formats klasöründeki tüm formatları analiz et
python ../audio_duration_calculator.py other_formats
```
