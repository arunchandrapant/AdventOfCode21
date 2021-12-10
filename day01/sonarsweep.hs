import System.IO
import Control.Monad

main = do
    contents <- readFile "input"
    let input = map read (words $ contents)
    print (countIncrements $ input)
    print (countIncrSliding $ input)

countIncrements :: [Int] -> Int
countIncrements [a] = 0
countIncrements (a:b:xs) = if b > a
                                  then 1 + countIncrements(b:xs)
                                  else countIncrements(b:xs)


countIncrSliding :: [Int] -> Int
countIncrSliding [a, b, c] = 0
countIncrSliding (a:b:c:d:xs) = if b + c + d > a + b + c
                                   then 1 + countIncrSliding(b:c:d:xs)
                                   else countIncrSliding(b:c:d:xs)
