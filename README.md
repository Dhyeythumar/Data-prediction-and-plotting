# Data-prediction-and-plotting
### Objective
The objective for this topic is to predict the third-semester pointers on the basis of the first and second-semester pointers values. And to create a method which can predict the near future data (one or two values) to its possible amount of accuracy by using the minimal amount of data.

### Approach
- The first approach is to apply linear regression to the give data set, but for applying that the data should be related. Yes, data here is not related as the semester changes subject weightage also changes credits assigned to them also changes as in the first year there were 27 credits and in second year 26 so if we apply linear regression to the data then the prediction values would be based on previous year's marks distribution pattern. 

- So dropping the above idea, another approach is taken into consideration in this case it is assumed that the pointers will increase in a rectangular hyperbole fashion so as the distance between the pointers will follow the same trend but this theory ruled out because on plotting the rectangular hyperbole and the line joining the two pointers, intersect only at two points (i.e both line and rectangular hyperbole are almost parallel).

On x-axis pointers are plotted and on y-axis difference between the pointers are plotted.
![Graph Image](https://github.com/Dhyeythumar/Data-prediction-and-plotting/blob/master/documents/graph.png?raw=true)
*As we can see in the graph, line and rectangular hyperbola are almost parallel except two points which are values of pointer values of first and second semester.*

- The other approach to this problem is that pointers will increases or decreases in an exponential fashion i.e same as the rectangular hyperbole graph. This graph is used again because it closely resembles the behavior of the pointers i.e the difference between the pointers decreases as it approaches 10 and same happens but in reverse order when the pointer goes away from 10 i.e difference increases.  The equation [difference =e^2.1/2*current_pointer] is used here, by this base value is calculated for each student by taking 2.1 as general value (a starting value) and then replacing that with a base value for the further calculation. But this base value is not that much accurate enough, as it is calculate on the bases of two values so not enough data to study the nature of base value but can be used to predict the third value. Error function can be made by taking the standard deviation between of calculated base value and the actual value. One more barrier here is the approximations or precision which propagates, and error value increases.

