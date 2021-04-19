select country, AVG(salary) from Employee
group by country
having AVG(Salary)>30000
