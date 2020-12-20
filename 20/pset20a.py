SQUARELENGTH = 12
SQUAREAREA = pow(SQUARELENGTH, 2)

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().split("\n\n")

    tiles = {}

    for i in rawinput:
        input = i.split()
        name = input[1].split(":")[0]
        contents = []
        for i in input[2:]:
            content = []
            for j in i:
                content.append(j)
            contents.append(content)
        tiles[name] = contents
    
    edge_dict = {}
    for i in tiles:
        edges = getEdges(tiles[i])
        # print(edges)
        for edge in edges:
            edge_dict[edge_id(edge)] = edge
            
    edge_counts = {}
    for i in tiles:
        edges = getEdges(tiles[i])
        for edge in edges:
            if edge_id(edge) not in edge_counts:
                edge_counts[edge_id(edge)] = 1
            else:
                edge_counts[edge_id(edge)] += 1
    # print(edge_counts)

    tile_one_edge_counts = []
    for i in tiles:
        number_with_edge = 0
        edges = getEdges(tiles[i])
        for edge in edges:
            if edge_counts[edge_id(edge)] == 1:
                number_with_edge += 1
        if number_with_edge == 2:
            tile_one_edge_counts.append(i)
    
    ans = 1
    for i in tile_one_edge_counts:
        ans *= int(i)
    print(ans)


def edge_id(edge):
    multiplier = 512
    id = 0
    # print(edge)
    for i in edge:
        if i == '#':
            id += multiplier
        multiplier //= 2
    return id


def getEdges(tiles):

    result = []

    top = getTop(tiles)
    right = getRight(tiles)
    bottom = getBottom(tiles)
    left = getLeft(tiles)
    topreversed = getTop(tiles)
    topreversed.reverse()
    rightreversed = getRight(tiles)
    rightreversed.reverse()
    bottomreversed = getBottom(tiles)
    bottomreversed.reverse()
    leftreversed = getLeft(tiles)
    leftreversed.reverse()

    if edge_id(top) > edge_id(topreversed):
        result.append(top)
    else:
        result.append(topreversed)
    if edge_id(right) > edge_id(rightreversed):
        result.append(right)
    else:
        result.append(rightreversed)
    if edge_id(bottom) > edge_id(bottomreversed):
        result.append(bottom)
    else:
        result.append(bottomreversed)
    if edge_id(left) > edge_id(leftreversed):
        result.append(left)
    else:
        result.append(leftreversed)

    return result



def getTop(image) :
    return list(image[0])


def getRight(image):
    result = []
    for i in image:
        result.append(i[-1])
    return list(result)


def getBottom(image):
    return list(image[-1])


def getLeft(image):
    result = []
    for i in image:
        result.append(i[0])
    return list (result)


if __name__ == "__main__":
    main()