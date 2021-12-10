-- Day 3 Part 2
-- Find life support rating of submarine

import System.IO
import Control.Monad
import Data.Char

main = do
    contents <- readFile "input"
    let input = lines contents
    print $ lifeSupportRating input

type DiagnosticLog = [String]

type GasValue = String

type GasRating = Int

type Position = Int

type BitCount = (Int, Int)

data Gas = Oxygen | Cdo

data Bit = Zero | One
            deriving (Eq)


-- Get count of zeroes and ones in the log at a given position
bitCountAtPosition :: DiagnosticLog -> Position -> BitCount
bitCountAtPosition [] pos = (0, 0)
bitCountAtPosition (x:xs) pos
    | val == '1' = (zeroes, ones + 1)
    | otherwise  = (zeroes + 1, ones)
    where (zeroes, ones) = bitCountAtPosition xs pos
          val = x !! pos


-- Finds out which bit is deciding big given count of bits and gas
getDecidingBit :: BitCount -> Gas -> Bit
getDecidingBit (zeroes, ones) Oxygen = if ones >= zeroes then One else Zero
getDecidingBit (zeroes, ones) Cdo = if zeroes <= ones then Zero else One


-- Filter log to get entries where bit at a position matches supplied args
filterByBits :: DiagnosticLog -> Position -> Bit -> DiagnosticLog
filterByBits [] _ _ = []
filterByBits (x:xs) pos bit
    | bit == Zero && x !! pos == '0' = [x] ++ filterByBits xs pos bit
    | bit == One && x !! pos == '1'  = [x] ++ filterByBits xs pos bit
    | otherwise                      = filterByBits xs pos bit


-- Get gas rating in log format (binary string)
getGasValue :: DiagnosticLog -> Gas -> GasValue
getGasValue log gas = getGasValue' log gas 0
    where 
        getGasValue' [x] gas _ = x
        getGasValue' (x:xs) gas pos = getGasValue' filteredLog gas (pos + 1)
            where 
                filteredLog = filterByBits (x:xs) pos (getDecidingBit (bitCountAtPosition (x:xs) pos) gas)



-- Convert gas rating value from binary string to integer
gasValueToInt :: GasValue -> Int
gasValueToInt x = sum [(digitToInt value) * (2^index) | (index, value) <- l]
                    where l = zip [0..] (reverse x)


-- Calculate life support rating
lifeSupportRating :: DiagnosticLog -> Int
lifeSupportRating log = gasValueToInt (getGasValue log Oxygen) * gasValueToInt (getGasValue log Cdo)

