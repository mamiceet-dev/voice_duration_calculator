#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audio File Duration Calculator
Calculates the total duration of audio files (MP3, WAV, FLAC, OGG, M4A, AAC, WMA, etc.)
Requires: mutagen library
"""

import os
from pathlib import Path
from datetime import timedelta

try:
    from mutagen import File as MutagenFile
    from mutagen.mp3 import MP3
    from mutagen.wave import WAVE
    from mutagen.flac import FLAC
    from mutagen.oggvorbis import OggVorbis
    from mutagen.mp4 import MP4
    from mutagen.easyid3 import EasyID3
except ImportError:
    print("Error: 'mutagen' library is required.")
    print("Install it using: pip install mutagen")
    exit(1)


def get_audio_duration(file_path):
    """
    Gets the duration of an audio file in seconds.
    Supports: MP3, WAV, FLAC, OGG, M4A, AAC, WMA, and more.
    """
    try:
        audio = MutagenFile(file_path)
        if audio is not None and hasattr(audio.info, 'length'):
            return audio.info.length
        else:
            print(f"Warning: Could not read duration for {file_path}")
            return 0
    except Exception as e:
        print(f"Error ({file_path}): {e}")
        return 0


def format_duration(seconds):
    """Converts seconds to hours:minutes:seconds format"""
    td = timedelta(seconds=seconds)
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
    secs = td.seconds % 60
    
    if td.days > 0:
        hours += td.days * 24
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def calculate_total_duration(folder_path, file_extensions=None):
    """
    Calculates the total duration of all audio files in the folder.
    
    Args:
        folder_path: Path to the folder containing audio files
        file_extensions: List of file extensions to process (e.g., ['.mp3', '.wav'])
                        If None, processes all common audio formats
    """
    if file_extensions is None:
        file_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac', '.wma', '.opus', '.ape', '.alac']
    
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' not found!")
        return
    
    # Collect all audio files with specified extensions
    audio_files = []
    for ext in file_extensions:
        audio_files.extend(folder.glob(f"*{ext}"))
        audio_files.extend(folder.glob(f"*{ext.upper()}"))
    
    # Remove duplicates and sort
    audio_files = sorted(set(audio_files))
    
    if not audio_files:
        print(f"No audio files found in '{folder_path}' folder!")
        print(f"Searched for extensions: {', '.join(file_extensions)}")
        return
    
    print(f"\n{'='*70}")
    print(f"Audio File Analysis - '{folder.name}' folder")
    print(f"{'='*70}\n")
    
    total_duration = 0
    total_size = 0
    successful_files = 0
    
    print(f"Found {len(audio_files)} files.\n")
    print(f"{'File Name':<45} {'Duration':>12} {'Size':>10}")
    print(f"{'-'*70}")
    
    for audio_file in sorted(audio_files):
        duration = get_audio_duration(audio_file)
        file_size = audio_file.stat().st_size
        
        if duration > 0:
            successful_files += 1
            total_duration += duration
            total_size += file_size
            
            size_mb = file_size / (1024 * 1024)
            print(f"{audio_file.name:<45} {format_duration(duration):>12} {size_mb:>9.2f}MB")
        else:
            print(f"{audio_file.name:<45} {'ERROR':>12} {'-':>10}")
    
    print(f"{'-'*70}")
    print(f"\n{'TOTAL:':<45} {format_duration(total_duration):>12}")
    print(f"{'Successful Files:':<45} {successful_files:>12}")
    print(f"{'Failed Files:':<45} {len(audio_files) - successful_files:>12}")
    print(f"{'Total Size:':<45} {total_size / (1024*1024):>9.2f} MB")
    
    if successful_files > 0:
        print(f"{'Average File Duration:':<45} {format_duration(total_duration/successful_files):>12}")
        print(f"{'Average File Size:':<45} {(total_size/successful_files) / (1024*1024):>9.2f} MB")
    
    print(f"\n{'='*70}\n")
    
    return total_duration, successful_files, total_size


def main():
    import sys
    
    print("\n=== Audio File Duration Calculator ===\n")
    
    # Command line argument or user input
    if len(sys.argv) > 1:
        folder_input = sys.argv[1]
    else:
        folder_input = input("Enter the path to the folder containing audio files: ").strip()
    
    if not folder_input:
        print("Error: No folder path specified!")
        print("Usage: python audio_duration_calculator.py <folder_path>")
        return
    
    # Optional: specify file extensions
    print("\nSupported formats: MP3, WAV, FLAC, OGG, M4A, AAC, WMA, OPUS, APE, ALAC")
    print("Press Enter to process all formats, or specify extensions (e.g., .mp3,.wav):")
    ext_input = input("> ").strip()
    
    if ext_input:
        extensions = [ext.strip() if ext.strip().startswith('.') else f'.{ext.strip()}' 
                     for ext in ext_input.split(',')]
        calculate_total_duration(folder_input, extensions)
    else:
        calculate_total_duration(folder_input)


if __name__ == "__main__":
    main()
