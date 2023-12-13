import os

dir = './ft_fun'
final_content = [[] for _ in range(750)]
for file in os.listdir(dir):
    f = open(os.path.join(dir, file))
    content = f.read()
    last_line = content.split("\n")[-1]
    idx_file = int(last_line[6:])
    final_content[idx_file - 1].append(content)
file_content = '\n'.join([' '.join(inner_array) for inner_array in final_content])
with open('out.c', 'w') as file:
    file.write(file_content)