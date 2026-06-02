-- Lists all cities with their corresponding state names

-- Display city id, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
