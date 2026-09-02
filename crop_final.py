from PIL import Image

def crop_all(path, out_prefix, cells):
    img = Image.open(path)
    for idx, (x0, y0, x1, y1) in enumerate(cells, start=1):
        crop = img.crop((x0, y0, x1, y1))
        out = f"{out_prefix}_{idx:02d}.jpg"
        crop.save(out, quality=95)
        print(out, crop.size)

# images.jpeg - Planche 5, Le chat, 3 rows x 4 cols
# row1 col1/col2 get a taller top to crop out the header title bleeding into their cells
cells_1 = [
    (5,105,355,380), (355,68,742,380), (742,5,1144,380), (1144,5,1531,380),
    (5,380,411,708), (411,380,711,708), (711,380,1148,708), (1148,380,1531,708),
    (5,708,354,1019), (354,708,689,1019), (689,708,1090,1019), (1090,708,1531,1019),
]
crop_all("images.jpeg", "panels/planche5_lechat", cells_1)

# images2.jpeg - Planche 3, Poses emblematiques, 2 rows x 5 cols
cells_2 = [
    (5,55,283,540), (283,55,590,540), (590,55,923,540), (923,55,1192,540), (1192,55,1531,540),
    (5,540,308,1017), (308,540,602,1017), (602,540,902,1017), (902,540,1201,1017), (1201,540,1531,1017),
]
crop_all("images2.jpeg", "panels/planche3_poses", cells_2)
