#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MP3 File Duration Calculator
Calculates the total duration of MP3 audio files
Requires: mutagen library
"""

import os
from pathlib import Path
from datetime import timedelta

try:
    from mutagen.mp3 import MP3
except ImportError:
    print("Error: 'mutagen' library is required.")
    print("Install it using: pip install mutagen")
    exit(1)


def get_mp3_duration(file_path):
    """
    Gets the duration of an MP3 file in seconds.
    """
    try:
        audio = MP3(file_path)
        return audio.info.length
    except Exception as e:
        print(f"Error ({file_path}): {e}")
        return 0


def get_mp3_info(file_path):
    """
    Gets detailed information about an MP3 file.
    Returns: (duration, bitrate, sample_rate, channels)
    """
    try:
        audio = MP3(file_path)
        return (
            audio.info.length,
            audio.info.bitrate // 1000,  # Convert to kbps
            audio.info.sample_rate,
            audio.info.channels
        )
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
    Calculates the total duration of all MP3 files in the folder.
    
    Args:
        folder_path: Path to the folder containing MP3 files
        show_details: If True, shows bitrate and other technical details
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' not found!")
        return
    
    mp3_files = list(folder.glob("*.mp3")) + list(folder.glob("*.MP3"))
    mp3_files = sorted(set(mp3_files))
    
    if not mp3_files:
        print(f"No MP3 files found in '{folder_path}' folder!")
        return
    
    print(f"\n{'='*80}")
    print(f"MP3 File Analysis - '{folder.name}' folder")
    print(f"{'='*80}\n")
    
    total_duration = 0
    total_size = 0
    total_bitrate = 0
    successful_files = 0
    
    print(f"Found {len(mp3_files)} files.\n")
    
    if show_details:
        print(f"{'File Name':<40} {'Duration':>10} {'Bitrate':>8} {'Size':>10}")
        print(f"{'-'*80}")
    else:
        print(f"{'File Name':<50} {'Duration':>15} {'Size':>12}")
        print(f"{'-'*80}")
    
    for mp3_file in mp3_files:
        file_size = mp3_file.stat().st_size
        
        if show_details:
            duration, bitrate, sample_rate, channels = get_mp3_info(mp3_file)
        else:
            duration = get_mp3_duration(mp3_file)
            bitrate = 0
        
        if duration > 0:
            successful_files += 1
            total_duration += duration
            total_size += file_size
            total_bitrate += bitrate
            
            size_mb = file_size / (1024 * 1024)
            
            if show_details:
                print(f"{mp3_file.name:<40} {format_duration(duration):>10} {bitrate:>6}kbps {size_mb:>9.2f}MB")
            else:
                print(f"{mp3_file.name:<50} {format_duration(duration):>15} {size_mb:>11.2f}MB")
        else:
            print(f"{mp3_file.name:<50} {'ERROR':>15} {'-':>12}")
    
    print(f"{'-'*80}")
    print(f"\n{'TOTAL:':<50} {format_duration(total_duration):>15}")
    print(f"{'Successful Files:':<50} {successful_files:>15}")
    
    if successful_files != len(mp3_files):
        print(f"{'Failed Files:':<50} {len(mp3_files) - successful_files:>15}")
    
    print(f"{'Total Size:':<50} {total_size / (1024*1024):>12.2f} MB")
    
    if successful_files > 0:
        print(f"{'Average File Duration:':<50} {format_duration(total_duration/successful_files):>15}")
        print(f"{'Average File Size:':<50} {(total_size/successful_files) / (1024*1024):>12.2f} MB")
        
        if show_details and total_bitrate > 0:
            print(f"{'Average Bitrate:':<50} {total_bitrate//successful_files:>12} kbps")
    
    print(f"\n{'='*80}\n")
    
    return total_duration, successful_files, total_size


def main():
    import sys
    
    print("\n=== MP3 File Duration Calculator ===\n")
    
    # Command line argument or user input
    if len(sys.argv) > 1:
        folder_input = sys.argv[1]
        show_details = '--details' in sys.argv or '-d' in sys.argv
    else:
        folder_input = input("Enter the path to the folder containing MP3 files: ").strip()
        detail_choice = input("Show detailed info (bitrate, etc.)? (y/n): ").strip().lower()
        show_details = detail_choice == 'y'
    
    if not folder_input:
        print("Error: No folder path specified!")
        print("Usage: python mp3_duration_calculator.py <folder_path> [--details]")
        return
    
    calculate_total_duration(folder_input, show_details)


if __name__ == "__main__":
    main()
