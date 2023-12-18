def unpack_rgb(rgb_tuple):
    r,g,b = rgb_tuple
    return r,g,b

rgb_color = (255,128,0)
result = unpack_rgb(rgb_color)

for item in result:
    print(item)
