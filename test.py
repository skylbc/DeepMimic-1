
#text_file = open("data/motions/humanoid3d_backflip.txt", "r")
text_file = open("data/motions/humanoid3d_cartwheel.txt", "r")
lines = text_file.read().split(',')
print(lines)
print(len(lines))
text_file.close()