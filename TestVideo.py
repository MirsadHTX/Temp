from moviepy.editor import *

video = VideoFileClip("..\ZZPicturesFiles\TestVideo.mp4").subclip(2,6)

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
#result.write_videofile("myHolidays_edited.webm",fps=25) # Many options.