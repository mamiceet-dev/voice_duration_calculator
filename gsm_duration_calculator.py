#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GSM File Duration Calculator
Calculates the total duration of GSM audio files
"""

import os
import struct
from pathlib import Path
from datetime import timedelta


def get_gsm_duration(file_path):
    """
    Calculates the duration of a GSM file in seconds.
    GSM 6.10 format: 8000 Hz sample rate, each frame contains 160 samples (20ms)
    Each frame is 33 bytes
    """
    try:
        file_size = os.path.getsize(file_path)
        # GSM 6.10: 33 byte frame = 20ms audio
        frame_size = 33
        frame_duration = 0.02  # 20 milliseconds
        
        num_frames = file_size / frame_size
        duration = num_frames * frame_duration
        
        return duration
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


def calculate_total_duration(folder_path):
    """Calculates the total duration of all GSM files in the folder"""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' not found!")
        return
    
    gsm_files = list(folder.glob("*.gsm"))
    
    if not gsm_files:
        print(f"No GSM files found in '{folder_path}' folder!")
        return
    
    print(f"\n{'='*70}")
    print(f"GSM File Analysis - '{folder.name}' folder")
    print(f"{'='*70}\n")
    
    total_duration = 0
    total_size = 0
    
    print(f"Found {len(gsm_files)} files.\n")
    print(f"{'File Name':<50} {'Duration':>15}")
    print(f"{'-'*70}")
    
    for gsm_file in sorted(gsm_files):
        duration = get_gsm_duration(gsm_file)
        file_size = gsm_file.stat().st_size
        
        total_duration += duration
        total_size += file_size
        
        print(f"{gsm_file.name:<50} {format_duration(duration):>15}")
    
    print(f"{'-'*70}")
    print(f"\n{'TOTAL:':<50} {format_duration(total_duration):>15}")
    print(f"{'Total File Count:':<50} {len(gsm_files):>15}")
    print(f"{'Total Size:':<50} {total_size / (1024*1024):>12.2f} MB")
    print(f"{'Average File Duration:':<50} {format_duration(total_duration/len(gsm_files)):>15}")
    print(f"\n{'='*70}\n")
    
    return total_duration, len(gsm_files), total_size


def main():
    import sys
    
    print("\n=== GSM File Duration Calculator ===\n")
    
    # Command line argument or user input
    if len(sys.argv) > 1:
        folder_input = sys.argv[1]
    else:
        folder_input = input("Enter the path to the folder containing GSM files: ").strip()
    
    if not folder_input:
        print("Error: No folder path specified!")
        print("Usage: python gsm_duration_calculator.py <folder_path>")
        return
    
    calculate_total_duration(folder_input)


if __name__ == "__main__":
    main()
