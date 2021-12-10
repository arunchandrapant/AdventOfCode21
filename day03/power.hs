-- Day 3 Part 1
-- Find power consumption of submarine

import System.IO
import Control.Monad
import Data.Char

main = do
    contents <- readFile "input"
    let input = lines contents
    print $ getPowerConsumption $ input


-- do integer addition of all bits in each column in log
countBits :: [String] -> [Int]
countBits [x] = binToArr x
countBits (x:xs) = zipWith (+) (binToArr x) (countBits xs)


-- convert bits in string to bits in integer array
binToArr :: String -> [Int]
binToArr [] = []
binToArr (x:xs) = [digitToInt x] ++ binToArr xs


-- calculate value for gamma
getGamma :: [Int] -> Int -> [Int]
getGamma [] a = []
getGamma (x:xs) a 
    | xi > (ai / 2.0) = [1] ++ getGamma xs a
    | otherwise       = [0] ++ getGamma xs a
    where ai = fromIntegral a :: Float
          xi = fromIntegral x :: Float


-- take a bit array and returns its complement
complementBits :: [Int] -> [Int]
complementBits [] = []
complementBits (x:xs) 
    | x == 1    = [0] ++ complementBits xs
    | otherwise = [1] ++ complementBits xs

-- convert list of bits into integer
binArrToNum :: [Int] -> Int
binArrToNum x = sum [value * (2^index) | (index, value) <- l]
                    where l = zip [0..] (reverse x)

-- function to combine all utility function and get final result
getPowerConsumption :: [String] -> Int
getPowerConsumption a = (binArrToNum gammaBits) * (binArrToNum epsilonBits)
        where gammaBits = getGamma (countBits a) (length a)
              epsilonBits = complementBits gammaBits
