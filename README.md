# fixsrt
Adjusts the times in a subtitle srt file by +/- n seconds. 

Given an input file and number of seconds to adjust the times by, 
this function will create a new file with the same name as the original 
file but with " fixed" appended before the extension.

## Example
Here is an example to increment the subtitles by 2 seconds in the file myfilm.srt. The output file would be ~/Movies/myfilm fixed.srt

`python fixsrt.py "~/Movies/myfilm.srt" 2`

Here is an example to decrement the subtitles by -1 seconds in the file myfilm.srt. The output file would be ~/Movies/myfilm fixed.srt

`python fixsrt.py "~/Movies/myfilm.srt" -1`

