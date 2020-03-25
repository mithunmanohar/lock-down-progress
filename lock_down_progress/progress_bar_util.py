import math
import time
from PIL import Image, ImageDraw, ImageFont


def genrate_progress_bar(days_progressed, total_days):
    W, H = 1000, 150
    canvas = Image.new('RGB', (W, H), color='#303030')
    image = ImageDraw.Draw(canvas)
    p_bar_w = (days_progressed * (1000/total_days))
    shape = [(0, 0), (p_bar_w, W)] 
    image.rectangle(shape, fill ='#76E565')
    percentage_progress = str(math.floor((days_progressed / total_days) * 100)) + '%'
    w, h = image.textsize(percentage_progress)
    font = ImageFont.truetype('../fonts/arial.ttf', size=25);
    image.text(((p_bar_w-w)/2,(H-h)/2), percentage_progress, spacing=5, fill='black', font=font)
    canvas.save(r'progress_bar.jpg', quality=100)


if __name__ == '__main__':
    genrate_progress_bar(22, 21)
