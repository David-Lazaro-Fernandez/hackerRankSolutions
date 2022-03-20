
height = [1,8,6,2,5,4,8,3,7]
left = 0 
right = len(height)-1
max_area=0
while(left != right):
    
    if(height[left] >= height[right]):
        lowest_element = height[right]
    else:
        lowest_element = height[left]
    area = ((right-left) * lowest_element)
    if(area > max_area):
        max_area = area
    if(height[left] <= height[right]):
        left +=1
    else:
        right-=1
    
print(max_area)