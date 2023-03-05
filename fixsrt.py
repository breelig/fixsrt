import re
import sys
import os

def adjust_srt_time(srt_file, n):
    with open(srt_file, 'r', encoding='iso-8859-1') as f:
        srt_data = f.read()
    
    pattern = r'(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)'
    new_srt_data = re.sub(pattern, lambda m: adjust_time(m.group(1), n) + ' --> ' + adjust_time(m.group(2), n), srt_data)
    
    # Get the directory and base filename of the original file
    dir_name, base_name = os.path.split(srt_file)
    # Split the base filename into the filename and extension
    file_name, ext = os.path.splitext(base_name)
    # Construct the new filename with " fixed" appended before the extension
    new_file_name = f"{file_name} fixed{ext}"
    # Join the directory and new filename to get the full path of the new file
    new_file_path = os.path.join(dir_name, new_file_name)
    
    with open(new_file_path, 'w', encoding='iso-8859-1') as f:
        f.write(new_srt_data)

def adjust_time(time_str, n):
    h, m, s_ms = time_str.split(':')
    s, ms = s_ms.split(',')
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
    new_total_seconds = total_seconds + n
    new_h = str(new_total_seconds // 3600).zfill(2)
    new_m = str((new_total_seconds // 60) % 60).zfill(2)
    new_s = str(new_total_seconds % 60).zfill(2)
    new_ms = ms
    return f'{new_h}:{new_m}:{new_s},{new_ms}'

# Example usage
# adjust_srt_time('example.srt', 5) # increments by 5 seconds
# adjust_srt_time('example.srt', -3) # decrements by 3 seconds

def main():
    # Check if the SRT file and time adjustment were specified as command line arguments
    if len(sys.argv) >= 2:
        srt_file = sys.argv[1]
    else:
        srt_file = input("Enter the path to the SRT file: ")
    
    if len(sys.argv) >= 3:
        n = int(sys.argv[2])
    else:
        n = int(input("Enter the number of seconds to adjust the times by (positive or negative): "))
    
    adjust_srt_time(srt_file, n)
    print("Done!")

if __name__ == "__main__":
    main()