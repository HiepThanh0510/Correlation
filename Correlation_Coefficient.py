def find_corr_x_y(x,y):                                         
    n = len(x)                                                  
    prod = []
    for xi,yi in zip(x,y):                                      
         prod.append(xi*yi)
         
    sum_prod_x_y = sum(prod)                                    
    
    sum_x = sum(x)
    sum_y = sum(y)
    
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2 
    
    x_square = []
    for xi in x:
        x_square.append(xi**2)            
    x_square_sum = sum(x_square)
    y_square=[]
    for yi in y:
        y_square.append(yi**2)        
    y_square_sum = sum(y_square)
    
    # Use formula to calculate correlation                      
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    
    return correlation

x = [5, 20, 25, 5, 8, 9, 9]
y = [1, 6, 12, 8, 6, 21, 10]
y2 = []
for i in y:
    y2.append(i*2+1)
print(y2)
    
print('Correlation coefficient of x,y: ',find_corr_x_y(x,y))
print('Correlation coefficient of x,y: ',find_corr_x_y(x,y2))