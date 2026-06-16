"""Generate scrolling-text GIF for GitHub profile README."""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 220
BG = (255, 255, 255)
FRAMES = 120
FRAME_MS = 33
OUT = r"d:\我的HTML创建中\bowen352121-bit\assets\scroll-bg.gif"

LINES = [
    {"text": "MONSTER APPRECIATION ZONE ZERO JUSTICE WILL PREVAIL NEVER FORGET YOUR DREAM   ", "y": 28, "size": 22, "color": (161, 161, 170), "dir": 1},
    {"text": "BELIEVE IN YOURSELF LIGHT BEATS DARKNESS SHINZO SASAGEYO HERO KNIGHT   ", "y": 68, "size": 18, "color": (100, 116, 139), "dir": -1},
    {"text": "ZENLESS ZONE ZERO CHUANSHI RISHI MENG   ", "y": 108, "size": 26, "color": (113, 113, 122), "dir": 1},
    {"text": "HYPHAE BOWEN KNIGHT DREAM SURMON CODE INSIGHT NEVER GIVE UP   ", "y": 148, "size": 17, "color": (148, 163, 184), "dir": -1},
    {"text": "KIDS HERO JUSTICE ZZZ EMPTY CALIBER SHINZO SASAGEYO   ", "y": 188, "size": 20, "color": (168, 162, 158), "dir": 1},
]


def get_font(size: int):
    try:
        return ImageFont.truetype("arialbd.ttf", size)
    except OSError:
        return ImageFont.load_default()


def measure(draw, text, font):
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


probe = Image.new("RGB", (1, 1), BG)
probe_draw = ImageDraw.Draw(probe)
for line in LINES:
    line["font"] = get_font(line["size"])
    line["width"] = measure(probe_draw, line["text"], line["font"])

frames = []
for f in range(FRAMES):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    progress = f / FRAMES
    for line in LINES:
        tw = line["width"]
        offset = progress * tw
        x = -offset if line["dir"] == 1 else offset - tw
        draw.text((x, line["y"]), line["text"] * 2, fill=line["color"], font=line["font"])
    frames.append(img)

frames[0].save(
    OUT,
    save_all=True,
    append_images=frames[1:],
    duration=FRAME_MS,
    loop=0,
    optimize=False,
)
print(f"Saved {OUT} ({FRAMES} frames @ {FRAME_MS}ms)")
