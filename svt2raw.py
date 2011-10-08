#-*- coding: utf-8 -*-
__author__ = 'Vladimir Ignatyev'

import sys

FRAME_CHUNK_SIZE = 0x25800
UNKNOWN_SIG = 0x410

def convert(svt_file_name, output_dir, frame_start, frame_end):
    src_file = open(svt_file_name, 'rb')
    pos = 0xA27 + ((frame_start -1) * (FRAME_CHUNK_SIZE + UNKNOWN_SIG))
    frame_num = frame_start

    while frame_num <= frame_end:
        src_file.seek(pos)
        frame = src_file.read(FRAME_CHUNK_SIZE)
        out_file_name = output_dir + "{0}.raw".format(frame_num)
        out_file = open(out_file_name, 'wb')
        out_file.write(frame)
        out_file.close()
        frame_num += 1
        pos += UNKNOWN_SIG + FRAME_CHUNK_SIZE
	print "{0} frames successfully converted".format(frame_end - frame_start + 1)
		
if len(sys.argv) < 2:
	print "\n"
	print "Converts video-frames from .svt file to .raw images\n"
	print "Usage: svt2raw file_name output_dir start_frame end_frame"
	
else:
	file_name = sys.argv[1]
	output_dir = sys.argv[2]
	start_frame = int(sys.argv[3])
	end_frame = int(sys.argv[4])
	
	convert(file_name, output_dir, start_frame, end_frame)

  