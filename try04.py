import threading
import sys
import select
import cv2

video2 = cv2.VideoCapture(4)

frame_size2 = (int(video2.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT)))    # 获取摄像头分辨率

FPS2 = video2.get(cv2.CAP_PROP_FPS)    # 获取摄像头帧率
print("FPS2: ", FPS2)

# 保存视频
code = cv2.VideoWriter_fourcc('D','I','V','X')  # 编码格式
fps = 30  # 保存视频的帧率
# filename1 = "video1.avi"  # 保存视频的路径和名字
filename2 = "video2.avi"  # 保存视频的路径和名字

out2 = cv2.VideoWriter(filename2, code, FPS2, frameSize=frame_size2, isColor=True)  # 保存视频的视频流

control_bit = input('Please input a control bit (0 or 1):')
print(control_bit)

def listen_for_exit_command():
    while True:
        # print("\nType '0' to exit.")
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline()
            if line.strip() == '0':
                print("Exiting...")
                break

# Start a background thread that listens for the exit command
thread = threading.Thread(target=listen_for_exit_command)
thread.daemon = True  # Daemonize thread
thread.start()

# Your main program can continue running here
try:
    # while True:
        # Your main program loop
        if control_bit == '1':
            while video2.isOpened():
        
                ret2, frame2 = video2.read()
        
                if ret2:
            
                    frame2 = cv2.resize(frame2, frame_size2, interpolation=cv2.INTER_CUBIC)
                    
                    out2.write(frame2)
        video2.release()

        out2.release()

        cv2.destroyAllWindows()
except KeyboardInterrupt:
    pass
