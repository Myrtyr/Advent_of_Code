with open("data/input_for_day20.txt", "r") as f:
    text = f.read().split("\n\n")[:-1]

images = []
for elt in text:
    images.append([elt.split("\n")[0], elt.split("\n")[1:]])
amount_of_images = 0
image_dict = {}
for elt in images:
    image_border_north = elt[1][0]
    image_border_south = elt[1][-1]
    image_border_west = ""
    for row in elt[1]:
        image_border_west += row[0]
    image_border_east = ""
    for row in elt[1]:
        image_border_east += row[-1]
    amount_of_images += 1
    image_dict[elt[0]] = [image_border_north, image_border_north[::-1], image_border_east, image_border_east[::-1], image_border_south, image_border_south[::-1], image_border_west, image_border_west[::-1]]
# guessing the image is square, so 12*12
number_of_neighbors = dict.fromkeys(image_dict.keys(), 0)
neighbors_of_image = dict.fromkeys(image_dict.keys(), {})
for image_name in image_dict:
    for other_image in image_dict:
        for border_index in range(len(image_dict[image_name])):
            image_border = image_dict[image_name][border_index]
            if image_border in image_dict[other_image] and image_name != other_image:
                number_of_neighbors[image_name] += 1
                print(image_name, other_image, border_index)
                neighbors_of_image[image_name][other_image] = border_index
start = 1
corners = []
sides = []
middles = []
for key, value in number_of_neighbors.items():
    if value == 4:
        corners.append(key)
        start *= int(key[5:-1])
    elif value == 6:
        sides.append(key)
    elif value == 8:
        sides.append(key)
    else:
        print("aaaaaah",key)
print("The answer to exercise 1 is:", start)

while corners or sides or middles:
    for elt in corners:
        print(elt)
        print(neighbors_of_image[elt])
    break
