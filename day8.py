#!/usr/bin/python3

from collections import Counter

# test_input = []
with open('day8.in', 'r') as f:
    test_data = f.read()

# test_data = '123456789012'

w = 25
h = 6
i = 0
# layers = []
layers = [test_data[i:i+w*h] for i in range(0, len(test_data), w*h)]
counters = []
for layer in layers:
    counters.append(Counter(layer))

sorted_counters = sorted(counters, key=lambda x: x.get('0', 0))

less_zeroes = sorted_counters[0]

print(less_zeroes['1'] * less_zeroes['2'])
# print(layers[0], layers[1])

result_img = ''
# print(layers[0])
# print(len(layers))
# print(list(zip(*layers)))
for pixels in zip(*list(map(list, layers))):
    # print(list(filter(lambda x: x != '2', pixels)))
    result_img += '#' if list(filter(lambda x: x != '2', pixels))[0] == '1' else ' '

# test_layers = [layers[1], layers[1]]*10
# print(test_layers)

# for pixel in range(w*h):
#     for layer in test_layers:
#         if layer[pixel] == '2':
#             continue
#         result_img += '#' if layer[pixel] == '1' else ' '
#         break

# print(len(result_img))
for i in range(0,w*h, w):
    print(result_img[i:i+w])