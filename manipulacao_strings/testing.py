phrase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tincidunt dapibus turpis, eu lacinia justo pharetra at. Maecenas ipsum metus, vestibulum sit amet tellus ut, elementum pretium orci. Quisque consequat sed felis at tristique.'
start = 'Lorem'
end = 'amet'
first = phrase.split(start)
second = first[1].split(end)
#second = first[1].split(end)
print(second[0])