import System.IO
import Control.Monad

main = do
    contents <- readFile "input"
    let input = lines contents
    print $ result $ navigate $ input

type Pos = (Int, Int)

data Move = Forward Int | Up Int | Down Int

move :: Move -> Pos -> Pos
move (Forward a) (x,y) = (x + a, y)
move (Up a) (x, y)     = (x, y - a)
move (Down a) (x, y)   = (x, y + a)


navigate :: [String] -> Pos
navigate [] = (0, 0)
navigate (x:xs) = if command == "forward"
                     then move (Forward value) (navigate xs)
                  else if command == "up"
                     then move (Up value) (navigate xs)
                  else move (Down value) (navigate xs)
                      where
                          commandSplit = words $ x
                          command = commandSplit !! 0
                          value = read $ commandSplit !! 1

result :: Pos -> Int
result (x,y) = x * y
