input = "1000\n\
\2000\n\
\3000\n\
\\n\
\4000\n\
\\n\
\5000\n\
\6000\n\
\\n\
\7000\n\
\8000\n\
\9000\n\
\\n\
\10000"

sum_players [] = []
sum_players (n:ns)
    | n == ""   = sum_player ns:sum_players ns
    | otherwise = sum_players ns
    where sum_player [] = 0
          sum_player ("":_) = 0
          sum_player (n:ns) = x + sum_player ns
            where x = read n :: Integer

max_player ps = go 0 ps
    where go m [] = m
          go m (p:ps)
            | p > m     = go p ps
            | otherwise = go m ps
    
main = do
    print . max_player . sum_players $ "":lines input