#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAV File Duration Calculator
Calculates the total duration of WAV audio files
No external dependencies required (uses wave module from standard library)
"""

import os
import wave
from pathlib import Path
from datetime import timedelta


def get_wav_duration(file_path):
    """
    Gets the duration of a WAV file in seconds.
    Uses the wave module from Python standard library.
    """
    try:
        with wave.open(str(file_path), 'r') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            return duration
    except Exception as e:
        print(f"Error ({file_path}): {e}")
        return 0


def get_wav_info(file_path):
    """
    Gets detailed information about a WAV file.
    Returns: (duration, sample_rate, channels, sample_width)
    """
    try:
        with wave.open(str(file_path), 'r') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            duration = frames / float(rate)
            return (duration, rate, channels, sample_width)
    except Exception as e:
        return (0, 0, 0, 0)


def format_duration(seconds):
    """Converts seconds to hours:minutes:seconds format"""
    td = timedelta(seconds=seconds)
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
    secs = td.seconds % 60
    
    if td.days > 0:
        hours += td.days * 24
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def calculate_total_duration(folder_path, show_details=False):
    """
    Calculates the total duration of all WAV files in the folder.
    
    Args:
        folder_path: Path to the folder containing WAV files
        show_details: If True, shows sample rate, channels and other technical details
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' not found!")
        return
    
    wav_files = list(folder.glob("*.wav")) + list(folder.glob("*.WAV"))
    wav_files = sorted(set(wav_files))
    
    if not wav_files:
        print(f"No WAV files found in '{folder_path}' folder!")
        return
    
    print(f"\n{'='*85}")
    print(f"WAV File Analysis - '{folder.name}' folder")
    print(f"{'='*85}\n")
    
    total_duration = 0
    total_size = 0
    successful_files = 0
    
    print(f"Found {len(wav_files)} files.\n")
    
    if show_details:
        print(f"{'File Name':<35} {'Duration':>10} {'Rate':>8} {'Ch':>3} {'Bits':>4} {'Size':>10}")
        print(f"{'-'*85}")
    else:
        print(f"{'File Name':<50} {'Duration':>15} {'Size':>12}")
        print(f"{'-'*85}")
    
    for wav_file in wav_files:
        file_size = wav_file.stat().st_size
        
        if show_details:
            duration, sample_rate, channels, sample_width = get_wav_info(wav_file)
        else:
            duration = get_wav_duration(wav_file)
            sample_rate = channels = sample_width = 0
        
        if duration > 0:
            successful_files += 1
            total_duration += duration
            total_size += file_size
            
            size_mb = file_size / (1024 * 1024)
            
            if show_details:
                bits = sample_width * 8
                rate_khz = sample_rate / 1000
                print(f"{wav_file.name:<35} {format_duration(duration):>10} {rate_khz:>6.1f}kHz {channels:>3} {bits:>4} {size_mb:>9.2f}MB")
            else:
                print(f"{wav_file.name:<50} {format_duration(duration):>15} {size_mb:>11.2f}MB")
        else:
            print(f"{wav_file.name:<50} {'ERROR':>15} {'-':>12}")
    
    print(f"{'-'*85}")
    print(f"\n{'TOTAL:':<50} {format_duration(total_duration):>15}")
    print(f"{'Successful Files:':<50} {successful_files:>15}")
    
    if successful_files != len(wav_files):
        print(f"{'Failed Files:':<50} {len(wav_files) - successful_files:>15}")
    
    print(f"{'Total Size:':<50} {total_size / (1024*1024):>12.2f} MB")
    
    if successful_files > 0:
        print(f"{'Average File Duration:':<50} {format_duration(total_duration/successful_files):>15}")
        print(f"{'Average File Size:':<50} {(total_size/successful_files) / (1024*1024):>12.2f} MB")
    
    print(f"\n{'='*85}\n")
    
    return total_duration, successful_files, total_size


def main():
    import sys
    
    print("\n=== WAV File Duration Calculator ===\n")
    
    # Command line argument or user input
    if len(sys.argv) > 1:
        folder_input = sys.argv[1]
        show_details = '--details' in sys.argv or '-d' in sys.argv
    else:
        folder_input = input("Enter the path to the folder containing WAV files: ").strip()
        detail_choice = input("Show detailed info (sample rate, channels, etc.)? (y/n): ").strip().lower()
        show_details = detail_choice == 'y'
    
    if not folder_input:
        print("Error: No folder path specified!")
        print("Usage: python wav_duration_calculator.py <folder_path> [--details]")
        return
    
    calculate_total_duration(folder_input, show_details)


if __name__ == "__main__":
    main()
