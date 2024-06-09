
import cv2
import numpy as np
import asyncio
import aioconsole
# from pynput.keyboard import Key, Listener
# import asyncio

async def async_input(prompt: str) -> str:
    return await aioconsole.ainput(prompt)

# create video shooting function
async def video_shooting():

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

    # def on_press(key):
    #     # Check if the key has a char attribute
    #     if hasattr(key, 'char'):
    #         # Check if the pressed key is '0'
    #             if key.char == '0':
    #             # Stop listener
    #                 return False
                
    # Collect events until released



    control_bit = input('Please input a control bit (0 or 1):')
    print(control_bit)


    if control_bit == '1':
        while video2.isOpened():

            
    
            ret2, frame2 = video2.read()
    
            if ret2:
            
                frame2 = cv2.resize(frame2, frame_size2, interpolation=cv2.INTER_CUBIC)
                
                out2.write(frame2)  # 将图像写入视频流，生成视频

            # with Listener(on_press=on_press) as listener:
            #     a = listener.join()
            # if a == None:
            #     break    
            user_input  = await async_input("waiting for input: ")
            if user_input == '0':
                print("Exiting...")
                break
            

    video2.release()

    out2.release()

    cv2.destroyAllWindows()

async def main():
    await video_shooting()

asyncio.run(main())