main = putStrLn "Hello, world2!"
sumSq x y = x^2 + y^2
lenVec3 x y z = sqrt x^2 + y^2 + z^2

sign x = if x > 0 then 1 else (if x < 0 then (-1) else 0)

twoDigits2Int x y = if (&&) (isDigit x isDigit y) then digitToInt x * 10 + digitToInt y else 100



