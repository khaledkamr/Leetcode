SELECT x, y, z, IF(
    x + y > z and
    x + z > y and
    y + z > x,
    "Yes",
    "No"
) AS Triangle
FROM Triangle