-- 1. Electric vehicles registered per year
SELECT 
    model_year, 
    COUNT(*) AS total
FROM vehicles
GROUP BY model_year
ORDER BY model_year;

-- 2. Top 10 most registered electric vehicle models
SELECT 
    model, 
    COUNT(*) AS total
FROM vehicles
GROUP BY model
ORDER BY total DESC
LIMIT 10;

-- 3. Geographic concentration of CAFV-eligible vehicles
SELECT 
    county, 
    COUNT(*) AS total
FROM vehicles
WHERE clean_alternative_fuel_vehicle_cafv_eligibility ILIKE '%eligible%'
GROUP BY county
ORDER BY total DESC;

-- 4. Year-over-year change in registrations per county
WITH yearly_totals AS (
  SELECT 
    county,
    model_year,
    COUNT(*) AS total
  FROM vehicles
  GROUP BY county, model_year
)
SELECT 
  county,
  model_year,
  total,
  total - LAG(total) OVER (PARTITION BY county ORDER BY model_year) AS yoy_change
FROM yearly_totals
ORDER BY county, model_year;

