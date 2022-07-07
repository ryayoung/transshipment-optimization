### We are revisiting a transshipment problem similar to one that we solved in the second class of Week 2. In this problem, Elmore's Ski Boots is the manufacturer of the finest ski boots available. There are three plants that manufacture the boots, two distribution centers, and five warehouses. We need to ship the boots to the warehouses at a minimum cost satisfying the constraints outlined in the spreadsheet. Namely, each plant can only produce so much product, the amount of boots passing through the distribution centers has to remain constant (in has to equal out), and each warehouse has a minimum amount that they need in order to satisfy demand. The data are given in the Excel file quiz-1.xlsx  Download quiz-1.xlsx. Put your answers into this python notebook  Download python notebook. You will need to submit the notebook saved as an html file.  

### Answer the following questions 

1. What is the minimum cost to ship these boots from our plants to the warehouses while satisfying all of our constraints? 
2. What are the final values of the decision variables?
3. Is there any slack in the system? If so, what is the amount/route that shows slack?
4. Suppose management tells us that the per unit shipping cost from Plant P3 to Distribution Center D1 is going to change to \$.60. How do your answers to 1. and 2. change? 
5. Show the values of the decision variables as barcharts using seaborn. Create a separate plot for Plants to Distribution Centers (colored by DCs) and another for DCs to Warehouses (colored by WHs).
6. Create a sequence of shipping costs (P3 to D1) from 0.5 to 0.7 in one cent increments (21 unique values).
    1. Make a plot showing how the overall shipping costs change as a function of this sequence.
    2. Make two plots showing: (1) the amount of boots shipped between Plant P3 and the two distribution centers and (2) the amount of boots shipped between each distribution center and the five warehouses. The lines be shown using different colors.
7. Finally, let's investigate how changing the demand on the third warehouse changes the final value of the objective function. Create a sequence of demands from 4700 to 7300 by 100 units. Plots those demands on the x axis and the final minimum cost on the y.