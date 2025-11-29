# Audio Duration Calculator Suite

A collection of Python scripts to calculate the total duration of audio files in various formats.

---

# Ses Dosyası Süre Hesaplayıcı Paketi

Çeşitli formatlardaki ses dosyalarının toplam süresini hesaplayan Python scriptleri koleksiyonu.

---

## English

### Description

This suite includes four specialized scripts for calculating audio file durations:

1. **GSM Duration Calculator** (`gsm_duration_calculator.py`) - For GSM 6.10 format files
2. **MP3 Duration Calculator** (`mp3_duration_calculator.py`) - For MP3 files with detailed metadata
3. **WAV Duration Calculator** (`wav_duration_calculator.py`) - For WAV files using standard library
4. **Universal Audio Calculator** (`audio_duration_calculator.py`) - Supports MP3, WAV, FLAC, OGG, M4A, AAC, WMA, OPUS, APE, ALAC

Each script provides detailed information about:
- Individual file durations
- Total duration of all files
- File count and total size
- Average file duration
- Technical details (bitrate, sample rate, channels - depending on format)

### Features

- ✅ Multiple format support (GSM, MP3, WAV, FLAC, OGG, M4A, AAC, WMA, and more)
- ✅ Accurate duration calculation for each format
- ✅ Batch processing of multiple files
- ✅ Detailed file-by-file analysis
### Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
# For GSM and WAV calculators - no installation needed (standard library only)

# For MP3 and Universal Audio calculator:
pip install -r requirements.txt

# Or install manually:
pip install mutagen
```
- ✅ No dependencies for GSM and WAV (uses only standard library)

### Requirements

#### For GSM and WAV calculators:
- Python 3.6 or higher
- No external dependencies (uses only standard library)
### Usage

#### 1. GSM Duration Calculator

```bash
# Command line
python gsm_duration_calculator.py <folder_path>

# Interactive mode
python gsm_duration_calculator.py
```

#### 2. MP3 Duration Calculator

```bash
# Basic mode
python mp3_duration_calculator.py <folder_path>

# With detailed info (bitrate, etc.)
python mp3_duration_calculator.py <folder_path> --details

# Interactive mode
python mp3_duration_calculator.py
```

#### 3. WAV Duration Calculator

```bash
# Basic mode
python wav_duration_calculator.py <folder_path>
### Example Output

#### GSM Calculator:
```
======================================================================
GSM File Analysis - 'recordings' folder
======================================================================

Found 150 files.

File Name                                          Duration
----------------------------------------------------------------------
recording_001.gsm                                   00:02:34
recording_002.gsm                                   00:01:45
...
----------------------------------------------------------------------

TOTAL:                                              05:45:32
Total File Count:                                        150
Total Size:                                          125.45 MB
Average File Duration:                               00:02:18
======================================================================
```

#### MP3 Calculator (with --details):
```
================================================================================
MP3 File Analysis - 'music' folder
================================================================================

Found 50 files.

File Name                                Duration  Bitrate      Size
--------------------------------------------------------------------------------
song_001.mp3                              00:03:45   320kbps     8.52MB
song_002.mp3                              00:04:12   256kbps     7.73MB
### Technical Details

#### GSM 6.10 Format:
- Sample rate: 8000 Hz
- Frame size: 33 bytes
- Frame duration: 20 milliseconds
- Each frame contains 160 samples
- **Formula:** `Duration = (File Size / 33 bytes) × 0.02 seconds`

#### MP3 Format:
### File Structure

```
voicetime_calculator/
├── audio_files/                    # Sample folders for audio files
│   ├── gsm_files/                  # Place GSM files here
│   ├── mp3_files/                  # Place MP3 files here
│   ├── wav_files/                  # Place WAV files here
│   ├── other_formats/              # Place other formats here
│   └── README.md                   # Audio files directory guide
├── gsm_duration_calculator.py      # GSM format calculator
├── mp3_duration_calculator.py      # MP3 format calculator  
├── wav_duration_calculator.py      # WAV format calculator
├── audio_duration_calculator.py    # Universal audio calculator
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```eads RIFF header information
- Supports various sample rates and bit depths
- **Formula:** `Duration = Frames / Sample Rate`

#### Universal Audio Calculator:
- Uses `mutagen` library for format detection and metadata reading
- Automatically handles different audio codecs
- Supported formats: MP3, WAV, FLAC, OGG Vorbis, M4A/AAC, WMA, OPUS, APE, ALAC
- Gracefully handles corrupted or unsupported files=================
```

#### WAV Calculator (with --details):
```
=====================================================================================
WAV File Analysis - 'recordings' folder
=====================================================================================

Found 25 files.

File Name                           Duration      Rate  Ch Bits       Size
-------------------------------------------------------------------------------------
recording_001.wav                    00:02:15   44.1kHz   2   16      23.52MB
recording_002.wav                    00:01:48   48.0kHz   2   24      31.18MB
...
-------------------------------------------------------------------------------------

TOTAL:                                              00:45:30
Successful Files:                                         25
Total Size:                                          658.75 MB
Average File Duration:                               00:01:49
=====================================================================================
```
### Troubleshooting

**Error: 'mutagen' library is required**
- Install the library: `pip install mutagen`
- Only needed for MP3 and Universal Audio calculator
- GSM and WAV calculators don't need external libraries

**Error: Folder not found**
- Make sure the folder path is correct
- Use absolute paths for better reliability
- On Windows, you can use either `\` or `/` as path separator

**No audio files found**
- Ensure files have the correct extension (.mp3, .wav, .gsm, etc.)
- Check that the folder path is correct
- For Universal Audio calculator, verify the file format is supported

**Duration shows as 00:00:00 or ERROR**
- File may be corrupted
- File format may not match the extension
- For MP3/Universal calculator: check if mutagen is installed correctly
## Türkçe

### Açıklama

Bu paket, ses dosyası sürelerini hesaplamak için dört özel script içerir:

1. **GSM Süre Hesaplayıcı** (`gsm_duration_calculator.py`) - GSM 6.10 format dosyaları için
2. **MP3 Süre Hesaplayıcı** (`mp3_duration_calculator.py`) - Detaylı metadata ile MP3 dosyaları için
3. **WAV Süre Hesaplayıcı** (`wav_duration_calculator.py`) - Standart kütüphane ile WAV dosyaları için
4. **Evrensel Ses Hesaplayıcı** (`audio_duration_calculator.py`) - MP3, WAV, FLAC, OGG, M4A, AAC, WMA, OPUS, APE, ALAC destekler

Her script aşağıdaki bilgileri sağlar:
- Her dosyanın ayrı ayrı süresi
- Tüm dosyaların toplam süresi
- Dosya sayısı ve toplam boyut
- Ortalama dosya süresi
- Teknik detaylar (bitrate, sample rate, kanal sayısı - formata göre)

### Özellikler

- ✅ Çoklu format desteği (GSM, MP3, WAV, FLAC, OGG, M4A, AAC, WMA ve daha fazlası)
- ✅ Her format için doğru süre hesaplaması
- ✅ Toplu dosya işleme
- ✅ Detaylı dosya bazlı analiz
- ✅ Özet istatistikler (toplam, ortalama, dosya sayısı, boyut)
- ✅ Teknik metadata gösterimi (opsiyonel)
- ✅ Temiz, formatlanmış çıktı
- ✅ Komut satırı ve interaktif modlar
- ✅ GSM ve WAV için bağımlılık yok (sadece standart kütüphane)

### Gereksinimler

#### GSM ve WAV hesaplayıcıları için:
- Python 3.6 veya üzeri
- Harici bağımlılık yok (sadece standart kütüphane)

#### MP3 ve Evrensel Ses hesaplayıcısı için:
- Python 3.6 veya üzeri
- `mutagen` kütüphanesi
python mp3_duration_calculator.py C:\Music\MyPlaylist --details
python audio_duration_calculator.py D:\AudioFiles

# Linux/Mac
python wav_duration_calculator.py /home/user/recordings --details
python audio_duration_calculator.py /path/to/music
```# Method 2: Interactive Mode

Simply run the script without arguments:
```bash
python gsm_duration_calculator.py
```

Then enter the folder path when prompted:
```
Enter the path to the folder containing GSM files: C:\audio_files
```

### Example Output

```
=======================================================================
GSM File Analysis - 'audio_files' folder
=======================================================================

Found 150 files.

File Name                                          Duration
-----------------------------------------------------------------------
recording_001.gsm                                   00:02:34
recording_002.gsm                                   00:01:45
recording_003.gsm                                   00:03:12
...

-----------------------------------------------------------------------

TOTAL:                                              05:45:32
Total File Count:                                        150
Total Size:                                          125.45 MB
Average File Duration:                               00:02:18

=======================================================================
```

### Technical Details

The script calculates duration based on the GSM 6.10 format specifications:
- Sample rate: 8000 Hz
- Frame size: 33 bytes
- Frame duration: 20 milliseconds
- Each frame contains 160 samples

**Formula:** `Duration = (File Size / 33 bytes) × 0.02 seconds`

### Kurulum

1. Bu depoyu klonlayın veya indirin
2. Gerekli bağımlılıkları yükleyin:

### Kullanım

#### 1. GSM Süre Hesaplayıcı

```bash
# Komut satırı
python gsm_duration_calculator.py <klasor_yolu>

# İnteraktif mod
python gsm_duration_calculator.py
```

#### 2. MP3 Süre Hesaplayıcı

```bash
# Temel mod
python mp3_duration_calculator.py <klasor_yolu>

# Detaylı bilgi ile (bitrate vb.)
python mp3_duration_calculator.py <klasor_yolu> --details

# İnteraktif mod
python mp3_duration_calculator.py
```

#### 3. WAV Süre Hesaplayıcı

```bash
# Temel mod
python wav_duration_calculator.py <klasor_yolu>

# Detaylı bilgi ile (sample rate, kanal, bit derinliği)
python wav_duration_calculator.py <klasor_yolu> --details

# İnteraktif mod
python wav_duration_calculator.py
```

#### 4. Evrensel Ses Hesaplayıcı

```bash
# Tüm desteklenen formatları işle
python audio_duration_calculator.py <klasor_yolu>

# Sadece belirli formatları işle
python audio_duration_calculator.py <klasor_yolu>
### Örnek Çıktılar

Yukarıdaki "Example Output" bölümüne bakın - tüm hesaplayıcılar için detaylı örnekler mevcut. Açıklama

Bu script GSM 6.10 formatındaki ses dosyalarını analiz eder ve toplam sürelerini hesaplar. Aşağıdaki bilgileri sağlar:
- Her dosyanın ayrı ayrı süresi
- Tüm dosyaların toplam süresi
- Dosya sayısı ve toplam boyut
- Ortalama dosya süresi

### Özellikler

- ✅ Doğru GSM 6.10 format süre hesaplaması
- ✅ Toplu dosya işleme
- ✅ Detaylı dosya bazlı analiz
- ✅ Özet istatistikler (toplam, ortalama, dosya sayısı, boyut)
- ✅ Temiz, formatlanmış çıktı
- ✅ Komut satırı ve interaktif modlar

### Gereksinimler

- Python 3.6 veya üzeri
- Harici bağımlılık yok (sadece standart kütüphane kullanır)

### Kurulum

### Teknik Detaylar

#### GSM 6.10 Format:
- Örnekleme hızı: 8000 Hz
- Frame boyutu: 33 byte
- Frame süresi: 20 milisaniye
- Her frame 160 örnek içerir
- **Formül:** `Süre = (Dosya Boyutu / 33 byte) × 0.02 saniye`

#### MP3 Format:
- ID3 etiketlerini ve ses özelliklerini okumak için `mutagen` kütüphanesi kullanır
- Tüm MP3 varyantlarını destekler (CBR, VBR, ABR)
- Dosya metadata'sından bitrate, sample rate, kanal sayısını okur

### Dosya Yapısı

```
voicetime_calculator/
├── gsm_duration_calculator.py      # GSM format hesaplayıcı
├── mp3_duration_calculator.py      # MP3 format hesaplayıcı
├── wav_duration_calculator.py      # WAV format hesaplayıcı
├── audio_duration_calculator.py    # Evrensel ses hesaplayıcı
### Sorun Giderme

**Hata: 'mutagen' kütüphanesi gerekli**
- Kütüphaneyi yükleyin: `pip install mutagen`
- Sadece MP3 ve Evrensel Ses hesaplayıcısı için gerekli
- GSM ve WAV hesaplayıcıları harici kütüphane gerektirmez

**Hata: Klasör bulunamadı**
- Klasör yolunun doğru olduğundan emin olun
- Daha iyi güvenilirlik için mutlak yollar kullanın
- Windows'ta yol ayırıcı olarak `\` veya `/` kullanabilirsiniz

**Ses dosyası bulunamadı**
- Dosyaların doğru uzantıya sahip olduğundan emin olun (.mp3, .wav, .gsm vb.)
- Klasör yolunun doğru olduğunu kontrol edin
- Evrensel Ses hesaplayıcısı için, dosya formatının desteklendiğini doğrulayın

**Süre 00:00:00 veya ERROR gösteriyor**
- Dosya bozuk olabilir
- Dosya formatı uzantıyla eşleşmiyor olabilir
- MP3/Evrensel hesaplayıcı için: mutagen'in doğru yüklendiğini kontrol edin
- Bilinmeyen formatlar için Evrensel Ses hesaplayıcısını kullanmayı deneyin

**Dosyalar işlendi ama süre yanlış görünüyor**
- GSM: Dosyaların gerçekten GSM 6.10 formatında olduğundan emin olun
- MP3: VBR dosyaları mutagen tarafından doğru şekilde işlenir
- WAV: Dosyanın standart PCM WAV formatında olup olmadığını kontrol edin
```bash
python gsm_duration_calculator.py C:\ses_dosyalari
```

veya Linux/Mac'te:
```bash
python gsm_duration_calculator.py /yol/ses_dosyalari
```

#### Yöntem 2: İnteraktif Mod

Script'i argümansız çalıştırın:
```bash
python gsm_duration_calculator.py
```

Sonra istendiğinde klasör yolunu girin:
```
Enter the path to the folder containing GSM files: C:\ses_dosyalari
```

### Örnek Çıktı

```
=======================================================================
GSM File Analysis - 'ses_dosyalari' folder
=======================================================================

Found 150 files.

File Name                                          Duration
-----------------------------------------------------------------------
kayit_001.gsm                                       00:02:34
kayit_002.gsm                                       00:01:45
kayit_003.gsm                                       00:03:12
...

-----------------------------------------------------------------------

TOTAL:                                              05:45:32
Total File Count:                                        150
Total Size:                                          125.45 MB
Average File Duration:                               00:02:18

=======================================================================
```

### Teknik Detaylar

Script, GSM 6.10 format özelliklerine göre süre hesaplar:
- Örnekleme hızı: 8000 Hz
- Frame boyutu: 33 byte
- Frame süresi: 20 milisaniye
- Her frame 160 örnek içerir

**Formül:** `Süre = (Dosya Boyutu / 33 byte) × 0.02 saniye`

### Dosya Yapısı

```
voicetime_calculator/
├── audio_files/                    # Ses dosyaları için örnek klasörler
│   ├── gsm_files/                  # GSM dosyalarını buraya yerleştirin
│   ├── mp3_files/                  # MP3 dosyalarını buraya yerleştirin
│   ├── wav_files/                  # WAV dosyalarını buraya yerleştirin
│   ├── other_formats/              # Diğer formatları buraya yerleştirin
│   └── README.md                   # Ses dosyaları klasör rehberi
├── gsm_duration_calculator.py      # GSM format hesaplayıcı
├── mp3_duration_calculator.py      # MP3 format hesaplayıcı
├── wav_duration_calculator.py      # WAV format hesaplayıcı
├── audio_duration_calculator.py    # Evrensel ses hesaplayıcı
├── requirements.txt                # Python bağımlılıkları
└── README.md                       # Bu dosya
```

### Sorun Giderme

**Hata: Klasör bulunamadı**
- Klasör yolunun doğru olduğundan emin olun
- Daha iyi güvenilirlik için mutlak yollar kullanın
- Windows'ta yol ayırıcı olarak `\` veya `/` kullanabilirsiniz

**GSM dosyası bulunamadı**
- Dosyaların `.gsm` uzantısına sahip olduğundan emin olun
- Klasörün GSM ses dosyaları içerdiğini kontrol edin

### Lisans

Bu proje açık kaynaklıdır ve ücretsiz kullanıma açıktır.

### Katkıda Bulunma

İyileştirmeler için issue açabilir, depoyu fork'layabilir ve pull request oluşturabilirsiniz.

---

## Support / Destek

If you encounter any issues or have questions, please open an issue on GitHub.

Herhangi bir sorunla karşılaşırsanız veya sorularınız varsa, lütfen GitHub'da bir issue açın.
