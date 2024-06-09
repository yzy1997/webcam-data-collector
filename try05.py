import cv2
import asyncio
import aioconsole

async def async_input(prompt: str) -> str:
    return await aioconsole.ainput(prompt)

# Function to check for exit command asynchronously
async def check_exit():
    while True:
        user_input = await async_input("Type '0' to stop recording: ")
        if user_input.strip() == '0':
            return True
    return False

# Video shooting function, slightly modified
async def video_shooting(exit_event: asyncio.Event):
    video2 = cv2.VideoCapture(4)

    frame_size2 = (int(video2.get(cv2.CAP_PROP_FRAME_WIDTH)),
                   int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    FPS2 = video2.get(cv2.CAP_PROP_FPS)
    print("FPS2: ", FPS2)

    code = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    filename2 = "video2.avi"

    out2 = cv2.VideoWriter(filename2, code, FPS2, frameSize=frame_size2, isColor=True)

    while not exit_event.is_set():
        ret2, frame2 = video2.read()
        if ret2:
            frame2 = cv2.resize(frame2, frame_size2, interpolation=cv2.INTER_CUBIC)
            out2.write(frame2)
        else:
            break

    video2.release()
    out2.release()
    cv2.destroyAllWindows()

async def main():
    exit_event = asyncio.Event()
    
    # Task for checking exit command
    exit_task = asyncio.create_task(check_exit())
    # Task for video shooting
    video_task = asyncio.create_task(video_shooting(exit_event))

    # Wait for the exit command
    await exit_task
    # Signal the video shooting task to stop
    exit_event.set()
    # Wait for the video shooting task to finish
    await video_task

asyncio.run(main())
