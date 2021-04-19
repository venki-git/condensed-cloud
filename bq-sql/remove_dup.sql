SELECT FirstName, 
    LastName, 
    Country
FROM Employee
GROUP BY FirstName, 
      LastName, 
      Country
HAVING COUNT(*) > 1;
