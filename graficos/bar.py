
import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'anger':0.088776, 'disgust':0.041964, 'fear':0.08432,
        'joy':0.302678, "sadness": 0.298589}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='green',
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()